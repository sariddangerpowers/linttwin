"""The Python fix oracles as one check: what a fix breaks, and attribution limited to the checks that failed."""
from linttwin.python_check import violations

ORIG = "def f(xs):\n    for x in xs:\n        if x:\n            return x\n    else:  # nothing found\n        return None\n"
FIXED = "def f(xs):\n    for x in xs:\n        if x:\n            return x\n    return None\n"     # ruff PLW0120 (RF-3)


def test_a_dropped_comment_is_the_only_violation():
    assert violations(ORIG, FIXED) == {"comment_lost": ["# nothing found"]}


def test_attribution_runs_only_the_checks_that_failed():
    assert violations(ORIG, FIXED, kinds={"I1_dead_code"}) == {}
    assert violations(ORIG, FIXED, kinds={"comment_lost"}) == {"comment_lost": ["# nothing found"]}


def test_a_syntax_error_is_always_reported():
    assert "syntax" in violations(ORIG, "def f(xs:\n    return None\n", kinds={"comment_lost"})
