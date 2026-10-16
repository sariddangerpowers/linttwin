
## ruff :: SIM105
reference: flake8 | only ruff: 48 | only reference: 850 | packages: 142
top messages: [only_reference] Use 'contextlib.suppress(Exception)' ×149 || [only_reference] Use 'contextlib.suppress(KeyError)' ×107 || [only_reference] Use 'contextlib.suppress(AttributeError)' ×80 || [only_reference] Use 'contextlib.suppress(ValueError)' ×53

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/codehilite.py:330
message: Use `contextlib.suppress(ValueError)` instead of `try`-`except`-`pass`
```
  328|                 # manually set unknown keywords.
  329|                 if isinstance(value, str):
  330|                     try:
  331|                         # Attempt to parse `str` as a boolean value
  332|                         value = parseBoolValue(value, preserve_none=True)
```

### only_rewrite example — executing .0/tests/small_samples/88f983dcf04b0d0b09cb105943226d186f9f6a8ada3da7c48a1a3a1c0d947995.py:19
message: Use `contextlib.suppress(Exception)` instead of `try`-`except`-`pass`
```
   17| 
   18|     def generator_wrapper(*args, **kwargs):
   19|         try:
   20|             method, incoming = (gen.send, (yield outgoing))
   21|         except Exception as e:
```

### only_rewrite example — ruff ruff-0.17.0/crates/ruff_python_parser/resources/inline/ok/except_star_py311.py:2
message: Use `contextlib.suppress(ValueError)` instead of `try`-`except`-`pass`
```
    1| # parse_options: {"target-version": "3.11"}
    2| try: ...
    3| except* ValueError: ...
```

### only_reference example — cloudpickle cloudpickle-3.1.2/cloudpickle/cloudpickle.py:229
message: Use 'contextlib.suppress(Exception)'
```
  227|         ):
  228|             continue
  229|         try:
  230|             if _getattribute(module, name) is obj:
  231|                 return module_name
```

### only_reference example — cachetools cachetools-7.2.1/src/cachetools/_cached.py:184
message: Use 'contextlib.suppress(KeyError)'
```
  182|         k = key(*args, **kwargs)
  183|         with lock:
  184|             try:
  185|                 return cache[k]
  186|             except KeyError:
```

### only_reference example — aiobotocore aiobotocore-3.9.2/aiobotocore/eventstream.py:40
message: Use 'contextlib.suppress(StopIteration)'
```
   38| 
   39|     async def get_initial_response(self):
   40|         try:
   41|             async for event in self._event_generator:
   42|                 event_type = event.headers.get(':event-type')
```

## ruff :: E402
reference: flake8 | only ruff: 432 | only reference: 454 | packages: 50
top messages: [only_reference] module level import not at top of file ×454 || [only_rewrite] Module level import not at top of file ×432

### only_rewrite example — et-xmlfile et_xmlfile-2.0.0/et_xmlfile/xmlfile.py:7
message: Module level import not at top of file
```
    5| 
    6| 
    7| from contextlib import contextmanager
    8| 
    9| from xml.etree.ElementTree import (
```

### only_rewrite example — dill dill-0.4.1/dill/_objects.py:17
message: Module level import not at top of file
```
   15| # helper imports
   16| import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning)
   17| import sys
   18| import queue as Queue
   19| #import dbm as anydbm #XXX: delete foo
```

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module2.py:112
message: Module level import not at top of file
```
  110|     
  111|     return Aaaa
  112| from os.path import abspath
  113| import os as myos
  114| 
```

### only_reference example — charset-normalizer charset_normalizer-3.5.2/docs/conf.py:26
message: module level import not at top of file
```
   24| sys.path.insert(0, os.path.abspath(".."))
   25| 
   26| import charset_normalizer
   27| 
   28| # -- General configuration ------------------------------------------------
```

### only_reference example — contourpy contourpy-1.4.0/docs/sphinxext/name_supports.py:12
message: module level import not at top of file
```
   10| 
   11| sys.path.insert(0, ".")
   12| from table import Table
   13| 
   14| 
```

### only_reference example — chardet chardet-7.6.0/scripts/benchmark_memory.py:28
message: module level import not at top of file
```
   26| sys.path.insert(0, str(Path(__file__).resolve().parent))
   27| 
   28| from utils import format_bytes as _format_bytes
   29| from utils import percentiles
   30| 
```

## ruff :: SIM117
reference: flake8 | only ruff: 245 | only reference: 591 | packages: 59
top messages: [only_rewrite] Use a single `with` statement with multiple contexts instead of nested `with` statements ×245 || [only_reference] Use 'with mock.patch.object(transport_class, '__init__') as patched, mock.patch('google.au ×138 || [only_reference] Use 'with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_v ×137 || [only_reference] Use 'with tt.AssertPrints('Wall time: ', suppress=False), tt.AssertPrints('CPU times: ', s ×11

### only_rewrite example — aiobotocore aiobotocore-3.9.2/tests/botocore_tests/functional/test_retry.py:89
message: Use a single `with` statement with multiple contexts instead of nested `with` statements
```
   87| 
   88| async def test_can_override_max_attempts(patched_session):
   89|     async with patched_session.create_client(
   90|         'dynamodb', REGION, config=Config(retries={'max_attempts': 1})
   91|     ) as client:
```

### only_rewrite example — asyncpg asyncpg-0.32.0/tests/test_pool.py:147
message: Use a single `with` statement with multiple contexts instead of nested `with` statements
```
  145|             fut.set_result(con)
  146| 
  147|         async with self.create_pool(database='postgres',
  148|                                     init_size=5, min_size=1, max_size=5,
  149|                                     setup=setup) as pool:
```

### only_rewrite example — anyio anyio-4.15.1/tests/test_taskgroups.py:486
message: Use a single `with` statement with multiple contexts instead of nested `with` statements
```
  484| 
  485|     with pytest.raises(ExceptionGroup) as exc:
  486|         async with anyio.create_task_group() as outer_tg:
  487|             async with anyio.create_task_group() as inner_tg:
  488|                 inner_tg.start_soon(sleep_and_raise)
```

### only_reference example — anyio anyio-4.15.1/tests/test_taskgroups.py:715
message: Use 'with pytest.raises(TimeoutError), fail_after(delay) as scope:' instead of multiple with statements
```
  713| @pytest.mark.parametrize("delay", [0, 0.1], ids=["instant", "delayed"])
  714| async def test_fail_after(delay: float) -> None:
  715|     with pytest.raises(TimeoutError):
  716|         with fail_after(delay) as scope:
  717|             try:
```

### only_reference example — azure-identity azure_identity-1.26.0/tests/test_powershell_credential.py:311
message: Use 'with patch.dict('os.environ', {'SYSTEMROOT': 'foo'}), patch(POPEN, Popen):' instead of multiple with statements
```
  309| 
  310|     with patch(AzurePowerShellCredential.__module__ + ".sys.platform", "win32"):
  311|         with patch.dict("os.environ", {"SYSTEMROOT": "foo"}):
  312|             with patch(POPEN, Popen):
  313|                 with pytest.raises(CredentialUnavailableError, match=AZ_ACCOUNT_NOT_INSTALLED):
```

### only_reference example — google-api-python-client google_api_python_client-2.201.0/tests/test_discovery.py:884
message: Use 'with mock.patch.dict('os.environ', {'GOOGLE_API_USE_CLIENT_CERTIFICATE': use_client_cert}), self.assertRaises(MutualTLSChannelError):' instead of multiple 
```
  882|             "os.environ", {"GOOGLE_API_USE_MTLS_ENDPOINT": use_mtls_env}
  883|         ):
  884|             with mock.patch.dict(
  885|                 "os.environ", {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert}
  886|             ):
```

## ruff :: PLR1711
reference: pylint | only ruff: 316 | only reference: 382 | packages: 84
top messages: [only_reference] Useless return at end of function or method ×382 || [only_rewrite] Useless `return` statement at end of function ×316

### only_rewrite example — async-timeout async_timeout-5.0.1/async_timeout/__init__.py:269
message: Useless `return` statement at end of function
```
  267|             self._state = _State.EXIT
  268|             self._reject()
  269|             return None
  270| 
  271|         def _on_timeout(self) -> None:
```

### only_rewrite example — aiohappyeyeballs aiohappyeyeballs-2.7.1/tests/test_impl.py:539
message: Useless `return` statement at end of function
```
  537|             raise OSError(5, "ipv6 fail")
  538| 
  539|         return None
  540| 
  541|     m_socket.socket = _socket  # type: ignore
```

### only_rewrite example — asgiref asgiref-3.12.1/asgiref/timeout.py:113
message: Useless `return` statement at end of function
```
  111|             self._cancel_handler = None
  112|         self._task = None
  113|         return None
  114| 
  115|     def _cancel_task(self) -> None:
```

### only_reference example — async-timeout async_timeout-5.0.1/async_timeout/__init__.py:260
message: Useless return at end of function or method
```
  258|             self._reschedule()
  259| 
  260|         def _do_exit(self, exc_type: Optional[Type[BaseException]]) -> None:
  261|             if exc_type is asyncio.CancelledError and self._state == _State.TIMEOUT:
  262|                 assert self._task is not None
```

### only_reference example — asgiref asgiref-3.12.1/asgiref/timeout.py:53
message: Useless return at end of function or method
```
   51|         return self._do_enter()
   52| 
   53|     def __exit__(
   54|         self,
   55|         exc_type: type[BaseException],
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/dynamodb/_utils.py:295
message: Useless return at end of function or method
```
  293|         return self
  294| 
  295|     def __exit__(
  296|         self,
  297|         exception_type: type[BaseException] | None,
```

## ruff :: E741
reference: flake8 | only ruff: 598 | only reference: 74 | packages: 34
top messages: [only_rewrite] Ambiguous variable name: `l` ×481 || [only_rewrite] Ambiguous variable name: `I` ×97 || [only_reference] ambiguous variable name 'I' ×41 || [only_reference] ambiguous variable name 'l' ×25

### only_rewrite example — attrs attrs-26.1.0/typing-examples/mypy.py:264
message: Ambiguous variable name: `l`
```
  262|     )
  263| 
  264|     l: Any = attr.ib(
  265|         validator=attr.validators.not_(attr.validators.in_("abc"))
  266|     )
```

### only_rewrite example — execnet execnet-2.1.2/src/execnet/multi.py:292
message: Ambiguous variable name: `l`
```
  290|     ) -> list[tuple[Channel, Any]] | list[Any]:
  291|         assert not hasattr(self, "_queue")
  292|         l: list[object] = []
  293|         for ch in self._channels:
  294|             obj = ch.receive()
```

### only_rewrite example — dill dill-0.4.1/dill/tests/test_classdef.py:264
message: Ambiguous variable name: `l`
```
  262|             return isinstance(cls, mcls)
  263| 
  264|     l = locals()
  265|     exec("""class subclass_with_new(metaclass=metaclass_with_new):
  266|         def __new__(cls):
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/merge/util.py:102
message: ambiguous variable name 'l'
```
  100| 
  101|     def __init__(self, lst):
  102|         self.l = lst
  103|         self.d = {id(v): i for i, v in enumerate(lst)}
  104|         self.s = set()
```

### only_reference example — mypy mypy-2.4.0/mypyc/test/test_emitfunc.py:98
message: ambiguous variable name 'l'
```
   96|         self.m = add_local("m", int_rprimitive)
   97|         self.k = add_local("k", int_rprimitive)
   98|         self.l = add_local("l", list_rprimitive)
   99|         self.ll = add_local("ll", list_rprimitive)
  100|         self.o = add_local("o", object_rprimitive)
```

### only_reference example — mpmath mpmath-1.4.1/mpmath/tests/test_matrices.py:251
message: ambiguous variable name 'l'
```
  249|                                                   dtype=object)).all()
  250|     if numpy.__version__ >= '2':
  251|         pytest.raises(ValueError, lambda: numpy.array(matrix(l), copy=False))
  252| 
  253| def test_interval_matrix_scalar_mult():
```

## ruff :: N999
reference: flake8 | only ruff: 591 | only reference: 0 | packages: 32
top messages: [only_rewrite] Invalid module name: 'fontTools' ×45 || [only_rewrite] Invalid module name: 'IPython' ×17 || [only_rewrite] Invalid module name: 'A' ×2 || [only_rewrite] Invalid module name: 'pointPen' ×2

### only_rewrite example — defusedxml defusedxml-0.7.1/defusedxml/cElementTree.py:1
message: Invalid module name: 'cElementTree'
```
    1| # defusedxml
    2| #
    3| # Copyright (c) 2013 by Christian Heimes <christian@python.org>
```

### only_rewrite example — azure-identity azure_identity-1.26.0/tests/integration/azure-functions/RunTest/__init__.py:1
message: Invalid module name: 'RunTest'
```
    1| # ------------------------------------
    2| # Copyright (c) Microsoft Corporation.
    3| # Licensed under the MIT License.
```

### only_rewrite example — click click-8.5.0/tests/test_utils/test_LazyFile.py:1
message: Invalid module name: 'test_LazyFile'
```
    1| import click
    2| 
    3| 
```

## ruff :: N818
reference: flake8 | only ruff: 346 | only reference: 243 | packages: 107
top messages: [only_rewrite] Exception name `InvalidVersion` should be named with an Error suffix ×9 || [only_rewrite] Exception name `RequestException` should be named with an Error suffix ×5 || [only_rewrite] Exception name `ConnectTimeout` should be named with an Error suffix ×5 || [only_rewrite] Exception name `MissingSchema` should be named with an Error suffix ×5

### only_rewrite example — authlib authlib-1.8.0/authlib/jose/errors.py:55
message: Exception name `InvalidAlgorithmForMultipleRecipientsMode` should be named with an Error suffix
```
   53| 
   54| 
   55| class InvalidAlgorithmForMultipleRecipientsMode(JoseError):
   56|     error = "invalid_algorithm_for_multiple_recipients_mode"
   57| 
```

### only_rewrite example — defusedxml defusedxml-0.7.1/defusedxml/common.py:18
message: Exception name `DefusedXmlException` should be named with an Error suffix
```
   16| 
   17| 
   18| class DefusedXmlException(ValueError):
   19|     """Base exception"""
   20| 
```

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/exceptions.py:10
message: Exception name `FeatureNotFound` should be named with an Error suffix
```
    8| 
    9| 
   10| class FeatureNotFound(ValueError):
   11|     """Exception raised by the BeautifulSoup constructor if no parser with the
   12|     requested features is found.
```

### only_reference example — exceptiongroup exceptiongroup-1.3.1/tests/test_exceptions.py:861
message: exception name 'MyExceptionGroup' should be named with an Error suffix
```
  859|                 pytest.fail("should not be reached")
  860| 
  861|         class MyExceptionGroup(base, MyException):
  862|             pass
  863| 
```

### only_reference example — anyio anyio-4.15.1/src/anyio/_core/_exceptions.py:166
message: exception name 'TaskCancelled' should be named with an Error suffix
```
  164| 
  165| 
  166| class TaskCancelled(TaskFailed):
  167|     """
  168|     Raised when awaiting on, or attempting to access the return value of, a
```

### only_reference example — docker docker-7.2.0/docker/errors.py:96
message: exception name 'ImageNotFound' should be named with an Error suffix
```
   94| 
   95| 
   96| class ImageNotFound(NotFound):
   97|     pass
   98| 
```

## ruff :: SIM103
reference: flake8 | only ruff: 538 | only reference: 0 | packages: 86
top messages: [only_rewrite] Return the condition directly ×162 || [only_rewrite] Return the negated condition directly ×119 || [only_rewrite] Return the condition `bool(hasattr(sys, 'getandroidapilevel'))` directly ×7 || [only_rewrite] Return the condition `not (type_ == "table" and name == "parent")` directly ×6

### only_rewrite example — awscli awscli-1.46.1/awscli/s3transfer/utils.py:326
message: Return the condition `bool(stat.S_ISSOCK(mode))` directly
```
  324|             return True
  325|         # Socket.
  326|         if stat.S_ISSOCK(mode):
  327|             return True
  328|         return False
```

### only_rewrite example — asn1crypto asn1crypto-1.5.1/asn1crypto/x509.py:288
message: Return the condition `hostname.lower() == other_hostname.lower()` directly
```
  286|             return False
  287| 
  288|         if hostname.lower() != other_hostname.lower():
  289|             return False
  290| 
```

### only_rewrite example — boto3 boto3-1.43.113/boto3/dynamodb/types.py:158
message: Return the condition `value is None` directly
```
  156| 
  157|     def _is_null(self, value):
  158|         if value is None:
  159|             return True
  160|         return False
```

## ruff :: PLC0415
reference: pylint | only ruff: 64 | only reference: 457 | packages: 53
top messages: [only_rewrite] `import` should be at the top-level of a file ×64 || [only_reference] Import outside toplevel (litellm.proxy._experimental.mcp_server.mcp_server_manager.global_ ×12 || [only_reference] Import outside toplevel (jnius.autoclass) ×12 || [only_reference] Import outside toplevel (litellm.proxy.auth.auth_utils.get_request_route) ×10

### only_rewrite example — docstring-parser docstring_parser-0.18.0/docstring_parser/tests/test_parse_from_object.py:13
message: `import` should be at the top-level of a file
```
   11| def test_from_module_attribute_docstrings() -> None:
   12|     """Test the parse of attribute docstrings from a module."""
   13|     from . import test_parse_from_object  # pylint: disable=C0415,W0406
   14| 
   15|     docstring = parse_from_object(test_parse_from_object)
```

### only_rewrite example — fastjsonschema fastjsonschema-2.22.2/fastjsonschema/ref_resolver.py:66
message: `import` should be at the top-level of a file
```
   64|         result = handlers[scheme](uri)
   65|     else:
   66|         from urllib.request import urlopen
   67| 
   68|         with urlopen(uri) as response:
```

### only_rewrite example — dnspython dnspython-2.9.0/dns/asyncquery.py:527
message: `import` should be at the top-level of a file
```
  525|     if resolver is None:
  526|         # pylint: disable=import-outside-toplevel,redefined-outer-name
  527|         import dns.asyncresolver
  528| 
  529|         resolver = dns.asyncresolver.Resolver()
```

### only_reference example — distro distro-1.9.0/tests/test_distro.py:46
message: Import outside toplevel (distro)
```
   44|     def test_cant_use_on_windows(self) -> None:
   45|         try:
   46|             import distro  # NOQA
   47|         except ImportError as ex:
   48|             assert "Unsupported platform" in str(ex)
```

### only_reference example — asyncpg asyncpg-0.32.0/tests/test__sourcecode.py:21
message: Import outside toplevel (flake8)
```
   19|     def test_flake8(self):
   20|         try:
   21|             import flake8  # NoQA
   22|         except ImportError:
   23|             raise unittest.SkipTest('flake8 module is missing')
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/s3/_s3_tables_iceberg.py:112
message: Import outside toplevel (pyiceberg.exceptions.NoSuchTableError, pyiceberg.exceptions.RESTError)
```
  110|     ... )
  111|     """
  112|     from pyiceberg.exceptions import NoSuchTableError, RESTError  # noqa: PLC0415
  113|     from pyiceberg.expressions import AlwaysTrue  # noqa: PLC0415
  114| 
```

## ruff :: SIM113
reference: flake8 | only ruff: 107 | only reference: 372 | packages: 79
top messages: [only_reference] Use enumerate for 'count' ×72 || [only_reference] Use enumerate for 'i' ×42 || [only_reference] Use enumerate for 'row' ×33 || [only_rewrite] Use `enumerate()` for index variable `i` in `for` loop ×27

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/tests/__init__.py:258
message: Use `enumerate()` for index variable `idx` in `for` loop
```
  256|                     child, child.next_sibling, None
  257|                 )
  258|             idx += 1
  259| 
  260|         child = descendant if descendant is not None else child
```

### only_rewrite example — awswrangler awswrangler-3.17.1/awswrangler/athena/_cache.py:223
message: Use `enumerate()` for index variable `num_executions_inspected` in `for` loop
```
  221|                     query_execution_payload=query_info,
  222|                 )
  223|         num_executions_inspected += 1
  224|         _logger.debug("num_executions_inspected: %s", num_executions_inspected)
  225|         if num_executions_inspected >= max_cache_query_inspections:
```

### only_rewrite example — gitdb gitdb-4.0.12/gitdb/test/performance/test_pack_streaming.py:45
message: Use `enumerate()` for index variable `count` in `for` loop
```
   43|         st = time()
   44|         for sha in pdb.sha_iter():
   45|             count += 1
   46|             pdb.stream(sha)
   47|             if count == ni:
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/tests/__init__.py:181
message: Use enumerate for 'idx'
```
  179|             )
  180| 
  181|         idx = 0
  182|         child = None
  183|         last_child = None
```

### only_reference example — chardet chardet-7.6.0/scripts/diagnose_accuracy.py:69
message: Use enumerate for 'total'
```
   67|     ] = []  # (expected, language, size, path)
   68| 
   69|     total = 0
   70|     correct = 0
   71| 
```

### only_reference example — docutils docutils-0.23/tools/dev/generate_punctuation_chars.py:297
message: Use enumerate for 'c'
```
  295|     """Line-wrap a unicode string literal definition."""
  296|     s = s.encode('unicode-escape').decode()
  297|     c = len(startstring)
  298|     left_indent = ' '*(c - len(startstring.lstrip(' ')))
  299|     line_start_string = f"\n    {left_indent}'"
```

## ruff :: PLR0917
reference: pylint | only ruff: 121 | only reference: 325 | packages: 35
top messages: [only_reference] Too many positional arguments (6/5) ×95 || [only_reference] Too many positional arguments (7/5) ×54 || [only_rewrite] Too many positional arguments (6 > 5) ×46 || [only_reference] Too many positional arguments (8/5) ×42

### only_rewrite example — attrs attrs-26.1.0/tests/strategies.py:121
message: Too many positional arguments (6 > 5)
```
  119| 
  120| @st.composite
  121| def simple_classes(
  122|     draw,
  123|     slots=None,
```

### only_rewrite example — google-genai google_genai-2.30.1/google/genai/_gaos/utils/metadata.py:92
message: Too many positional arguments (7 > 5)
```
   90|     multipart: Optional[MultipartFormMetadata] = None
   91| 
   92|     def __init__(
   93|         self,
   94|         security: Optional[SecurityMetadata] = None,
```

### only_rewrite example — opentelemetry-sdk opentelemetry_sdk-1.45.1/tests/test_configurator.py:265
message: Too many positional arguments (7 > 5)
```
  263|         return "CustomSampler"
  264| 
  265|     def should_sample(
  266|         self,
  267|         parent_context: Context | None,
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/postgresql.py:245
message: Too many positional arguments (9/5)
```
  243| 
  244| @overload
  245| def read_sql_query(
  246|     sql: str,
  247|     con: "pg8000.Connection",
```

### only_reference example — babel babel-2.18.0/babel/numbers.py:204
message: Too many positional arguments (6/5)
```
  202| 
  203| @overload
  204| def get_territory_currencies(
  205|     territory: str,
  206|     start_date: datetime.date | None = ...,
```

### only_reference example — anyio anyio-4.15.1/src/anyio/_core/_concurrency_utils.py:64
message: Too many positional arguments (6/5)
```
   62| 
   63| @overload
   64| async def gather(
   65|     coro1: Coroutine[Any, Any, R],
   66|     coro2: Coroutine[Any, Any, S],
```

## ruff :: E701
reference: flake8 | only ruff: 42 | only reference: 374 | packages: 27
top messages: [only_reference] multiple statements on one line (colon) ×374 || [only_rewrite] Multiple statements on one line (colon) ×42

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/clientmodule_test.py:4
message: Multiple statements on one line (colon)
```
    2| from data.suppliermodule_test import Interface as IFace, DoNothing
    3| 
    4| class Toto: pass
    5| 
    6| class Ancestor:
```

### only_rewrite example — executing executing-2.3.0/tests/small_samples/ordinary_comparison_is_not_annotation_code.py:3
message: Multiple statements on one line (colon)
```
    1| # User-written code resembling an annotation header must still map to AST nodes.
    2| def callback(format, /):
    3|     if format > 2: raise NotImplementedError
```

### only_rewrite example — black black-26.10.1/tests/data/cases/pattern_matching_style.py:3
message: Multiple statements on one line (colon)
```
    1| # flags: --minimum-version=3.10
    2| match something:
    3|     case b(): print(1+1)
    4|     case c(
    5|         very_complex=True,
```

### only_reference example — black black-26.10.1/tests/data/miscellaneous/force_pyi.py:7
message: multiple statements on one line (colon)
```
    5| def zoo(): ...
    6| 
    7| class A: ...
    8| @bar
    9| class B:
```

### only_reference example — aiobotocore aiobotocore-3.9.2/tests/test_config.py:84
message: multiple statements on one line (colon)
```
   82| 
   83|     # A subclass is still the httpx backend, so it gets the same validation.
   84|     class MyHttpxSession(HttpxSession): ...
   85| 
   86|     with pytest.raises(
```

### only_reference example — anthropic anthropic-1.13.0/tests/test_response.py:22
message: multiple statements on one line (colon)
```
   20| 
   21| 
   22| class ConcreteBaseAPIResponse(APIResponse[bytes]): ...
   23| 
   24| 
```

## ruff :: B905
reference: flake8 | only ruff: 276 | only reference: 130 | packages: 18
top messages: [only_rewrite] `zip()` without an explicit `strict=` parameter ×276 || [only_reference] `zip()` without an explicit `strict=` parameter. ×130

### only_rewrite example — asttokens asttokens-3.0.2/asttokens/util.py:154
message: `zip()` without an explicit `strict=` parameter
```
  152|     # override the iteration order: instead of <all keys>, <all values>,
  153|     # yield keys and values in source order (key1, value1, key2, value2, ...)
  154|     for (key, value) in zip(node.keys, node.values):
  155|       if key is not None:
  156|         yield key
```

### only_rewrite example — executing executing-2.3.0/tests/samples/bird.py:1011
message: `zip()` without an explicit `strict=` parameter
```
 1009| 
 1010|             indices = set(_sample_indices(num_cols, max_cols))
 1011|             for i, (formatted_name, label) in enumerate(zip(val.columns.format(sparsify=False),
 1012|                                                             val.columns)):
 1013|                 if i in indices:
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/matrices/linsolve.py:103
message: `zip()` without an explicit `strict=` parameter
```
  101|     for i, v in P.items():
  102|         sol[syms[i]].append(K.to_sympy(v))
  103|     for npi, Vi in zip(nonpivots, V):
  104|         sym = syms[npi]
  105|         for i, v in Vi.items():
```

### only_reference example — aioitertools aioitertools-0.13.0/aioitertools/itertools.py:176
message: `zip()` without an explicit `strict=` parameter.
```
  174|             ...  # 0, 3, 4
  175|     """
  176|     async for value, selector in zip(itr, selectors):
  177|         if selector:
  178|             yield value
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/cu2qu/ufo.py:196
message: `zip()` without an explicit `strict=` parameter.
```
  194| 
  195|     try:
  196|         segments_by_location = zip(*[_get_segments(g) for g in glyphs])
  197|     except UnequalZipLengthsError:
  198|         raise IncompatibleSegmentNumberError(glyphs)
```

### only_reference example — more-itertools more_itertools-11.2.0/more_itertools/recipes.py:767
message: `zip()` without an explicit `strict=` parameter.
```
  765|     """
  766|     trues, after = tee(it)
  767|     trues = compress(takewhile(predicate, trues), zip(after))
  768|     return trues, after
  769| 
```

## ruff :: F821
reference: flake8 | only ruff: 350 | only reference: 56 | packages: 9
top messages: [only_rewrite] Undefined name `self` ×34 || [only_rewrite] Undefined name `token` ×25 || [only_rewrite] Undefined name `Dict` ×23 || [only_rewrite] Undefined name `syms` ×22

### only_rewrite example — dill dill-0.4.1/dill/_dill.py:1716
message: Undefined name `diff`
```
 1714|         if obj.__name__.split('.', 1)[0] != "dill":
 1715|             try:
 1716|                 changed = diff.whats_changed(obj, seen=pickler._diff_cache)[0]
 1717|             except RuntimeError:  # not memorised module, probably part of dill
 1718|                 pass
```

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/format.py:4
message: Undefined name `function`
```
    2| """
    3| 
    4| function('aeozrijz\
    5| earzer', hop)
    6| # XXX write test
```

### only_rewrite example — executing .0/tests/small_samples/2fa69a57eb3b16f9ce0d5be427ad471c93a54c6d7e68b5be024b6a046ecc6bb2.py:16
message: Undefined name `self`
```
   14| # 
   15| 
   16| with self as session:
   17|     assert isinstance
   18|     db_func
```

### only_reference example — langchain-core langchain_core-1.6.10/tests/unit_tests/utils/test_function_calling.py:56
message: undefined name 'foo'
```
   54| def annotated_function() -> Callable[[int, Literal["bar", "baz"]], None]:
   55|     def dummy_function(
   56|         arg1: ExtensionsAnnotated[int, "foo"],
   57|         arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"],
   58|     ) -> None:
```

### only_reference example — pydantic pydantic-2.14.1/tests/test_forward_ref.py:962
message: undefined name 'types'
```
  960|     class Expression_(BaseModel):
  961|         model_config = dict(undefined_types_warning=False)
  962|         Or: ForwardRef("types['allOfExpressions']")
  963|         Not: ForwardRef("types['allOfExpression']")
  964| 
```

### only_reference example — typing-extensions typing_extensions-4.16.0/src/test_typing_extensions.py:1556
message: undefined name 'hello'
```
 1554|         arg = 42
 1555|         self.assertIs(assert_type(arg, 42), arg)
 1556|         self.assertIs(assert_type(arg, 'hello'), arg)
 1557| 
 1558| 
```

## ruff :: PLR0915
reference: pylint | only ruff: 231 | only reference: 170 | packages: 101
top messages: [only_reference] Too many statements (51/50) ×88 || [only_rewrite] Too many statements (51 > 50) ×50 || [only_rewrite] Too many statements (52 > 50) ×41 || [only_rewrite] Too many statements (53 > 50) ×23

### only_rewrite example — decorator decorator-5.3.1/src/decorator/__init__.py:368
message: Too many statements (55 > 50)
```
  366| 
  367| # inspired from simplegeneric by P.J. Eby and functools.singledispatch
  368| def dispatch_on(*dispatch_args):
  369|     """
  370|     Factory of decorators turning a function into a generic function
```

### only_rewrite example — asyncpg asyncpg-0.32.0/tests/test_codecs.py:1286
message: Too many statements (51 > 50)
```
 1284|             ''')
 1285| 
 1286|     async def test_custom_codec_binary(self):
 1287|         """Test encoding/decoding using a custom codec in binary mode."""
 1288|         await self.con.execute('''
```

### only_rewrite example — babel babel-2.18.0/tests/test_dates.py:1033
message: Too many statements (51 > 50)
```
 1031| 
 1032| 
 1033| def test_week_numbering_friday_mindays_1():
 1034|     locale = Locale.parse('dv_MV')
 1035|     assert locale.first_week_day == 4
```

### only_reference example — aiobotocore aiobotocore-3.9.2/aiobotocore/httpsession.py:272
message: Too many statements (53/50)
```
  270|         )
  271| 
  272|     async def send(self, request):
  273|         try:
  274|             proxy_url = self._proxy_config.proxy_url_for(request.url)
```

### only_reference example — contourpy contourpy-1.4.0/lib/contourpy/convert.py:189
message: Too many statements (51/50)
```
  187| 
  188| 
  189| def _convert_filled_from_ChunkCombinedOffsetOffset(
  190|     filled: cpy.FillReturn_ChunkCombinedOffsetOffset,
  191|     fill_type_to: FillType,
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/catalog/_create.py:39
message: Too many statements (80/50)
```
   37| 
   38| 
   39| def _create_table(  # noqa: PLR0912,PLR0915
   40|     database: str,
   41|     table: str,
```

## ruff :: PLC1802
reference: pylint | only ruff: 22 | only reference: 333 | packages: 39
top messages: [only_reference] Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty ×333 || [only_rewrite] `len(kwargs)` used as condition without comparison ×4 || [only_rewrite] `len(actual)` used as condition without comparison ×2 || [only_rewrite] `len(tags)` used as condition without comparison ×2

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/legacy.py:32
message: `len(kwargs)` used as condition without comparison
```
   30|                                   to their more modern equivalents?
   31|     """
   32|     if len(kwargs):
   33|         warn(
   34|             f"charset-normalizer disregard arguments '{','.join(list(kwargs.keys()))}' in legacy function detect()"
```

### only_rewrite example — azure-identity azure_identity-1.26.0/tests/test_default_async.py:122
message: `len(actual)` used as condition without comparison
```
  120|     def assert_credentials_not_present(chain, *credential_classes):
  121|         actual = {c.__class__ for c in chain.credentials}
  122|         assert len(actual)
  123| 
  124|         # no unexpected credential is in the chain
```

### only_rewrite example — docutils docutils-0.23/docutils/writers/html5_polyglot/__init__.py:267
message: `len(tags)` used as condition without comparison
```
  265|             tags = [cls for cls in self.supported_inline_tags
  266|                     if cls in classes]
  267|             if len(tags):
  268|                 node.html5tagname = tags[0]
  269|                 classes.remove(node.html5tagname)
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/element.py:3269
message: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty
```
 3267|         breadth-first sequence.
 3268|         """
 3269|         if not len(self.contents):
 3270|             return
 3271|         # _last_descendant() can't return None here because
```

### only_reference example — gitdb gitdb-4.0.12/gitdb/test/test_pack.py:163
message: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty
```
  161| 
  162|                 # try all calls
  163|                 assert len(entity.collect_streams(info.binsha))
  164|                 oinfo = entity.info(info.binsha)
  165|                 assert isinstance(oinfo, OInfo)
```

### only_reference example — alembic alembic-1.20.0/tests/test_batch.py:924
message: Do not use `len(SEQUENCE)` without comparison to determine if a sequence is empty
```
  922|         new_table = self._assert_impl(impl)
  923|         assert not new_table.c.id.primary_key
  924|         assert not len(new_table.primary_key)
  925| 
  926| 
```

## ruff :: PLC0206
reference: pylint | only ruff: 111 | only reference: 242 | packages: 58
top messages: [only_reference] Consider iterating with .items() ×242 || [only_rewrite] Extracting value from dictionary without calling `.items()` ×111

### only_rewrite example — authlib authlib-1.8.0/authlib/oauth2/claims.py:42
message: Extracting value from dictionary without calling `.items()`
```
   40| 
   41|     def _extract_validate_hooks(self, options: dict[str, ClaimsOption]):
   42|         for key in options:
   43|             validate = options[key].pop("validate", None)
   44|             if validate:
```

### only_rewrite example — azure-core azure_core-1.41.0/azure/core/utils/_connection_string_parser.py:36
message: Extracting value from dictionary without calling `.items()`
```
   34|         # if duplicate case insensitive keys are passed in, raise error
   35|         new_args_dict = {}
   36|         for key in args_dict.keys():  # pylint: disable=consider-using-dict-items
   37|             new_key = key.lower()
   38|             if new_key in new_args_dict:
```

### only_rewrite example — alembic alembic-1.20.0/alembic/autogenerate/compare/constraints.py:436
message: Extracting value from dictionary without calling `.items()`
```
  434|         obj_added(obj)
  435| 
  436|     for uq_sig in unnamed_metadata_uniques:
  437|         if uq_sig not in conn_uniques_by_sig:
  438|             obj_added(unnamed_metadata_uniques[uq_sig])
```

### only_reference example — boto3 boto3-1.43.113/boto3/s3/transfer.py:365
message: Consider iterating with .items()
```
  363|         # S3TransferConfig so we add aliases so you can still access the
  364|         # old version of the names.
  365|         for alias in self.ALIAS:
  366|             setattr(
  367|                 self,
```

### only_reference example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/cd.py:62
message: Consider iterating with .items()
```
   60|         [
   61|             character_range
   62|             for character_range in seen_ranges
   63|             if seen_ranges[character_range] / character_count >= 0.15
   64|         ]
```

### only_reference example — authlib authlib-1.8.0/authlib/jose/rfc7517/jwk.py:38
message: Consider iterating with .items()
```
   36|         if kty is None:
   37|             raw_key = load_pem_key(raw)
   38|             for _kty in cls.JWK_KEY_CLS:
   39|                 key_cls = cls.JWK_KEY_CLS[_kty]
   40|                 if key_cls.validate_raw_key(raw_key):
```

## ruff :: PLR1716
reference: pylint | only ruff: 2 | only reference: 343 | packages: 64
top messages: [only_reference] Simplify chained comparison between the operands: 19968 <= cp <= 40959 ×48 || [only_reference] Simplify chained comparison between the operands: size == height <= width ×8 || [only_reference] Simplify chained comparison between the operands: min_image_tiles <= width * height <= max ×6 || [only_reference] Simplify chained comparison between the operands: 0 < x < 5 ×4

### only_rewrite example — pymupdf pymupdf-1.28.2/src/__init__.py:18515
message: Contains chained boolean comparison that can be simplified
```
18513| 
18514| def _INRANGE(v, low, high):
18515|     return low <= v and v <= high
18516| 
18517| 
```

### only_rewrite example — scipy scipy-1.18.1/subprojects/pyprima/pyprima/pyprima/src/pyprima/cobyla/cobylb.py:671
message: Contains chained boolean comparison that can be simplified
```
  669|     # Postconditions
  670|     if DEBUGGING:
  671|         assert cpen >= cpen and cpen > 0
  672|         assert preref + cpen * prerec > 0 or info == DAMAGING_ROUNDING or \
  673|             not (prerec >= 0 and np.maximum(prerec, preref) > 0) or not np.isfinite(preref)
```

### only_reference example — defusedxml defusedxml-0.7.1/defusedxml/xmlrpc.py:65
message: Simplify chained comparison between the operands: 0 <= limit < len(decoded)
```
   63|     f.close()
   64|     gzf.close()
   65|     if limit >= 0 and len(decoded) > limit:
   66|         raise ValueError("max gzipped payload length exceeded")
   67|     return decoded
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/dammit.py:1408
message: Simplify chained comparison between the operands: 55296 <= numeric <= 57343
```
 1406|             return replacement, True
 1407| 
 1408|         if numeric >= 0xd800 and numeric <= 0xdfff:
 1409|             # "If the number is a surrogate, then this is a
 1410|             # surrogate-character-reference parse error. Set the
```

### only_reference example — babel babel-2.18.0/babel/dates.py:2022
message: Simplify chained comparison between the operands: opt_width <= 2 < input_width
```
 2020|                 distance += 0x1000
 2021|             elif field == 'M' and (
 2022|                 (input_width > 2 and opt_width <= 2) or (input_width <= 2 and opt_width > 2)
 2023|             ):
 2024|                 # Magic weight constant for "text turns into a number"
```

## ruff :: SIM115
reference: flake8 | only ruff: 186 | only reference: 149 | packages: 82
top messages: [only_rewrite] Use a context manager for opening files ×186 || [only_reference] Use context handler for opening files ×149

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/diagnose.py:253
message: Use a context manager for opening files
```
  251| def profile(num_elements: int = 100000, parser: str = "lxml") -> None:
  252|     """Use Python's profiler on a randomly generated document."""
  253|     filehandle = tempfile.NamedTemporaryFile()
  254|     filename = filehandle.name
  255| 
```

### only_rewrite example — asyncpg asyncpg-0.32.0/tests/test_connect.py:1271
message: Use a context manager for opening files
```
 1269| 
 1270|     def test_connect_connection_service_file(self):
 1271|         connection_service_file = tempfile.NamedTemporaryFile(
 1272|             'w+t', delete=False)
 1273|         connection_service_file.write(textwrap.dedent('''
```

### only_rewrite example — anyio anyio-4.15.1/src/anyio/_core/_tempfile.py:98
message: Use a context manager for opening files
```
   96|     async def __aenter__(self) -> AsyncFile[AnyStr]:
   97|         fp = await to_thread.run_sync(
   98|             lambda: tempfile.TemporaryFile(
   99|                 self.mode,
  100|                 self.buffering,
```

### only_reference example — awscli awscli-1.46.1/awscli/s3transfer/utils.py:287
message: Use context handler for opening files
```
  285| 
  286|     def open(self, filename, mode):
  287|         return open(filename, mode)
  288| 
  289|     def remove_file(self, filename):
```

### only_reference example — aiofiles aiofiles-25.1.0/tests/threadpool/test_concurrency.py:19
message: Use context handler for opening files
```
   17|     def new_open(*args, **kwargs):
   18|         time.sleep(1)
   19|         return open(*args, **kwargs)
   20| 
   21|     monkeypatch.setattr(aiofiles.threadpool, "sync_open", value=new_open)
```

### only_reference example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/cli/__main__.py:75
message: Use context handler for opening files
```
   73|         # all other arguments are used as file names
   74|         try:
   75|             return open(string, self._mode, self._bufsize, self._encoding, self._errors)
   76|         except OSError as e:
   77|             message = f"can't open '{string}': {e}"
```

## ruff :: PLR0124
reference: pylint | only ruff: 2 | only reference: 329 | packages: 27
top messages: [only_reference] Redundant comparison - transport.operations_client is transport.operations_client ×208 || [only_reference] Redundant comparison - 
 == 
 ×12 || [only_reference] Redundant comparison - cond1 == cond1 ×10 || [only_reference] Redundant comparison - 1 == 1 ×7

### only_rewrite example — attrs attrs-26.1.0/tests/test_dunders.py:964
message: Name compared with itself, consider replacing `NOTHING == NOTHING`
```
  962|         All instances are equal.
  963|         """
  964|         assert NOTHING == NOTHING == NOTHING
  965|         assert not (NOTHING != NOTHING)
  966|         assert 1 != NOTHING
```

### only_rewrite example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/statement/raise.py:58
message: Name compared with itself
```
   56| raise aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa[aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:bbbbbbbbbbbbbbbbbbbbbbbbbb]
   57| 
   58| raise aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa < aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa <aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa
   59| 
   60| raise aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfk < (aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajl < aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlah
```

### only_reference example — jaraco-functools jaraco_functools-4.6.0/test_functools.py:142
message: Redundant comparison - ob.mything == ob.mything
```
  140|         ob = ClassUnderTest()
  141| 
  142|         assert ob.mything == ob.mything
  143| 
  144|     @pytest.mark.xfail(reason="can't replace property with cache; #6")
```

### only_reference example — google-auth google_auth-2.62.0/tests/oauth2/test_credentials.py:68
message: Redundant comparison - creds.scopes is creds.scopes
```
   66| 
   67|         # Verify consistency (property returns the same object)
   68|         assert creds.scopes is creds.scopes
   69| 
   70|         # Verify modifications persist
```

### only_reference example — jsonpointer jsonpointer-3.2.1/tests.py:162
message: Redundant comparison - self.ptr1 in self.ptr1
```
  160|     def test_contains_magic(self):
  161|         self.assertTrue(self.ptr2 in self.ptr1)
  162|         self.assertTrue(self.ptr1 in self.ptr1)
  163|         self.assertFalse(self.ptr3 in self.ptr1)
  164| 
```

## ruff :: W291
reference: flake8 | only ruff: 326 | only reference: 4 | packages: 4
top messages: [only_rewrite] Trailing whitespace ×326 || [only_reference] trailing whitespace ×4

### only_rewrite example — markdown markdown-3.11.1/tests/test_syntax/extensions/test_tables.py:35
message: Trailing whitespace
```
   33| ------------- | -------------
   34|    | Content Cell
   35| Content Cell  |  
   36| """
   37| 
```

### only_rewrite example — executing .0/tests/small_samples/a9cf2f563ac80ad0066c4ef3ac10fa2f146252db49b3a0a9cb69e0c03e07827b.py:2
message: Trailing whitespace
```
    1| # This sample was generated for the following code mutation detected by mutmut:
    2| # 
    3| # --- executing/_position_node_finder.py
    4| # +++ executing/_position_node_finder.py
```

### only_rewrite example — black black-26.10.1/tests/data/cases/form_feeds.py:86
message: Trailing whitespace
```
   84| 
   85| pass
   86| 
   87| 
   88| 
```

### only_reference example — black black-26.10.1/tests/data/cases/form_feeds.py:39
message: trailing whitespace
```
   37| 
   38| 
   39| 
   40| 
   41| #
```

### only_reference example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/black/cases/form_feeds.py:37
message: trailing whitespace
```
   35| 
   36| 
   37| 
   38| #
   39| 
```

## ruff :: PLW0012
reference: pylint | only ruff: 0 | only reference: 285 | packages: 8
top messages: [only_reference] Unknown option value for 'disable', expected a valid pylint message and got 'g-import-not- ×129 || [only_reference] Unknown option value for 'disable', expected a valid pylint message and got 'g-multiple-im ×44 || [only_reference] Unknown option value for 'disable', expected a valid pylint message and got 'do-not-import ×15 || [only_reference] Unknown option value for 'disable', expected a valid pylint message and got 'docstring-mis ×15

### only_reference example — azure-identity azure_identity-1.26.0/azure/identity/_internal/msal_managed_identity_client.py:22
message: Unknown option value for 'disable', expected a valid pylint message and got 'client-accepts-api-version-keyword'
```
   20| 
   21| 
   22| class MsalManagedIdentityClient(abc.ABC):  # pylint:disable=client-accepts-api-version-keyword
   23|     """Base class for managed identity client wrapping MSAL ManagedIdentityClient."""
   24| 
```

### only_reference example — azure-core azure_core-1.41.0/azure/core/rest/_requests_basic.py:27
message: Unknown option value for 'disable', expected a valid pylint message and got 'networking-import-outside-azure-core-transport'
```
   25| # --------------------------------------------------------------------------
   26| import collections.abc as collections
   27| from requests.structures import (  # pylint: disable=networking-import-outside-azure-core-transport
   28|     CaseInsensitiveDict,
   29| )
```

### only_reference example — grpcio ith-bazel/third_party/googletest/googletest/test/googletest-fail-if-no-test-linked-test.py:1
message: Unknown option value for 'disable', expected a valid pylint message and got 'g-interpreter-mismatch'
```
    1| #!/usr/bin/env python3  # pylint: disable=g-interpreter-mismatch
    2| #
    3| # Copyright 2025, Google Inc.
```
