"""linttwin: do Rust-rewritten linters keep their promises?

    linttwin setup [--pinned]                 install the linters to compare (latest, or the paper's versions)
    linttwin check DIR [DIR ...]              compare ruff / oxlint / Biome with the tools they replace, and test
                                              their safe fixes, on the given projects
    linttwin findings                         re-run the reproducers of every bug LintTwin found
    linttwin corpus --dir corpus              download the paper's corpus (top PyPI and npm packages)
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import os
import sys
import tempfile
import time

from . import __version__
from . import common as c
from . import report
from .toolchain import DEFAULT_PREFIX, Toolchain, ToolchainError, setup

BOLD, DIM, RED, GREEN, RESET = ("\033[1m", "\033[2m", "\033[31m", "\033[32m", "\033[0m") if sys.stdout.isatty() else ("",) * 5


def _run_pool(fn, jobs, n, label):
    outs = []
    t0 = time.time()
    with cf.ProcessPoolExecutor(max_workers=n) as ex:
        futs = [ex.submit(fn, j) for j in jobs]
        for i, fu in enumerate(cf.as_completed(futs), 1):
            try:
                outs.append(fu.result())
            except Exception as e:  # noqa: BLE001
                c.log("%s: a chunk failed: %r" % (label, e))
            if i % 10 == 0 or i == len(futs):
                c.log("%s: %d/%d chunks (%.0fs)" % (label, i, len(futs), time.time() - t0))
    return outs


def cmd_check(a):
    tc = Toolchain(a.prefix)
    dirs = [os.path.abspath(d) for d in a.dirs]
    for d in dirs:
        if not os.path.isdir(d):
            sys.exit("not a directory: %s" % d)
    tools = ["ruff", "oxlint", "biome"] if a.tool == "all" else [a.tool]
    work = tempfile.mkdtemp(prefix="linttwin_cfg_")
    results = []
    for tool in tools:
        if tool == "ruff":
            if not tc.has_python():
                c.log("skipping ruff: Python linters not installed (run `linttwin setup`)")
                continue
            from . import python_check as pc
            opts = pc.options(tc, pylint=a.pylint, no_fixes=a.no_fixes, rcdir=work)
            jobs, skipped, nfiles = pc.jobs_for(dirs, opts)
            fn = pc.check_chunk
        else:
            if not tc.has_js():
                c.log("skipping %s: JavaScript linters not installed (run `linttwin setup`)" % tool)
                continue
            from . import js_check as jc
            opts = jc.options(tc, tool, no_fixes=a.no_fixes, cfg_root=work)
            jobs, skipped, nfiles = jc.jobs_for(tool, dirs, opts)
            fn = jc.check_chunk
        if not jobs:
            continue
        c.log("%s: %d files in %d projects (%s); %d rule pairs" % (tool, nfiles, len(dirs), dict(skipped) or "none skipped",
                                                                   len(opts.get("pairs") or opts.get("codes"))))
        res = report.Result(tool)
        for out in _run_pool(fn, jobs, a.jobs, tool):
            res.add(out)
        results.append(res)
    if not results:
        sys.exit("nothing to check (no .py or .js files, or no linters installed)")
    path = report.write(results, a.out, {"packages": len(dirs), "versions": tc.versions()})
    print()
    for r in results:
        ndiv = sum(k for (_, _, side), k in r.counts.items() if side != "both")
        nagree = sum(k for (_, _, side), k in r.counts.items() if side == "both")
        rules = len({(ref, rule) for (ref, rule, side), k in r.counts.items() if side != "both" and k})
        print("%s%-7s%s %s%d%s diagnostics agree with the original, %s%d%s disagree across %d rules; "
              "%s%d%s %s a safe-fix check" % (BOLD, r.tool, RESET, GREEN, nagree, RESET, RED if ndiv else "", ndiv,
                                              RESET, rules, RED if r.stats["fix_violations"] else "",
                                              r.stats["fix_violations"], RESET,
                                              "file fails" if r.stats["fix_violations"] == 1 else "files fail"))
    print("\nreport: %s" % path)


def cmd_findings(a):
    from .findings import FINDINGS, check
    tc = Toolchain(a.prefix)
    n = 0
    chosen = [f for f in FINDINGS if not a.tool or f["tool"] == a.tool]
    print("%-6s %-7s %-36s %-11s %s" % ("id", "tool", "rule", "status", "evidence"))
    for f in chosen:
        try:
            ok, ev = check(f, tc)
        except ToolchainError as e:
            ok, ev = None, str(e).splitlines()[0]
        n += bool(ok)
        status = (RED + "reproduces" + RESET) if ok else (GREEN + "fixed?" + RESET) if ok is False else "skipped"
        pad = " " * max(0, 11 - len("reproduces" if ok else "fixed?" if ok is False else "skipped"))
        print("%-6s %-7s %-36s %s%s %s" % (f["id"], f["tool"], f["rule"], status, pad, ev[:110]))
    print("\n%d of %d findings reproduce with %s" % (n, len(chosen), ", ".join("%s %s" % kv for kv in tc.versions().items())))


def cmd_setup(a):
    try:
        v = setup(a.prefix, pinned=a.pinned, log=lambda m: c.log(m))
    except ToolchainError as e:
        sys.exit(str(e))
    print("installed in %s:" % os.path.abspath(os.path.expanduser(str(a.prefix))))
    for k, val in v.items():
        print("  %-24s %s" % (k, val))


def cmd_corpus(a):
    from .corpus import download
    done = download(a.dir, a.pypi, a.npm)
    print("corpus in %s: %d PyPI and %d npm packages" % (a.dir, done["pypi"], done["npm"]))
    print("next: linttwin check %s/pypi/* --tool ruff ; linttwin check %s/npm/* --tool oxlint" % (a.dir, a.dir))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="linttwin", description="Do Rust-rewritten linters keep their promises?")
    ap.add_argument("--version", action="version", version="linttwin " + __version__)
    ap.add_argument("--prefix", default=str(DEFAULT_PREFIX), help="where the linters are installed (default %(default)s)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("setup", help="install the linters to compare")
    s.add_argument("--pinned", action="store_true", help="install the exact versions used in the paper")
    s.set_defaults(fn=cmd_setup)
    s = sub.add_parser("check", help="compare the rewrites with the original tools on your code")
    s.add_argument("dirs", nargs="+", help="project directories (each is checked as one package)")
    s.add_argument("--tool", choices=["ruff", "oxlint", "biome", "all"], default="all")
    s.add_argument("--pylint", action="store_true", help="also compare ruff's PL rules with pylint (slower)")
    s.add_argument("--no-fixes", action="store_true", help="skip the safe-fix checks")
    s.add_argument("--out", default="linttwin-report", help="report directory (default %(default)s)")
    s.add_argument("--jobs", type=int, default=os.cpu_count() or 2)
    s.set_defaults(fn=cmd_check)
    s = sub.add_parser("findings", help="re-run the reproducers of the bugs LintTwin found")
    s.add_argument("--tool", choices=["ruff", "oxlint", "biome"])
    s.set_defaults(fn=cmd_findings)
    s = sub.add_parser("corpus", help="download the paper's corpus")
    s.add_argument("--dir", default="corpus")
    s.add_argument("--pypi", type=int, default=300)
    s.add_argument("--npm", type=int, default=100)
    s.set_defaults(fn=cmd_corpus)
    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
