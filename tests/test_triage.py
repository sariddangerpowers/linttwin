"""The triage protocol: cases from a report's records, the causes the study found, and the checks on the verdicts."""
import gzip
import json

from linttwin import report, triage
from linttwin.toolchain import Toolchain


def _report(tmp_path):
    """a report with two rules the study knows (PLR2004, no-var's fix) and three it does not."""
    divs = [
        dict(tool="ruff", reference="flake8", package="a", file="x.py", rule="F999", side="ruff_only", line=3, n=2,
             message="unused thing", context="    3| x = 1"),
        dict(tool="ruff", reference="flake8", package="b", file="y.py", rule="F999", side="reference_only", line=7,
             n=1, message="unused thing", context="    7| y = 2"),
        dict(tool="ruff", reference="pylint", package="a", file="x.py", rule="PLR2004", side="reference_only", line=5,
             n=4, message="magic value", context="    5| if a == 3:"),
        dict(tool="oxlint", reference="eslint", package="c", file="z.js", rule="no-thing", side="oxlint_only", line=1,
             message="no thing", context="    1| thing()", eslint_rules=["no-thing"]),
    ]
    fixes = [
        dict(tool="oxlint", package="c", file="z.js", kinds=["syntax"], detail={"syntax": "x"}, rules=["no-var"],
             per_rule=[{"rule": "no-var", "kinds": ["syntax"], "detail": {"syntax": "x"}}], diff="-var x\n+const x"),
        dict(tool="oxlint", package="d", file="w.js", kinds=["comment_lost"], detail={"comment_lost": ["// a"]},
             rules=["made-up-rule"], diff="-a // a\n+a",
             per_rule=[{"rule": "made-up-rule", "kinds": ["comment_lost"], "detail": {"comment_lost": ["// a"]}}]),
    ]
    for name, recs in (("divergences.jsonl.gz", divs), ("fixes.jsonl.gz", fixes)):
        with gzip.open(tmp_path / name, "wt") as f:
            f.writelines(json.dumps(r) + "\n" for r in recs)
    (tmp_path / "meta.json").write_text(json.dumps({"versions": {"ruff": "0.17.0"}}))
    return str(tmp_path)


def test_known_causes_cover_the_study():
    known = triage.known_causes()
    assert sum(kind == "rule" for _, kind, _ in known) == 268          # 271 rules, 3 left UNCLEAR
    assert sum(kind == "fix" for _, kind, _ in known) == 19
    assert {cause for cause, _ in known.values()} <= set(triage.CAUSES) | {"GAP"}
    for (tool, kind, rule), (cause, reason) in known.items():          # every bug names its finding, or says why not
        if cause == "BUG":
            assert reason.endswith(")") and ("-" in reason.rsplit("(", 1)[1] or "not reported" in reason), rule


def test_triage_writes_cases_and_prompts_and_leaves_out_known_causes(tmp_path):
    index = triage.write(_report(tmp_path), Toolchain(tmp_path / "prefix"))
    assert {(c["tool"], c["case"]) for c in index["cases"]} == {
        ("oxlint", "made-up-rule (safe fix)"), ("ruff", "F999"), ("oxlint", "no-thing")}
    assert {(c["tool"], c["rule"]) for c in index["known"]} == {("ruff", "PLR2004"), ("oxlint", "no-var")}
    cases = open(index["files"][0]).read()
    assert cases.startswith("## oxlint :: made-up-rule (safe fix)")     # safe fixes first, as in the study
    assert "reference: flake8 | only ruff: 2 | only flake8: 1 | packages: 2" in cases
    assert "### only flake8 — b y.py:7" in cases
    for name in ("classify.md", "verify.md"):
        prompt = (tmp_path / "triage" / "prompts" / name).read_text()
        assert "{" not in prompt and "}" not in prompt                  # every placeholder is filled
    classify = (tmp_path / "triage" / "prompts" / "classify.md").read_text()
    assert index["files"][0] in classify and "tool\trule\tcause\tconfidence\treason\tevidence\n" in classify


def test_collect_checks_the_verdicts_and_tallies(tmp_path):
    rep = _report(tmp_path)
    triage.write(rep, Toolchain(tmp_path / "prefix"))
    (tmp_path / "triage" / "verdicts" / "batch_01.tsv").write_text(
        "tool\trule\tcause\tconfidence\treason\tevidence\n"
        "ruff\tF999\tBUG\thigh\tmisses it\trepro: x = 1\n"
        "oxlint\tno-thing\tMAYBE\thigh\t?\t?\n"
        "oxlint\tghost-rule\tDOC\thigh\tdocs\tquote\n")
    (tmp_path / "triage" / "verified.tsv").write_text(
        "tool\trule\tverdict\tconfidence\trepro\tevidence\tnote\n"
        "ruff\tF999\tCONFIRMED\thigh\tx = 1\treproduces on 0.17.0\t\n")
    summary, problems = triage.collect(rep)
    assert any("'MAYBE' is not a cause" in p for p in problems)
    assert any("no case oxlint :: ghost-rule" in p for p in problems)
    assert "2 cases have no verdict" in problems                        # no-thing and the safe-fix case
    causes = (tmp_path / "triage" / "causes.tsv").read_text()
    assert "ruff\trule\tF999\t3\tBUG\tverifier: CONFIRMED\treproduces on 0.17.0\n" in causes
    assert "ruff\trule\tPLR2004\t4\tCFG\tstudy\t" in causes
    assert summary[-1] == "new bugs: 1 (1 verified)"


def test_check_report_marks_known_causes(tmp_path):
    r = report.Result("ruff")
    r.add({"counts": {("pylint", "PLR2004", "reference_only"): 4, ("flake8", "F999", "ruff_only"): 2},
           "stats": {}, "divergences": [], "fixes": [], "bugs": [], "crashes": []})
    md = open(report.write([r], str(tmp_path), {"packages": 1, "versions": {}}, known=triage.known_causes())).read()
    unknown = md.split("without a known cause")[1].split("###")[0]
    known = md.split("with a cause known from the study")[1].split("###")[0]
    assert "`F999`" in unknown and "`PLR2004`" not in unknown
    assert "`PLR2004`" in known and "| CFG: " in known
    assert json.loads((tmp_path / "meta.json").read_text())["tools"] == ["ruff"]
