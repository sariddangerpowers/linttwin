"""Matching JavaScript diagnostics: ESLint rows and the multiset match. No linters needed."""
from linttwin.js_check import eslint_rows, match


def msg(rule, line, col):
    return {"rule": rule, "line": line, "col": col, "msg": "m"}


def test_repeated_reports_on_one_line_all_count():
    rows = eslint_rows([msg("no-magic-numbers", 15, 24), msg("no-magic-numbers", 15, 33)],
                       {"no-magic-numbers": "no-magic-numbers"})
    assert len(rows) == 2


def test_nested_nodes_reported_at_one_position_all_count():
    rows = eslint_rows([msg("no-bitwise", 4, 9), msg("no-bitwise", 4, 9)], {"no-bitwise": "no-bitwise"})
    assert len(rows) == 2


def test_two_mapped_rules_reporting_the_same_nodes_count_once_per_node():
    pairs = {"no-negated-condition": "style/noNegationElse", "unicorn/no-negated-condition": "style/noNegationElse"}
    rows = eslint_rows([msg("no-negated-condition", 3, 1), msg("no-negated-condition", 3, 1),
                        msg("unicorn/no-negated-condition", 3, 1), msg("unicorn/no-negated-condition", 3, 1)], pairs)
    assert len(rows) == 2


def test_two_eslint_rules_on_the_same_node_count_once():
    pairs = {"no-negated-condition": "style/noNegationElse", "unicorn/no-negated-condition": "style/noNegationElse"}
    rows = eslint_rows([msg("no-negated-condition", 3, 1), msg("unicorn/no-negated-condition", 3, 1)], pairs)
    assert len(rows) == 1


def test_unmapped_rules_are_dropped():
    assert eslint_rows([msg("no-console", 1, 1)], {"no-var": "no-var"}) == []


def test_match_is_a_multiset_match_with_two_line_tolerance():
    both, e_left, o_left = match([("r", 15), ("r", 15), ("r", 40)], [("r", (15,)), ("r", (15,)), ("r", (42,)), ("r", (90,))])
    assert both["r"] == 3
    assert e_left == []
    assert o_left == [("r", 90)]
