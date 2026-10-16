
## ruff :: W293
reference: flake8 | only ruff: 105 | only reference: 0 | packages: 4
top messages: [only_rewrite] Blank line contains whitespace ×105

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:28
message: Blank line contains whitespace
```
   26|     """hehe"""
   27|     a = 1
   28|     
   29|     def __init__(self):
   30|         try:
```

### only_rewrite example — executing .0/tests/small_samples/88f983dcf04b0d0b09cb105943226d186f9f6a8ada3da7c48a1a3a1c0d947995.py:6
message: Blank line contains whitespace
```
    4| # +++ executing/_position_node_finder.py
    5| # @@ -11,7 +11,7 @@
    6|  
    7|  
    8| #  def parents(node: EnhancedAST) -> Iterator[EnhancedAST]:
```

### only_rewrite example — black black-26.10.1/tests/data/cases/form_feeds.py:1
message: Blank line contains whitespace
```
    1| 
    2| 
    3| 
```

## ruff :: PLW0406
reference: pylint | only ruff: 1 | only reference: 95 | packages: 22
top messages: [only_reference] Module import itself ×95 || [only_rewrite] Module `docstring_parser.tests.test_parse_from_object` imports itself ×1

### only_rewrite example — docstring-parser docstring_parser-0.18.0/docstring_parser/tests/test_parse_from_object.py:13
message: Module `docstring_parser.tests.test_parse_from_object` imports itself
```
   11| def test_from_module_attribute_docstrings() -> None:
   12|     """Test the parse of attribute docstrings from a module."""
   13|     from . import test_parse_from_object  # pylint: disable=C0415,W0406
   14| 
   15|     docstring = parse_from_object(test_parse_from_object)
```

### only_reference example — jaraco-functools jaraco_functools-4.6.0/jaraco/functools/__init__.py:4
message: Module import itself
```
    2| 
    3| import collections.abc
    4| import functools
    5| import inspect
    6| import itertools
```

### only_reference example — gunicorn gunicorn-26.2.0/gunicorn/app/wsgiapp.py:65
message: Module import itself
```
   63|     generic WSGI applications.
   64|     """
   65|     from gunicorn.app.wsgiapp import WSGIApplication
   66|     WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
   67| 
```

### only_reference example — litellm litellm-1.105.0/litellm/types/llms/openai.py:7
message: Module import itself
```
    5| 
    6| import httpx
    7| from openai import Omit
    8| from openai._legacy_response import (
    9|     HttpxBinaryResponseContent as _HttpxBinaryResponseContent,
```

## ruff :: PLR0911
reference: pylint | only ruff: 49 | only reference: 24 | packages: 13
top messages: [only_rewrite] Too many return statements (7 > 6) ×13 || [only_rewrite] Too many return statements (8 > 6) ×10 || [only_reference] Too many return statements (13/6) ×7 || [only_rewrite] Too many return statements (9 > 6) ×7

### only_rewrite example — azure-core azure_core-1.41.0/tests/specs_sdk/modeltypes/modeltypes/_utils/serialization.py:956
message: Too many return statements (14 > 6)
```
  954|         return serialized
  955| 
  956|     def serialize_object(self, attr, **kwargs):  # pylint: disable=too-many-return-statements
  957|         """Serialize a generic object.
  958|         This will be handled as a dictionary. If object passed in is not
```

### only_rewrite example — google-genai google_genai-2.30.1/google/genai/_gaos/utils/serializers.py:186
message: Too many return statements (9 > 6)
```
  184| 
  185| 
  186| def _construct_lenient(value: Any, typ: Any, depth: int) -> Any:
  187|     if depth > _CONSTRUCT_UNVALIDATED_MAX_DEPTH:
  188|         return value
```

### only_rewrite example — azure-storage-blob azure_storage_blob-12.31.0/azure/storage/blob/_shared/authentication.py:58
message: Too many return statements (7 > 6)
```
   56| 
   57| 
   58| def compare(lhs: str, rhs: str) -> int:  # pylint:disable=too-many-return-statements
   59|     tables = [table_lv0, table_lv4]
   60|     curr_level, i, j, n = 0, 0, 0, len(tables)
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/timestream/_read.py:23
message: Too many return statements (8/6)
```
   21| 
   22| 
   23| def _cast_value(value: str, dtype: str) -> Any:  # noqa: PLR0911
   24|     if dtype == "VARCHAR":
   25|         return value
```

### only_reference example — marshmallow marshmallow-4.3.1/src/marshmallow/error_store.py:37
message: Too many return statements (10/6)
```
   35| 
   36| 
   37| def merge_errors(errors1, errors2):  # noqa: PLR0911
   38|     """Deeply merge two error messages.
   39| 
```

### only_reference example — narwhals narwhals-2.27.1/tests/translate/get_native_namespace_test.py:16
message: Too many return statements (10/6)
```
   14| 
   15| 
   16| def _get_expected_namespace(constructor_name: str) -> Any | None:  # noqa: PLR0911
   17|     """Get expected namespace module for a given constructor."""
   18|     if "pandas" in constructor_name:
```

## ruff :: C420
reference: flake8 | only ruff: 72 | only reference: 0 | packages: 26
top messages: [only_rewrite] Unnecessary dict comprehension for iterable; use `dict.fromkeys` instead ×72

### only_rewrite example — azure-storage-blob azure_storage_blob-12.31.0/tests/test_container_async.py:860
message: Unnecessary dict comprehension for iterable; use `dict.fromkeys` instead
```
  858|             permission=ContainerSasPermissions(read=True), expiry=expiry_time, start=start_time
  859|         )
  860|         identifiers = {i: access_policy for i in range(2)}
  861| 
  862|         # Act
```

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/feaLib/builder.py:1435
message: Unnecessary dict comprehension for iterable; use `dict.fromkeys` instead
```
 1433|         self.add_any_subst_(
 1434|             location,
 1435|             {g: (replacement,) for g in itertools.product(*glyphs)},
 1436|         )
 1437| 
```

### only_rewrite example — huggingface-hub huggingface_hub-2.2.0/src/huggingface_hub/hf_api.py:6692
message: Unnecessary dict comprehension for iterable; use `dict.fromkeys` instead
```
 6690|                 metadata=None,
 6691|                 sharded=False,
 6692|                 weight_map={
 6693|                     tensor_name: constants.SAFETENSORS_SINGLE_FILE for tensor_name in file_metadata.tensors.keys()
 6694|                 },
```

## ruff :: B017
reference: flake8 | only ruff: 71 | only reference: 0 | packages: 9
top messages: [only_rewrite] Do not assert blind exception: `Exception` ×71

### only_rewrite example — fonttools fonttools-4.66.1/Tests/misc/xmlWriter_test.py:54
message: Do not assert blind exception: `Exception`
```
   52| 
   53|     def test_encoding_other(self):
   54|         self.assertRaises(Exception, XMLWriter, BytesIO(), encoding="iso-8859-1")
   55| 
   56|     def test_write(self):
```

### only_rewrite example — ipython ipython-9.17.1/tests/test_run.py:408
message: Do not assert blind exception: `Exception`
```
  406|     from nbformat import v4, writes
  407| 
  408|     pytest.raises(Exception, _ip.run_line_magic, "run")
  409|     pytest.raises(Exception, _ip.run_line_magic, "run", "foobar.ipynb")
  410| 
```

### only_rewrite example — multiprocess multiprocess-0.70.19/py3.9/multiprocess/tests/__init__.py:2980
message: Do not assert blind exception: `Exception`
```
 2978|         # Because we are using xmlrpclib for serialization instead of
 2979|         # pickle this will cause a serialization error.
 2980|         self.assertRaises(Exception, queue.put, time.sleep)
 2981| 
 2982|         # Make queue finalizer run before the server is stopped
```

## ruff :: N801
reference: flake8 | only ruff: 66 | only reference: 0 | packages: 12
top messages: [only_rewrite] Class name `fabs` should use CapWords convention ×3 || [only_rewrite] Class name `foo` should use CapWords convention ×3 || [only_rewrite] Class name `debile` should use CapWords convention ×2 || [only_rewrite] Class name `name_2` should use CapWords convention ×2

### only_rewrite example — attrs attrs-26.1.0/tests/test_validators.py:396
message: Class name `TestIn_` should use CapWords convention
```
  394| 
  395| 
  396| class TestIn_:
  397|     """
  398|     Tests for `in_`.
```

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/format.py:20
message: Class name `debile` should use CapWords convention
```
   18|     return a + b + c
   19| 
   20| class debile(dict,
   21|              object):
   22|     pass
```

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/misc/testTools.py:99
message: Class name `TestXMLReader_` should use CapWords convention
```
   97| 
   98| 
   99| class TestXMLReader_(object):
  100|     def __init__(self):
  101|         from xml.parsers.expat import ParserCreate
```

## ruff :: B006
reference: flake8 | only ruff: 9 | only reference: 54 | packages: 13
top messages: [only_reference] Do not use mutable data structures for argument defaults.  They are created during functio ×54 || [only_rewrite] Do not use mutable data structures for argument defaults ×9

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/jscode.py:58
message: Do not use mutable data structures for argument defaults
```
   56|     })
   57| 
   58|     def __init__(self, settings={}):
   59|         CodePrinter.__init__(self, settings)
   60|         self.known_functions = dict(known_functions)
```

### only_reference example — anthropic anthropic-1.13.0/src/anthropic/lib/bedrock/_mantle.py:290
message: Do not use mutable data structures for argument defaults.  They are created during function definition time. All calls to the function reuse this one instance o
```
  288|         set_default_query: Mapping[str, object] | None = None,
  289|         middleware: Sequence[MiddlewareInput] | None | NotGiven = not_given,
  290|         _extra_kwargs: Mapping[str, Any] = {},
  291|     ) -> Self:
  292|         """
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/ufoLib/filenames.py:222
message: Do not use mutable data structures for argument defaults.  They are created during function definition time. All calls to the function reuse this one instance o
```
  220| 
  221| def handleClash1(
  222|     userName: str, existing: Iterable[str] = [], prefix: str = "", suffix: str = ""
  223| ) -> str:
  224|     """A helper function that resolves collisions with existing names when choosing a filename.
```

### only_reference example — google-cloud-aiplatform google_cloud_aiplatform-2.4.0/agentplatform/_genai/_runtimes_utils.py:709
message: Do not use mutable data structures for argument defaults.  They are created during function definition time. All calls to the function reuse this one instance o
```
  707|     *,
  708|     schema_name: Optional[str] = None,
  709|     descriptions: Mapping[str, str] = {},
  710|     required: Sequence[str] = [],
  711| ) -> Dict[str, Any]:
```

## ruff :: PLW1508
reference: pylint | only ruff: 49 | only reference: 13 | packages: 30
top messages: [only_rewrite] Invalid type for environment variable default; expected `str` or `None` ×49 || [only_reference] os.getenv default type is builtins.int. Expected str or None. ×11 || [only_reference] os.getenv default type is asyncpg.connect_utils.SessionAttribute.any. Expected str or None ×1 || [only_reference] os.getenv default type is builtins.bool. Expected str or None. ×1

### only_rewrite example — azure-identity azure_identity-1.26.0/azure/identity/_credentials/environment.py:77
message: Invalid type for environment variable default; expected `str` or `None`
```
   75|                 password=os.environ.get(EnvironmentVariables.AZURE_CLIENT_CERTIFICATE_PASSWORD),
   76|                 send_certificate_chain=bool(
   77|                     os.environ.get(EnvironmentVariables.AZURE_CLIENT_SEND_CERTIFICATE_CHAIN, False)
   78|                 ),
   79|                 **kwargs
```

### only_rewrite example — azure-core azure_core-1.41.0/azure/core/pipeline/policies/_universal.py:491
message: Invalid type for environment variable default; expected `str` or `None`
```
  489|             redacted_url = sanitize_url(http_request.url, self.allowed_query_params, self.REDACTED_PLACEHOLDER)
  490| 
  491|             multi_record = os.environ.get(HttpLoggingPolicy.MULTI_RECORD_LOG, False)
  492|             if multi_record:
  493|                 logger.log(log_level, "Request URL: %r", redacted_url)
```

### only_rewrite example — cffi cffi-2.1.1/setup.py:165
message: Invalid type for environment variable default; expected `str` or `None`
```
  163|     library_dirs.append('/usr/local/lib')
  164| 
  165| forced_extra_objs = os.environ.get('CFFI_FORCE_STATIC', [])
  166| if forced_extra_objs:
  167|     forced_extra_objs = forced_extra_objs.split(';')
```

### only_reference example — asyncpg asyncpg-0.32.0/asyncpg/connect_utils.py:843
message: os.getenv default type is asyncpg.connect_utils.SessionAttribute.any. Expected str or None.
```
  841| 
  842|     if target_session_attrs is None:
  843|         target_session_attrs = os.getenv(
  844|             "PGTARGETSESSIONATTRS", SessionAttribute.any
  845|         )
```

### only_reference example — litellm litellm-1.105.0/litellm/types/integrations/slack_alerting.py:56
message: os.getenv default type is builtins.int. Expected str or None.
```
   54|     daily_report_frequency: int = Field(
   55|         default=int(
   56|             os.getenv(
   57|                 "SLACK_DAILY_REPORT_FREQUENCY",
   58|                 int(SlackAlertingArgsEnum.daily_report_frequency.value),
```

### only_reference example — narwhals narwhals-2.27.1/src/narwhals/_utils.py:1502
message: os.getenv default type is builtins.int. Expected str or None.
```
 1500|         terminal_width = os.get_terminal_size().columns
 1501|     except OSError:
 1502|         terminal_width = int(os.getenv("COLUMNS", 80))  # noqa: PLW1508
 1503|     native_lines = native_repr.expandtabs().splitlines()
 1504|     max_native_width = max(len(line) for line in native_lines)
```

## ruff :: PLR1708
reference: pylint | only ruff: 0 | only reference: 59 | packages: 24
top messages: [only_reference] Do not raise StopIteration in generator, use return statement instead ×59

### only_reference example — annotated-types annotated_types-0.8.0/tests/test_main.py:101
message: Do not raise StopIteration in generator, use return statement instead
```
   99|     assert origin is Annotated
  100|     args = iter(get_args(tp))
  101|     next(args)
  102|     for arg in args:
  103|         if isinstance(arg, annotated_types.BaseMetadata):
```

### only_reference example — docutils docutils-0.23/docutils/utils/code_analyzer.py:85
message: Do not raise StopIteration in generator, use return statement instead
```
   83|         """
   84|         tokens = iter(tokens)
   85|         (lasttype, lastval) = next(tokens)
   86|         for ttype, value in tokens:
   87|             if ttype is lasttype:
```

### only_reference example — httpx2 httpx2-2.13.1/httpx2/_auth.py:73
message: Do not raise StopIteration in generator, use return statement instead
```
   71| 
   72|         flow = self.auth_flow(request)
   73|         request = next(flow)
   74| 
   75|         while True:
```

## ruff :: F822
reference: flake8 | only ruff: 16 | only reference: 40 | packages: 4
top messages: [only_rewrite] Undefined name `Any` in `__all__` ×15 || [only_reference] undefined name 'NIC_DUPLEX_FULL' in __all__ ×3 || [only_reference] undefined name 'MiniCPMV4_7PreTrainedModel' in __all__ ×3 || [only_reference] undefined name 'GlmPreTrainedModel' in __all__ ×2

### only_rewrite example — black black-26.10.1/tests/data/cases/comments2.py:12
message: Undefined name `Any` in `__all__`
```
   10| __all__ = [
   11|     # Super-special typing primitives.
   12|     'Any',
   13|     'Callable',
   14|     'ClassVar',
```

### only_rewrite example — ruff ruff-0.17.0/crates/ruff/resources/test/fixtures/cache_remove_old_files/source.py:4
message: Undefined name `b` in `__all__`
```
    2| a = 1
    3| 
    4| __all__ = list(["a", "b"])
```

### only_reference example — psutil psutil-7.2.2/psutil/_common.py:38
message: undefined name 'NIC_DUPLEX_FULL' in __all__
```
   36| 
   37| # fmt: off
   38| __all__ = [
   39|     # OS constants
   40|     'FREEBSD', 'BSD', 'LINUX', 'NETBSD', 'OPENBSD', 'MACOS', 'OSX', 'POSIX',
```

### only_reference example — transformers transformers-5.19.0/src/transformers/models/cosmos3_omni/modular_cosmos3_omni.py:109
message: undefined name 'Cosmos3OmniModel' in __all__
```
  107| 
  108| 
  109| __all__ = [
  110|     "Cosmos3OmniConfig",
  111|     "Cosmos3OmniForConditionalGeneration",
```

## ruff :: SIM112
reference: flake8 | only ruff: 55 | only reference: 0 | packages: 18
top messages: [only_rewrite] Use capitalized environment variable `PROGRAMFILES(X86)` instead of `ProgramFiles(x86)` ×7 || [only_rewrite] Use capitalized environment variable `PROMETHEUS_MULTIPROC_DIR` instead of `prometheus_mul ×5 || [only_rewrite] Use capitalized environment variable `VAR` instead of `var` ×4 || [only_rewrite] Use capitalized environment variable `WINDOWSSDKVERSION` instead of `WindowsSDKVersion` ×4

### only_rewrite example — defusedxml defusedxml-0.7.1/tests.py:61
message: Use capitalized environment variable `FTP_PROXY` instead of `ftp_proxy`
```
   59| os.environ["http_proxy"] = "http://127.0.9.1:9"
   60| os.environ["https_proxy"] = os.environ["http_proxy"]
   61| os.environ["ftp_proxy"] = os.environ["http_proxy"]
   62| 
   63| 
```

### only_rewrite example — gitpython gitpython-3.2.0/git/index/fun.py:84
message: Use capitalized environment variable `SYSTEMROOT` instead of `SystemRoot`
```
   82| def _is_in_windows_system_root(path: str) -> bool:
   83|     """Return whether ``path`` is inside the Windows installation directory."""
   84|     system_root = os.environ.get("SystemRoot")
   85|     if not system_root:
   86|         return False
```

### only_rewrite example — awscli awscli-1.46.1/awscli/testutils.py:381
message: Use capitalized environment variable `COMSPEC` instead of `ComSpec`
```
  379|             'AWS_SHARED_CREDENTIALS_FILE': '',
  380|         }
  381|         if os.environ.get('ComSpec'):
  382|             self.environ['ComSpec'] = os.environ['ComSpec']
  383|         self.environ_patch = mock.patch('os.environ', self.environ)
```

## ruff :: N813
reference: flake8 | only ruff: 12 | only reference: 40 | packages: 10
top messages: [only_rewrite] Camelcase `ElementTree` imported as lowercase `etree` ×11 || [only_reference] camelcase '_WebSocketConnect' imported as lowercase 'connect' ×7 || [only_reference] camelcase 'IPython.testing.tools' imported as lowercase 'tt' ×4 || [only_reference] camelcase 'fontTools.feaLib.ast' imported as lowercase 'ast' ×2

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/toc.py:31
message: Camelcase `ElementTree` imported as lowercase `etree`
```
   29| import unicodedata
   30| from copy import deepcopy
   31| import xml.etree.ElementTree as etree
   32| from typing import TYPE_CHECKING, Any, Iterator, MutableSet
   33| 
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/subresultants_qq_zz.py:250
message: Camelcase `Dummy` imported as lowercase `var`
```
  248| from sympy.core.numbers import nan
  249| from sympy.core.singleton import S
  250| from sympy.core.symbol import Dummy as var
  251| from sympy.functions.elementary.complexes import Abs, sign
  252| from sympy.functions.elementary.integers import floor
```

### only_reference example — ipython ipython-9.17.1/tests/test_tips.py:12
message: camelcase 'IPython.core.tips' imported as lowercase 'tips_mod'
```
   10| import pytest
   11| 
   12| import IPython.core.tips as tips_mod
   13| 
   14| all_tips = _tips["random"] + list(_tips["every_year"].values())
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/feaLib/parser.py:6
message: camelcase 'fontTools.feaLib.ast' imported as lowercase 'ast'
```
    4| from fontTools.misc.encodingTools import getEncoding
    5| from fontTools.misc.textTools import tobytes, tostr
    6| import fontTools.feaLib.ast as ast
    7| import logging
    8| import os
```

### only_reference example — openai openai-3.29.0/src/openai/resources/responses/responses.py:4522
message: camelcase '_WebSocketConnect' imported as lowercase 'connect'
```
 4520|     async def _connect_ws(self, extra_query: Query, extra_headers: Headers) -> AsyncWebSocketConnection:
 4521|         try:
 4522|             from ...lib._websocket import _WebSocketConnect as connect
 4523|         except ImportError as exc:
 4524|             raise OpenAIError("You need to install `openai[realtime]` to use this method") from exc
```

## ruff :: N817
reference: flake8 | only ruff: 0 | only reference: 51 | packages: 17
top messages: [only_reference] camelcase 'xml.etree.ElementTree' imported as acronym 'ET' ×43 || [only_reference] camelcase 'ElementTree' imported as acronym 'ET' ×7 || [only_reference] camelcase '_CustomTextWrap' imported as acronym 'CTW' ×1

### only_reference example — et-xmlfile et_xmlfile-2.0.0/et_xmlfile/incremental_tree.py:44
message: camelcase 'xml.etree.ElementTree' imported as acronym 'ET'
```
   42| import io
   43| 
   44| import xml.etree.ElementTree as ET
   45| 
   46| 
```

### only_reference example — docutils docutils-0.23/test/test_writers/test_odt.py:38
message: camelcase 'xml.etree.ElementTree' imported as acronym 'ET'
```
   36| import sys
   37| import unittest
   38| import xml.etree.ElementTree as ET
   39| import zipfile
   40| 
```

### only_reference example — azure-core azure_core-1.41.0/tests/test_rest_http_response.py:17
message: camelcase 'xml.etree.ElementTree' imported as acronym 'ET'
```
   15| from azure.core.rest._requests_basic import RestRequestsTransportResponse
   16| from azure.core.exceptions import HttpResponseError
   17| import xml.etree.ElementTree as ET
   18| from utils import readonly_checks
   19| 
```

## ruff :: PLW0108
reference: pylint | only ruff: 38 | only reference: 7 | packages: 12
top messages: [only_rewrite] Lambda may be unnecessary; consider inlining inner function ×38 || [only_reference] Lambda may not be necessary ×7

### only_rewrite example — greenlet greenlet-3.5.6/src/greenlet/tests/test_leaks.py:58
message: Lambda may be unnecessary; consider inlining inner function
```
   56|         # pylint:disable=unnecessary-lambda
   57|         g = greenlet.greenlet(
   58|             lambda *args: greenlet.getcurrent().parent.switch(*args))
   59|         for _ in range(100):
   60|             g.switch(*args)
```

### only_rewrite example — mypy mypy-2.4.0/mypyc/codegen/emitclass.py:73
message: Lambda may be unnecessary; consider inlining inner function
```
   71| 
   72| SLOT_DEFS: SlotTable = {
   73|     "__init__": ("tp_init", lambda c, t, e: generate_init_for_class(c, t, e)),
   74|     "__call__": ("tp_call", lambda c, t, e: generate_call_wrapper(c, t, e)),
   75|     "__str__": ("tp_str", native_slot),
```

### only_rewrite example — tqdm tqdm-4.70.1/tests/tests_perf.py:52
message: Lambda may be unnecessary; consider inlining inner function
```
   50|         return process_time() - start
   51| 
   52|     yield lambda: elapser()
   53|     spent = elapser()
   54| 
```

### only_reference example — psutil psutil-7.2.2/psutil/__init__.py:1565
message: Lambda may not be necessary
```
 1563| 
 1564| 
 1565| process_iter.cache_clear = lambda: _pmap.clear()  # noqa: PLW0108
 1566| process_iter.cache_clear.__doc__ = "Clear process_iter() internal cache."
 1567| 
```

### only_reference example — pytest pytest-9.1.1/src/_pytest/timing.py:36
message: Lambda may not be necessary
```
   34|     # Note: using a `lambda` to correctly get the mocked time via `MockTiming`.
   35|     # pylint: disable-next=lambda-assignment
   36|     time: float = dataclasses.field(default_factory=lambda: time(), init=False)  # noqa: PLW0108
   37| 
   38|     # Performance counter tick of the instant, used to measure precise elapsed time.
```

### only_reference example — pandas pandas-3.0.6/pandas/tests/scalar/timestamp/methods/test_replace.py:140
message: Lambda may not be necessary
```
  138|         "tz, normalize",
  139|         [
  140|             ("pytz/US/Eastern", lambda x: x.tzinfo.normalize(x)),
  141|             (gettz("US/Eastern"), lambda x: x),
  142|         ],
```

## ruff :: N804
reference: flake8 | only ruff: 7 | only reference: 31 | packages: 22
top messages: [only_reference] first argument of a classmethod should be named 'cls' ×31 || [only_rewrite] First argument of a class method should be named `cls` ×7

### only_rewrite example — executing executing-2.3.0/tests/samples/tracer2.py:121
message: First argument of a class method should be named `cls`
```
  119|             return super(TracerMeta, cls).__call__(*args, **kwargs)
  120| 
  121|     def __enter__(self):
  122|         return self.default.__enter__(context=1)
  123| 
```

### only_rewrite example — sympy sympy-1.14.0/sympy/core/function.py:927
message: First argument of a class method should be named `cls`
```
  925|     _kwargs: dict[str, bool | None] = {}
  926| 
  927|     def __hash__(self):
  928|         return hash((self.class_key(), frozenset(self._kwargs.items())))
  929| 
```

### only_reference example — asyncpg asyncpg-0.32.0/asyncpg/pool.py:49
message: first argument of a classmethod should be named 'cls'
```
   47| 
   48|     def __new__(
   49|         mcls,
   50|         name: str,
   51|         bases: tuple[Type[Any], ...],
```

### only_reference example — dill dill-0.4.1/dill/tests/test_classdef.py:256
message: first argument of a classmethod should be named 'cls'
```
  254| def test_metaclass():
  255|     class metaclass_with_new(type):
  256|         def __new__(mcls, name, bases, ns, **kwds):
  257|             cls = super().__new__(mcls, name, bases, ns, **kwds)
  258|             assert mcls is not None
```

### only_reference example — google-api-core google_api_core-2.42.0/google/api_core/exceptions.py:100
message: first argument of a classmethod should be named 'cls'
```
   98|     """Metaclass for registering GoogleAPICallError subclasses."""
   99| 
  100|     def __new__(mcs, name, bases, class_dict):
  101|         cls = type.__new__(mcs, name, bases, class_dict)
  102|         if cls.code is not None:
```

## ruff :: SIM905
reference: flake8 | only ruff: 35 | only reference: 0 | packages: 13
top messages: [only_rewrite] Consider using a list literal instead of `str.split` ×35

### only_rewrite example — coverage coverage-7.16.2/tests/test_execfile.py:79
message: Consider using a list literal instead of `str.split`
```
   77|     def test_universal_newlines(self) -> None:
   78|         # Make sure we can read any sort of line ending.
   79|         pylines = """# try newlines|print('Hello, world!')|""".split("|")
   80|         for nl in ["\n", "\r\n", "\r"]:
   81|             with open("nl.py", "wb") as fpy:
```

### only_rewrite example — httplib2 httplib2-0.32.0/tests/test_http.py:388
message: Consider using a list literal instead of `str.split`
```
  386|     # All methods can be used
  387|     http = httplib2.Http()
  388|     cases = "DELETE GET HEAD POST PUT EVEN_NEW_ONES".split(" ")
  389|     with tests.server_route(routes, request_count=len(cases) * 2) as uri:
  390|         for method in cases:
```

### only_rewrite example — grpcio grpcio-1.84.0/third_party/boringssl-with-bazel/util/generate_build_files.py:36
message: Consider using a list literal instead of `str.split`
```
   34| 
   35| 
   36| LICENSE_TEMPLATE = """Copyright 2015 The BoringSSL Authors
   37| 
   38| Licensed under the Apache License, Version 2.0 (the "License");
```

## ruff :: N816
reference: flake8 | only ruff: 34 | only reference: 1 | packages: 5
top messages: [only_rewrite] Variable `certCnt` in global scope should not be mixedCase ×3 || [only_rewrite] Variable `illegalCharacters` in global scope should not be mixedCase ×2 || [only_rewrite] Variable `dup_LC` in global scope should not be mixedCase ×2 || [only_rewrite] Variable `dup_TC` in global scope should not be mixedCase ×2

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/misc/filenames.py:21
message: Variable `illegalCharacters` in global scope should not be mixedCase
```
   19| 
   20| illegalCharacters = r"\" * + / : < > ? [ \ ] | \0".split(" ")
   21| illegalCharacters += [chr(i) for i in range(1, 32)]
   22| illegalCharacters += [chr(0x7F)]
   23| reservedFileNames = "CON PRN AUX CLOCK$ NUL A:-Z: COM1".lower().split(" ")
```

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/smarty.py:101
message: Variable `punctClass` in global scope should not be mixedCase
```
   99| 
  100| # Constants for quote education.
  101| punctClass = r"""[!"#\$\%'()*+,-.\/:;<=>?\@\[\\\]\^_`{|}~]"""
  102| endOfWordClass = r"[\s.,;:!?)]"
  103| closeClass = r"[^\ \t\r\n\[\{\(\-\u0002\u0003]"
```

### only_rewrite example — pyasn1-modules pyasn1_modules-0.4.2/tools/x509dump-rfc5280.py:48
message: Variable `certCnt` in global scope should not be mixedCase
```
   46|     assert encoder.encode(cert) == substrate, 'cert recode fails'
   47| 
   48|     certCnt += 1
   49| 
   50| print('*** %s PEM cert(s) de/serialized' % certCnt)
```

### only_reference example — pyparsing pyparsing-3.3.3/pyparsing/__init__.py:141
message: variable '__versionTime__' in global scope should not be mixedCase
```
  139| __version_time__ = "25 Aug 2026 04:00 UTC"
  140| __version__ = __version_info__.__version__
  141| __versionTime__ = __version_time__
  142| __author__ = "Paul McGuire <ptmcg.gm+pyparsing@gmail.com>"
  143| 
```

## ruff :: PLW0642
reference: pylint | only ruff: 0 | only reference: 34 | packages: 7
top messages: [only_reference] Invalid assignment to A in method ×9 || [only_reference] Invalid assignment to args in method ×8 || [only_reference] Invalid assignment to K0 in method ×6 || [only_reference] Invalid assignment to f in method ×4

### only_reference example — jinja2 jinja2-3.1.6/src/jinja2/runtime.py:290
message: Invalid assignment to __self in method
```
  288|             # loops and blocks without mutating the context itself
  289|             if kwargs.get("_loop_vars"):
  290|                 __self = __self.derived(kwargs["_loop_vars"])
  291|             if kwargs.get("_block_vars"):
  292|                 __self = __self.derived(kwargs["_block_vars"])
```

### only_reference example — mako mako-1.4.3/mako/parsetree.py:238
message: Invalid assignment to cls in method
```
  236| 
  237|         try:
  238|             cls = _TagMeta._classmap[keyword]
  239|         except KeyError:
  240|             raise exceptions.CompileException(
```

### only_reference example — proto-plus proto_plus-1.29.0/proto/message.py:203
message: Invalid assignment to mcls in method
```
  201|         # MyMessage.field in m
  202|         if opt_attrs:
  203|             mcls = type("AttrsMeta", (mcls,), opt_attrs)
  204| 
  205|         # Determine the filename.
```

## ruff :: SIM116
reference: flake8 | only ruff: 0 | only reference: 30 | packages: 15
top messages: [only_reference] Use a dictionary lookup instead of 3+ if/elif-statements: return {1: [('theme', str(color) ×4 || [only_reference] Use a dictionary lookup instead of 3+ if/elif-statements: return {'channel': {'p': pubsub, ×2 || [only_reference] Use a dictionary lookup instead of 3+ if/elif-statements: return {1: large_data[:size], 2: ×1 || [only_reference] Use a dictionary lookup instead of 3+ if/elif-statements: return {1: large_text[:size], 2: ×1

### only_reference example — aiohttp aiohttp-3.14.5/tests/test_payload.py:399
message: Use a dictionary lookup instead of 3+ if/elif-statements: return {1: large_data[:size], 2: large_data[DEFAULT_CHUNK_SIZE:DEFAULT_CHUNK_SIZE + size], 3: large_da
```
  397|         # Return data based on how many times read was called
  398|         call_count = len(read_sizes)
  399|         if call_count == 1:
  400|             return large_data[:size]
  401|         elif call_count == 2:
```

### only_reference example — lxml lxml-6.1.3/src/lxml/html/__init__.py:717
message: Use a dictionary lookup instead of 3+ if/elif-statements: return {'comment': HtmlComment, 'PI': HtmlProcessingInstruction, 'entity': HtmlEntity}.get(node_type)
```
  715|         if node_type == 'element':
  716|             return self._element_classes.get(name.lower(), HtmlElement)
  717|         elif node_type == 'comment':
  718|             return HtmlComment
  719|         elif node_type == 'PI':
```

### only_reference example — mpmath mpmath-1.4.1/mpmath/libmp/libmpc.py:249
message: Use a dictionary lookup instead of 3+ if/elif-statements: return {0: (v, fzero), 1: (fzero, v), 2: (mpf_neg(v), fzero)}.get(n, (fzero, mpf_neg(v)))
```
  247|         v = mpf_pow_int(b, n, prec, rnd)
  248|         n %= 4
  249|         if n == 0:
  250|             return v, fzero
  251|         elif n == 1:
```

## ruff :: PLW0177
reference: pylint | only ruff: 28 | only reference: 2 | packages: 4
top messages: [only_rewrite] Comparing against a NaN value; use `np.isnan` instead ×26 || [only_rewrite] Comparing against a NaN value; use `math.isnan` instead ×2 || [only_reference] Comparison 'a != approx(x)' should be 'not math.isnan(approx(x))' ×1 || [only_reference] Comparison 'a != approx(np.array(x))' should be 'not math.isnan(approx(np.array(x)))' ×1

### only_rewrite example — pandas pandas-3.0.6/pandas/tests/indexes/numeric/test_indexing.py:547
message: Comparing against a NaN value; use `np.isnan` instead
```
  545|     def test_contains_float64_nans(self):
  546|         index = Index([1.0, 2.0, np.nan], dtype=np.float64)
  547|         assert np.nan in index
  548| 
  549|     def test_contains_float64_not_nans(self):
```

### only_rewrite example — scikit-learn scikit_learn-1.9.1/sklearn/utils/tests/test_param_validation.py:138
message: Comparing against a NaN value; use `np.isnan` instead
```
  136| def test_nan_not_in_interval(interval):
  137|     """Check that np.nan is not in any interval."""
  138|     assert np.nan not in interval
  139| 
  140| 
```

### only_rewrite example — scipy scipy-1.18.1/scipy/sparse/tests/test_base.py:490
message: Comparing against a NaN value; use `np.isnan` instead
```
  488| 
  489|                 with np.errstate(invalid='ignore'):
  490|                     assert_array_equal_dtype((datsp < np.nan).toarray(),
  491|                                              dat < np.nan)
  492| 
```

### only_reference example — pytest pytest-9.1.1/testing/python/approx.py:595
message: Comparison 'a != approx(x)' should be 'not math.isnan(approx(x))'
```
  593|         for op, a, x in examples:
  594|             # Nothing is equal to NaN by default.
  595|             assert a != approx(x)
  596| 
  597|             # If ``nan_ok=True``, then NaN is equal to NaN.
```

## ruff :: PLW0133
reference: pylint | only ruff: 0 | only reference: 29 | packages: 12
top messages: [only_reference] Exception statement has no effect ×29

### only_reference example — attrs attrs-26.1.0/tests/test_functional.py:625
message: Exception statement has no effect
```
  623|             x = attr.ib()
  624| 
  625|         FooError(1)
  626| 
  627|     def test_eq_only(self, slots, frozen):
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/s3/_read_parquet.py:507
message: Exception statement has no effect
```
  505| 
  506|     if bulk_read and validate_schema:
  507|         exceptions.InvalidArgumentCombination("Cannot validate schema when bulk reading data files.")
  508| 
  509|     s3_client = _utils.client(service_name="s3", session=boto3_session)
```

### only_reference example — exceptiongroup exceptiongroup-1.3.1/tests/test_exceptions.py:112
message: Exception statement has no effect
```
  110|         msg = "Cannot nest BaseExceptions in 'MyEG'"
  111|         with self.assertRaisesRegex(TypeError, msg):
  112|             MyEG("eg", [ValueError(12), KeyboardInterrupt(42)])
  113| 
  114|     @pytest.mark.skipif(
```

## ruff :: SIM222
reference: flake8 | only ruff: 16 | only reference: 8 | packages: 12
top messages: [only_rewrite] Use `True` instead of `True or ...` ×11 || [only_reference] Use 'True' instead of '... or True' ×8 || [only_rewrite] Use `7` instead of `7 or ...` ×2 || [only_rewrite] Use `1` instead of `1 or ...` ×2

### only_rewrite example — executing .0/tests/small_samples/d6d7ea7eb0c3608d8e642a9f78cce7ac05f00f9615d424cc902606412fff6809.py:16
message: Use `True` instead of `True or ...`
```
   14| # 
   15| 
   16| if True or type:
   17|     obj['Filter'] = []
```

### only_rewrite example — parso parso-0.8.7/test/normalizer_issue_files/E50.py:4
message: Use `'1234567890123456789012345678901234567890123456789012345678901234567890'` instead of `'12345678901234567890123456789012345678901234567890123456789012345678
```
    2| a = '12345678901234567890123456789012345678901234567890123456789012345678901234567890'
    3| #: E501:80
    4| a = '1234567890123456789012345678901234567890123456789012345678901234567890' or \
    5|     6
    6| #: E501+1:80
```

### only_rewrite example — pymupdf pymupdf-1.28.2/src/__init__.py:10153
message: Use `True` instead of `True or ...`
```
10151| 
10152|     def _get_textpage(self, clip=None, flags=0, matrix=None):
10153|         if 1 or g_use_extra:
10154|             ll_tpage = extra.page_get_textpage(self.this, clip, flags, matrix)
10155|             tpage = mupdf.FzStextPage(ll_tpage)
```

### only_reference example — opentelemetry-exporter-otlp-proto-http rter_otlp_proto_http-1.45.1/src/opentelemetry/exporter/otlp/proto/http/_common/__init__.py:192
message: Use 'True' instead of '... or True'
```
  190| ) -> BaseHTTPTransport:
  191|     verify: bool | str = (
  192|         certificate_file
  193|         or os.environ.get(certificate_env_var)
  194|         or os.environ.get(OTEL_EXPORTER_OTLP_CERTIFICATE)
```

### only_reference example — sentry-sdk sentry_sdk-2.72.0/tests/test_transport.py:594
message: Use 'True' instead of '... or True'
```
  592|     )
  593|     # get rid of threading making things hard to track
  594|     monkeypatch.setattr(client.transport._worker, "submit", lambda x: x() or True)
  595| 
  596|     client.capture_event({"type": "transaction"})
```

### only_reference example — numpy numpy-2.5.4/numpy/_core/tests/test_ufunc.py:1543
message: Use 'True' instead of '... or True'
```
 1541|                         np.array([x or None for x in a], dtype=object))
 1542|         assert_equal(np.logical_or(a, True),
 1543|                         np.array([x or True for x in a], dtype=object))
 1544|         assert_equal(np.logical_or(a, 12),
 1545|                         np.array([x or 12 for x in a], dtype=object))
```
