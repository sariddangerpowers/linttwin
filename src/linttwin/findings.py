"""The bugs LintTwin found, as executable reproducers.

`linttwin findings` re-runs every reproducer against the installed tool versions and reports whether each bug still
reproduces, so the list stays honest as the tools evolve.

Optional keys: `source_type` ("module" or "commonjs", the default) is how ESLint parses a JavaScript reproducer; `path`
and `files` place the reproducer, and any files it needs, in a package layout.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile

from . import common as c
from . import js_check
from . import python_check

# ---------------------------------------------------------------- the registry

RUFF_SECOND_PASS = "https://github.com/astral-sh/ruff/issues/29422"     # ten bugs in one issue, as ruff asked
OXC_SECOND_PASS = "https://github.com/oxc-project/oxc/issues/27746"     # twenty bugs in one issue

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
    # --- oxlint: second pass (batch triage), reported together
    dict(id="OX-11", tool="oxlint", rule="no-unused-vars", kind="false report",
         summary="Calls a variable unused when its only use is a call in a ternary branch (or after `&&`/`||`) in a "
                 "non-last element of a comma expression.",
         reference="ESLint counts the call as a use.", found_in="ajv", issue=OXC_SECOND_PASS, check=("parity", {}),
         source="let a = (v) => v;\nmodule.exports = (x, y) => (x ? a(y) : 0, y);\n"),
    dict(id="OX-12", tool="oxlint", rule="class-methods-use-this", kind="false report",
         summary="Reports a method whose only `this` is in a parameter default.",
         reference="ESLint counts `this` in the parameters.", found_in="ajv", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source="export class A {\n  t(errors = this.errors) { return errors; }\n}\n"),
    dict(id="OX-13", tool="oxlint", rule="no-useless-assignment", kind="false and missed reports",
         summary="Reports a class-field write to an outer `let` (`id = ++ID`) and misses a dead initializer that a "
                 "loop condition overwrites after `&&`.",
         reference="ESLint does the opposite in both cases.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source="let ID = 0;\nexport class A {\n  id = ++ID;\n}\nexport function g(s, re) {\n  let m = null;\n"
                "  while (s && (m = re.exec(s))) { s = m[1]; }\n  return s;\n}\n"),
    dict(id="OX-14", tool="oxlint", rule="unicorn/no-array-callback-reference", kind="false report",
         summary="Reports a callback that is a call expression, such as `arr.forEach(make(x))`.",
         reference="eslint-plugin-unicorn ignores every call expression.", found_in="top-100 npm packages",
         issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source="export function f(arr, make, x) {\n  arr.forEach(make(x));\n  return arr.map(make(x));\n}\n"),
    dict(id="OX-15", tool="oxlint", rule="block-scoped-var", kind="false report",
         summary="When a `var` is redeclared in a block, reports the bare outer declaration and a parameter of the same "
                 "name as used outside their binding context.",
         reference="ESLint reports only references.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source="export function f(a) {\n  var x;\n  if (a) { var x; }\n}\nexport function g(a, y) {\n  if (a) { var y; }\n}\n"),
    dict(id="OX-16", tool="oxlint", rule="unicorn/prefer-at", kind="double and missed reports",
         summary="Reports `arr.slice(-1)[0]` twice, and misses it on the right-hand side of an assignment.",
         reference="eslint-plugin-unicorn reports each once.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {"count": True}), source_type="module",
         source="export function f(arr) {\n  return arr.slice(-1)[0];\n}\nexport function g(arr) {\n  let k;\n"
                "  k = arr.slice(-1)[0];\n  return k;\n}\n"),
    dict(id="OX-17", tool="oxlint", rule="sort-imports", kind="missed report",
         summary="Checks only the imports before the first other statement, such as TypeScript's hoisted `var _a`.",
         reference="ESLint checks every import (`allowSeparatedGroups` is false by default).", found_in="yargs-parser",
         issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source='var _a;\nimport { format } from "util";\nimport { normalize, resolve } from "path";\n'
                "export { _a, format, normalize, resolve };\n"),
    dict(id="OX-18", tool="oxlint", rule="unicorn/prefer-string-raw", kind="missed report",
         summary="Skips the string value of a property whose key is not a string literal (`{ b: \"a\\\\b\" }`).",
         reference="eslint-plugin-unicorn reports it.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source='export const o = { b: "a\\\\b" };\nexport const s = "a\\\\b";\nexport const p = { "k": "a\\\\b" };\n'),
    dict(id="OX-19", tool="oxlint", rule="unicorn/prefer-regexp-test", kind="missed report",
         summary="Misses `.match()` as an operand of `&&` or `||` in a condition.",
         reference="eslint-plugin-unicorn reports it.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source="export function f(a, s) {\n  if (a && s.match(/x/)) {}\n  if (s.match(/x/) || a) {}\n"
                "  if (s.match(/x/)) {}\n}\n"),
    dict(id="OX-20", tool="oxlint", rule="prefer-template", kind="missed report",
         summary="Skips a concatenation that has a `+` anywhere above it, across ternaries and function bodies.",
         reference="ESLint merges only directly chained `+` operands.", found_in="top-100 npm packages",
         issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source='export function f(a, b, c) {\n  return a + (b ? "|" + c : "");\n}\n'
                'export const g = (x) => x + [1].map(function (y) { return "v" + y; }).length;\n'
                'export const h = (c) => "|" + c;\n'),
    dict(id="OX-21", tool="oxlint", rule="no-param-reassign", kind="missed report",
         summary="Misses a reassigned rest parameter.",
         reference="ESLint reports it.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source="export function f(...args) {\n  args = args.reverse();\n  return args;\n}\n"
                "export function g(x) {\n  x = 1;\n  return x;\n}\n"),
    dict(id="OX-22", tool="oxlint", rule="max-params", kind="missed report",
         summary="Does not count the rest parameter, so `(a, b, c, ...rest)` passes the default limit of three.",
         reference="ESLint counts it.", found_in="yargs", issue=OXC_SECOND_PASS, check=("parity", {}),
         source_type="module",
         source="export const o = {\n  __n: (a, b, c, ...rest) => rest.length + a + b + c,\n};\n"
                "export function f(a, b, c, ...rest) { return rest; }\nexport function g(a, b, c, d) { return d; }\n"),
    dict(id="OX-23", tool="oxlint", rule="no-loop-func", kind="missed report",
         summary="Misses a function in a loop that reads a `var` declared before the loop and written after it.",
         reference="ESLint treats any write at or after the start of the loop as unsafe.", found_in="tslib",
         issue=OXC_SECOND_PASS, check=("parity", {}),
         source="var done = false;\nvar out = [];\nfor (var i = 0; i < 3; i++) {\n"
                "  out.push(function () { if (done) throw 0; });\n}\ndone = true;\nmodule.exports = out;\n"),
    dict(id="OX-24", tool="oxlint", rule="no-lonely-if", kind="missed report",
         summary="Misses the final `else { if }` of an else-if chain.",
         reference="ESLint reports it.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source="if (a) {} else if (d) {} else { if (b) {} }\n"),
    dict(id="OX-25", tool="oxlint", rule="unicorn/catch-error-name", kind="missed report",
         summary="Skips every unused catch parameter whose name starts with `_`.",
         reference="eslint-plugin-unicorn, like oxlint's own docs, exempts only an unused `_`.", found_in="yargs",
         issue=OXC_SECOND_PASS, check=("parity", {}),
         source="try { y(); } catch (_err) {}\ntry { y(); } catch (_) {}\ntry { y(); } catch (_err) { console.log(_err); }\n"),
    dict(id="OX-26", tool="oxlint", rule="unicorn/prefer-type-error", kind="missed report",
         summary="Misses a type check in parentheses, such as `!(x instanceof Y)`.",
         reference="eslint-plugin-unicorn reports it.", found_in="top-100 npm packages", issue=OXC_SECOND_PASS,
         check=("parity", {}), source_type="module",
         source='export function f(x, Y) {\n  if (!(x instanceof Y)) {\n    throw new Error("bad");\n  }\n}\n'),
    dict(id="OX-27", tool="oxlint", rule="unicorn/prefer-string-replace-all", kind="missed report",
         summary="Misses a global regex held in a variable.",
         reference="eslint-plugin-unicorn resolves the pattern; oxlint keeps that upstream test commented out.",
         found_in="top-100 npm packages", issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source='const RE = /a/g;\nexport const out = s.replace(RE, "b");\nexport const out2 = s.replace(/a/g, "b");\n'),
    dict(id="OX-28", tool="oxlint", rule="unicorn/prefer-native-coercion-functions", kind="missed report",
         summary="Skips object methods and `key: function` properties.",
         reference="eslint-plugin-unicorn reports them; oxlint keeps those upstream tests under a TODO.", found_in="qs",
         issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source="export const o = {\n  p: function (v) { return String(v); },\n  m(v) { return String(v); },\n"
                "  a: (v) => String(v),\n};\n"),
    dict(id="OX-29", tool="oxlint", rule="sort-keys", kind="missed report",
         summary="Skips computed keys with a simple name, such as `[S]`.",
         reference="ESLint sorts them by that name, as its docs say.", found_in="top-100 npm packages",
         issue=OXC_SECOND_PASS, check=("parity", {}), source_type="module",
         source='const S = Symbol("s");\nexport const obj5 = {a: 1, ["c"]: 3, b: 2};\nexport const obj6 = {a: 1, [S]: 3, b: 2};\n'),
    dict(id="OX-30", tool="oxlint", rule="sort-vars", kind="fewer reports",
         summary="Reports a declaration once, where ESLint reports every name that is out of order.",
         reference="ESLint's test for `var c, d, a, b` expects two reports, and oxlint ports that test.",
         found_in="top-100 npm packages", issue=OXC_SECOND_PASS, check=("parity", {"count": True}),
         source="var c, a, b;\n"),
    # --- oxlint: found by `linttwin triage` on ajv 6.15.0, outside the study's corpus (20 Oct 2026)
    dict(id="OX-31", tool="oxlint", rule="no-useless-concat", kind="missed report",
         summary="Misses a concatenation of literals when an operand is in parentheses: `'a' + ('b')`.",
         reference="ESLint reports it; its own test `(foo + 'a') + ('b' + 'c')` expects two reports.",
         found_in="ajv 6.15.0", issue="https://github.com/oxc-project/oxc/issues/27982", check=("parity", {}),
         source="var a = 'a' + ('b');\nvar b = ('a') + 'b';\n"),
    dict(id="OX-32", tool="oxlint", rule="no-unassigned-vars", kind="false report",
         summary="Reports a variable that a later `var` redeclaration assigns: `var x; var x = k;`.",
         reference="ESLint counts the redeclaration's initializer as a write.",
         found_in="ajv 6.15.0", issue="https://github.com/oxc-project/oxc/issues/27982", check=("parity", {}),
         source="function f(k) {\n  var x;\n  var x = k;\n  return x;\n}\nf(1);\n"),
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
    # --- ruff: second pass (batch triage and ruff's own fix errors), reported together
    dict(id="RF-5", tool="ruff", rule="UP034", kind="safe fix breaks code",
         summary="Removing the parentheses around a generator expression that is a class's only base gives "
                 "`class Foo(base for base in bases):`, which does not parse; ruff reverts the fix.",
         reference="The parentheses are needed there.", found_in="ruff 0.17.0 (a parser fixture in its sdist)",
         issue=RUFF_SECOND_PASS, check=("fix_error", {}),
         source="bases = (object,)\n\n\nclass Foo((base for base in bases)):\n    pass\n"),
    dict(id="RF-6", tool="ruff", rule="F402", kind="missed report",
         summary="Misses a loop variable that shadows an import when the loop is inside an `if` (since ruff 0.1.12).",
         reference="pyflakes reports it; it skips only mutually exclusive branches.",
         found_in="httplib2, more-itertools, mpmath, litellm, numpy", issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="from os import path\n\n\ndef f(xs):\n    for path in xs:\n        pass\n\n\n"
                "def g(xs, c):\n    if c:\n        for path in xs:\n            pass\n"),
    dict(id="RF-7", tool="ruff", rule="F823", kind="missed report",
         summary="Misses a read of a global before a local assignment when the function assigns the name more than once.",
         reference="pyflakes reports it; the code raises UnboundLocalError.", found_in="black, ruff (test fixtures)",
         issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="x = 1\n\n\ndef f():\n    print(x)\n    x = 2\n\n\ndef g():\n    print(x)\n    x = 2\n    x = 3\n"),
    dict(id="RF-8", tool="ruff", rule="B012", kind="missed report",
         summary="Misses a `return` in an `else` branch or an `except` handler inside `finally`.",
         reference="flake8-bugbear reports every one.", found_in="multiprocess, prompt_toolkit",
         issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="def f(a):\n    try:\n        pass\n    finally:\n        if a:\n            pass\n        else:\n"
                "            return 1\n\n\ndef g():\n    try:\n        pass\n    finally:\n        try:\n"
                "            pass\n        except ValueError:\n            return 2\n"),
    dict(id="RF-9", tool="ruff", rule="SIM102", kind="missed report",
         summary="Misses a collapsible `elif` when the first branch has more than one statement.",
         reference="flake8-simplify reports it.", found_in="top-300 PyPI packages", issue=RUFF_SECOND_PASS,
         check=("py_parity", {}),
         source="def f(a, c, d):\n    if a:\n        print(a)\n        print(c)\n    elif c:\n        if d:\n"
                "            print(d)\n\n\ndef g(a, c, d):\n    if a:\n        print(a)\n    elif c:\n        if d:\n"
                "            print(d)\n"),
    dict(id="RF-10", tool="ruff", rule="SIM401", kind="false report",
         summary="Reports the expression form on receivers that are not known dicts, including `self` in a dict "
                 "subclass's own `get`, where the unsafe fix recurses forever.",
         reference="flake8-simplify does not; ruff limits the statement form to known dicts.",
         found_in="top-300 PyPI packages", issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="class Cache(dict):\n    def get(self, key, default=None):\n"
                "        return self[key] if key in self else default\n"),
    dict(id="RF-11", tool="ruff", rule="PLW1641", kind="missed and false reports",
         summary="Ignores chained assignments: misses `__eq__ = __ne__ = op` and reports a class that sets "
                 "`__hash__ = _h = None`.",
         reference="pylint's eq_without_hash extension reads every binding.", found_in="dateutil, numpy",
         issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="def op(a, b):\n    return a is b\n\n\nclass A:\n    __eq__ = __ne__ = op\n\n\nclass B:\n"
                "    __eq__ = op\n\n\nclass F:\n    __eq__ = op\n    __hash__ = _h = None\n"),
    dict(id="RF-12", tool="ruff", rule="PLR1736", kind="missed report",
         summary="Does not check a comprehension's `if` clauses, nor an `enumerate()` that is not its first `for`.",
         reference="pylint reports both.", found_in="sympy", issue=RUFF_SECOND_PASS, check=("py_parity", {}),
         source="def f(xs):\n    return [1 for i, x in enumerate(xs) if xs[i]]\n\n\n"
                "def g(xs, ys):\n    return [xs[i] for _ in ys for i, x in enumerate(xs)]\n"),
    dict(id="RF-13", tool="ruff", rule="PLW0406", kind="missed report",
         summary="Misses `from <this module> import <name>`, the example in ruff's own documentation.",
         reference="pylint reports it.", found_in="top-300 PyPI packages", issue=RUFF_SECOND_PASS,
         check=("py_parity", {}), path="pkg/mod.py", files={"pkg/__init__.py": ""},
         source="from pkg.mod import foo\nfrom .mod import foo as f2\n\n\ndef foo(): ...\n"),
    dict(id="RF-14", tool="ruff", rule="N801", kind="false report",
         summary="Flags a CapWords class name with a trailing underscore (`Fine_`).",
         reference="pep8-naming strips underscores at both ends.", found_in="top-300 PyPI packages",
         issue=RUFF_SECOND_PASS, check=("py_parity", {}), source="class Fine_:\n    pass\n"),
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
    dict(id="BI-5", tool="biome", rule="no-case-declarations", kind="false report",
         summary="`noSwitchDeclarations` reports a `var` declaration in a switch clause, which ESLint documents as valid.",
         reference="ESLint's `no-case-declarations` covers only lexical declarations.", found_in="ajv 6.15.0",
         issue="https://github.com/biomejs/biome/issues/12475", check=("migration", {}),
         source="var a = 1;\nswitch (a) {\n  case 1:\n    var x = 1;\n    break;\n}\n"),
]


# ---------------------------------------------------------------- checks

def _tmpfiles(f):
    """Write the reproducer, and any files it needs, to a new directory -> (directory, reproducer path)."""
    d = tempfile.mkdtemp(prefix="linttwin_f_")
    rel = f.get("path") or ("repro.js" if f["tool"] in ("oxlint", "biome") else "repro.py")
    for name, text in [*f.get("files", {}).items(), (rel, f["source"])]:
        os.makedirs(os.path.dirname(os.path.join(d, name)), exist_ok=True)
        c.wr(os.path.join(d, name), text)
    return d, os.path.join(d, rel)


def _lines(lines, count):
    # the lines that have reports; with `count`, one entry per report, so that two reports on a line differ from one
    return sorted(lines) if count else sorted(set(lines))


def _eslint_lines(node, path, rule, source_type="commonjs", count=False):
    res = node.helper("eslint", {"cwd": os.path.dirname(path), "sourceType": source_type, "files": [path],
                                 "rules": {rule: "error"}, "inline": False})
    return _lines([m["line"] for r in res for m in r["msgs"] if m["rule"] == rule], count)


def _oxlint_lines(tc, path, rule, count=False):
    cfg = path + ".oxlintrc.json"
    js_check.oxlint_config([rule], cfg)
    diags, _ = js_check.run_oxlint(tc.js("oxlint"), cfg, [path], cwd=os.path.dirname(path))
    return _lines([lb.get("span", {}).get("line", 0) for d in diags or [] if js_check.ox_rule(d.get("code")) == rule
                   for lb in (d.get("labels") or [{}])[:1]], count)


def _python_lines(tc, path, rule, rcdir, count=False):
    """-> (reference tool, its report lines, ruff's report lines) for one rule: pylint for PL codes, else flake8."""
    rj, _, _ = python_check.ruff_json(tc.py("ruff"), [path], ["--select", rule])
    ruff = _lines([x["location"]["row"] for x in rj if x["code"] == rule], count)
    if rule.startswith("PL"):
        o = python_check.options(tc, pylint=True, rcdir=rcdir)
        rows, _, _ = python_check.pylint_rows(o["pylint"], [path], [rule[2:]], o["rcfile"], o["pl_ext"])
        return "pylint", _lines([r[1] for r in rows if r[2] == rule], count), ruff
    rows, _, _ = python_check.flake8_rows(tc.py("flake8"), [path], [rule])
    return "flake8", _lines([r[1] for r in rows if r[2] == rule], count), ruff


def check(f: dict, tc) -> tuple:
    """-> (reproduces: bool, evidence: str)."""
    kind, args = f["check"]
    node = js_check.Node(tc)
    d, p = _tmpfiles(f)
    st = f.get("source_type", "commonjs")
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
            e = _eslint_lines(node, p, f["rule"], st, args.get("count"))
            o = _oxlint_lines(tc, p, f["rule"], args.get("count"))
            return e != o, "ESLint lines %s, oxlint lines %s" % (e, o)
        if kind == "py_parity":
            ref, e, r = _python_lines(tc, p, f["rule"], d, args.get("count"))
            return e != r, "%s lines %s, ruff lines %s" % (ref, e, r)
        if kind == "fix_error":
            r = subprocess.run([tc.py("ruff"), "check", "--isolated", "--no-cache", "--select", f["rule"], "--fix", p],
                               capture_output=True, text=True)
            err = next((l.strip() for l in r.stderr.splitlines() if "introduced a syntax error" in l.lower()), "")
            return bool(err), err or "fix applied without errors"
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
            e = _eslint_lines(node, p, f["rule"], st)
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
