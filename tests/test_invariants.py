"""The structural fix oracle: it must flag a fix that dedents by the wrong amount, and stay quiet on correct fixes."""
import ast
import textwrap

from linttwin import invariants


def src(s):
    return textwrap.dedent(s).lstrip("\n")


def reachable(code, stmt):
    """reachability flags of `stmt` (one per occurrence, in source order) in `code`."""
    flags = invariants._reachability(ast.parse(src(code)))
    return flags[invariants._h(ast.dump(ast.parse(stmt).body[0]))]


# ruff 0.17.0's RET505 fix of this input (issue astral-sh/ruff#29381): the comments are dedented, `return 2` is not,
# so it lands in the `if` block, after `return 1`.
ORIG = """
def f(a):
    if a:
        return 1
    else:
        # one
          # two
        return 2
"""
RUFF_FIX = """
def f(a):
    if a:
        return 1
        # one
    # two
        return 2
"""
CORRECT_FIX = """
def f(a):
    if a:
        return 1
    # one
      # two
    return 2
"""


def test_wrong_dedent_is_caught_by_both_invariants():
    v = invariants.check(src(ORIG), src(RUFF_FIX))
    assert v["I1_dead_code"] == ["return 2"]
    assert v["I2_moved_into_block"][0]["from"] == "orelse"
    assert v["I2_moved_into_block"][0]["into"] == "body"


def test_correct_dedent_passes():
    assert invariants.check(src(ORIG), src(CORRECT_FIX)) == {}


def test_code_that_was_already_dead_may_stay_dead():
    orig = "def f(a):\n    return 0\n    if a:\n        return 1\n    else:\n        return 2\n"
    fixed = "def f(a):\n    return 0\n    if a:\n        return 1\n    return 2\n"
    assert invariants.check(orig, fixed) == {}


def test_unparseable_input_is_left_to_the_syntax_oracle():
    assert invariants.check(src(ORIG), "def f(a:\n") == {}


def test_a_context_manager_may_swallow_a_raise():
    assert reachable("""
        def f(cm):
            with cm:
                raise ValueError
            cleanup()
        """, "cleanup()") == [True]
    assert reachable("""
        def f():
            raise ValueError
            cleanup()
        """, "cleanup()") == [False]


def test_a_loop_else_without_break_always_runs():
    assert reachable("""
        def f(xs):
            for x in xs:
                use(x)
            else:
                return 1
            cleanup()
        """, "cleanup()") == [False]
    assert reachable("""
        def f(xs):
            for x in xs:
                if x:
                    break
            else:
                return 1
            cleanup()
        """, "cleanup()") == [True]


def test_a_finally_that_returns_ends_the_block():
    assert reachable("""
        def f():
            try:
                work()
            finally:
                return 1
            cleanup()
        """, "cleanup()") == [False]


def test_a_statement_moved_out_of_its_container_is_not_a_branch_switch():
    orig = "for x in xs:\n    if x:\n        continue\n    else:\n        use(x)\n"
    fixed = "for x in xs:\n    if x:\n        continue\n    use(x)\n"
    assert invariants.check(orig, fixed) == {}
