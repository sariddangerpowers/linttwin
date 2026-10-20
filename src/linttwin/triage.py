"""Triage: the protocol that turns LintTwin's report into causes, written for an LLM agent (or a person) to follow.

`linttwin triage REPORT` writes REPORT/triage/: one case per rule that disagrees with its original and per rule whose
safe fix fails a check, the two prompts of the protocol and a README. A classifier gives every case one cause from
CAUSES and backs it with a documentation quote, an issue or a reproducer; a verifier then tries to refute every bug.
`linttwin triage REPORT --collect` checks their answers against the protocol and tallies the causes.

The protocol is the one of the paper's batch pass (triage/prompts/ in the repository). The causes the study found are
in known_causes.tsv: `check` marks those rules in its report, and `triage` leaves them out unless --all.
"""
from __future__ import annotations

import collections
import csv
import glob
import gzip
import json
import os
import time

KNOWN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "known_causes.tsv")
FIX = " (safe fix)"                      # marks a safe-fix case in section headers and verdicts
TRACKER = {"ruff": "astral-sh/ruff", "oxlint": "oxc-project/oxc", "biome": "biomejs/biome"}
CAUSES = {   # the batch pass's classes, in its words
    "BUG": "likely a bug in the rewrite: it behaves differently from the rule it declares equivalent, on the same code, "
           "and this is not documented, not tracked, and not explained by options or defaults. Give a minimal "
           "reproducer.",
    "TRACKED": "an open or closed issue in the rewrite's tracker already covers it (cite the number).",
    "DOC": "a documented or clearly deliberate design difference (cite the documentation you found).",
    "LAG": "the rewrite lags behind (or is ahead of) a newer release of the original, whose default or behaviour "
           "changed.",
    "REF": "the original tool is wrong (its own bug, false positive or false negative) and the rewrite is right.",
    "CFG": "explained by options, defaults or plugin configuration, including LintTwin's own setup.",
    "ANCHOR": "both tools report the same finding, at positions LintTwin's matcher could not pair (e.g. different lines "
              "of a long multi-line statement, or a file-level against a line-level report): an artefact of the "
              "comparison, not a difference between the tools.",
    "PARSE": "parsing, syntax-version or encoding differences (e.g. Python 2 test data, files one tool reads "
             "differently).",
    "UNCLEAR": "cannot be decided with reasonable effort (say what is missing).",
}
VERDICTS = {"CONFIRMED": "BUG", "DUPLICATE": "TRACKED", "FIXED-ON-MAIN": "TRACKED", "DOCUMENTED": "DOC",
            "INTENDED": "DOC", "NOT-REPRODUCED": "UNCLEAR", "DEBATABLE": "UNCLEAR", "NOT-A-BUG": "UNCLEAR"}
CASE_COLUMNS = ("tool", "rule", "cause", "confidence", "reason", "evidence")
VERIFIED_COLUMNS = ("tool", "rule", "verdict", "confidence", "repro", "evidence", "note")

CLASSIFY = """\
You are triaging the cases LintTwin found when it ran Rust rewrites of linters next to the tools they claim to
re-implement ({pairs}) on the same code, every rule at its default options (ruff, flake8 and pylint aligned at line
length 88 and Python 3.12). Versions: {versions}.

Your cases are in {case_files}. Each "## tool :: rule" section is a rule that disagrees with its original: the
reports only the rewrite makes, the reports only the original makes, the number of packages, the top messages and up
to three real examples per side with source context. Each "## tool :: rule (safe fix)" section is a rule whose safe
fix failed one of LintTwin's checks (the code no longer parses, a comment was lost or changed, a name became
undefined, or, in Python, a statement became unreachable or moved between blocks), with an example.

For EVERY case, give exactly one cause (the one that explains most of the case; mention a secondary cause in the
reason if it is mixed):
{causes}
For a safe-fix case, BUG means the fix breaks the code or its comments although the rewrite marks it as safe, DOC means
the rewrite documents this behaviour of the fix (for example, ruff deletes comments together with whole statements),
and REF means the original tool's own fix does the same.

Evidence you can use (read only: do not post, comment or file anything anywhere):
- Documentation: `{ruff} rule <CODE>` (ruff's rule docs, which often state deviations from the original),
  `{pylint} --help-msg=<msgid>`, `{biome} explain <ruleName>`; online, https://docs.astral.sh/ruff/rules/,
  https://eslint.org/docs/latest/rules/<rule>, https://oxc.rs/docs/guide/usage/linter/rules/eslint/<rule>.html (or
  /unicorn/<rule>.html), https://biomejs.dev/linter/rules/ and the flake8 plugins' READMEs.
- Trackers: issues and pull requests, open and closed, of {trackers}, for example
  `gh api -X GET search/issues -f q='repo:{tracker} <terms>'`.
- Reproducers, encouraged for BUG candidates: write a tiny file under {scratch} and run one tool at a time:
  `{ruff} check --isolated --select <CODE> f.py`, `{flake8} --isolated --select <CODE> f.py`,
  `{pylint} --disable=all --enable=<msgid> f.py`, `{oxlint} -A all -D <rule> f.js`, ESLint with a flat config that
  enables only the rule (`{eslint} --no-config-lookup -c cfg.mjs f.js`; import eslint-plugin-unicorn from
  {node_modules} for unicorn rules), and `{biome} lint f.js` next to a biome.json that enables only the rule.

Write your verdicts to {verdicts}/batch_NN.tsv, one file per case file (NN as in its name), tab-separated, with this
header line:
tool\trule\tcause\tconfidence\treason\tevidence
Copy tool and rule exactly from the section header (for a safe-fix case, the rule followed by "{fix}"). Confidence is
high, med or low. Keep the reason to one sentence and the evidence to a documentation quote, an issue number or a
reproducer result. Every case gets exactly one row.

When done, return a short summary: per file, the number of cases per cause, and one line for each BUG and UNCLEAR
case. Be careful and literal: a wrong BUG costs credibility with the maintainers, and a DOC needs a real documentation
statement or an unmistakably deliberate behaviour.
"""

VERIFY = """\
You are a skeptical verifier. A triage of the cases LintTwin found ({versions}) produced bug candidates: the rows with
cause BUG or UNCLEAR in {verdicts}/batch_*.tsv; the cases themselves are in {case_files}. Try to KILL each candidate.
A wrong report costs credibility with the maintainers, so only a claim that survives every check below counts as
CONFIRMED. Do not post, comment, or open issues or pull requests anywhere.

For EACH candidate:
a. Reproduce it from scratch with a minimal snippet, default options, one tool at a time (the commands are in
   {classify}). Keep scratch files under {scratch}.
b. Confirm that the original tool's behaviour is the intended one: its documentation or its own tests. If the
   original's behaviour is arguably its own bug, the verdict is DEBATABLE.
c. Read the rewrite's documentation for the rule, and the rule's source and tests: a stated difference, or an upstream
   test that is commented out with a reason, means INTENDED.
d. Search the rewrite's tracker ({trackers}) thoroughly: issues and pull requests, open and closed, with several
   phrasings (the rule's name in kebab and snake case, key words of the behaviour), and the recent commits to the
   rule's source. A fix merged after the release you tested means FIXED-ON-MAIN.
e. Give exactly one verdict: CONFIRMED (new, reproduces, the original's behaviour is intended, nothing in the docs, the
   tracker or main), DUPLICATE (cite the issue), FIXED-ON-MAIN (cite the pull request), DOCUMENTED (cite the docs),
   INTENDED (cite the code comment or the maintainers' statement), NOT-REPRODUCED, DEBATABLE (say why) or NOT-A-BUG
   (say what the triage misread).

Write {verified}, tab-separated, with this header line:
tool\trule\tverdict\tconfidence\trepro\tevidence\tnote
Copy tool and rule from the verdicts. Put the reproducer on one line, with \\n for newlines. Then return a short
summary: the number of candidates per verdict, and one line for each CONFIRMED candidate with its minimal reproducer
and the difference.
"""

README = """\
# Triage

LintTwin wrote {n} cases from the report in {report}: {n_rules} rules that disagree with their original and {n_fixes}
rules whose safe fixes fail a check, in {n_files} files under cases/. {known}

The protocol has three steps. The agent can be any LLM agent that can read files, run commands and write files (the
paper used Claude Code), or a person.

1. Classify: give an agent the prompt in prompts/classify.md. It gives every case one cause and writes
   verdicts/batch_NN.tsv. For many cases, split the case files across several agents.
2. Verify: give a second agent prompts/verify.md. It tries to refute every BUG and UNCLEAR case and writes
   verified.tsv.
3. Collect: `linttwin triage {report} --collect` checks the answers against the protocol, then writes tally.md and
   causes.tsv.
"""


def known_causes(path=KNOWN):
    """{(tool, kind, rule): (cause, reason)} from the study; the rules it left UNCLEAR still need a cause."""
    with open(path, newline="") as fh:
        rows = csv.DictReader((ln for ln in fh if not ln.startswith("#")), delimiter="\t", quoting=csv.QUOTE_NONE)
        return {(r["tool"], r["kind"], r["rule"]): (r["cause"], r["reason"]) for r in rows if r["cause"] != "UNCLEAR"}


def _records(path):
    if os.path.exists(path):
        with gzip.open(path, "rt") as fh:
            for line in fh:
                yield json.loads(line)


def rule_cases(report_dir, max_examples=3):
    """{(tool, rule): case} for every rule that disagrees: counts, top messages, examples from different packages."""
    cases = {}
    for d in _records(os.path.join(report_dir, "divergences.jsonl.gz")):
        c = cases.get((d["tool"], d["rule"]))
        if c is None:
            c = cases[(d["tool"], d["rule"])] = {
                "kind": "rule", "tool": d["tool"], "rule": d["rule"], "reference": d["reference"],
                "eslint_rules": d.get("eslint_rules"), "only_rewrite": 0, "only_reference": 0, "packages": set(),
                "messages": collections.Counter(), "examples": {"rewrite": [], "reference": []},
                "spare": {"rewrite": [], "reference": []}}
        side = "reference" if d["side"] == "reference_only" else "rewrite"
        n = d.get("n", 1)
        c["only_" + side] += n
        c["packages"].add(d["package"])
        c["messages"][(side, " ".join((d.get("message") or "").split()))] += n
        ex, spare = c["examples"][side], c["spare"][side]
        if len(ex) < max_examples:
            if all(e["package"] != d["package"] for e in ex):
                ex.append(d)
            elif len(spare) < max_examples and all((e["file"], e["line"]) != (d["file"], d["line"]) for e in ex + spare):
                spare.append(d)
    for c in cases.values():
        for side in ("rewrite", "reference"):
            c["examples"][side] += c["spare"][side][:max_examples - len(c["examples"][side])]
        del c["spare"]
        c["packages"] = len(c["packages"])
    return cases


def fix_cases(report_dir, max_examples=2):
    """{(tool, rule + FIX): case} for every rule whose safe fix fails a check on its own (or files that fail only in
    combination): files, packages, the checks that failed and examples from different packages."""
    cases = {}
    for x in _records(os.path.join(report_dir, "fixes.jsonl.gz")):
        for rule in x["rules"] or ["(only in combination)"]:
            c = cases.setdefault((x["tool"], rule + FIX), {
                "kind": "fix", "tool": x["tool"], "rule": rule, "files": 0, "packages": set(),
                "checks": collections.Counter(), "examples": []})
            hit = next((h for h in x["per_rule"] if h["rule"] == rule), x)
            c["files"] += 1
            c["packages"].add(x["package"])
            c["checks"].update(hit["kinds"])
            if len(c["examples"]) < max_examples and all(e["package"] != x["package"] for e in c["examples"]):
                own = not x["rules"] or x["rules"][0] == rule      # the stored diff is the first failing rule's
                c["examples"].append({"package": x["package"], "file": x["file"], "detail": hit["detail"],
                                      "diff": x["diff"] if own else None})
    for c in cases.values():
        c["packages"] = len(c["packages"])
    return cases


def _size(c):
    return c["files"] if c["kind"] == "fix" else c["only_rewrite"] + c["only_reference"]


def _reference_name(c):
    return "ESLint" if c["reference"] == "eslint" else c["reference"]


def _case_markdown(c):
    tool = c["tool"]
    if c["kind"] == "fix":
        L = ["## %s :: %s%s\n" % (tool, c["rule"], FIX),
             "files whose safe fix fails a check: %d | packages: %d | checks failed: %s\n"
             % (c["files"], c["packages"], ", ".join("%s ×%d" % kv for kv in c["checks"].most_common()))]
        for e in c["examples"]:
            L.append("\n### %s %s\nfailed: %s\n" % (e["package"], e["file"], json.dumps(e["detail"])[:600]))
            if e["diff"]:
                L.append("```diff\n%s\n```\n" % e["diff"][:2500])
        return "".join(L) + "\n"
    ref = _reference_name(c)
    L = ["## %s :: %s\n" % (tool, c["rule"])]
    mapped = "" if not c["eslint_rules"] or c["eslint_rules"] == [c["rule"]] else \
        " (ESLint rules: %s)" % ", ".join(c["eslint_rules"])
    L.append("reference: %s%s | only %s: %d | only %s: %d | packages: %d\n"
             % (ref, mapped, tool, c["only_rewrite"], ref, c["only_reference"], c["packages"]))
    top = c["messages"].most_common(5)
    L.append("top messages: %s\n" % " || ".join("[only %s] %s ×%d" % (tool if s == "rewrite" else ref, m[:160], k)
                                                 for (s, m), k in top))
    for side in ("rewrite", "reference"):
        for d in c["examples"][side]:
            L.append("\n### only %s — %s %s:%s\nmessage: %s\n```\n%s\n```\n"
                     % (tool if side == "rewrite" else ref, d["package"], d["file"], d["line"],
                        " ".join((d.get("message") or "").split())[:300], d.get("context", "")))
    return "".join(L) + "\n"


def _tool_paths(tc):
    """paths in the prompts; the linters need not be installed when the cases are written."""
    py, js = tc.py_dir / "bin", tc.js_dir / "node_modules" / ".bin"
    return {"ruff": py / "ruff", "flake8": py / "flake8", "pylint": py / "pylint", "eslint": js / "eslint",
            "oxlint": js / "oxlint", "biome": js / "biome", "node_modules": tc.js_dir / "node_modules"}


def write(report_dir, tc, include_known=False, batch=25, limit=None):
    """write report_dir/triage: cases, prompts, README and index.json. Returns the index."""
    meta_path = os.path.join(report_dir, "meta.json")
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    known = known_causes()
    every = list(fix_cases(report_dir).values()) + list(rule_cases(report_dir).values())
    every.sort(key=lambda c: (c["kind"] != "fix", -_size(c), c["tool"], c["rule"]))
    todo, skipped = [], []
    for c in every:
        k = known.get((c["tool"], c["kind"], c["rule"]))
        (skipped if k and not include_known else todo).append((c, k))
    if limit is not None:
        todo = todo[:limit]
    tdir = os.path.join(os.path.abspath(report_dir), "triage")       # absolute: the prompts name these paths
    for sub in ("cases", "prompts", "verdicts", "scratch"):
        os.makedirs(os.path.join(tdir, sub), exist_ok=True)
    files = []
    for i in range(0, len(todo), batch):
        path = os.path.join(tdir, "cases", "batch_%02d.md" % (i // batch + 1))
        with open(path, "w") as fh:
            fh.writelines(_case_markdown(c) for c, _ in todo[i:i + batch])
        files.append(path)
    tools = sorted({c["tool"] for c, _ in todo}) or sorted(TRACKER)
    pairs = {"ruff": "ruff against flake8 and pylint", "oxlint": "oxlint against ESLint and eslint-plugin-unicorn",
             "biome": "Biome against ESLint and eslint-plugin-unicorn"}
    fill = {k: str(v) for k, v in _tool_paths(tc).items()}
    fill.update(
        pairs="; ".join(pairs[t] for t in tools),
        versions=", ".join("%s %s" % kv for kv in meta.get("versions", {}).items()) or "as installed",
        case_files=", ".join(files) if len(files) < 4 else os.path.join(tdir, "cases", "batch_*.md"),
        causes="\n".join("- %s: %s" % kv for kv in CAUSES.items()),
        trackers=", ".join(TRACKER[t] for t in tools), tracker=TRACKER[tools[0]], scratch=os.path.join(tdir, "scratch"),
        verdicts=os.path.join(tdir, "verdicts"), verified=os.path.join(tdir, "verified.tsv"),
        classify=os.path.join(tdir, "prompts", "classify.md"), fix=FIX)
    with open(fill["classify"], "w") as fh:
        fh.write(CLASSIFY.format(**fill))
    with open(os.path.join(tdir, "prompts", "verify.md"), "w") as fh:
        fh.write(VERIFY.format(**fill))
    entry = lambda c, k: {"tool": c["tool"], "kind": c["kind"], "rule": c["rule"],          # noqa: E731
                          "case": c["rule"] + (FIX if c["kind"] == "fix" else ""), "size": _size(c),
                          "known": k and {"cause": k[0], "reason": k[1]}}
    index = {"report": os.path.abspath(report_dir), "written": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
             "versions": meta.get("versions", {}), "cases": [entry(c, k) for c, k in todo],
             "known": [entry(c, k) for c, k in skipped], "files": files}
    with open(os.path.join(tdir, "index.json"), "w") as fh:
        json.dump(index, fh, indent=1)
    n_fix = sum(c["kind"] == "fix" for c, _ in todo)
    with open(os.path.join(tdir, "README.md"), "w") as fh:
        fh.write(README.format(
            n=len(todo), report=report_dir, n_rules=len(todo) - n_fix, n_fixes=n_fix, n_files=len(files),
            known=("%d more rules have a cause known from the LintTwin study and are left out (index.json lists them; "
                   "--all includes them)." % len(skipped)) if skipped else ""))
    return index


def _tsv(path):
    with open(path, newline="") as fh:
        r = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        rows = [{k.strip(): (v or "").strip() for k, v in row.items() if k} for row in r]
        return rows, [f.strip() for f in r.fieldnames or []]


def collect(report_dir):
    """check the verdicts against the protocol and tally the causes. Returns (summary lines, problems)."""
    tdir = os.path.join(report_dir, "triage")
    index = json.load(open(os.path.join(tdir, "index.json")))
    cases = {(c["tool"], c["case"]): c for c in index["cases"]}
    problems, verdicts, verified = [], {}, {}
    for path in sorted(glob.glob(os.path.join(tdir, "verdicts", "*.tsv"))):
        rows, cols = _tsv(path)
        name = os.path.basename(path)
        if [c for c in CASE_COLUMNS if c not in cols]:
            problems.append("%s: the header must be %s" % (name, "\\t".join(CASE_COLUMNS)))
            continue
        for i, r in enumerate(rows, 2):
            key, cause, where = (r["tool"], r["rule"]), r["cause"].upper(), "%s:%d" % (name, i)
            if key not in cases:
                problems.append("%s: no case %s :: %s" % ((where,) + key))
            elif cause not in CAUSES:
                problems.append("%s: %s :: %s: %r is not a cause" % ((where,) + key + (r["cause"],)))
            elif key in verdicts:
                problems.append("%s: %s :: %s has a second verdict" % ((where,) + key))
            else:
                if not r["evidence"]:
                    problems.append("%s: %s :: %s gives no evidence" % ((where,) + key))
                if r["confidence"].lower() not in ("high", "med", "low"):
                    problems.append("%s: %s :: %s: confidence must be high, med or low" % ((where,) + key))
                verdicts[key] = dict(r, cause=cause)
    vpath = os.path.join(tdir, "verified.tsv")
    if os.path.exists(vpath):
        rows, cols = _tsv(vpath)
        if [c for c in VERIFIED_COLUMNS if c not in cols]:
            problems.append("verified.tsv: the header must be %s" % "\\t".join(VERIFIED_COLUMNS))
            rows = []
        for i, r in enumerate(rows, 2):
            key, v = (r["tool"], r["rule"]), r["verdict"].upper()
            if v not in VERDICTS:
                problems.append("verified.tsv:%d: %r is not a verdict" % (i, r["verdict"]))
            elif verdicts.get(key, {}).get("cause") not in ("BUG", "UNCLEAR"):
                problems.append("verified.tsv:%d: %s :: %s is not a BUG or UNCLEAR case" % ((i,) + key))
            else:
                verified[key] = dict(r, verdict=v)
    final = []          # (case entry, cause, source, reason)
    for key, c in cases.items():
        v = verdicts.get(key)
        if v is None:
            final.append((c, "UNTRIAGED", "-", "no verdict"))
        elif key in verified:
            w = verified[key]
            final.append((c, VERDICTS[w["verdict"]], "verifier: " + w["verdict"], w["evidence"] or w["note"]))
        else:
            final.append((c, v["cause"], "classifier, not verified" if v["cause"] == "BUG" else "classifier",
                          v["reason"]))
    final += [(c, c["known"]["cause"], "study", c["known"]["reason"]) for c in index["known"]]
    untriaged = sum(1 for _, cause, _, _ in final if cause == "UNTRIAGED")
    if untriaged:
        problems.append("%d cases have no verdict" % untriaged)
    with open(os.path.join(tdir, "causes.tsv"), "w") as fh:
        fh.write("tool\tkind\trule\tsize\tcause\tsource\treason\n")
        for c, cause, src, reason in final:
            fh.write("\t".join((c["tool"], c["kind"], c["rule"], str(c["size"]), cause, src,
                                " ".join(reason.split()))) + "\n")
    L = ["# Triage tally\n\n", "Report: %s; versions: %s.\n\n" % (
        index["report"], ", ".join("%s %s" % kv for kv in index["versions"].items()) or "unknown")]
    summary = []
    for tool in sorted({c["tool"] for c, *_ in final}):
        rules = [(c, cause) for c, cause, *_ in final if c["tool"] == tool and c["kind"] == "rule"]
        total = sum(c["size"] for c, _ in rules) or 1
        by = collections.defaultdict(lambda: [0, 0])
        for c, cause in rules:
            by[cause][0] += 1
            by[cause][1] += c["size"]
        L.append("## %s: %d rules, %d disagreeing reports\n\n| cause | rules | reports | share |\n|---|---:|---:|---:|\n"
                 % (tool, len(rules), sum(c["size"] for c, _ in rules)))
        for cause in list(CAUSES) + sorted(k for k in by if k not in CAUSES):   # the study also has GAP
            if cause in by:
                L.append("| %s | %d | %d | %.1f%% |\n" % (cause, by[cause][0], by[cause][1], 100 * by[cause][1] / total))
        fixes = [(c, cause) for c, cause, *_ in final if c["tool"] == tool and c["kind"] == "fix"]
        if fixes:
            L.append("\nSafe fixes that fail a check: %s.\n" % ", ".join(
                "%s %s (%d files)" % (c["rule"], cause, c["size"]) for c, cause in fixes))
        L.append("\n")
        summary.append("%-7s %d rules: %s" % (tool, len(rules), ", ".join(
            "%s %d (%.0f%%)" % (k, v[0], 100 * v[1] / total) for k, v in sorted(by.items(), key=lambda kv: -kv[1][1]))))
    bugs = [(c, src, reason) for c, cause, src, reason in final if cause == "BUG" and src != "study"]
    if bugs:
        L.append("## Bugs from this triage\n\n| tool | case | source | reason |\n|---|---|---|---|\n")
        L += ["| %s | `%s` | %s | %s |\n" % (c["tool"], c["case"], src, reason.replace("|", "/")[:300])
              for c, src, reason in bugs]
    with open(os.path.join(tdir, "tally.md"), "w") as fh:
        fh.writelines(L)
    summary.append("new bugs: %d (%d verified)" % (len(bugs), sum(s.startswith("verifier") for _, s, _ in bugs)))
    return summary, problems
