"""The registry of findings is well formed. Re-running the reproducers needs the linters: `linttwin findings`."""
import ast

from linttwin.findings import FINDINGS

CHECKS = {"fix_breaks_syntax", "fix_changes_comments", "parity", "migration", "fix_changes_behaviour",
          "fix_drops_comment", "py_parity", "fix_error"}


def test_ids_are_unique_and_tools_known():
    ids = [f["id"] for f in FINDINGS]
    assert len(ids) == len(set(ids)) == 47
    assert {f["tool"] for f in FINDINGS} == {"ruff", "oxlint", "biome"}


def test_javascript_source_types_are_known():
    for f in FINDINGS:
        assert f.get("source_type", "commonjs") in ("module", "commonjs"), f["id"]


def test_every_finding_has_a_known_check_and_a_reproducer():
    for f in FINDINGS:
        assert f["check"][0] in CHECKS, f["id"]
        assert f["source"].strip(), f["id"]


def test_python_reproducers_parse():
    for f in FINDINGS:
        if f["tool"] == "ruff":
            ast.parse(f["source"])
