"""Download the corpus used in the paper: source releases of the most-downloaded PyPI and npm packages."""
from __future__ import annotations

import ast
import io
import json
import os
import tarfile
import urllib.request
import zipfile

from .common import log

TOP_PYPI = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages.min.json"
TOP_NPM = "https://unpkg.com/npm-high-impact@latest/lib/top.js"
UA = {"User-Agent": "linttwin (+https://github.com/sariddangerpowers/linttwin)"}


def _get(url, timeout=300):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def _extract(blob, name, dest):
    os.makedirs(dest, exist_ok=True)
    if name.endswith((".tar.gz", ".tgz")):
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as t:
            t.extractall(dest, filter="data")
    elif name.endswith((".zip", ".whl")):
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            z.extractall(dest)
    elif name.endswith(".tar.bz2"):
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:bz2") as t:
            t.extractall(dest, filter="data")


def download(out_dir, n_pypi=300, n_npm=100):
    """<out_dir>/pypi/<name>/ (latest sdist, or a wheel if there is none) and <out_dir>/npm/<name>/ (latest tarball)."""
    done = {"pypi": 0, "npm": 0}
    if n_pypi:
        for row in json.loads(_get(TOP_PYPI))["rows"][:n_pypi]:
            name = row["project"]
            dest = os.path.join(out_dir, "pypi", name)
            if os.path.exists(dest):
                done["pypi"] += 1
                continue
            try:
                meta = json.loads(_get("https://pypi.org/pypi/%s/json" % name))
                files = meta.get("urls", [])
                pick = next((f for f in files if f["packagetype"] == "sdist"), None) or \
                    next((f for f in files if f["filename"].endswith(".whl")), None)
                if pick:
                    _extract(_get(pick["url"]), pick["filename"], dest)
                    json.dump({"name": name, "version": meta["info"]["version"], "file": pick["filename"]},
                              open(dest + ".json", "w"))
                    done["pypi"] += 1
            except Exception as ex:  # noqa: BLE001
                log("PyPI %s failed: %r" % (name, ex))
    if n_npm:
        src = _get(TOP_NPM).decode("utf-8", "replace")      # an ES module: export const top = ['semver', ...]
        for name in ast.literal_eval(src[src.index("["):src.rindex("]") + 1])[:n_npm]:
            dest = os.path.join(out_dir, "npm", name.replace("/", "__"))
            if os.path.exists(dest):
                done["npm"] += 1
                continue
            try:
                meta = json.loads(_get("https://registry.npmjs.org/%s/latest" % name.replace("/", "%2f")))
                _extract(_get(meta["dist"]["tarball"]), "x.tgz", dest)
                json.dump({"name": name, "version": meta.get("version")}, open(dest + ".json", "w"))
                done["npm"] += 1
            except Exception as ex:  # noqa: BLE001
                log("npm %s failed: %r" % (name, ex))
    return done
