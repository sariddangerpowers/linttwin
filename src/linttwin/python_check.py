"""ruff against the tools it replaces (flake8 + plugins, optionally pylint), and ruff's safe fixes.

Parity: every STABLE ruff rule of the pyflakes (F), pycodestyle (E, W), flake8-bugbear (B), flake8-comprehensions (C4),
flake8-simplify (SIM) and pep8-naming (N) families is run in both tools, isolated from project configuration, on the
same files, line length 88. Diagnostics are matched as multisets on (file, code, line), then on (file, code, innermost
enclosing statement), so different anchoring inside one statement does not count. With `pylint=True`, ruff's stable
`PL*` rules are compared with pylint (all optional pylint extensions loaded).

Safe fixes: `ruff check --select ALL --fix` (safe fixes only) on a copy of the files, minus rules whose fixes rewrite
comments by design. A changed file violates the safe-fix promise if it no longer compiles, lost a comment, gained a
pyflakes undefined name, or breaks a structural invariant (a reachable statement became dead; a statement switched
branch). Each violation is attributed by re-applying every safe-fixable rule of the file alone. Ruff's own
"this indicates a bug in Ruff" messages are recorded too.
"""
from __future__ import annotations

import ast
import collections
import json
import os
import re
import shutil
import subprocess
import tempfile

from . import common as c
from . import invariants

FAMILIES = ("Pyflakes", "pycodestyle", "flake8-bugbear", "flake8-comprehensions", "flake8-simplify", "pep8-naming")
SKIP_PARITY = {"E902", "E999", "W505"}          # I/O error, removed syntax-error code, needs a doc length in both tools
FIX_IGNORE = ["RUF100", "UP009", "PLR2044"]     # safe fixes that remove a comment by design
RUFF_COMMON = ["--isolated", "--no-cache", "--no-respect-gitignore", "--line-length", "88", "--target-version", "py312",
               "--exit-zero"]
RUFF_FILE_NOQA = re.compile(r"^[ \t]*#[ \t]*ruff[ \t]*:[ \t]*noqa", re.I | re.M)   # file-level exemption flake8 ignores
CHUNK = 300


def ruff_rules(tc) -> list:
    return json.loads(subprocess.run([tc.py("ruff"), "rule", "--all", "--output-format", "json"],
                                     capture_output=True, text=True).stdout)


def parity_codes(rules) -> list:
    return sorted(r["code"] for r in rules if r["linter"] in FAMILIES and "Stable" in r["status"]
                  and r["code"] not in SKIP_PARITY)


def pylint_codes(rules) -> list:
    return sorted(r["code"] for r in rules if r["linter"] == "Pylint" and "Stable" in r["status"])


# ---------------------------------------------------------------- tool runners

def ruff_json(ruff, files, extra):
    r = subprocess.run([ruff, "check", *RUFF_COMMON, "--output-format", "json", *extra, *files], capture_output=True,
                       text=True)
    try:
        out = json.loads(r.stdout or "[]")
    except json.JSONDecodeError:
        out = []
    return out, r.stderr, c.finished(r)


def flake8_rows(flake8, files, codes):
    fmt = "%(path)s\t%(row)d\t%(col)d\t%(code)s\t%(text)s"
    r = subprocess.run([flake8, "--isolated", "-j", "1", "--max-line-length", "88", "--select", ",".join(codes),
                        "--format", fmt, "--exit-zero", *files], capture_output=True, text=True)
    rows = []
    for line in r.stdout.splitlines():
        p = line.split("\t", 4)
        if len(p) == 5 and p[1].isdigit():
            rows.append((p[0], int(p[1]), p[3], p[4]))
    # with --exit-zero, flake8 exits non-zero only when it aborts; a plugin crash on one file aborts the whole run and
    # is printed on stdout, with no reports for any file
    if r.returncode != 0:
        return [], (r.stderr + r.stdout)[-800:], False
    return rows, r.stderr, c.finished(r)


def pylint_rows(pylint, files, ids, rcfile, ext):
    r = subprocess.run([pylint, "--rcfile", rcfile, "--load-plugins=" + ",".join(ext), "--disable=all",
                        "--enable=" + ",".join(ids), "--output-format=json", "--jobs=1", "--persistent=n", "--score=n",
                        *files], capture_output=True, text=True)
    want = set(ids)     # pylint also emits pragma and import messages that --disable=all cannot turn off (W0012, ...)
    try:
        rows = [(m["path"], m["line"], "PL" + m["message-id"], m["message"]) for m in json.loads(r.stdout or "[]")
                if m["message-id"] in want]
    except json.JSONDecodeError:
        return [], (r.stdout + r.stderr)[-800:], False
    ok = not (r.returncode & 32) and "traceback (most recent call last)" not in r.stderr.lower()
    return rows, r.stderr, ok


def fix_batch(ruff, paths, extra, content):
    """apply `ruff --fix` to paths; on a crash, restore and fix file by file, leaving crashing files untouched."""
    _, err, ok = ruff_json(ruff, paths, extra + ["--fix"])
    if ok:
        return err, []
    errs, crashed = [], []
    for p in paths:
        c.wr(p, content[p])
        _, e1, ok1 = ruff_json(ruff, [p], extra + ["--fix"])
        errs.append(e1)
        if not ok1:
            crashed.append((p, e1[-500:]))
            c.wr(p, content[p])
    return "\n".join(errs), crashed


def stmt_map(src):
    """line -> start line of the innermost statement containing it."""
    m = {}
    try:
        tree = ast.parse(src)
    except (SyntaxError, RecursionError):
        return m
    nodes = [n for n in ast.walk(tree) if isinstance(n, ast.stmt)]
    nodes.sort(key=lambda n: -((n.end_lineno or n.lineno) - n.lineno))
    for n in nodes:
        for ln in range(n.lineno, (n.end_lineno or n.lineno) + 1):
            m[ln] = n.lineno
    return m


def match(pkg, src, rel, ruff_rows, ref_rows, reference, out):
    """multiset matching of ruff vs reference diagnostics for one file; updates out["counts"] / out["divergences"]."""
    rc = collections.Counter((code, ln) for ln, code, _ in ruff_rows)
    fc = collections.Counter((code, ln) for ln, code, _ in ref_rows)
    both = rc & fc
    for (code, _), k in both.items():
        out["counts"][(reference, code, "both")] += k
    rl, fl = rc - both, fc - both
    if not (rl or fl):
        return
    sm = stmt_map(src)
    rs, fs = collections.Counter(), collections.Counter()
    for (code, ln), k in rl.items():
        rs[(code, sm.get(ln, ln))] += k
    for (code, ln), k in fl.items():
        fs[(code, sm.get(ln, ln))] += k
    b2 = rs & fs
    for (code, _), k in b2.items():
        out["counts"][(reference, code, "both")] += k
    for side, cnt, raw in (("ruff_only", rs - b2, ruff_rows), ("reference_only", fs - b2, ref_rows)):
        for (code, s), k in cnt.items():
            out["counts"][(reference, code, side)] += k
            for ln, code2, msg in raw:
                if code2 == code and sm.get(ln, ln) == s:
                    out["divergences"].append({"tool": "ruff", "reference": reference, "package": pkg, "file": rel,
                                               "rule": code, "side": side, "line": ln, "n": k, "message": msg,
                                               "context": c.context(src, ln)})
                    break


# ---------------------------------------------------------------- one chunk of one package

def check_chunk(job):
    pkg, root, rels, opts = job
    ruff = opts["ruff"]
    src = {r: c.rd(os.path.join(root, r)) for r in rels}
    out = {"counts": collections.Counter(), "divergences": [], "fixes": [], "bugs": [], "crashes": [],
           "stats": collections.Counter()}
    # ---- 1. parity
    par = [r for r in rels if not RUFF_FILE_NOQA.search(src[r])]
    out["stats"]["files_compared"] += len(par)
    if par:
        pfiles = [os.path.join(root, r) for r in par]
        rj, crash_r = c.batch(lambda fs: ruff_json(ruff, fs, ["--select", ",".join(opts["codes"])]), pfiles)
        frows, crash_f = c.batch(lambda fs: flake8_rows(opts["flake8"], fs, opts["codes"]), pfiles)
        refs = [("flake8", frows, crash_f)]
        if opts.get("pylint"):
            pj, crash_rp = c.batch(lambda fs: ruff_json(ruff, fs, ["--select", ",".join(opts["pl_codes"])]), pfiles)
            prows, crash_p = c.batch(lambda fs: pylint_rows(opts["pylint"], fs, [x[2:] for x in opts["pl_codes"]],
                                                            opts["rcfile"], opts["pl_ext"]), pfiles)
            refs.append(("pylint", prows, crash_p + crash_rp))
        for tool, lst in [("ruff", crash_r)] + [(n, cr) for n, _, cr in refs]:
            for f, e in lst:
                out["crashes"].append({"tool": tool, "package": pkg, "file": os.path.relpath(f, root), "stderr": e})
        crashed = {f for f, _ in crash_r} | {f for _, _, cr in refs for f, _ in cr}
        R = collections.defaultdict(list)
        for d in rj:
            if d["filename"] not in crashed:
                R[os.path.relpath(d["filename"], root)].append((d["location"]["row"], d["code"], d["message"]))
        if opts.get("pylint"):
            RP = collections.defaultdict(list)
            for d in pj:
                if d["filename"] not in crashed:
                    RP[os.path.relpath(d["filename"], root)].append((d["location"]["row"], d["code"], d["message"]))
        for name, rows, _ in refs:
            F = collections.defaultdict(list)
            for path, row, code, text in rows:
                path = path if os.path.isabs(path) else os.path.join(os.getcwd(), path)
                if path not in crashed:
                    F[os.path.relpath(path, root)].append((row, code, text))
            ruff_side = RP if name == "pylint" else R
            for rel in set(ruff_side) | set(F):
                if rel in src:
                    match(pkg, src[rel], rel, ruff_side.get(rel, []), F.get(rel, []), name, out)
    # ---- 2. safe fixes
    if not opts.get("no_fixes"):
        check_fixes(pkg, root, rels, src, opts, out)
    return out


def check_fixes(pkg, root, rels, src, opts, out):
    ruff = opts["ruff"]
    allx = ["--select", "ALL", "--ignore", ",".join(FIX_IGNORE)]
    tmp = tempfile.mkdtemp(prefix="linttwin_")
    try:
        for r in rels:
            os.makedirs(os.path.dirname(os.path.join(tmp, r)), exist_ok=True)
            c.wr(os.path.join(tmp, r), src[r])
        tfiles = [os.path.join(tmp, r) for r in rels]
        base, _ = c.batch(lambda fs: ruff_json(ruff, fs, allx), tfiles)
        safe = collections.defaultdict(set)
        for d in base:
            if d.get("fix") and d["fix"].get("applicability") == "safe" and d.get("code"):
                safe[os.path.relpath(d["filename"], tmp)].add(d["code"])
        ferr, crashed = fix_batch(ruff, tfiles, allx, {os.path.join(tmp, r): src[r] for r in rels})
        for f, e in crashed:
            out["crashes"].append({"tool": "ruff", "package": pkg, "file": os.path.relpath(f, tmp), "stderr": e})
        for line in ferr.splitlines():
            if any(m in line.lower() for m in c.SELF_REPORTED_BUG):
                out["bugs"].append({"tool": "ruff", "package": pkg, "line": line[:600]})
        fixed = {r: c.rd(os.path.join(tmp, r)) for r in rels}
        changed = [r for r in rels if fixed[r] != src[r]]
        out["stats"]["files_fixed"] += len(rels)
        out["stats"]["files_changed"] += len(changed)
        for r in changed:
            v = violations(src[r], fixed[r])
            if not v:
                continue
            out["stats"]["fix_violations"] += 1
            hits, hdiff = [], ""
            for code in sorted(safe.get(r, ()))[:80]:
                one = tempfile.mkdtemp(prefix="linttwin1_")
                try:
                    p = os.path.join(one, r)
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                    c.wr(p, src[r])
                    ruff_json(ruff, [p], ["--select", code, "--fix"])
                    f1 = c.rd(p)
                    if f1 != src[r]:
                        v1 = violations(src[r], f1, kinds=set(v))
                        if v1:
                            hits.append({"rule": code, "kinds": sorted(v1), "detail": v1})
                            hdiff = hdiff or c.udiff(src[r], f1, r)
                finally:
                    shutil.rmtree(one, ignore_errors=True)
            out["fixes"].append({"tool": "ruff", "package": pkg, "file": r, "kinds": sorted(v), "detail": v,
                                 "rules": [h["rule"] for h in hits], "per_rule": hits,
                                 "diff": hdiff or c.udiff(src[r], fixed[r], r)})
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def violations(orig: str, fixed: str, kinds=None) -> dict:
    """the checks this fix fails. `kinds` (rule attribution) limits the work to the checks that failed for the full fix;
    the syntax check always runs, since the others need code that parses."""
    def want(*ks):
        return kinds is None or any(k in kinds for k in ks)

    v = {}
    e = c.compiles(fixed)
    if e:
        v["syntax"] = e
    if want("comment_lost"):
        co, cf = c.py_comments(orig), c.py_comments(fixed)
        if co is not None and cf is not None:
            lost = co - cf
            if lost:
                v["comment_lost"] = sorted(lost.elements())[:10]
    if "syntax" not in v:
        if want("undefined_name"):
            uf, uo = c.py_undefined_names(fixed), c.py_undefined_names(orig)
            if uf is not None and uo is not None:
                new = uf - uo
                if new:
                    v["undefined_name"] = sorted("%s %s" % (k, a) for (k, a) in new.elements())[:10]
        if want(*invariants.KINDS):
            v.update(invariants.check(orig, fixed))
    return v


def jobs_for(package_dirs, opts):
    jobs, skipped, nfiles = [], collections.Counter(), 0
    for root in package_dirs:
        rels, sk = c.python_files(root)
        skipped.update(sk)
        nfiles += len(rels)
        pkg = os.path.basename(os.path.normpath(root))
        for i in range(0, len(rels), CHUNK):
            jobs.append((pkg, root, rels[i:i + CHUNK], opts))
    return jobs, skipped, nfiles


def options(tc, pylint=False, no_fixes=False, rcdir=None) -> dict:
    rules = ruff_rules(tc)
    opts = {"ruff": tc.py("ruff"), "flake8": tc.py("flake8"), "codes": parity_codes(rules), "no_fixes": no_fixes,
            "rule_names": {r["code"]: r["name"] for r in rules}}
    if pylint:
        ext = subprocess.run([tc.py("python"), "-c", "import pkgutil, pylint.extensions as e; "
                              "print(','.join('pylint.extensions.' + m.name for m in pkgutil.iter_modules(e.__path__) "
                              "if not m.name.startswith('_')))"], capture_output=True, text=True).stdout.strip()
        rcfile = os.path.join(rcdir or tempfile.mkdtemp(prefix="linttwin_rc_"), "empty_pylintrc")
        open(rcfile, "w").write("")
        opts.update(pylint=tc.py("pylint"), pl_codes=pylint_codes(rules), pl_ext=[x for x in ext.split(",") if x],
                    rcfile=rcfile)
    return opts
