"""Structural invariants that a behaviour-preserving ("safe") fix must keep.

I1 nothing reachable becomes dead: every simple statement that occurs exactly once, unchanged, in both versions and is
   reachable before the fix must still be reachable after it. Reachability is computed: a statement is dead if an
   earlier statement in its block always leaves the block (`return` / `continue` / `break`; `raise` unless a context
   manager could swallow it; an `if`/`else` or `try` whose every branch leaves; a loop whose `else` always runs and
   leaves).
I2 no branch switching: such a statement must not stay in the same container (same header, same ancestor headers) but
   switch block, e.g. from an `if`'s `else` into its body, or from a loop's `else` into the loop body. This is the shape
   of a fix that dedents by the wrong amount. A correct dedent moves the statement out of the container altogether.

check(orig_src, fixed_src) -> dict of violated invariant -> details (empty if both hold or either side does not parse).
"""
from __future__ import annotations

import ast
import collections
import hashlib

TERMINATORS = (ast.Return, ast.Raise, ast.Continue, ast.Break)
BLOCK_FIELDS = ("body", "orelse", "finalbody", "handlers", "cases")
TRIVIAL = (ast.Pass, ast.Continue, ast.Break)
HEADER_FIELDS = ("name", "test", "target", "iter", "items", "type", "subject", "pattern", "guard")
TRY_TYPES = tuple(t for t in (getattr(ast, "Try", None), getattr(ast, "TryStar", None)) if t)


def _h(s: str) -> str:
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def _header(node: ast.AST) -> str:
    parts = [type(node).__name__]
    for f in HEADER_FIELDS:
        v = getattr(node, f, None)
        if v is None:
            continue
        if isinstance(v, list):
            parts.append(f + "=" + "|".join(ast.dump(x) if isinstance(x, ast.AST) else str(x) for x in v))
        elif isinstance(v, ast.AST):
            parts.append(f + "=" + ast.dump(v))
        else:
            parts.append(f + "=" + str(v))
    return _h("/".join(parts))


# ---------------------------------------------------------------- I1: reachability

def _has_break(block) -> bool:
    """a `break` that belongs to this loop (not to a nested loop)."""
    stack = list(block)
    while stack:
        n = stack.pop()
        if isinstance(n, ast.Break):
            return True
        if isinstance(n, (ast.For, ast.AsyncFor, ast.While, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        for f in BLOCK_FIELDS:
            v = getattr(n, f, None)
            if isinstance(v, list):
                stack.extend(x for x in v if isinstance(x, ast.AST))
    return False


def _always_exits(s: ast.stmt, allow_raise: bool = True) -> bool:
    """the statement never falls through to the next one. A `raise` counts only where no enclosing context manager
    could swallow it (allow_raise); a loop counts only via an `else` that always runs (no `break`)."""
    if isinstance(s, ast.Raise):
        return allow_raise
    if isinstance(s, TERMINATORS):
        return True
    if isinstance(s, ast.If):
        return bool(s.orelse) and _block_exits(s.body, allow_raise) and _block_exits(s.orelse, allow_raise)
    if isinstance(s, TRY_TYPES):
        if s.finalbody and _block_exits(s.finalbody, allow_raise):
            return True
        main = _block_exits(s.body, allow_raise) or (bool(s.orelse) and _block_exits(s.orelse, allow_raise))
        return main and all(_block_exits(h.body, allow_raise) for h in s.handlers)
    if isinstance(s, (ast.With, ast.AsyncWith)):
        return False        # the context manager may swallow an exception raised by ANY statement of its body
    if isinstance(s, (ast.For, ast.AsyncFor, ast.While)):
        return bool(s.orelse) and not _has_break(s.body) and _block_exits(s.orelse, allow_raise)
    return False


def _block_exits(block, allow_raise: bool = True) -> bool:
    return any(_always_exits(x, allow_raise) for x in block)


def _reachability(tree: ast.AST) -> dict:
    """fingerprint of each non-trivial simple statement -> list of reachable flags (source order)."""
    out = collections.defaultdict(list)

    def walk(block, reach, allow_raise):
        for st in block:
            if isinstance(st, ast.stmt) and not _is_container(st) and not isinstance(st, TRIVIAL):
                out[_h(ast.dump(st))].append(reach)
            ar = allow_raise and not isinstance(st, (ast.With, ast.AsyncWith))
            for f in BLOCK_FIELDS:
                for child in _kids(st, f):
                    if isinstance(child, ast.excepthandler) or type(child).__name__ == "match_case":
                        walk(child.body, reach, ar)
                kids = [c for c in _kids(st, f) if isinstance(c, ast.stmt)]
                if kids:
                    walk(kids, reach, ar)
            if reach and isinstance(st, ast.stmt) and _always_exits(st, allow_raise):
                reach = False

    walk(tree.body, True, True)
    return out


# ---------------------------------------------------------------- I2: block membership

def _is_container(node: ast.AST) -> bool:
    for g in BLOCK_FIELDS:
        v = getattr(node, g, None)
        if isinstance(v, list) and v and isinstance(v[0], ast.AST):
            return True
    return False


def _kids(node: ast.AST, f: str):
    v = getattr(node, f, None)
    return [c for c in v if isinstance(c, ast.AST)] if isinstance(v, list) else []


def _align(orig: ast.AST, fixed: ast.AST, mapping: dict) -> None:
    """map containers of the fixed tree to containers of the original, block by block, in two passes:
    (1) anchors: containers whose whole subtree is unchanged, aligned like a diff on full-subtree fingerprints;
    (2) inside each gap between anchors, containers aligned like a diff on their headers.
    Only 'equal' runs are paired; anything else (inserted, deleted, renamed, moved) stays unmapped, i.e. "new".
    Paired containers are recursed into."""
    import difflib
    for f in BLOCK_FIELDS:
        co = [c for c in _kids(orig, f) if _is_container(c)]
        cf = [c for c in _kids(fixed, f) if _is_container(c)]
        if not co or not cf:
            continue
        full = difflib.SequenceMatcher(None, [_h(ast.dump(c)) for c in co], [_h(ast.dump(c)) for c in cf], autojunk=False)
        for tag, i1, i2, j1, j2 in full.get_opcodes():
            if tag == "equal":
                for a, b in zip(co[i1:i2], cf[j1:j2]):
                    mapping[id(b)] = id(a)
                    _align(a, b, mapping)
            elif tag == "replace":
                ga, gb = co[i1:i2], cf[j1:j2]
                hdr = difflib.SequenceMatcher(None, [_header(c) for c in ga], [_header(c) for c in gb], autojunk=False)
                for t2, k1, k2, l1, l2 in hdr.get_opcodes():
                    if t2 == "equal":
                        for a, b in zip(ga[k1:k2], gb[l1:l2]):
                            mapping[id(b)] = id(a)
                            _align(a, b, mapping)


def _chains(tree: ast.AST, mapping=None):
    """fingerprint of each non-trivial simple statement -> [(chain, lineno, text)]; chain = tuple of (container key,
    block field) from the module down. In the original tree a container's key is its own id(); in the fixed tree it is the
    id() of the original container it was aligned with, or a fresh marker if unaligned."""
    out = collections.defaultdict(list)

    def key(node):
        if mapping is None:
            return id(node)
        return mapping.get(id(node), ("new", id(node)))

    def visit(node, chain):
        k = key(node)
        for f in BLOCK_FIELDS:
            for child in _kids(node, f):
                el = chain + ((k, f),)
                if _is_container(child):
                    visit(child, el)
                elif isinstance(child, ast.stmt) and not isinstance(child, TRIVIAL):
                    out[_h(ast.dump(child))].append((el, child.lineno, ast.unparse(child)[:120]))

    visit(tree, ())
    return out


def _nearest(tree: ast.AST) -> dict:
    """fingerprint of each non-trivial simple statement -> [(ancestor header path, nearest container header, field,
    lineno, text)]."""
    out = collections.defaultdict(list)

    def visit(node, path):
        h = "module" if isinstance(node, ast.Module) else _header(node)
        for f in BLOCK_FIELDS:
            for child in _kids(node, f):
                if _is_container(child):
                    visit(child, path + (h,))
                elif isinstance(child, ast.stmt) and not isinstance(child, TRIVIAL):
                    out[_h(ast.dump(child))].append((path, h, f, child.lineno, ast.unparse(child)[:120]))

    visit(tree, ())
    return out


def check(orig_src: str, fixed_src: str) -> dict:
    try:
        to, tf = ast.parse(orig_src), ast.parse(fixed_src)
    except (SyntaxError, RecursionError, ValueError):
        return {}
    v = {}
    try:
        ro, rf = _reachability(to), _reachability(tf)
        no, nf = _nearest(to), _nearest(tf)
    except RecursionError:
        return v
    died = []
    for fp, flags in ro.items():
        if len(flags) == 1 and len(rf.get(fp, [])) == 1 and flags[0] and not rf[fp][0]:
            died.append(no[fp][0][4] if fp in no else fp)
    if died:
        v["I1_dead_code"] = died[:10]
    moved = []
    for fp, occ in no.items():
        if len(occ) != 1 or len(nf.get(fp, [])) != 1:
            continue
        (path_o, h_o, f_o, ln_o, txt), (path_f, h_f, f_f, ln_f, _) = occ[0], nf[fp][0]
        if h_o == h_f and path_o == path_f and f_o != f_f and h_o != "module":
            moved.append({"stmt": txt, "line_before": ln_o, "line_after": ln_f, "from": f_o, "into": f_f})
    if moved:
        v["I2_moved_into_block"] = moved[:10]
    return v
