"""Aggregate chunk results and write the report (markdown) plus raw records (JSON Lines)."""
from __future__ import annotations

import collections
import gzip
import json
import os

SIDE_LABEL = {"ruff_only": "only {tool}", "oxlint_only": "only {tool}", "biome_only": "only {tool}",
              "reference_only": "only {ref}"}


class Result:
    def __init__(self, tool):
        self.tool = tool
        self.counts = collections.Counter()
        self.divergences, self.fixes, self.bugs, self.crashes = [], [], [], []
        self.stats = collections.Counter()
        self.packages = collections.defaultdict(set)      # (reference, rule, side) -> packages

    def add(self, out):
        self.counts.update(out["counts"])
        self.stats.update(out["stats"])
        for d in out["divergences"]:
            self.packages[(d["reference"], d["rule"], d["side"])].add(d["package"])
            self.divergences.append(d)
        self.fixes.extend(out["fixes"])
        self.bugs.extend(out["bugs"])
        self.crashes.extend(out["crashes"])


def write(results, out_dir, meta, max_examples=3):
    os.makedirs(out_dir, exist_ok=True)
    with gzip.open(os.path.join(out_dir, "divergences.jsonl.gz"), "wt") as f:
        for r in results:
            for d in r.divergences:
                f.write(json.dumps(d) + "\n")
    with gzip.open(os.path.join(out_dir, "fixes.jsonl.gz"), "wt") as f:
        for r in results:
            for x in r.fixes:
                f.write(json.dumps(x) + "\n")
    with open(os.path.join(out_dir, "crashes.jsonl"), "w") as f:
        for r in results:
            for x in r.crashes + [dict(b, kind="self-reported") for b in r.bugs]:
                f.write(json.dumps(x) + "\n")
    L = ["# LintTwin report\n\n",
         "- Packages: %d; tool versions: %s\n" % (meta["packages"], ", ".join("%s %s" % kv for kv in meta["versions"].items())),
         "- Raw records: `divergences.jsonl.gz`, `fixes.jsonl.gz`, `crashes.jsonl`\n\n"]
    for r in results:
        L.append("## %s\n\n" % r.tool)
        L.append("- Files compared: %d; changed by safe fixes: %d; fixes violating a check: %d; crashes: %d; "
                 "self-reported tool bugs: %d\n\n" % (r.stats["files_compared"], r.stats["files_changed"],
                                                       r.stats["fix_violations"], len(r.crashes), len(r.bugs)))
        rows = collections.defaultdict(lambda: collections.Counter())
        for (reference, rule, side), k in r.counts.items():
            rows[(reference, rule)][side] += k
        div = [(key, cnt) for key, cnt in rows.items() if any(s != "both" for s in cnt)]
        if div:
            L.append("### Rules that disagree with the original tool\n\n| reference | rule | agree | only %s | only reference | packages |\n"
                     "|---|---|---|---|---|---|\n" % r.tool)
            for (reference, rule), cnt in sorted(div, key=lambda kv: -sum(v for s, v in kv[1].items() if s != "both")):
                only_tool = sum(v for s, v in cnt.items() if s.endswith("_only") and s != "reference_only")
                pk = set().union(*(r.packages[(reference, rule, s)] for s in cnt if s != "both"))
                L.append("| %s | `%s` | %d | %d | %d | %d |\n" % (reference, rule, cnt["both"], only_tool,
                                                               cnt["reference_only"], len(pk)))
            L.append("\n")
            shown = collections.Counter()
            for d in r.divergences:
                key = (d["rule"], d["side"])
                if shown[key] >= max_examples or shown[d["rule"]] >= max_examples * 2:
                    continue
                shown[key] += 1
                shown[d["rule"]] += 1
                who = r.tool if d["side"] != "reference_only" else d["reference"]
                L.append("<details><summary><code>%s</code>: only %s reports, %s %s:%d</summary>\n\n%s\n\n```\n%s\n```\n</details>\n\n"
                         % (d["rule"], who, d["package"], d["file"], d["line"], d.get("message", "").replace("\n", " "),
                            d["context"]))
        if r.fixes:
            by = collections.defaultdict(list)
            for x in r.fixes:
                for rule in (x["rules"] or ["(only in combination)"]):
                    by[rule].append(x)
            L.append("### Safe fixes that fail a check\n\n| rule | files | packages | checks failed |\n|---|---|---|---|\n")
            for rule, xs in sorted(by.items(), key=lambda kv: -len({x["package"] for x in kv[1]})):
                kinds = collections.Counter(k for x in xs for k in x["kinds"])
                L.append("| `%s` | %d | %d | %s |\n" % (rule, len(xs), len({x["package"] for x in xs}),
                                                       ", ".join("%s ×%d" % kv for kv in kinds.most_common())))
            L.append("\n")
            for rule, xs in sorted(by.items(), key=lambda kv: -len({x["package"] for x in kv[1]}))[:15]:
                x = xs[0]
                pr = next((h for h in x["per_rule"] if h["rule"] == rule), None)
                L.append("<details><summary><code>%s</code> in %s/%s</summary>\n\n%s\n\n```diff\n%s\n```\n</details>\n\n"
                         % (rule, x["package"], x["file"], json.dumps((pr or x)["detail"])[:600], x["diff"][:2500]))
        if r.bugs or r.crashes:
            L.append("### Crashes and self-reported bugs\n\n")
            for b in (r.bugs + r.crashes)[:20]:
                L.append("- %s %s: `%s`\n" % (b.get("package"), b.get("file", ""),
                                             (b.get("line") or b.get("stderr", "")).strip().replace("\n", " | ")[-240:]))
            L.append("\n")
    path = os.path.join(out_dir, "report.md")
    open(path, "w").write("".join(L))
    return path
