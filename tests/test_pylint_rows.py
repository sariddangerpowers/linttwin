"""Only the requested pylint messages are compared."""
import json
import stat
import sys

from linttwin.python_check import pylint_rows

MSGS = [{"path": "a.py", "line": 3, "message-id": "W0406", "message": "Module import itself"},
        {"path": "a.py", "line": 1, "message-id": "W0012", "message": "Unknown option value for 'disable'"},
        {"path": "a.py", "line": 2, "message-id": "E0011", "message": "Unrecognized file option 'break'"}]


def test_messages_pylint_emits_unasked_are_dropped(tmp_path):
    fake = tmp_path / "pylint"
    fake.write_text("#!%s\nprint(%r)\n" % (sys.executable, json.dumps(MSGS)))
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    rows, _err, ok = pylint_rows(str(fake), ["a.py"], ["W0406"], "rcfile", [])
    assert ok
    assert rows == [("a.py", 3, "PLW0406", "Module import itself")]
