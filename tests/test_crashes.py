"""A tool that aborts on one file must not hide the reports for the other files of its batch."""
import stat
import subprocess
import sys

from linttwin import common as c
from linttwin.python_check import flake8_rows

# flake8 aborts the whole run when a plugin crashes on any file: it prints the failure on stdout, prints no report for
# any file and exits 1, even with --exit-zero
FAKE_FLAKE8 = '''#!%s
import sys
files = sys.argv[sys.argv.index("--exit-zero") + 1:]
if any("boom" in f for f in files):
    print('%%s: "flake8-bugbear" failed during execution due to RecursionError()' %% files[0])
    sys.exit(1)
for f in files:
    print("%%s\\t1\\t1\\tE501\\tline too long" %% f)
''' % sys.executable


def test_a_flake8_plugin_crash_loses_only_the_crashing_file(tmp_path):
    fake = tmp_path / "flake8"
    fake.write_text(FAKE_FLAKE8)
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    good, boom = str(tmp_path / "good.py"), str(tmp_path / "boom.py")
    rows, crashed = c.batch(lambda fs: flake8_rows(str(fake), fs, ["E501"]), [good, boom])
    assert rows == [(good, 1, "E501", "line too long")]
    assert [f for f, _ in crashed] == [boom]
    assert "failed during execution" in crashed[0][1]


def test_a_biome_panic_is_a_crash():
    r = subprocess.CompletedProcess([], 1, "", "Biome encountered an unexpected error\n\nThis is a bug in Biome")
    assert not c.finished(r)
    assert c.finished(subprocess.CompletedProcess([], 1, "", "lint\n\n  x Some errors were emitted while running checks."))
