
## ruff :: B025
reference: flake8 | only ruff: 5 | only reference: 1 | packages: 1
top messages: [only_rewrite] try-except block with duplicate exception `BaseException` ×3 || [only_rewrite] try-except block with duplicate exception `Exception` ×2 || [only_reference] Exception `Exception` has been caught multiple times. Only the first exceptException will  ×1

### only_rewrite example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/statement/try.py:180
message: try-except block with duplicate exception `BaseException`
```
  178|     pass
  179| except (  # We wrap these and preserve the parens
  180|         BaseException, Exception, ValueError):
  181|     pass
  182| except (
```

### only_reference example — ruff f-0.17.0/crates/ruff_python_parser/resources/inline/ok/except_stmt_as_name_soft_keyword.py:1
message: Exception `Exception` has been caught multiple times. Only the first exceptException will be considered and all other exceptException catches can be safely remo
```
    1| try: ...
    2| except Exception as match: ...
    3| except Exception as case: ...
```

## ruff :: B009
reference: flake8 | only ruff: 4 | only reference: 1 | packages: 3
top messages: [only_rewrite] Do not call `getattr` with a constant attribute value. It is not any safer than normal pro ×4 || [only_reference] Do not call getattr with a constant attribute value, it is not any safer than normal prope ×1

### only_rewrite example — asttokens asttokens-3.0.2/asttokens/mark_tokens.py:355
message: Do not call `getattr` with a constant attribute value. It is not any safer than normal property access.
```
  353|     last = first_token
  354|     while True:
  355|       if util.match_token(last, getattr(token, "FSTRING_START")):
  356|         # Python 3.12+ has tokens for the start (e.g. `f"`) and end (`"`)
  357|         # of the f-string. We can't just look for the next FSTRING_END
```

### only_rewrite example — psycopg2-binary psycopg2-binary-2.9.13/tests/test_extras_dictcursor.py:502
message: Do not call `getattr` with a constant attribute value. It is not any safer than normal property access.
```
  500|         curs.execute('select 1 as \xe5h\xe9')
  501|         rv = curs.fetchone()
  502|         self.assertEqual(getattr(rv, '\xe5h\xe9'), 1)
  503| 
  504|     def test_minimal_generation(self):
```

### only_reference example — pandas pandas-3.0.6/pandas/tests/base/test_constructors.py:114
message: Do not call getattr with a constant attribute value, it is not any safer than normal property access.
```
  112|         t._freeze()
  113|         assert "__frozen" in dir(t)
  114|         assert getattr(t, "__frozen")
  115|         msg = "You cannot add any new attribute"
  116|         with pytest.raises(AttributeError, match=msg):
```

## ruff :: PLE0304
reference: pylint | only ruff: 0 | only reference: 5 | packages: 3
top messages: [only_reference] __bool__ does not return bool ×5

### only_reference example — langchain-core langchain_core-1.6.10/tests/unit_tests/load/test_serializable.py:35
message: __bool__ does not return bool
```
   33| 
   34| class NonBoolObj:
   35|     def __bool__(self) -> bool:
   36|         msg = "Truthiness can't be determined"
   37|         raise ValueError(msg)
```

### only_reference example — narwhals narwhals-2.27.1/src/narwhals/series.py:265
message: __bool__ does not return bool
```
  263|     """
  264| 
  265|     def __bool__(self) -> NoReturn:
  266|         msg = (
  267|             "the truth value of a Series is ambiguous"
```

### only_reference example — pytest pytest-9.1.1/src/_pytest/python_api.py:84
message: __bool__ does not return bool
```
   82|         )
   83| 
   84|     def __bool__(self):
   85|         __tracebackhide__ = True
   86|         raise AssertionError(
```

## ruff :: PLW1510
reference: pylint | only ruff: 0 | only reference: 4 | packages: 3
top messages: [only_reference] 'subprocess.run' used without explicitly defining the value for 'check'. ×4

### only_reference example — attrs attrs-26.1.0/tests/test_pyright.py:22
message: 'subprocess.run' used without explicitly defining the value for 'check'.
```
   20| 
   21| def parse_pyright_output(test_file: Path) -> set[tuple[str, str]]:
   22|     pyright = subprocess.run(  # noqa: PLW1510
   23|         ["pyright", "--outputjson", str(test_file)], capture_output=True
   24|     )
```

### only_reference example — hatchling hatchling-1.32.4/src/hatchling/builders/binary.py:195
message: 'subprocess.run' used without explicitly defining the value for 'check'.
```
  193|             kwargs["stderr"] = subprocess.STDOUT
  194| 
  195|         process = subprocess.run(*args, **kwargs)  # noqa: PLW1510
  196|         if process.returncode:
  197|             message = f"Compilation failed (code {process.returncode})"
```

### only_reference example — setuptools setuptools-84.0.0/setuptools/tests/test_dist_info.py:144
message: 'subprocess.run' used without explicitly defining the value for 'check'.
```
  142|     }
  143|     cmd = [sys.executable, "-c", "__import__('setuptools').setup()", *map(str, cmd)]
  144|     return subprocess.run(cmd, **opts)  # noqa: PLW1510 # check provided via opts
  145| 
  146| 
```

## ruff :: F901
reference: flake8 | only ruff: 4 | only reference: 0 | packages: 1
top messages: [only_rewrite] `raise NotImplemented` should be `raise NotImplementedError` ×4

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/suppliermodule_test.py:8
message: `raise NotImplemented` should be `raise NotImplementedError`
```
    6| class Interface:
    7|     def get_value(self):
    8|         raise NotImplemented()
    9| 
   10|     def set_value(self, value):
```

## ruff :: PLE0302
reference: pylint | only ruff: 1 | only reference: 3 | packages: 4
top messages: [only_reference] The special method '__pow__' expects between 1 or 2 param(s), 0 was given ×2 || [only_rewrite] The special method `__next__` expects 1 parameter, 2 were given ×1 || [only_reference] The special method '__get__' expects 2 param(s), 0 was given ×1

### only_rewrite example — jedi jedi-0.20.1/test/test_api/test_interpreter.py:630
message: The special method `__next__` expects 1 parameter, 2 were given
```
  628|             pass
  629| 
  630|         def __next__(self, key) -> float:  # type: ignore[empty-body]
  631|             pass
  632| 
```

### only_reference example — mypy mypy-2.4.0/mypy/stubgenc.py:208
message: The special method '__get__' expects 2 param(s), 0 was given
```
  206|         )
  207| 
  208|     def __get__(self) -> None:  # noqa: PLE0302
  209|         """
  210|         This exists to make this object look like a method descriptor and thus
```

### only_reference example — scikit-learn scikit_learn-1.9.1/sklearn/conftest.py:300
message: The special method '__pow__' expects between 1 or 2 param(s), 0 was given
```
  298|             return super().__imul__(other)
  299| 
  300|         def __pow__(self, *args, **kwargs):
  301|             raise ValueError("spmatrix ** used here! Use sparse.linalg.matrix_power?")
  302| 
```

### only_reference example — scipy scipy-1.18.1/scipy/sparse/_base.py:1096
message: The special method '__pow__' expects between 1 or 2 param(s), 0 was given
```
 1094|         return NotImplemented
 1095| 
 1096|     def __pow__(self, *args, **kwargs):
 1097|         return self.power(*args, **kwargs)
 1098| 
```

## ruff :: B030
reference: flake8 | only ruff: 0 | only reference: 4 | packages: 2
top messages: [only_reference] Except handlers should only be names of exception classes ×4

### only_reference example — google-cloud-storage google_cloud_storage-3.17.0/tests/conformance/test_bidi_reads.py:124
message: Except handlers should only be names of exception classes
```
  122|             assert len(buffer.getvalue()) == 9 * 1024
  123| 
  124|         except scenario["expected_error"] as e:
  125|             print(f"Caught expected exception for {scenario['name']}: {e}")
  126| 
```

### only_reference example — sqlalchemy sqlalchemy-2.1.4/lib/sqlalchemy/orm/exc.py:227
message: Except handlers should only be names of exception classes
```
  225|     try:
  226|         mappers = base.manager_of_class(cls).mappers  # type: ignore[attr-defined]  # noqa: E501
  227|     except (
  228|         UnmappedClassError,
  229|         TypeError,
```

## ruff :: C400
reference: flake8 | only ruff: 4 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary generator (rewrite as a list comprehension) ×3 || [only_rewrite] Unnecessary generator (rewrite using `list()`) ×1

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:197
message: Unnecessary generator (rewrite as a list comprehension)
```
  195|              {tester(x) for x in [1]}])
  196|         # or are of different types
  197|         str([{tester(x) for x in [1]}, list(tester(x) for x in [1])])
  198|         # but not if everything is the same
  199|         # noinspection PyTypeChecker
```

## ruff :: PLW0245
reference: pylint | only ruff: 0 | only reference: 4 | packages: 1
top messages: [only_reference] Super call without brackets ×4

### only_reference example — matplotlib matplotlib-3.11.2/lib/matplotlib/_mathtext.py:2662
message: Super call without brackets
```
 2660|             # kern() and hpack() needed to get the metrics right after
 2661|             # extending
 2662|             super.kern()
 2663|             super.hpack()
 2664| 
```

## ruff :: F502
reference: flake8 | only ruff: 0 | only reference: 4 | packages: 2
top messages: [only_reference] '...' % ... expected mapping but got sequence ×4

### only_reference example — black black-26.10.1/tests/data/cases/preview_long_strings__regression.py:105
message: '...' % ... expected mapping but got sequence
```
  103| func_call_where_string_arg_has_old_fmt_and_bad_parens(
  104|     (
  105|         "A long string with {}. This {} is so long that it is ridiculous. It can't fit on one line at alllll." % ("formatting", "string")
  106|     ),
  107| )
```

### only_reference example — ruff es/ruff_python_formatter/resources/test/fixtures/ruff/expression/binary_implicit_string.py:23
message: '...' % ... expected mapping but got sequence
```
   21| )
   22| 
   23| ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" "cccccccccccccccccccccccccccccccccccccccccccc" % (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa, b, c, d))
   24| ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" "cccccccccccccccccccccccccccccccccccccccccccc" % aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)
   25| 
```

## ruff :: PLE0704
reference: pylint | only ruff: 0 | only reference: 3 | packages: 3
top messages: [only_reference] The raise statement is not inside an except clause ×3

### only_reference example — anyio anyio-4.15.1/src/anyio/streams/tls.py:357
message: The raise statement is not inside an except clause
```
  355|         # Only reraise base exceptions and cancellation exceptions
  356|         if not isinstance(exc, Exception) or isinstance(exc, get_cancelled_exc_class()):
  357|             raise  # noqa: PLE0704
  358| 
  359|     async def serve(
```

### only_reference example — pip pip-26.2.1/src/pip/_internal/utils/misc.py:172
message: The raise statement is not inside an except clause
```
  170| 
  171| def _onerror_reraise(*_args: Any) -> None:
  172|     raise  # noqa: PLE0704 - Bare exception used to reraise existing exception
  173| 
  174| 
```

### only_reference example — pytest pytest-9.1.1/src/_pytest/logging.py:415
message: The raise statement is not inside an except clause
```
  413|             # to stderr with the call stack and some extra details.
  414|             # pytest wants to make such mistakes visible during testing.
  415|             raise  # noqa: PLE0704
  416| 
  417| 
```

## ruff :: F403
reference: flake8 | only ruff: 3 | only reference: 0 | packages: 2
top messages: [only_rewrite] `from _datetime import *` used; unable to detect undefined names ×2 || [only_rewrite] `from astroid.utils import *` used; unable to detect undefined names ×1

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:7
message: `from astroid.utils import *` used; unable to detect undefined names
```
    5| from astroid.node_classes import Name as NameNode
    6| from astroid import modutils
    7| from astroid.utils import *
    8| import os.path
    9| MY_DICT = {}
```

### only_rewrite example — executing .0/tests/small_samples/dc592fb930b28fe2b7181bec5d6f4b871bdd55c01bc22b0623e610eec70df7ab.py:1
message: `from _datetime import *` used; unable to detect undefined names
```
    1| from _datetime import *
```

## ruff :: B034
reference: flake8 | only ruff: 1 | only reference: 2 | packages: 2
top messages: [only_reference] sub should pass `count` and `flags` as keyword arguments to avoid confusion due to unintui ×2 || [only_rewrite] `re.sub` should pass `count` and `flags` as keyword arguments to avoid confusion due to un ×1

### only_rewrite example — asttokens asttokens-3.0.2/tests/tools.py:105
message: `re.sub` should pass `count` and `flags` as keyword arguments to avoid confusion due to unintuitive argument positions
```
  103|       # This is generally harmless and there's probably no good alternative,
  104|       # but in isolation it's invalid syntax
  105|       text = re.sub(r'^(\s*)elif(\W)', r'\1if\2', text, re.MULTILINE)
  106| 
  107|       rebuilt_node = test_case.parse_snippet(text, node)
```

### only_reference example — parso parso-0.8.7/test/normalizer_issue_files/E12_not_first.py:244
message: sub should pass `count` and `flags` as keyword arguments to avoid confusion due to unintuitive argument positions.
```
  242| 
  243| 
  244| fixed = (re.sub(r'\t+', ' ', target[c::-1], 1)[::-1] +
  245|          target[c + 1:])
  246| 
```

## ruff :: PLE0001
reference: pylint | only ruff: 0 | only reference: 3 | packages: 2
top messages: [only_reference] Cannot import 'usages' due to 'invalid syntax (test.completion.usages, line 19)' ×1 || [only_reference] Cannot import 'match' due to 'invalid syntax (match, line 351)' ×1 || [only_reference] Cannot import 'type' due to 'invalid syntax. Maybe you meant '==' or ':=' instead of '='?  ×1

### only_reference example — jedi jedi-0.20.1/test/completion/import_tree/references.py:1
message: Cannot import 'usages' due to 'invalid syntax (test.completion.usages, line 19)'
```
    1| from ..usages import usage_definition
    2| 
    3| 
```

### only_reference example — ruff 17.0/crates/ruff_python_parser/resources/inline/ok/from_import_soft_keyword_module_name.py:1
message: Cannot import 'match' due to 'invalid syntax (match, line 351)'
```
    1| from match import pattern
    2| from type import bar
    3| from case import pattern
```

## ruff :: N811
reference: flake8 | only ruff: 3 | only reference: 0 | packages: 1
top messages: [only_rewrite] Constant `GLUT` imported as non-constant `glut` ×2 || [only_rewrite] Constant `GL` imported as non-constant `gl` ×1

### only_rewrite example — ipython ipython-9.17.1/IPython/terminal/pt_inputhooks/glut.py:24
message: Constant `GLUT` imported as non-constant `glut`
```
   22| import time
   23| import signal
   24| import OpenGL.GLUT as glut
   25| import OpenGL.platform as platform
   26| from timeit import default_timer as clock
```

## ruff :: PLE1307
reference: pylint | only ruff: 0 | only reference: 3 | packages: 3
top messages: [only_reference] Argument 'builtins.NoneType' does not match format type 'd' ×1 || [only_reference] Argument 'builtins.str' does not match format type 'f' ×1 || [only_reference] Argument 'sympy.core.numbers.Integer' does not match format type 'i' ×1

### only_reference example — ipython ipython-9.17.1/IPython/lib/backgroundjobs.py:422
message: Argument 'builtins.NoneType' does not match format type 'd'
```
  420| 
  421|     def __repr__(self):
  422|         return '<BackgroundJob #%d: %s>' % (self.num, self.strform)
  423| 
  424|     def traceback(self):
```

### only_reference example — ruff f_python_formatter/resources/test/fixtures/black/cases/preview_long_strings__regression.py:115
message: Argument 'builtins.str' does not match format type 'f'
```
  113|                                     xxxx.xxxxxxxxxx,
  114|                                     xxxx.xxxxxxxxxx))
  115|                                 + (' %.3f (%s) to %.3f (%s).\n'
  116|                                    % (xxxx.xxxxxxxxx,
  117|                                       xxxx.xxxxxxxxxxxxxx(xxxx.xxxxxxxxx),
```

### only_reference example — sympy sympy-1.14.0/sympy/combinatorics/graycode.py:92
message: Argument 'sympy.core.numbers.Integer' does not match format type 'i'
```
   90|             obj._current = kw_args["start"]
   91|             if len(obj._current) > n:
   92|                 raise ValueError('Gray code start has length %i but '
   93|                 'should not be greater than %i' % (len(obj._current), n))
   94|         elif 'rank' in kw_args:
```

## ruff :: PLR0402
reference: pylint | only ruff: 1 | only reference: 2 | packages: 2
top messages: [only_reference] Use 'from pyarrow import ipc' instead ×1 || [only_reference] Use 'from pyarrow import types' instead ×1 || [only_rewrite] Use `from wcwidth import _wcwidth_c` in lieu of alias ×1

### only_rewrite example — wcwidth wcwidth-0.9.2/wcwidth/__init__.py:54
message: Use `from wcwidth import _wcwidth_c` in lieu of alias
```
   52|     try:
   53|         # local
   54|         import wcwidth._wcwidth_c as _wcwidth_c  # noqa: F401  pylint:disable=unused-import,consider-using-from-import
   55|     except ImportError:
   56|         pass
```

### only_reference example — pyarrow pyarrow-26.0.0/pyarrow/__init__.py:292
message: Use 'from pyarrow import ipc' instead
```
  290| 
  291| from pyarrow.ipc import serialize_pandas, deserialize_pandas
  292| import pyarrow.ipc as ipc
  293| 
  294| import pyarrow.types as types
```

## ruff :: C419
reference: flake8 | only ruff: 0 | only reference: 3 | packages: 2
top messages: [only_reference] Unnecessary list comprehension passed to all() prevents short-circuiting - rewrite as a ge ×3

### only_reference example — numpy numpy-2.5.4/numpy/_core/tests/test_nditer.py:1427
message: Unnecessary list comprehension passed to all() prevents short-circuiting - rewrite as a generator.
```
 1425|     a = arange(6).reshape(2, 3)
 1426|     i = nditer([a, a.T], [], [['readonly']] * 2, op_axes=[[0, 1], [1, 0]])
 1427|     assert_(all([x == y for (x, y) in i]))
 1428|     a = arange(24).reshape(2, 3, 4)
 1429|     i = nditer([a.T, a], [], [['readonly']] * 2, op_axes=[[2, 1, 0], None])
```

### only_reference example — redis redis-8.1.0/tests/test_asyncio/test_pubsub.py:905
message: Unnecessary list comprehension passed to all() prevents short-circuiting - rewrite as a generator.
```
  903|             assert (await wait_for_message(p))["type"] == "subscribe"
  904|         expected = [b"bar", b"baz", b"foo", b"quux"]
  905|         assert all([channel in await r.pubsub_channels() for channel in expected])
  906| 
  907|     @pytest.mark.onlynoncluster
```

## ruff :: E703
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Statement ends with an unnecessary semicolon ×2

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/format.py:33
message: Statement ends with an unnecessary semicolon
```
   31| 
   32| 
   33| __revision__.lower();
   34| 
```

## ruff :: C405
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary list literal (rewrite as a set literal) ×2

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/md_in_html.py:45
message: Unnecessary list literal (rewrite as a set literal)
```
   43|     def __init__(self, md: Markdown, *args, **kwargs):
   44|         # Block-level tags in which the content only gets span level parsing
   45|         self.span_tags = set(
   46|             ['address', 'dd', 'dt', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'legend', 'li', 'p', 'summary', 'td', 'th']
   47|         )
```

## ruff :: PLE1310
reference: pylint | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] String `lstrip` call contains duplicate characters (did you mean `removeprefix`?) ×2

### only_rewrite example — huggingface-hub huggingface_hub-2.2.0/src/huggingface_hub/inference/_common.py:295
message: String `lstrip` call contains duplicate characters (did you mean `removeprefix`?)
```
  293| 
  294|     # Decode payload
  295|     payload = line.lstrip("data:").rstrip("/n")
  296|     json_payload = json.loads(payload)
  297| 
```

## ruff :: C416
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary list comprehension (rewrite using `list()`) ×1 || [only_rewrite] Unnecessary set comprehension (rewrite using `set()`) ×1

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:629
message: Unnecessary list comprehension (rewrite using `list()`)
```
  627| 
  628|         if sys.version_info >= (3, 11):
  629|             assert [i for i in iter_test(ast.ListComp)] == [1, 2]
  630|             assert {i for i in iter_test(ast.SetComp)} == {1, 2}
  631|             assert {i: i for i in iter_test(ast.DictComp)} == {1: 1, 2: 2}
```
