"""Small helpers shared by the Python and JavaScript checkers."""
from __future__ import annotations

import collections
import difflib
import io
import json
import os
import subprocess
import sys
import time
import tokenize
import warnings

CRASH_MARKERS = ("overflowed its stack", "panicked", "fatal runtime error", "failed during execution",
                 "traceback (most recent call last)")
SELF_REPORTED_BUG = ("indicates a bug in ruff", "failed to converge", "fix introduced a syntax error")
MAX_PY_BYTES = 1_000_000
MAX_JS_BYTES = 300_000
MAX_JS_LINE = 1000          # longer lines mean minified or bundled output
JS_EXTS = (".js", ".mjs", ".cjs")


def log(msg: str) -> None:
    print("[linttwin %s] %s" % (time.strftime("%H:%M:%S"), msg), file=sys.stderr, flush=True)


def rd(path) -> str:
    with open(path, encoding="utf-8", newline="") as f:      # keep line endings exactly
        return f.read()


def wr(path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def udiff(a: str, b: str, path: str, n: int = 60) -> str:
    d = list(difflib.unified_diff(a.splitlines(), b.splitlines(), path, path, lineterm="", n=2))
    return "\n".join(d[:n]) + ("\n... (%d more lines)" % (len(d) - n) if len(d) > n else "")


def context(text: str, line: int, before: int = 2, after: int = 2, width: int = 300) -> str:
    lines = text.splitlines()
    lo, hi = max(0, line - 1 - before), min(len(lines), line + after)
    return "\n".join("%5d| %s" % (i + 1, lines[i][:width]) for i in range(lo, hi))


def finished(r: subprocess.CompletedProcess) -> bool:
    """the tool exited normally (no abort, panic, stack overflow or plugin crash)."""
    return r.returncode in (0, 1) and not any(m in (r.stderr or "").lower() for m in CRASH_MARKERS)


def batch(run, files):
    """run(files) -> (rows, stderr, finished). One file that crashes a tool must not wipe out the batch: on a crash,
    run file by file. -> (rows from files that finished, [(file, stderr tail) of files that crashed])."""
    rows, _err, ok = run(files)
    if ok:
        return rows, []
    rows, crashed = [], []
    for f in files:
        r1, e1, ok1 = run([f])
        if ok1:
            rows.extend(r1)
        else:
            crashed.append((f, e1[-500:]))
    return rows, crashed


# ---------------------------------------------------------------- Python-source oracles

def compiles(src: str):
    """None if the source compiles with this interpreter, else the error text."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            compile(src, "<f>", "exec", dont_inherit=True)
            return None
        except (SyntaxError, ValueError, RecursionError) as ex:
            return "%s: %s" % (type(ex).__name__, ex)


def py_comments(src: str):
    out = collections.Counter()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT:
                out[tok.string.rstrip()] += 1
    except (tokenize.TokenError, SyntaxError):
        return None
    return out


class _Rep:
    def __init__(self):
        self.msgs = []

    def unexpectedError(self, filename, msg):
        pass

    def syntaxError(self, filename, msg, lineno, offset, text):
        pass

    def flake(self, message):
        self.msgs.append(message)


def py_undefined_names(src: str):
    """pyflakes undefined-name messages, or None if pyflakes cannot analyse the file."""
    from pyflakes import api
    r = _Rep()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            api.check(src, "f.py", r)
        except RecursionError:
            return None
    return collections.Counter((type(m).__name__, m.message_args) for m in r.msgs
                               if type(m).__name__ in ("UndefinedName", "UndefinedLocal", "UndefinedExport"))


# ---------------------------------------------------------------- file discovery

def python_files(root: str):
    """parseable UTF-8 .py files under root (relative paths), plus counts of skipped files."""
    skipped = collections.Counter()
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if not os.path.islink(os.path.join(dp, d)) and d not in (".git", "node_modules", "__pycache__"))
        for fn in sorted(fns):
            if not fn.endswith(".py"):
                continue
            p = os.path.join(dp, fn)
            if os.path.islink(p):
                continue
            if os.path.getsize(p) > MAX_PY_BYTES:
                skipped["too_big"] += 1
                continue
            try:
                src = rd(p)
            except (UnicodeDecodeError, OSError):
                skipped["not_utf8"] += 1
                continue
            if compiles(src):
                skipped["does_not_compile"] += 1
                continue
            out.append(os.path.relpath(p, root))
    return out, skipped


def js_files(root: str):
    """non-minified .js/.mjs/.cjs files under root (absolute paths), plus counts of skipped files."""
    skipped = collections.Counter()
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in ("node_modules", ".git") and not os.path.islink(os.path.join(dp, d)))
        for fn in sorted(fns):
            if not fn.endswith(JS_EXTS) or fn.endswith((".min.js", ".min.mjs", ".min.cjs")):
                continue
            p = os.path.join(dp, fn)
            if os.path.islink(p):
                continue
            if os.path.getsize(p) > MAX_JS_BYTES:
                skipped["too_big"] += 1
                continue
            try:
                s = rd(p)
            except (UnicodeDecodeError, OSError):
                skipped["not_utf8"] += 1
                continue
            if s and max(len(x) for x in s.splitlines() or [""]) > MAX_JS_LINE:
                skipped["minified"] += 1
                continue
            out.append(p)
    return out, skipped


def nearest_package_type(path: str, root: str, cache: dict) -> str:
    """Node's rule: the nearest package.json's "type" ("module" or "commonjs")."""
    d = os.path.dirname(path)
    while True:
        if d in cache:
            return cache[d]
        pj = os.path.join(d, "package.json")
        if os.path.exists(pj):
            try:
                t = json.load(open(pj)).get("type", "commonjs")
            except (OSError, ValueError, AttributeError):
                t = "commonjs"
            cache[d] = t
            return t
        if os.path.abspath(d) == os.path.abspath(root) or d == os.path.dirname(d):
            cache[d] = "commonjs"
            return "commonjs"
        d = os.path.dirname(d)
