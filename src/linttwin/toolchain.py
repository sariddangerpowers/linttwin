"""Install and locate the linters LintTwin compares.

Python linters live in a virtual environment (<prefix>/py), JavaScript linters in an npm prefix (<prefix>/js).
`--pinned` installs the exact versions used in the paper; the default installs the latest releases.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

PINNED_PY = {
    "ruff": "0.17.0",
    "flake8": "7.4.1",
    "flake8-bugbear": "26.9.30",
    "flake8-comprehensions": "3.17.0",
    "flake8-simplify": "0.31.1",
    "pep8-naming": "0.15.1",
    "pycodestyle": "2.15.0",
    "pyflakes": "4.0.3",
    "pylint": "4.1.3",
}
PINNED_JS = {
    "eslint": "10.12.0",
    "@eslint/js": "10.0.1",
    "eslint-plugin-unicorn": "78.0.0",
    "globals": "17.13.0",
    "oxlint": "1.88.0",
    "@biomejs/biome": "2.5.15",
}
DEFAULT_PREFIX = Path(os.environ.get("LINTTWIN_HOME", Path.home() / ".linttwin"))


class ToolchainError(RuntimeError):
    pass


def _run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise ToolchainError("command failed: %s\n%s" % (" ".join(map(str, cmd)), (r.stdout + r.stderr)[-2000:]))
    return r.stdout


def setup(prefix: Path = DEFAULT_PREFIX, pinned: bool = False, log=print) -> dict:
    """create <prefix>/py (Python linters) and <prefix>/js (JavaScript linters); return the installed versions."""
    prefix = Path(prefix).expanduser().resolve()
    py_dir, js_dir = prefix / "py", prefix / "js"
    prefix.mkdir(parents=True, exist_ok=True)
    uv = shutil.which("uv")
    py_pkgs = ["%s==%s" % kv if pinned else kv[0] for kv in PINNED_PY.items()]
    if not (py_dir / "bin" / "python").exists():
        log("creating Python environment in %s" % py_dir)
        if uv:
            _run([uv, "venv", "--python", "3.12", str(py_dir)])
        else:
            _run([sys.executable, "-m", "venv", str(py_dir)])
    log("installing Python linters (%s)" % ("pinned" if pinned else "latest"))
    if uv:
        _run([uv, "pip", "install", "--python", str(py_dir / "bin" / "python"), *py_pkgs])
    else:
        _run([str(py_dir / "bin" / "python"), "-m", "pip", "install", "-q", *py_pkgs])
    npm = shutil.which("npm")
    if not npm or not shutil.which("node"):
        raise ToolchainError("Node.js (node and npm) is required for the JavaScript linters; install Node 20+ first")
    js_dir.mkdir(exist_ok=True)
    if not (js_dir / "package.json").exists():
        (js_dir / "package.json").write_text('{"name": "linttwin-js", "private": true}\n')
    js_pkgs = ["%s@%s" % kv if pinned else "%s@latest" % kv[0] for kv in PINNED_JS.items()]
    log("installing JavaScript linters (%s)" % ("pinned" if pinned else "latest"))
    _run([npm, "install", "--prefix", str(js_dir), "--no-audit", "--no-fund", *js_pkgs])
    tc = Toolchain(prefix)
    versions = tc.versions()
    (prefix / "versions.json").write_text(json.dumps(versions, indent=2) + "\n")
    return versions


class Toolchain:
    """paths to the installed linters."""

    def __init__(self, prefix: Path = DEFAULT_PREFIX):
        self.prefix = Path(prefix).expanduser().resolve()
        self.py_dir = self.prefix / "py"
        self.js_dir = self.prefix / "js"
        self.node = shutil.which("node") or "node"

    def py(self, name: str) -> str:
        p = self.py_dir / "bin" / name
        if not p.exists():
            raise ToolchainError("%s not found in %s; run `linttwin setup` first" % (name, self.py_dir))
        return str(p)

    def js(self, name: str) -> str:
        p = self.js_dir / "node_modules" / ".bin" / name
        if not p.exists():
            raise ToolchainError("%s not found in %s; run `linttwin setup` first" % (name, self.js_dir))
        return str(p)

    def has_python(self) -> bool:
        return (self.py_dir / "bin" / "ruff").exists() and (self.py_dir / "bin" / "flake8").exists()

    def has_js(self) -> bool:
        return (self.js_dir / "node_modules" / "eslint").exists()

    def versions(self) -> dict:
        out = {}

        def ver(cmd):
            try:
                return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout.strip().splitlines()[0]
            except (OSError, IndexError, subprocess.TimeoutExpired):
                return None

        def last_word(s):
            return s.split()[-1] if s else s

        def first_word(s):
            return s.split()[0] if s else s

        if self.has_python():
            out["ruff"] = last_word(ver([self.py("ruff"), "--version"]))
            out["flake8"] = first_word(ver([self.py("flake8"), "--version"]))
            if (self.py_dir / "bin" / "pylint").exists():
                out["pylint"] = last_word(ver([self.py("pylint"), "--version"]))
        if self.has_js():
            for pkg in ("eslint", "eslint-plugin-unicorn", "oxlint", "@biomejs/biome"):
                pj = self.js_dir / "node_modules" / pkg / "package.json"
                if pj.exists():
                    out[pkg] = json.loads(pj.read_text()).get("version")
            out["node"] = (ver([self.node, "--version"]) or "").lstrip("v") or None
        return out
