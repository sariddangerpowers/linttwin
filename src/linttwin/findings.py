"""The bugs LintTwin found, as executable reproducers.

`linttwin findings` re-runs every reproducer against the installed tool versions and reports whether each bug still
reproduces, so the list stays honest as the tools evolve.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile

from . import common as c
from . import js_check

# ---------------------------------------------------------------- the registry

FINDINGS = [
    # --- oxlint: safe fixes that break code or comments
    dict(id="OX-1", tool="oxlint", rule="no-var", kind="safe fix breaks code",
         summary="A redeclared `var` becomes two `const` declarations: `SyntaxError: Identifier 'x' has already been declared`.",
         reference="ESLint reports both declarations but does not fix a redeclared variable.",
         found_in="iconv-lite 0.7.3", issue="https://github.com/oxc-project/oxc/issues/27694",
         check=("fix_breaks_syntax", {}),
         source="var x = 1;\nvar x = 2;\nconsole.log(x);\n"),
    dict(id="OX-2", tool="oxlint", rule="unicorn/catch-error-name", kind="safe fix breaks code",
         summary="Renames `catch (e)` to `error` although the block already declares `const error`: SyntaxError.",
         reference="eslint-plugin-unicorn renames to `error_`.", found_in="esbuild 0.28.2", issue="https://github.com/oxc-project/oxc/issues/27700",
         check=("fix_breaks_syntax", {}),
         source='try {\n  run();\n} catch (e) {\n  const error = new Error("wrapped", { cause: e });\n  throw error;\n}\n'),
    dict(id="OX-3", tool="oxlint", rule="sort-keys", kind="safe fix alters a comment",
         summary="Moving a property with a trailing comment to the last slot appends the comma inside the comment (`// note,`).",
         reference="ESLint's sort-keys has no autofix.", found_in="ajv 8.20.0, eslint-scope 9.1.2", issue="https://github.com/oxc-project/oxc/issues/27704",
         check=("fix_changes_comments", {}),
         source="const o = {\n  b: 1, // note\n  a: 2,\n};\nconsole.log(o);\n"),
    # --- oxlint: rules that disagree with ESLint
    dict(id="OX-4", tool="oxlint", rule="no-setter-return", kind="missed report",
         summary="Misses a setter that returns a value inside an `Object.defineProperty` descriptor.",
         reference="ESLint reports it (descriptors are documented as covered).", found_in="esbuild 0.28.2", issue="https://github.com/oxc-project/oxc/issues/27710",
         check=("parity", {}),
         source='const o = {};\nlet v;\nObject.defineProperty(o, "x", {\n  get: () => v,\n  set: (nv) => (v = nv),\n});\nmodule.exports = o;\n'),
    dict(id="OX-5", tool="oxlint", rule="no-div-regex", kind="missed report",
         summary="Misses a regex whose leading `=` has a quantifier (`/=+$/`); `/=a/` is caught.",
         reference="ESLint reports both.", found_in="iconv-lite 0.7.3", issue="https://github.com/oxc-project/oxc/issues/27710",
         check=("parity", {}),
         source='module.exports = (s) => s.replace(/=+$/, "");\n'),
    dict(id="OX-6", tool="oxlint", rule="no-self-compare", kind="false report",
         summary="Reports `\"\u0100\" !== \"\\u0100\"` (equal values, different source text), an encoding self-check.",
         reference="ESLint compares tokens and does not report it.", found_in="iconv-lite 0.7.3", issue=None,
         check=("parity", {}),
         source='if ("\u0100" !== "\\u0100") { console.log("bad encoding"); }\n'),
    dict(id="OX-7", tool="oxlint", rule="no-magic-numbers", kind="missed report",
         summary="Treats every unary operator like `-`: `exports.a = void 0` and `exports.b = ~5` go unreported.",
         reference="ESLint reports both (and, like oxlint, skips `-7`).", found_in="14 of the top-100 npm packages",
         issue="https://github.com/oxc-project/oxc/issues/27710", check=("parity", {}),
         source="exports.a = void 0;\nexports.b = ~5;\nexports.c = -7;\n"),
    dict(id="OX-8", tool="oxlint", rule="id-length", kind="missed report",
         summary="Misses short identifiers that are destructuring assignment targets (`[ix, s] = ...`, `[q] = [2]`).",
         reference="ESLint reports them.", found_in="argparse, readable-stream, lru-cache, tslib", issue="https://github.com/oxc-project/oxc/issues/27710",
         check=("parity", {}),
         source='let ix, s;\nfor ([ix, s] of [[1, "a"]]) { console.log(ix, s); }\nlet q;\n[q] = [2];\nconsole.log(q);\n'),
    dict(id="OX-9", tool="oxlint", rule="no-shadow", kind="missed report",
         summary="Misses a named function expression that shadows the variable it initialises through a call.",
         reference="ESLint reports it (`ignoreOnInitialization` defaults to false in both).", found_in="argparse, fs-extra",
         issue=None, check=("parity", {}),
         source="const emptyDir = wrap(async function emptyDir(dir) { return dir; });\nmodule.exports = emptyDir;\n"),
    dict(id="OX-10", tool="oxlint", rule="unicorn/consistent-function-scoping", kind="false report",
         summary="Reports a function that refers to itself through the const it is assigned to.",
         reference="eslint-plugin-unicorn treats that reference as a capture.", found_in="chalk, ignore, pretty-format",
         issue="https://github.com/oxc-project/oxc/issues/27710", check=("parity", {}),
         source="const make = (self) => {\n  const builder = (...args) => builder.apply(null, args);\n  builder.self = self;\n  return builder;\n};\nmodule.exports = make;\n"),
    # --- ruff: safe fixes
    dict(id="RF-1", tool="ruff", rule="RET505", kind="safe fix changes behaviour",
         summary="When an `else` body starts with two or more comments indented differently from the code, the dedent is "
                 "computed from the second comment: the fix either fails with \"Fix introduced a syntax error\" or moves "
                 "code into the `if` block. Also affects RET506, RET507, RET508 and PLW0120.",
         reference="A correct fix dedents the `else` body to the level of the `if`.",
         found_in="sympy 1.14.0 (syntax-error variant)", issue="https://github.com/astral-sh/ruff/issues/29381",
         check=("fix_changes_behaviour", {"call": "f(False)"}),
         source="def f(a):\n    if a:\n        return 1\n    else:\n        # one\n          # two\n        return 2\n"),
    dict(id="RF-2", tool="ruff", rule="PLR5501", kind="safe fix drops a comment",
         summary="Collapsing `else: if` into `elif` deletes a trailing comment on the `else:` line.",
         reference="Ruff marks fixes that would delete comments as unsafe.", found_in="contourpy 1.4.0", issue="https://github.com/astral-sh/ruff/issues/29395",
         check=("fix_drops_comment", {}),
         source="def f(a, b):\n    if a:\n        return 1\n    else:  # explain the fallback\n        if b:\n            return 2\n        else:\n            return 3\n"),
    dict(id="RF-3", tool="ruff", rule="PLW0120", kind="safe fix drops a comment",
         summary="Removing a useless loop `else:` deletes the trailing comment on the `else:` line.",
         reference="Ruff marks fixes that would delete comments as unsafe.", found_in="pydantic 2.14.1", issue="https://github.com/astral-sh/ruff/issues/29395",
         check=("fix_drops_comment", {}),
         source="def f(xs):\n    for x in xs:\n        if x:\n            return x\n    else:  # nothing found\n        return None\n"),
    dict(id="RF-4", tool="ruff", rule="UP035", kind="safe fix drops a comment",
         summary="Rewriting a multi-line `from typing import (` deletes the comment on its first line (here a `noqa`).",
         reference="Ruff marks fixes that would delete comments as unsafe.", found_in="asyncpg 0.32.0", issue="https://github.com/astral-sh/ruff/issues/29400",
         check=("fix_drops_comment", {}),
         source="from typing import (  # noqa: F401\n    Awaitable as Awaitable,\n)\n"),
    # --- Biome
    dict(id="BI-1", tool="biome", rule="one-var", kind="migration inverts a rule",
         summary="`biome migrate eslint` maps `one-var` (default \"always\": combine declarations) to "
                 "`useSingleVarDeclarator`, which enforces the opposite.",
         reference="ESLint reports `let b` (should be combined); the migrated Biome config reports `let c = 1, d = 2`.",
         found_in="80 of the top-100 npm packages", issue="https://github.com/biomejs/biome/issues/12373", check=("migration", {}),
         source="function f() {\n  let a = 1;\n  let b = 2;\n  return a + b;\n}\nfunction g() {\n  let c = 1, d = 2;\n  return c + d;\n}\nmodule.exports = [f, g];\n"),
    dict(id="BI-2", tool="biome", rule="eqeqeq", kind="migration drops checks",
         summary="`biome migrate eslint` maps `eqeqeq` to `noDoubleEquals` with `ignoreNull` left on, so `x == null` "
                 "is no longer reported.",
         reference="ESLint's eqeqeq (\"always\") reports `x == null`.", found_in="24 of the top-100 npm packages",
         issue="https://github.com/biomejs/biome/issues/12374", check=("migration", {}),
         source='function f(a, b, x) {\n  if (typeof a == "object" && typeof b == "object") return 1;\n  if (x == null) return 2;\n  return 3;\n}\nmodule.exports = f;\n'),
    dict(id="BI-3", tool="biome", rule="no-setter-return", kind="missed report",
         summary="`noSetterReturn` misses a returning setter inside an `Object.defineProperty` descriptor (as oxlint, OX-4).",
         reference="ESLint reports it.", found_in="esbuild 0.28.2", issue="https://github.com/biomejs/biome/issues/12375", check=("migration", {}),
         source='const o = {};\nlet v;\nObject.defineProperty(o, "x", {\n  get: () => v,\n  set: (nv) => (v = nv),\n});\nmodule.exports = o;\n'),
]


# ---------------------------------------------------------------- checks

def _tmpfile(name, text):
    d = tempfile.mkdtemp(prefix="linttwin_f_")
    p = os.path.join(d, name)
    c.wr(p, text)
    return d, p


def _eslint_lines(node, path, rule):
    res = node.helper("eslint", {"cwd": os.path.dirname(path), "sourceType": "commonjs", "files": [path],
                                 "rules": {rule: "error"}, "inline": False})
    return sorted({m["line"] for r in res for m in r["msgs"] if m["rule"] == rule})


def _oxlint_lines(tc, path, rule):
    cfg = path + ".oxlintrc.json"
    js_check.oxlint_config([rule], cfg)
    diags, _ = js_check.run_oxlint(tc.js("oxlint"), cfg, [path], cwd=os.path.dirname(path))
    return sorted({lb.get("span", {}).get("line", 0) for d in diags or [] if js_check.ox_rule(d.get("code")) == rule
                   for lb in (d.get("labels") or [{}])[:1]})


def check(f: dict, tc) -> tuple:
    """-> (reproduces: bool, evidence: str)."""
    kind, args = f["check"]
    node = js_check.Node(tc)
    if f["tool"] in ("oxlint", "biome"):
        d, p = _tmpfile("repro.js", f["source"])
    else:
        d, p = _tmpfile("repro.py", f["source"])
    try:
        if kind == "fix_breaks_syntax":
            cfg = p + ".oxlintrc.json"
            js_check.oxlint_config([f["rule"]], cfg)
            js_check.run_oxlint(tc.js("oxlint"), cfg, [p], fix=True, cwd=d)
            r = subprocess.run([tc.node, "--check", p], capture_output=True, text=True)
            err = next((l.strip() for l in r.stderr.splitlines() if l.strip().startswith("SyntaxError")), r.stderr.strip()[:200])
            return r.returncode != 0, ("after --fix: " + err) if r.returncode else "fixed code parses"
        if kind == "fix_changes_comments":
            orig = p + ".orig.js"
            shutil.copyfile(p, orig)
            cfg = p + ".oxlintrc.json"
            js_check.oxlint_config([f["rule"]], cfg)
            js_check.run_oxlint(tc.js("oxlint"), cfg, [p], fix=True, cwd=d)
            o = node.helper("oracle", [{"orig": orig, "fixed": p, "sourceType": "commonjs"}])[0]
            return bool(o["lost"]), ("comment altered: %s" % o["lost"]) if o["lost"] else "comments preserved"
        if kind == "parity":
            e = _eslint_lines(node, p, f["rule"])
            o = _oxlint_lines(tc, p, f["rule"])
            return e != o, "ESLint lines %s, oxlint lines %s" % (e, o)
        if kind == "migration":
            biome = tc.js("biome")
            rules = js_check._biome_migrate(biome, [f["rule"]])
            target = [g + "/" + k for g, v in rules.items() if isinstance(v, dict) for k in v]
            if not target:
                return False, "biome migrate no longer maps %s" % f["rule"]
            cfg_dir = os.path.join(d, "cfg")
            os.makedirs(cfg_dir)
            json.dump({"vcs": {"enabled": False}, "formatter": {"enabled": False}, "assist": {"enabled": False},
                       "linter": {"enabled": True, "rules": rules}}, open(os.path.join(cfg_dir, "biome.json"), "w"))
            diags, _ = js_check.run_biome(biome, cfg_dir, [p])
            b = sorted({ln for title, _, ln, _ in diags if title == "lint/" + target[0]})
            e = _eslint_lines(node, p, f["rule"])
            return e != b, "ESLint %s lines %s; Biome %s lines %s" % (f["rule"], e, target[0], b)
        if kind in ("fix_changes_behaviour", "fix_drops_comment"):
            orig = c.rd(p)
            r = subprocess.run([tc.py("ruff"), "check", "--isolated", "--no-cache", "--select", f["rule"], "--fix", p],
                               capture_output=True, text=True)
            fixed = c.rd(p)
            if kind == "fix_drops_comment":
                co, cf = c.py_comments(orig), c.py_comments(fixed)
                lost = sorted((co - cf).elements()) if co is not None and cf is not None else []
                return bool(lost), ("comment deleted: %s" % lost) if lost else "comments preserved"
            ns1, ns2 = {}, {}
            exec(orig, ns1)
            try:
                exec(fixed, ns2)
                before, after = eval(args["call"], ns1), eval(args["call"], ns2)
            except Exception as ex:  # noqa: BLE001
                return True, "fixed code fails: %r" % ex
            if before != after:
                return True, "%s returns %r before the fix and %r after it" % (args["call"], before, after)
            if "syntax error" in r.stderr.lower():
                return True, "ruff: Fix introduced a syntax error"
            return False, "%s unchanged (%r)" % (args["call"], before)
        raise ValueError(kind)
    finally:
        shutil.rmtree(d, ignore_errors=True)
