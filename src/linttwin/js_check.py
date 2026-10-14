"""oxlint and Biome against ESLint (core rules + eslint-plugin-unicorn), and their safe fixes.

Rule pairs come from the rewrites' own claims:
  - oxlint: every non-type-aware oxlint rule whose name is an ESLint core or unicorn rule (not deprecated upstream);
  - Biome: `biome migrate eslint` (no inspired or nursery rules), run on each ESLint/unicorn rule alone, gives the Biome
    rule that Biome declares the same; one migration of all of them gives the options Biome uses to match ESLint.
Both tools run with default options, browser + node globals and no project configuration. ESLint parses each file as
Node would (.mjs or package "type": "module" -> module, else commonjs; the other type if that fails); files neither
parses are skipped. Diagnostics are matched as multisets on (file, rule, line), then greedily within 2 lines (any
oxlint label line counts). For Biome, ESLint runs with inline configuration off, since Biome ignores ESLint directives.

Safe fixes (oxlint --fix / biome lint --write) are applied to a copy. A changed file violates the promise if it no
longer parses (espree, same source type), lost or altered a comment, or gained an ESLint `no-undef` error. Each
violation is attributed by re-applying every fixable rule that fired on the file alone.
"""
from __future__ import annotations

import collections
import json
import os
import re
import shutil
import subprocess
import tempfile

from . import common as c

HELPER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "js_helper.mjs")
OX_CATEGORIES = ["correctness", "nursery", "pedantic", "perf", "restriction", "style", "suspicious"]
FIX_IGNORE = {"capitalized-comments"}        # its fix rewrites comments by design
FILE_RULES = {"max-lines", "unicorn/filename-case", "unicorn/no-empty-file"}   # one report per file
GH = re.compile(r"^::(\w+) title=([^,]+),file=(.*),line=(\d+),endLine=\d+,col=\d+,endColumn=\d+::(.*)$")
CHUNK = 150


class Node:
    def __init__(self, tc):
        self.tc = tc

    def helper(self, cmd, payload):
        d = tempfile.mkdtemp(prefix="linttwin_js_")
        try:
            i, o = os.path.join(d, "in.json"), os.path.join(d, "out.json")
            json.dump(payload, open(i, "w"))
            r = subprocess.run([self.tc.node, HELPER, str(self.tc.js_dir), cmd, i, o], capture_output=True, text=True)
            if r.returncode != 0 or not os.path.exists(o):
                raise RuntimeError("js helper '%s' failed: %s" % (cmd, (r.stderr or r.stdout)[-1500:]))
            return json.load(open(o))
        finally:
            shutil.rmtree(d, ignore_errors=True)

    def eslint_rules(self):
        """{"core": {name: {deprecated, fixable}}, "unicorn": {...}} from the installed ESLint and unicorn."""
        probe = tempfile.mktemp(suffix=".mjs", prefix="linttwin_rules_")
        open(probe, "w").write(
            "import { createRequire } from 'node:module'; import { pathToFileURL } from 'node:url';\n"
            "const require = createRequire(%r);\n" % os.path.join(str(self.tc.js_dir), "package.json")
            + "const { builtinRules } = require('eslint/use-at-your-own-risk');\n"
            "const u = (await import(pathToFileURL(require.resolve('eslint-plugin-unicorn')).href)).default;\n"
            "const out = {core: {}, unicorn: {}};\n"
            "for (const [k, v] of builtinRules) out.core[k] = {deprecated: !!(v.meta && v.meta.deprecated)};\n"
            "for (const [k, v] of Object.entries(u.rules)) out.unicorn[k] = {deprecated: !!(v.meta && v.meta.deprecated)};\n"
            "console.log(JSON.stringify(out));\n")
        try:
            r = subprocess.run([self.tc.node, probe], capture_output=True, text=True)
            if r.returncode != 0:
                raise RuntimeError("ESLint rule probe failed: " + r.stderr[-1000:])
            return json.loads(r.stdout)
        finally:
            os.remove(probe)


# ---------------------------------------------------------------- rule pairs

def oxlint_pairs(tc, node):
    em = node.eslint_rules()
    ox = json.loads(subprocess.run([tc.js("oxlint"), "--rules", "--format", "json"], capture_output=True, text=True).stdout)
    pairs, fixable = {}, set()
    for r in ox:
        if r.get("type_aware"):
            continue
        if r["scope"] == "eslint" and r["value"] in em["core"] and not em["core"][r["value"]]["deprecated"]:
            name = r["value"]
        elif r["scope"] == "unicorn" and r["value"] in em["unicorn"] and not em["unicorn"][r["value"]]["deprecated"]:
            name = "unicorn/" + r["value"]
        else:
            continue
        pairs[name] = name
        if "fix" in r.get("fix", "") and "dangerous" not in r.get("fix", ""):
            fixable.add(name)
    return pairs, fixable


def _biome_migrate(biome, rules):
    d = tempfile.mkdtemp(prefix="linttwin_bm_")
    try:
        json.dump({"root": True, "plugins": ["unicorn"], "rules": {r: "error" for r in rules}},
                  open(os.path.join(d, ".eslintrc.json"), "w"))
        open(os.path.join(d, "biome.json"), "w").write("{}")
        subprocess.run([biome, "migrate", "eslint", "--write"], cwd=d, capture_output=True, text=True)
        return json.load(open(os.path.join(d, "biome.json"))).get("linter", {}).get("rules", {})
    finally:
        shutil.rmtree(d, ignore_errors=True)


def biome_pairs(tc, node, cfg_dir):
    """ESLint rule -> Biome rule as declared by `biome migrate eslint`; writes the migrated config to cfg_dir. The
    rule-by-rule migration takes a minute or two, so it is cached per Biome / ESLint / unicorn version."""
    em = node.eslint_rules()
    biome = tc.js("biome")
    v = tc.versions()
    cache = tc.prefix / "cache" / ("biome-pairs-%s-eslint-%s-unicorn-%s.json"
                                   % (v.get("@biomejs/biome"), v.get("eslint"), v.get("eslint-plugin-unicorn")))
    if cache.exists():
        pairs = json.loads(cache.read_text())
    else:
        all_rules = [k for k, x in em["core"].items() if not x["deprecated"]] + \
                    ["unicorn/" + k for k, x in em["unicorn"].items() if not x["deprecated"]]
        c.log("biome: reading the ESLint -> Biome rule mapping from `biome migrate eslint` (%d rules; once per version)"
              % len(all_rules))
        pairs = {}
        for r in all_rules:
            got = [g + "/" + k for g, x in _biome_migrate(biome, [r]).items() if isinstance(x, dict) for k in x]
            if got:
                pairs[r] = got[0]
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(pairs, indent=1))
    os.makedirs(cfg_dir, exist_ok=True)
    json.dump({"vcs": {"enabled": False}, "files": {"ignoreUnknown": True, "maxSize": 5000000},
               "formatter": {"enabled": False}, "assist": {"enabled": False},
               "linter": {"enabled": True, "rules": _biome_migrate(biome, sorted(pairs))}},
              open(os.path.join(cfg_dir, "biome.json"), "w"))
    return pairs


def oxlint_config(rules, path):
    cfg = {"plugins": ["eslint", "unicorn"], "categories": {k: "off" for k in OX_CATEGORIES},
           "env": {"browser": True, "node": True, "es2021": True},
           "rules": {r if r.startswith("unicorn/") else "eslint/" + r: "error" for r in rules}}
    json.dump(cfg, open(path, "w"))


def run_oxlint(oxlint, cfg, files, fix=False, cwd=None):
    cmd = [oxlint, "-c", cfg, "--format", "json", "--no-ignore", "--disable-nested-config", "--threads", "1"]
    if fix:
        cmd.append("--fix")
    r = subprocess.run(cmd + files, capture_output=True, text=True, cwd=cwd)
    try:
        diags = json.loads(r.stdout).get("diagnostics", [])
    except json.JSONDecodeError:
        return [], (r.stdout + r.stderr)[-1500:]
    for d in diags:                             # oxlint prints file names relative to its working directory
        if d.get("filename"):
            d["filename"] = os.path.normpath(os.path.join(cwd or os.getcwd(), d["filename"]))
    return diags, r.stderr


def ox_rule(code):
    if not code or "(" not in code:
        return None
    plug, name = code.split("(", 1)
    name = name.rstrip(")")
    return name if plug == "eslint" else "%s/%s" % (plug, name)


def run_biome(biome, cfg_dir, files, write=False, only=None):
    cmd = [biome, "lint", "--config-path=" + cfg_dir, "--reporter=github", "--max-diagnostics=none",
           "--diagnostic-level=info"]
    if write:
        cmd.append("--write")
    if only:
        cmd.append("--only=" + only)
    r = subprocess.run(cmd + files, capture_output=True, text=True)
    out = []
    for line in r.stdout.splitlines():
        m = GH.match(line)
        if m:
            out.append((m.group(2), m.group(3), int(m.group(4)), m.group(5)))
    return out, r


def match(e_list, o_list):
    """multiset match per rule. e_list: [(rule, line)] from ESLint; o_list: [(rule, (lines...))] from the rewrite.
    Pass 1: the ESLint line is one of the rewrite's label lines; pass 2: the closest label line within 2 lines."""
    by_e, by_o = collections.defaultdict(list), collections.defaultdict(list)
    for r, ln in e_list:
        by_e[r].append(ln)
    for r, lns in o_list:
        by_o[r].append(lns)
    both, e_left, o_left = collections.Counter(), [], []
    for r in set(by_e) | set(by_o):
        es, os_ = sorted(by_e.get(r, [])), by_o.get(r, [])
        used = [False] * len(os_)
        rest = []
        for ln in es:
            j = next((j for j, lns in enumerate(os_) if not used[j] and ln in lns), None)
            if j is None:
                rest.append(ln)
            else:
                used[j] = True
                both[r] += 1
        for ln in rest:
            best, bd = None, 3
            for j, lns in enumerate(os_):
                if not used[j]:
                    dd = min(abs(x - ln) for x in lns)
                    if dd < bd:
                        best, bd = j, dd
            if best is None:
                e_left.append((r, ln))
            else:
                used[best] = True
                both[r] += 1
        o_left.extend((r, os_[j][0]) for j in range(len(os_)) if not used[j])
    return both, e_left, o_left


# ---------------------------------------------------------------- one chunk of one package

def check_chunk(job):
    tool, pkg, root, files, opts = job
    tc = opts["tc"]
    node = Node(tc)
    pairs = opts["pairs"]                          # ESLint rule -> rewrite rule
    inv = collections.defaultdict(list)
    for e, r in pairs.items():
        inv[r].append(e)
    out = {"counts": collections.Counter(), "divergences": [], "fixes": [], "bugs": [], "crashes": [],
           "stats": collections.Counter()}
    cache = {}
    cls = node.helper("classify", [{"path": f, "hint": "module" if f.endswith(".mjs") or (
        not f.endswith(".cjs") and c.nearest_package_type(f, root, cache) == "module") else "commonjs"} for f in files])
    st = {x["path"]: x["sourceType"] for x in cls if x["sourceType"]}
    files = [f for f in files if f in st]
    if not files:
        return out
    work = tempfile.mkdtemp(prefix="linttwin_w_")
    try:
        # ---- the rewrite's diagnostics
        R = collections.defaultdict(list)
        if tool == "oxlint":
            cfg = os.path.join(work, "oxlintrc.json")
            oxlint_config(sorted(pairs), cfg)
            diags, err = run_oxlint(opts["bin"], cfg, files, cwd=root)
            if err.strip() and not diags and "panicked" in err:
                out["crashes"].append({"tool": tool, "package": pkg, "file": "(chunk)", "stderr": err[-500:]})
            bad = set()
            for d in diags:
                rule = ox_rule(d.get("code"))
                if rule is None:
                    bad.add(d.get("filename"))
                    continue
                lines = tuple(lb.get("span", {}).get("line", 0) for lb in (d.get("labels") or [{}]))
                R[d["filename"]].append((rule, lines, d.get("message", "")))
            files = [f for f in files if f not in bad]
        else:
            diags, _ = run_biome(opts["bin"], opts["cfg_dir"], files)
            bad = {fn for title, fn, _, _ in diags if title == "parse"}
            files = [f for f in files if f not in bad]
            for title, fn, ln, msg in diags:
                if title.startswith("lint/") and fn not in bad:
                    R[fn].append((title[5:], (ln,), msg))
        out["stats"]["files_compared"] += len(files)
        # ---- ESLint's diagnostics, mapped to the rewrite's rule names
        E = {}
        for stype in ("module", "commonjs"):
            fs_ = [f for f in files if st[f] == stype]
            if not fs_:
                continue
            res = node.helper("eslint", {"cwd": root, "sourceType": stype, "files": fs_,
                                         "rules": {r: "error" for r in pairs}, "inline": tool != "biome"})
            for r in res:
                if any(m["fatal"] for m in r["msgs"]):
                    E[r["path"]] = None
                    continue
                seen, rows = set(), []
                for m in r["msgs"]:
                    t = pairs.get(m["rule"])
                    if t and (t, m["line"]) not in seen:
                        seen.add((t, m["line"]))
                        rows.append((t, m["line"], "%s: %s" % (m["rule"], m["msg"])))
                E[r["path"]] = rows
        for f in files:
            if E.get(f, []) is None:
                continue
            el, rl = E.get(f, []), R.get(f, [])
            both, e_left, r_left = match([(r, 0 if r in FILE_RULES else ln) for r, ln, _ in el],
                                         [(r, (0,) if r in FILE_RULES else lns) for r, lns, _ in rl])
            for r, k in both.items():
                out["counts"][("eslint", r, "both")] += k
            if e_left or r_left:
                text = c.rd(f)
                rel = os.path.relpath(f, root)
                for side, left, raw in (("reference_only", e_left, el), ("%s_only" % tool, r_left, rl)):
                    for r, ln in left:
                        out["counts"][("eslint", r, side)] += 1
                        msg = next((m for r2, l2, m in raw if r2 == r and (l2 == ln or isinstance(l2, tuple) and l2[0] == ln)), "")
                        out["divergences"].append({"tool": tool, "reference": "eslint", "package": pkg, "file": rel,
                                                   "rule": r, "eslint_rules": inv.get(r, [r]), "side": side, "line": ln,
                                                   "message": msg, "source_type": st[f], "context": c.context(text, ln)})
        # ---- safe fixes
        if not opts.get("no_fixes"):
            check_fixes(tool, pkg, root, files, st, R, opts, node, work, out)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    return out


def check_fixes(tool, pkg, root, files, st, R, opts, node, work, out):
    orig_dir, fix_dir = os.path.join(work, "orig"), os.path.join(work, "fix")
    rels = [os.path.relpath(f, root) for f in files]
    for d_ in (orig_dir, fix_dir):
        for rel in rels:
            os.makedirs(os.path.dirname(os.path.join(d_, rel)), exist_ok=True)
            shutil.copyfile(os.path.join(root, rel), os.path.join(d_, rel))
    if tool == "oxlint":
        fcfg = os.path.join(work, "oxlintrc_fix.json")
        oxlint_config([r for r in opts["pairs"] if r not in FIX_IGNORE], fcfg)
        run_oxlint(opts["bin"], fcfg, [os.path.join(fix_dir, r) for r in rels], fix=True, cwd=fix_dir)
    else:
        _, r = run_biome(opts["bin"], opts["cfg_dir"], [os.path.join(fix_dir, x) for x in rels], write=True)
        if "panicked" in (r.stderr or "").lower():
            out["crashes"].append({"tool": tool, "package": pkg, "file": "(fix pass)", "stderr": r.stderr[-500:]})
    changed = [x for x in rels if c.rd(os.path.join(fix_dir, x)) != c.rd(os.path.join(orig_dir, x))]
    out["stats"]["files_changed"] += len(changed)
    if not changed:
        return
    orc = node.helper("oracle", [{"orig": os.path.join(orig_dir, x), "fixed": os.path.join(fix_dir, x),
                                  "sourceType": st[os.path.join(root, x)]} for x in changed])
    undef = {}
    for side, d_ in (("orig", orig_dir), ("fix", fix_dir)):
        for stype in ("module", "commonjs"):
            fs_ = [os.path.join(d_, x) for x in changed if st[os.path.join(root, x)] == stype]
            if fs_:
                for res in node.helper("eslint", {"cwd": d_, "sourceType": stype, "files": fs_,
                                                  "rules": {"no-undef": "error"}, "inline": False}):
                    undef[(side, os.path.relpath(res["path"], d_))] = collections.Counter(
                        m["msg"] for m in res["msgs"] if m["rule"] == "no-undef")
    for x, o in zip(changed, orc):
        v = {}
        if o["syntax"]:
            v["syntax"] = o["syntax"]
        if o["lost"]:
            v["comment_lost"] = o["lost"]
        nu = undef.get(("fix", x), collections.Counter()) - undef.get(("orig", x), collections.Counter())
        if nu:
            v["undefined_name"] = sorted(nu)[:10]
        if not v:
            continue
        out["stats"]["fix_violations"] += 1
        src = c.rd(os.path.join(orig_dir, x))
        fired = sorted({r for r, _, _ in R.get(os.path.join(root, x), [])
                        if (tool == "biome" or r in opts["fixable"]) and r not in FIX_IGNORE})
        hits, hdiff = [], ""
        for rule in fired:
            one = tempfile.mkdtemp(prefix="linttwin_1_")
            try:
                p = os.path.join(one, "x", x)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                c.wr(p, src)
                if tool == "oxlint":
                    c1 = os.path.join(one, "c.json")
                    oxlint_config([rule], c1)
                    run_oxlint(opts["bin"], c1, [p], fix=True, cwd=os.path.join(one, "x"))
                else:
                    run_biome(opts["bin"], opts["cfg_dir"], [p], write=True, only=rule)
                f1 = c.rd(p)
                if f1 == src:
                    continue
                po = os.path.join(one, "orig.js")
                c.wr(po, src)
                o1 = node.helper("oracle", [{"orig": po, "fixed": p, "sourceType": st[os.path.join(root, x)]}])[0]
                v1 = {k: o1[k2] for k, k2 in (("syntax", "syntax"), ("comment_lost", "lost")) if o1[k2]}
                if v1:
                    hits.append({"rule": rule, "kinds": sorted(v1), "detail": v1})
                    hdiff = hdiff or c.udiff(src, f1, x)
            finally:
                shutil.rmtree(one, ignore_errors=True)
        out["fixes"].append({"tool": tool, "package": pkg, "file": x, "kinds": sorted(v), "detail": v,
                             "rules": [h["rule"] for h in hits], "per_rule": hits,
                             "diff": hdiff or c.udiff(src, c.rd(os.path.join(fix_dir, x)), x)})


def options(tc, tool, no_fixes=False, cfg_root=None) -> dict:
    node = Node(tc)
    if tool == "oxlint":
        pairs, fixable = oxlint_pairs(tc, node)
        return {"tc": tc, "bin": tc.js("oxlint"), "pairs": pairs, "fixable": fixable, "no_fixes": no_fixes}
    cfg_dir = os.path.join(cfg_root or tempfile.mkdtemp(prefix="linttwin_biome_"), "biome_config")
    pairs = biome_pairs(tc, node, cfg_dir)
    return {"tc": tc, "bin": tc.js("biome"), "pairs": pairs, "fixable": set(pairs.values()), "cfg_dir": cfg_dir,
            "no_fixes": no_fixes}


def jobs_for(tool, package_dirs, opts):
    jobs, skipped, nfiles = [], collections.Counter(), 0
    for root in package_dirs:
        files, sk = c.js_files(root)
        skipped.update(sk)
        nfiles += len(files)
        pkg = os.path.basename(os.path.normpath(root))
        for i in range(0, len(files), CHUNK):
            jobs.append((tool, pkg, root, files[i:i + CHUNK], opts))
    return jobs, skipped, nfiles
