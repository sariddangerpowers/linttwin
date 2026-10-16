
## ruff :: PLR2004
reference: pylint | only ruff: 2328 | only reference: 157523 | packages: 288
top messages: [only_reference] Consider using a named constant or an enum instead of ''python''. ×2881 || [only_reference] Consider using a named constant or an enum instead of ''win32''. ×1534 || [only_reference] Consider using a named constant or an enum instead of ''foo''. ×804 || [only_reference] Consider using a named constant or an enum instead of ''name_value''. ×736

### only_rewrite example — async-timeout async_timeout-5.0.1/tests/test_timeout.py:73
message: Magic value used in comparison, consider replacing `0.09` with a constant variable
```
   71|     assert resp == "done"
   72|     dt = loop.time() - t0
   73|     assert 0.09 < dt < 0.3, dt
   74| 
   75| 
```

### only_rewrite example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:5017
message: Magic value used in comparison, consider replacing `1950` with a constant variable
```
 5015|             value = value.astimezone(utc_with_dst)
 5016| 
 5017|             if not 1950 <= value.year <= 2049:
 5018|                 raise ValueError('Year of the UTCTime is not in range [1950, 2049], use GeneralizedTime instead')
 5019| 
```

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/api.py:434
message: Magic value used in comparison, consider replacing `2` with a constant variable
```
  432|                         chunk,
  433|                         threshold,
  434|                         explain and 1 <= len(cp_isolation) <= 2,
  435|                     )
  436|                 )
```

### only_reference example — annotated-doc annotated_doc-0.0.5/tests/test_main.py:9
message: Consider using a named constant or an enum instead of ''This is a test documentation.''.
```
    7| def test_doc_basic() -> None:
    8|     doc = Doc("This is a test documentation.")
    9|     assert doc.documentation == "This is a test documentation."
   10|     assert repr(doc) == "Doc('This is a test documentation.')"
   11|     assert hash(doc) == hash("This is a test documentation.")
```

### only_reference example — annotated-types annotated_types-0.8.0/annotated_types/__init__.py:338
message: Consider using a named constant or an enum instead of ''<lambda>''.
```
  336| 
  337|     def __repr__(self) -> str:
  338|         if getattr(self.func, "__name__", "<lambda>") == "<lambda>":
  339|             return f"{self.__class__.__name__}({self.func!r})"
  340|         if isinstance(self.func, (types.MethodType, types.BuiltinMethodType)) and (
```

### only_reference example — async-timeout async_timeout-5.0.1/tests/test_timeout.py:58
message: Consider using a named constant or an enum instead of ''done''.
```
   56|     async with timeout(0.5):
   57|         resp = await long_running_task()
   58|     assert resp == "done"
   59| 
   60| 
```

## ruff :: PLR2044
reference: pylint | only ruff: 1 | only reference: 45113 | packages: 229
top messages: [only_reference] Line with empty comment ×45113 || [only_rewrite] Line with empty comment ×1

### only_rewrite example — pymupdf pymupdf-1.28.2/src/__init__.py:16005
message: Line with empty comment
```
16003| 
16004|         self.last_point = None  # clean up ...
16005|         self.rect = None  #
16006|         self.draw_cont = ""  # for potential ...
16007|         self.text_cont = ""  # ...
```

### only_reference example — aiosignal aiosignal-1.4.0/docs/conf.py:2
message: Line with empty comment
```
    1| #!/usr/bin/env python3
    2| #
    3| # aiosignal documentation build configuration file, created by
    4| # sphinx-quickstart on Wed Mar  5 12:35:35 2014.
```

### only_reference example — async-timeout async_timeout-5.0.1/async_timeout/__init__.py:139
message: Line with empty comment
```
  137|         # Internal class, please don't instantiate it directly
  138|         # Use timeout() and timeout_at() public factories instead.
  139|         #
  140|         # Implementation note: `async with timeout()` is preferred
  141|         # over `with timeout()`.
```

### only_reference example — bcrypt bcrypt-5.0.0/src/bcrypt/__init__.py:4
message: Line with empty comment
```
    2| # you may not use this file except in compliance with the License.
    3| # You may obtain a copy of the License at
    4| #
    5| # http://www.apache.org/licenses/LICENSE-2.0
    6| #
```

## ruff :: E501
reference: flake8 | only ruff: 4646 | only reference: 30941 | packages: 219
top messages: [only_rewrite] Line too long (113 > 88) ×2273 || [only_reference] line too long (91 > 88 characters) ×1983 || [only_reference] line too long (90 > 88 characters) ×1771 || [only_reference] line too long (89 > 88 characters) ×1762

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/tests/test_large_payload.py:45
message: Line too long (110 > 88)
```
   43| def test_misleading_large_sequence():
   44|     content = (
   45|         ("hello simple ascii " * TOO_BIG_SEQUENCE) + ("我没有埋怨，磋砣的只是一些时间。 磋砣的只是一些时间。")
   46|     ).encode("utf_8")
   47| 
```

### only_rewrite example — awswrangler awswrangler-3.17.1/awswrangler/athena/_write_iceberg.py:422
message: Line too long (97 > 88)
```
  420|         order_by_clause = _build_order_by_clause(partition_cols)
  421|         sql_statement = f"""
  422|         INSERT INTO "{esc_database}"."{esc_table}" ({", ".join([f'"{x}"' for x in esc_columns])})
  423|         SELECT {", ".join([f'"{x}"' for x in esc_columns])}
  424|           FROM "{esc_database}"."{esc_source_table}"
```

### only_rewrite example — chardet chardet-7.6.0/tests/test_orchestrator.py:226
message: Line too long (93 > 88)
```
  224|     """run_pipeline should never return confidence > 1.0."""
  225|     # Use a CJK text that triggers the byte-coverage boost
  226|     data = "これは日本語のテストです。日本語の文章を検出できるかどうかを確認します。".encode(
  227|         "euc-jis-2004"
  228|     )
```

### only_reference example — bcrypt bcrypt-5.0.0/tests/test_bcrypt.py:288
message: line too long (94 > 88 characters)
```
  286| def test_checkpw_str_password():
  287|     with pytest.raises(TypeError):
  288|         bcrypt.checkpw("password", b"$2b$04$cVWp4XaNU8a4v1uMRum2SO")  # type: ignore[arg-type]
  289| 
  290| 
```

### only_reference example — anthropic anthropic-1.13.0/src/anthropic/types/refusal_stop_details.py:28
message: line too long (99 > 88 characters)
```
   26|       reasoning in the response text. To get reasoning in a structured form instead,
   27|       use
   28|       [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).
   29|     - `general_harms` - The request could be related to an area that was determined
   30|       as harmful. Benign work might sometimes trigger this category.
```

### only_reference example — aioitertools aioitertools-0.13.0/aioitertools/asyncio.py:64
message: line too long (139 > 88 characters)
```
   62|         # these values to existing Set[Awaitable] or even Set[Union[Awaitable, Future]],
   63|         # we need to first cast the results to something that we can actually use
   64|         # asyncio.Future: https://github.com/python/typeshed/blob/72ff7b94e534c610ddf8939bacbc55343e9465d2/stdlib/3/asyncio/futures.pyi#L30
   65|         # asyncio.wait(): https://github.com/python/typeshed/blob/72ff7b94e534c610ddf8939bacbc55343e9465d2/stdlib/3/asyncio/tasks.pyi#L89
   66|         done, pending = cast(
```

## ruff :: E101
reference: flake8 | only ruff: 0 | only reference: 10058 | packages: 13
top messages: [only_reference] indentation contains mixed spaces and tabs ×10058

### only_reference example — joblib joblib-1.6.0/doc/conf.py:162
message: indentation contains mixed spaces and tabs
```
  160| 
  161| versions_content = f"""[
  162| 	{{
  163| 		"name": "{release} (dev)",
  164| 		"version": "{release}",
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/tables/_t_r_a_k.py:18
message: indentation contains mixed spaces and tabs
```
   16| 
   17| TRAK_HEADER_FORMAT = """
   18| 	> # big endian
   19| 	version:     16.16F
   20| 	format:      H
```

### only_reference example — ipython ipython-9.17.1/IPython/core/display.py:650
message: indentation contains mixed spaces and tabs
```
  648| 
  649| _css_t = """var link = document.createElement("link");
  650| 	link.rel = "stylesheet";
  651| 	link.type = "text/css";
  652| 	link.href = "%s";
```

## ruff :: F401
reference: flake8 | only ruff: 119 | only reference: 9328 | packages: 84
top messages: [only_reference] '._utils.flatten' imported but unused ×57 || [only_reference] '._char_codes._BoolCodes' imported but unused ×41 || [only_reference] '.resources.beta' imported but unused ×32 || [only_reference] '._module_client.beta' imported but unused ×26

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:5
message: `astroid.node_classes.Name` imported but unused
```
    3| 
    4| __revision__ = '$Id: module.py,v 1.2 2005-11-02 11:56:54 syt Exp $'
    5| from astroid.node_classes import Name as NameNode
    6| from astroid import modutils
    7| from astroid.utils import *
```

### only_rewrite example — executing executing-2.3.0/tests/samples/bird.py:7
message: `typing.List` imported but unused
```
    5| standard_library.install_aliases()
    6| from future.utils import iteritems
    7| from typing import List, Dict, Any, Optional, NamedTuple, Tuple, Iterator, Iterable, Union, cast
    8| from types import FrameType, TracebackType, CodeType, FunctionType, ModuleType
    9| import typing
```

### only_rewrite example — tornado tornado-6.5.10/tornado/test/http1connection_test.py:2
message: `typing` imported but unused
```
    1| import socket
    2| import typing  # noqa(F401)
    3| 
    4| from tornado.http1connection import HTTP1Connection
```

### only_reference example — annotated-doc annotated_doc-0.0.5/src/annotated_doc/__init__.py:1
message: '.main.Doc' imported but unused
```
    1| from .main import Doc as Doc
    2| 
    3| __version__ = "0.0.5"
```

### only_reference example — anthropic anthropic-1.13.0/src/anthropic/types/beta/organization/analytics/__init__.py:3
message: '.user_list_params.UserListParams' imported but unused
```
    1| from __future__ import annotations
    2| 
    3| from .user_list_params import UserListParams as UserListParams
    4| from .skill_list_params import SkillListParams as SkillListParams
    5| from .plugin_list_params import PluginListParams as PluginListParams
```

### only_reference example — attrs attrs-26.1.0/src/attrs/setters.py:3
message: 'attr.setters.*' imported but unused
```
    1| # SPDX-License-Identifier: MIT
    2| 
    3| from attr.setters import *  # noqa: F403
```

## ruff :: PLC0414
reference: pylint | only ruff: 26 | only reference: 7002 | packages: 34
top messages: [only_reference] Import alias does not rename original package ×7002 || [only_rewrite] Import alias does not rename original package ×26

### only_rewrite example — anthropic anthropic-1.13.0/src/anthropic/types/message.py:10
message: Import alias does not rename original package
```
    8| from .diagnostics import Diagnostics
    9| from .stop_reason import StopReason
   10| from .content_block import ContentBlock, ContentBlock as ContentBlock
   11| from .message_param import MessageParam
   12| from .refusal_stop_details import RefusalStopDetails
```

### only_rewrite example — coverage coverage-7.16.2/tests/hypo.py:19
message: Import alias does not rename original package
```
   17| if testenv.USE_HYPOTHESIS:
   18|     from hypothesis import (
   19|         example as example,
   20|     )
   21|     from hypothesis import (
```

### only_rewrite example — gitpython gitpython-3.2.0/git/types.py:12
message: Import alias does not rename original package
```
   10|     NoReturn,
   11|     Optional,
   12|     Sequence as Sequence,
   13|     Tuple,
   14|     TYPE_CHECKING,
```

### only_reference example — annotated-doc annotated_doc-0.0.5/src/annotated_doc/__init__.py:1
message: Import alias does not rename original package
```
    1| from .main import Doc as Doc
    2| 
    3| __version__ = "0.0.5"
```

### only_reference example — anthropic anthropic-1.13.0/src/anthropic/types/beta/organization/plugins/__init__.py:3
message: Import alias does not rename original package
```
    1| from __future__ import annotations
    2| 
    3| from .beta_plugin_share import BetaPluginShare as BetaPluginShare
    4| from .share_list_params import ShareListParams as ShareListParams
    5| from .beta_plugin_version import BetaPluginVersion as BetaPluginVersion
```

### only_reference example — aiobotocore aiobotocore-3.9.2/aiobotocore/retries/bucket.py:6
message: Import alias does not rename original package
```
    4| 
    5| from botocore.exceptions import CapacityNotAvailableError
    6| from botocore.retries.bucket import Clock as Clock  # reexport # noqa
    7| 
    8| 
```

## ruff :: N806
reference: flake8 | only ruff: 5899 | only reference: 634 | packages: 49
top messages: [only_rewrite] Variable `A` in function should be lowercase ×721 || [only_rewrite] Variable `R` in function should be lowercase ×604 || [only_rewrite] Variable `F` in function should be lowercase ×533 || [only_rewrite] Variable `B` in function should be lowercase ×243

### only_rewrite example — asyncpg asyncpg-0.32.0/tests/test_pool.py:773
message: Variable `N` in function should be lowercase
```
  771|                 await worker(pool)
  772| 
  773|             N += 1
  774| 
  775|         async with self.create_pool(
```

### only_rewrite example — dill dill-0.4.1/version.py:36
message: Variable `README` in function should be lowercase
```
   34|                 continue
   35|             elif skip and line.startswith('    http'):
   36|                 README += '\n' + line
   37|             elif line.startswith('* with'): #XXX: don't indent
   38|                 README += line
```

### only_rewrite example — cffi cffi-2.1.1/testing/cffi1/test_verify1.py:1887
message: Variable `zeroL` in function should be lowercase
```
 1885|     pytest.raises(TypeError, lib.seeme2, 0)
 1886|     zeroL  = 99999999999999999999
 1887|     zeroL -= 99999999999999999999
 1888|     pytest.raises(TypeError, lib.seeme2, zeroL)
 1889| 
```

### only_reference example — attrs attrs-26.1.0/tests/test_funcs.py:552
message: variable 'T' in function should be lowercase
```
  550|         Works with generic classes.
  551|         """
  552|         T = TypeVar("T")
  553| 
  554|         @attr.define
```

### only_reference example — google-api-python-client google_api_python_client-2.201.0/googleapiclient/discovery.py:1649
message: variable 'tokenName' in function should be lowercase
```
 1647|     """
 1648|     return next(
 1649|         (tokenName for tokenName in _PAGE_TOKEN_NAMES if tokenName in fields), None
 1650|     )
 1651| 
```

### only_reference example — cffi cffi-2.1.1/src/cffi/backend_ctypes.py:743
message: variable 'BField' in function should be lowercase
```
  741|                                       "compile and install the _cffi_backend module.")
  742|         struct_or_union = CTypesStructOrUnion._ctype
  743|         fnames = [fname for (fname, BField, bitsize) in fields]
  744|         btypes = [BField for (fname, BField, bitsize) in fields]
  745|         bitfields = [bitsize for (fname, BField, bitsize) in fields]
```

## ruff :: W191
reference: flake8 | only ruff: 0 | only reference: 4645 | packages: 10
top messages: [only_reference] indentation contains tabs ×4645

### only_reference example — joblib joblib-1.6.0/doc/conf.py:162
message: indentation contains tabs
```
  160| 
  161| versions_content = f"""[
  162| 	{{
  163| 		"name": "{release} (dev)",
  164| 		"version": "{release}",
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/tables/_t_r_a_k.py:18
message: indentation contains tabs
```
   16| 
   17| TRAK_HEADER_FORMAT = """
   18| 	> # big endian
   19| 	version:     16.16F
   20| 	format:      H
```

### only_reference example — ipython ipython-9.17.1/IPython/core/display.py:650
message: indentation contains tabs
```
  648| 
  649| _css_t = """var link = document.createElement("link");
  650| 	link.rel = "stylesheet";
  651| 	link.type = "text/css";
  652| 	link.href = "%s";
```

## ruff :: B018
reference: flake8 | only ruff: 2212 | only reference: 1203 | packages: 130
top messages: [only_rewrite] Found useless expression. Either assign it to a variable or remove it. ×2057 || [only_reference] Found useless BinOp expression. Consider either assigning it to a variable or removing it. ×588 || [only_reference] Found useless Call expression. Consider either assigning it to a variable or removing it. ×510 || [only_rewrite] Found useless attribute access. Either assign it to a variable or remove it. ×155

### only_rewrite example — asgiref asgiref-3.12.1/tests/test_local.py:22
message: Found useless expression. Either assign it to a variable or remove it.
```
   20|     # Unassigned should be an error
   21|     with pytest.raises(AttributeError):
   22|         test_local.foo
   23|     # Assign and check it persists
   24|     test_local.foo = 1
```

### only_rewrite example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:2084
message: Found useless expression. Either assign it to a variable or remove it.
```
 2082| 
 2083|         # call native to set _unused_bits
 2084|         self.native
 2085| 
 2086|         return self._unused_bits
```

### only_rewrite example — cloudpickle cloudpickle-3.1.2/cloudpickle/cloudpickle.py:941
message: Found useless expression. Either assign it to a variable or remove it.
```
  939|     """Cell (containing values of a function's free variables) reducer."""
  940|     try:
  941|         obj.cell_contents
  942|     except ValueError:  # cell is empty
  943|         return _make_empty_cell, ()
```

### only_reference example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/api.py:344
message: Found useless Call expression. Consider either assigning it to a variable or removing it.
```
  342|         try:
  343|             if is_too_large_sequence and not is_multi_byte_decoder:
  344|                 str(
  345|                     (
  346|                         sequences[: int(50e4)]
```

### only_reference example — attrs attrs-26.1.0/typing-examples/baseline.py:79
message: Found useless Call expression. Consider either assigning it to a variable or removing it.
```
   77|     e.x
   78|     e.args
   79|     str(e)
   80| 
   81| 
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/tests/test_tree.py:44
message: Found useless Call expression. Consider either assigning it to a variable or removing it.
```
   42|     def test_unicode_attribute_find(self):
   43|         soup = self.soup('<h1 id="Räksmörgås">here it is</h1>')
   44|         str(soup)
   45|         assert "here it is" == soup.find(id="Räksmörgås").text
   46| 
```

## ruff :: PLR5501
reference: pylint | only ruff: 1677 | only reference: 1659 | packages: 136
top messages: [only_rewrite] Use `elif` instead of `else` then `if`, to reduce indentation ×1677 || [only_reference] Consider using "elif" instead of "else" then "if" to remove one indentation level ×1659

### only_rewrite example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:611
message: Use `elif` instead of `else` then `if`, to reduce indentation
```
  609|         elif hasattr(self, 'chosen'):
  610|             self.chosen.debug(nest_level + 2)
  611|         else:
  612|             if _PY2 and isinstance(self.native, byte_cls):
  613|                 print('%s    Native: b%s' % (prefix, repr(self.native)))
```

### only_rewrite example — boto3 boto3-1.43.113/boto3/dynamodb/transform.py:205
message: Use `elif` instead of `else` then `if`, to reduce indentation
```
  203|         if expr_attr_names_input in params:
  204|             params[expr_attr_names_input].update(generated_names)
  205|         else:
  206|             if generated_names:
  207|                 params[expr_attr_names_input] = generated_names
```

### only_rewrite example — cachetools cachetools-7.2.1/src/cachetools/_cachedmethod.py:405
message: Use `elif` instead of `else` then `if`, to reduce indentation
```
  403|         else:
  404|             wrapper = _unlocked_info(method, cache, key, info)
  405|     else:
  406|         if cond is not None and lock is not None:
  407|             wrapper = _condition(method, cache, key, lock, cond)
```

### only_reference example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:612
message: Consider using "elif" instead of "else" then "if" to remove one indentation level
```
  610|             self.chosen.debug(nest_level + 2)
  611|         else:
  612|             if _PY2 and isinstance(self.native, byte_cls):
  613|                 print('%s    Native: b%s' % (prefix, repr(self.native)))
  614|             else:
```

### only_reference example — boto3 boto3-1.43.113/boto3/dynamodb/transform.py:206
message: Consider using "elif" instead of "else" then "if" to remove one indentation level
```
  204|             params[expr_attr_names_input].update(generated_names)
  205|         else:
  206|             if generated_names:
  207|                 params[expr_attr_names_input] = generated_names
  208| 
```

### only_reference example — cachetools cachetools-7.2.1/src/cachetools/_cachedmethod.py:406
message: Consider using "elif" instead of "else" then "if" to remove one indentation level
```
  404|             wrapper = _unlocked_info(method, cache, key, info)
  405|     else:
  406|         if cond is not None and lock is not None:
  407|             wrapper = _condition(method, cache, key, lock, cond)
  408|         elif cond is not None:
```

## ruff :: SIM910
reference: flake8 | only ruff: 4 | only reference: 2856 | packages: 129
top messages: [only_reference] Use '_model_info.get("max_tokens")' instead of '_model_info.get('max_tokens', None)' ×141 || [only_reference] Use 'litellm_params.get("ssl_verify")' instead of 'litellm_params.get('ssl_verify', None)' ×112 || [only_reference] Use 'server_config.get("spec_path")' instead of 'server_config.get('spec_path', None)' ×37 || [only_reference] Use 'litellm_params.get("api_base")' instead of 'litellm_params.get('api_base', None)' ×32

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/tableform.py:126
message: Use `kwarg.get('pad')` instead of `kwarg.get('pad', None)`
```
  124| 
  125|         # fill out any short lines
  126|         pad = kwarg.get('pad', None)
  127|         ok_None = False
  128|         if pad is None:
```

### only_reference example — cloudpickle cloudpickle-3.1.2/cloudpickle/cloudpickle.py:294
message: Use 'sys.modules.get(module_name)' instead of 'sys.modules.get(module_name, None)'
```
  292|     # Note: if module_name is in sys.modules, the corresponding module is
  293|     # assumed importable at unpickling time. See #357
  294|     module = sys.modules.get(module_name, None)
  295|     if module is None:
  296|         # The main reason why obj's module would not be imported is that this
```

### only_reference example — boto3 boto3-1.43.113/boto3/resources/collection.py:76
message: Use 'self._params.get("limit")' instead of 'self._params.get('limit', None)'
```
   74| 
   75|         """
   76|         limit = self._params.get('limit', None)
   77| 
   78|         count = 0
```

### only_reference example — attrs attrs-26.1.0/src/attr/_make.py:893
message: Use 'base_cls.__dict__.get("__weakref__")' instead of 'base_cls.__dict__.get('__weakref__', None)'
```
  891|         weakref_inherited = False
  892|         for base_cls in self._cls.__mro__[1:-1]:
  893|             if base_cls.__dict__.get("__weakref__", None) is not None:
  894|                 weakref_inherited = True
  895|             existing_slots.update(
```

## ruff :: N802
reference: flake8 | only ruff: 2701 | only reference: 156 | packages: 29
top messages: [only_rewrite] Function name `_print_Pow` should be lowercase ×25 || [only_reference] function name 'do_GET' should be lowercase ×23 || [only_rewrite] Function name `_print_Rational` should be lowercase ×20 || [only_rewrite] Function name `_print_Piecewise` should be lowercase ×20

### only_rewrite example — asttokens asttokens-3.0.2/tests/test_asttokens.py:10
message: Function name `assertTokenizing` should be lowercase
```
    8| class TestASTTokens(unittest.TestCase):
    9| 
   10|   def assertTokenizing(self, generate_tokens):
   11|     source = "import re  # comment\n\nfoo = 'bar'\n"
   12|     atok = asttokens.ASTTokens(source, tokens=generate_tokens(source))
```

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/toc.py:82
message: Function name `stashedHTML2text` should be lowercase
```
   80| 
   81| @deprecated('Use `run_postprocessors`, `render_inner_html` and/or `striptags` instead.')
   82| def stashedHTML2text(text: str, md: Markdown, strip_entities: bool = True) -> str:
   83|     """ Extract raw HTML from stash, reduce to plain text and swap with placeholder. """
   84|     def _html_sub(m: re.Match[str]) -> str:
```

### only_rewrite example — executing .0/tests/small_samples/ba8bf627448498ff15c46e5e5549e2f2fc2716d45309504753d1dce79842bb0e.py:16
message: Function name `advancePastEmptyBuckets` should be lowercase
```
   14| # 
   15| 
   16| def advancePastEmptyBuckets():
   17|     return
   18|     (is_equal or is_equal)
```

### only_reference example — azure-identity azure_identity-1.26.0/azure/identity/_internal/auth_code_redirect_handler.py:16
message: function name 'do_GET' should be lowercase
```
   14|     """
   15| 
   16|     def do_GET(self):
   17|         if self.path.endswith("/favicon.ico"):  # deal with legacy IE
   18|             self.send_response(204)
```

### only_reference example — fastapi fastapi-0.143.0/tests/test_telemetry/test_runtime.py:544
message: function name 'do_POST' should be lowercase
```
  542| 
  543|     class Handler(BaseHTTPRequestHandler):
  544|         def do_POST(self):
  545|             self.rfile.read(int(self.headers["Content-Length"]))
  546|             received.append(self.path)
```

### only_reference example — botocore botocore-1.43.113/tests/functional/test_six_imports.py:34
message: function name 'visit_Import' should be lowercase
```
   32|         self.filename = filename
   33| 
   34|     def visit_Import(self, node):
   35|         for alias in node.names:
   36|             if getattr(alias, 'name', '') == 'six':
```

## ruff :: SIM300
reference: flake8 | only ruff: 2656 | only reference: 53 | packages: 82
top messages: [only_rewrite] Yoda condition detected ×2656 || [only_reference] Use '"\n" == "\n"' instead of '"\n" == "\n"' (Yoda-conditions) ×12 || [only_reference] Use '"cond1" == "cond1"' instead of '"cond1" == "cond1"' (Yoda-conditions) ×10 || [only_reference] Use '1 == 1' instead of '1 == 1' (Yoda-conditions) ×7

### only_rewrite example — attrs attrs-26.1.0/tests/test_dunders.py:786
message: Yoda condition detected
```
  784| 
  785|         i = C(23)
  786|         assert (42, [], 23) == (i._a, i._b, i.c)
  787| 
  788|     @given(booleans(), booleans())
```

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/tests/test_navigablestring.py:31
message: Yoda condition detected
```
   29|         assert "fee " == s.string
   30|         assert "fee" == s.get_text(strip=True)
   31|         assert ["fee "] == list(s.strings)
   32|         assert ["fee"] == list(s.stripped_strings)
   33|         assert ["fee "] == list(s._all_strings())
```

### only_rewrite example — aiobotocore aiobotocore-3.9.2/tests/botocore_tests/unit/test_session.py:117
message: Yoda condition detected
```
  115|             'endpoint_resolver', mock_resolver
  116|         )
  117|         assert ['foo'] == session.get_available_partitions()
  118| 
  119|     async def test_proxies_list_endpoints_to_resolver(self, session):
```

### only_reference example — jedi jedi-0.20.1/test/completion/precedence.py:62
message: Use '"a" == 3' instead of '3 == "a"' (Yoda-conditions)
```
   60| (3 + 'a')
   61| #? bool()
   62| (3 == 'a')
   63| #? bool()
   64| (3 >= 'a')
```

### only_reference example — gunicorn gunicorn-26.2.0/examples/boot_fail.py:8
message: Use '2 == 1' instead of '1 == 2' (Yoda-conditions)
```
    6| 
    7| def app(environ, start_response):
    8|     assert 1 == 2, "Shouldn't get here."
```

### only_reference example — parso parso-0.8.7/test/normalizer_issue_files/E25.py:31
message: Use '1 == 1' instead of '1 == 1' (Yoda-conditions)
```
   29|     )
   30| # Okay
   31| foo(bar=(1 == 1))
   32| foo(bar=(1 != 1))
   33| foo(bar=(1 >= 1))
```

## ruff :: N803
reference: flake8 | only ruff: 1746 | only reference: 0 | packages: 10
top messages: [only_rewrite] Argument name `K` should be lowercase ×365 || [only_rewrite] Argument name `K1` should be lowercase ×327 || [only_rewrite] Argument name `A` should be lowercase ×258 || [only_rewrite] Argument name `User` should be lowercase ×194

### only_rewrite example — alembic alembic-1.20.0/tests/test_autogen_indexes.py:1354
message: Argument name `CapT` should be lowercase
```
 1352|         ),
 1353|         (
 1354|             lambda CapT: Index("idx", "y", func.lower(CapT.c.XCol)),
 1355|             lambda CapT: Index("idx", func.lower(CapT.c.XCol)),
 1356|         ),
```

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/tables/otConverters.py:2981
message: Argument name `C` should be lowercase
```
 2979|     "MorxSubtable": MorxSubtableConverter,
 2980|     # "Template" types
 2981|     "AATLookup": lambda C: partial(AATLookup, tableClass=C),
 2982|     "AATLookupWithDataOffset": lambda C: partial(AATLookupWithDataOffset, tableClass=C),
 2983|     "MorphStateTable": lambda C: partial(MorphStateTable, tableClass=C),
```

### only_rewrite example — mpmath mpmath-1.4.1/demo/sofa.py:13
message: Argument name `A` should be lowercase
```
   11| mp.prec = 113
   12| 
   13| eqs = [lambda A, B, φ, θ: (A*(cos(θ) - cos(φ)) - 2*B*sin(φ)
   14|                            + (θ - φ - 1)*cos(θ) - sin(θ) + cos(φ) + sin(φ)),
   15|        lambda A, B, φ, θ: (A*(3*sin(θ) + sin(φ)) - 2*B*cos(φ)
```

## ruff :: PLE0309
reference: pylint | only ruff: 1 | only reference: 1510 | packages: 2
top messages: [only_reference] __hash__ does not return int ×1510 || [only_rewrite] `__hash__` does not return an integer ×1

### only_rewrite example — sqlalchemy sqlalchemy-2.1.4/lib/sqlalchemy/sql/cache_key.py:295
message: `__hash__` does not return an integer
```
  293|     def __hash__(self) -> Optional[int]:  # type: ignore[override]
  294|         """CacheKey itself is not hashable - hash the .key portion"""
  295|         return None
  296| 
  297|     def to_offline_string(
```

### only_reference example — google-cloud-aiplatform -2.4.0/google/cloud/aiplatform_v1beta1/services/vertex_rag_service/transports/rest_base.py:97
message: __hash__ does not return int
```
   95| 
   96|     class _BaseAskContexts:
   97|         def __hash__(self):  # pragma: NO COVER
   98|             return NotImplementedError("__hash__ must be implemented.")
   99| 
```

### only_reference example — sqlalchemy sqlalchemy-2.1.4/lib/sqlalchemy/sql/cache_key.py:293
message: __hash__ does not return int
```
  291|     # can't use "if not TYPE_CHECKING" because mypy rejects it
  292|     # inside of a NamedTuple
  293|     def __hash__(self) -> Optional[int]:  # type: ignore[override]
  294|         """CacheKey itself is not hashable - hash the .key portion"""
  295|         return None
```

## ruff :: SIM114
reference: flake8 | only ruff: 30 | only reference: 1182 | packages: 87
top messages: [only_rewrite] Combine `if` branches using logical `or` operator ×30 || [only_reference] Use logical or ((part.startswith('border:')) or (part.startswith('[') and part.endswith('] ×18 || [only_reference] Use logical or ((byte == b'*') or (byte == b'~')) and a single body ×18 || [only_reference] Use logical or ((part in ('roman', 'sans', 'mono')) or (part.startswith('border:'))) and a ×17

### only_rewrite example — dill dill-0.4.1/dill/detect.py:102
message: Combine `if` branches using logical `or` operator
```
  100|             # get methods
  101|             _ = getattr(obj, '__func__', None) # ismethod
  102|             if getattr(_, '__code__', None) is co: funcs.add(obj)
  103|             # get functions
  104|             elif getattr(obj, '__code__', None) is co: funcs.add(obj)
```

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:268
message: Combine `if` branches using logical `or` operator
```
  266| 
  267|         with self.assertRaises(tester(Exception)):
  268|             if tester(0):
  269|                 pass
  270|             elif tester(0):
```

### only_rewrite example — sympy sympy-1.14.0/sympy/integrals/manualintegrate.py:1282
message: Combine `if` branches using logical `or` operator
```
 1280|             # make sure dv is amenable to integration
 1281|             accept = False
 1282|             if index < 2:  # log and inverse trig are usually worth trying
 1283|                 accept = True
 1284|             elif (rule == pull_out_algebraic and dv.args and
```

### only_reference example — awscli awscli-1.46.1/awscli/s3transfer/download.py:1032
message: Use logical or ((chunk) or (self._num_reads == 1)) and a single body
```
 1030|         chunk = self._body.read(self._chunksize)
 1031|         self._num_reads += 1
 1032|         if chunk:
 1033|             return chunk
 1034|         elif self._num_reads == 1:
```

### only_reference example — build build-1.6.1/src/build/_compat/importlib.py:8
message: Use logical or ((TYPE_CHECKING) or (sys.version_info >= (3, 10, 2))) and a single body
```
    6| TYPE_CHECKING = False
    7| 
    8| if TYPE_CHECKING:
    9|     from importlib import metadata
   10| elif sys.version_info >= (3, 10, 2):
```

### only_reference example — asyncpg asyncpg-0.32.0/asyncpg/connection.py:2741
message: Use logical or ((hasattr(connection_settings, 'crdb_version')) or (hasattr(connection_settings, 'crate_version'))) and a single body
```
 2739|         jit = False
 2740|         sql_copy_from_where = False
 2741|     elif hasattr(connection_settings, 'crdb_version'):
 2742|         # CockroachDB detected.
 2743|         advisory_locks = False
```

## ruff :: N805
reference: flake8 | only ruff: 1109 | only reference: 44 | packages: 22
top messages: [only_rewrite] First argument of a method should be named `self` ×1109 || [only_reference] first argument of a method should be named 'self' ×44

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:68
message: First argument of a method should be named `self`
```
   66|     static_method = staticmethod(static_method)
   67|     
   68|     def class_method(cls):
   69|         """class method test"""
   70|         exec(a, b)
```

### only_rewrite example — docutils docutils-0.23/docutils/utils/math/math2html.py:46
message: First argument of a method should be named `self`
```
   44|     prefix = None
   45| 
   46|     def debug(cls, message) -> None:
   47|         "Show a debug message"
   48|         if not Trace.debugmode or Trace.quietmode:
```

### only_rewrite example — gunicorn gunicorn-26.2.0/gunicorn/config.py:1857
message: First argument of a method should be named `self`
```
 1855|     type = callable
 1856| 
 1857|     def on_starting(server):
 1858|         pass
 1859|     default = staticmethod(on_starting)
```

### only_reference example — anyio anyio-4.15.1/tests/test_taskgroups.py:2118
message: first argument of a method should be named 'self'
```
 2116|     """
 2117| 
 2118|     async def typetest_None(*, task_status: TaskStatus[None]) -> None:
 2119|         task_status.started()
 2120|         task_status.started(None)
```

### only_reference example — azure-core azure_core-1.41.0/azure/core/_enum_meta.py:46
message: first argument of a method should be named 'self'
```
   44|     """
   45| 
   46|     def __getitem__(cls, name: str) -> Any:
   47|         # disabling pylint bc of pylint bug https://github.com/PyCQA/astroid/issues/713
   48|         return super(CaseInsensitiveEnumMeta, cls).__getitem__(name.upper())
```

### only_reference example — httpx2 httpx2-2.13.1/httpx2/_status_codes.py:19
message: first argument of a method should be named 'self'
```
   17| 
   18| class _CodesMeta(EnumMeta):
   19|     def __getattribute__(cls, name: str) -> object:
   20|         if name in _DEPRECATED_CODES:
   21|             new_name = _DEPRECATED_CODES[name]
```

## ruff :: N815
reference: flake8 | only ruff: 244 | only reference: 886 | packages: 19
top messages: [only_rewrite] Variable `_print_SparseRepMatrix` in class scope should not be mixedCase ×16 || [only_rewrite] Variable `has_assoc_Ring` in class scope should not be mixedCase ×15 || [only_rewrite] Variable `has_assoc_Field` in class scope should not be mixedCase ×15 || [only_reference] variable 'mimeType' in class scope should not be mixedCase ×10

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/descriptor_crash.py:5
message: Variable `_urlOpen` in class scope should not be mixedCase
```
    3| 
    4| class Page(object):
    5|     _urlOpen = staticmethod(urllib.urlopen)
    6| 
    7|     def getPage(self, url):
```

### only_rewrite example — executing executing-2.3.0/executing/executing.py:460
message: Variable `visit_AsyncFunctionDef` in class scope should not be mixedCase
```
  458|                         self.visit(grandchild)
  459| 
  460|     visit_AsyncFunctionDef = visit_FunctionDef
  461| 
  462|     def visit_Lambda(self, node: ast.AST) -> None:
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/domains/realfield.py:60
message: Variable `is_RealField` in class scope should not be mixedCase
```
   58|     rep = 'RR'
   59| 
   60|     is_RealField = is_RR = True
   61| 
   62|     is_Exact = False
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/neptune/_client.py:38
message: variable 'namedGraphUri' in class scope should not be mixedCase
```
   36|     """Typed dictionary representing the additional parser configuration for the Neptune Bulk Loader."""
   37| 
   38|     namedGraphUri: NotRequired[str]
   39|     """
   40|     The default graph for all RDF formats when no graph is specified
```

### only_reference example — fastapi fastapi-0.143.0/fastapi/openapi/models.py:216
message: variable 'externalValue' in class scope should not be mixedCase
```
  214|     description: str | None
  215|     value: Any | None
  216|     externalValue: AnyUrl | None
  217| 
  218|     __pydantic_config__ = {"extra": "allow"}  # type: ignore[misc]  # ty: ignore[invalid-typed-dict-statement]
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/ttFont.py:430
message: variable 'writeVersion' in class scope should not be mixedCase
```
  428| 
  429|     class XMLSavingOptions(TypedDict):
  430|         writeVersion: bool
  431|         quiet: bool | None
  432|         tables: Sequence[str | bytes] | None
```

## ruff :: PLR0913
reference: pylint | only ruff: 272 | only reference: 826 | packages: 59
top messages: [only_reference] Too many arguments (6/5) ×132 || [only_reference] Too many arguments (7/5) ×117 || [only_rewrite] Too many arguments in function definition (6 > 5) ×105 || [only_reference] Too many arguments (9/5) ×101

### only_rewrite example — attrs attrs-26.1.0/tests/strategies.py:121
message: Too many arguments in function definition (6 > 5)
```
  119| 
  120| @st.composite
  121| def simple_classes(
  122|     draw,
  123|     slots=None,
```

### only_rewrite example — coverage coverage-7.16.2/coverage/control.py:142
message: Too many arguments in function definition (18 > 5)
```
  140|             return None
  141| 
  142|     def __init__(  # pylint: disable=too-many-arguments
  143|         self,
  144|         data_file: FilePath | DefaultValue | None = DEFAULT_DATAFILE,
```

### only_rewrite example — fsspec fsspec-2026.9.0/fsspec/implementations/smb.py:63
message: Too many arguments in function definition (11 > 5)
```
   61| 
   62|     # pylint: disable=too-many-arguments
   63|     def __init__(
   64|         self,
   65|         host,
```

### only_reference example — deprecated deprecated-3.0.0/src/deprecated/classic.py:330
message: Too many arguments (6/5)
```
  328| 
  329| @overload
  330| def deprecated[T: Deprecatable](
  331|     reason: str | None = "",
  332|     /,
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/postgresql.py:245
message: Too many arguments (9/5)
```
  243| 
  244| @overload
  245| def read_sql_query(
  246|     sql: str,
  247|     con: "pg8000.Connection",
```

### only_reference example — chardet chardet-7.6.0/src/chardet/detector.py:50
message: Too many arguments (10/5)
```
   48|     )
   49| 
   50|     def __init__(  # noqa: PLR0913
   51|         self,
   52|         lang_filter: LanguageFilter = LanguageFilter.ALL,
```

## ruff :: PLW0603
reference: pylint | only ruff: 967 | only reference: 30 | packages: 78
top messages: [only_rewrite] Using the global statement to update `master_key` is discouraged ×41 || [only_rewrite] Using the global statement to update `people` is discouraged ×31 || [only_reference] Using the global statement ×30 || [only_rewrite] Using the global statement to update `_current_process` is discouraged ×30

### only_rewrite example — colorama colorama-0.4.6/colorama/initialise.py:10
message: Using the global statement to update `orig_stdout` is discouraged
```
    8| 
    9| def _wipe_internal_state_for_tests():
   10|     global orig_stdout, orig_stderr
   11|     orig_stdout = None
   12|     orig_stderr = None
```

### only_rewrite example — asyncpg asyncpg-0.32.0/asyncpg/_testbase/__init__.py:244
message: Using the global statement to update `_default_cluster` is discouraged
```
  242| 
  243| def _init_default_cluster(initdb_options=None):
  244|     global _default_cluster
  245| 
  246|     if _default_cluster is None:
```

### only_rewrite example — anyio anyio-4.15.1/src/anyio/pytest_plugin.py:61
message: Using the global statement to update `_current_runner` is discouraged
```
   59|     backend_name: str, backend_options: dict[str, Any]
   60| ) -> Iterator[TestRunner]:
   61|     global _current_runner, _runner_leases, _runner_stack
   62|     if _current_runner is None:
   63|         asynclib = get_async_backend(backend_name)
```

### only_reference example — chardet chardet-7.6.0/scripts/utils.py:179
message: Using the global statement
```
  177| def _language_name_to_iso() -> dict[str, str]:
  178|     """Return (and memoize) the English-name -> ISO 639-1 mapping."""
  179|     global _LANGUAGE_NAME_TO_ISO  # noqa: PLW0603
  180|     if _LANGUAGE_NAME_TO_ISO is None:
  181|         try:
```

### only_reference example — alembic alembic-1.20.0/tests/test_offline_environment.py:23
message: Using the global statement
```
   21|         self.cfg = _no_sql_testing_config()
   22| 
   23|         global a, b, c
   24|         a, b, c = three_rev_fixture(self.cfg)
   25| 
```

### only_reference example — jedi jedi-0.20.1/test/completion/complex.py:6
message: Using the global statement
```
    4| 
    5| class Foo(object):
    6|     global time
    7|     asdf = time
    8| 
```

## ruff :: B008
reference: flake8 | only ruff: 16 | only reference: 896 | packages: 28
top messages: [only_reference] Do not perform function calls in argument defaults.  The call is performed only once at fu ×896 || [only_rewrite] Do not perform function call `QQ` in argument defaults; instead, perform the call within t ×9 || [only_rewrite] Do not perform function call `tester` in argument defaults; instead, perform the call with ×2 || [only_rewrite] Do not perform function call `iter` in argument defaults; instead, perform the call within ×1

### only_rewrite example — google-auth google_auth-2.62.0/tests/transport/aio/test_sessions.py:118
message: Do not perform function call `iter` in argument defaults; instead, perform the call within the function, or read the default from a module-level singleton varia
```
  116|         task = False
  117|         with patch(
  118|             "time.monotonic", side_effect=lambda it=iter([0, 0.25]): next(it, 0.75)
  119|         ):
  120|             with patch("asyncio.wait_for", lambda coro, _: coro):
```

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:101
message: Do not perform function call `tester` in argument defaults; instead, perform the call within the function, or read the default from a module-level singleton var
```
   99|         @empty_decorator.tester("2")
  100|         @empty_decorator
  101|         def foo2(_=tester("3"), __=tester("4")):
  102|             pass
  103| 
```

### only_rewrite example — matplotlib matplotlib-3.11.2/galleries/examples/text_labels_and_annotations/fancyarrow_demo.py:48
message: Do not perform function call `itertools.count` in argument defaults; instead, perform the call within the function, or read the default from a module-level sing
```
   46|     n = 2 if s.count(',') > 3 else 1
   47|     ax.text(1.4, 0,
   48|             re.sub(', ', lambda m, c=itertools.count(1): m.group()
   49|                    if next(c) % n else '\n', s),
   50|             verticalalignment="center", color="0.3")
```

### only_reference example — annotated-doc annotated_doc-0.0.5/scripts/prepare_release.py:106
message: Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the resu
```
  104| @app.command()
  105| def prepare(
  106|     bump: BumpType = typer.Argument(
  107|         ...,
  108|         envvar="PREPARE_RELEASE_BUMP",
```

### only_reference example — fastapi fastapi-0.143.0/docs_src/body_multiple_params/tutorial001_py310.py:17
message: Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the resu
```
   15| async def update_item(
   16|     *,
   17|     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
   18|     q: str | None = None,
   19|     item: Item | None = None,
```

### only_reference example — alembic alembic-1.20.0/alembic/config.py:126
message: Do not perform function calls in argument defaults.  The call is performed only once at function definition time. All calls to your function will reuse the resu
```
  124|         stdout: TextIO = sys.stdout,
  125|         cmd_opts: Namespace | None = None,
  126|         config_args: Mapping[str, Any] = util.immutabledict(),
  127|         attributes: dict[str, Any] | None = None,
  128|     ) -> None:
```

## ruff :: SIM118
reference: flake8 | only ruff: 902 | only reference: 3 | packages: 84
top messages: [only_rewrite] Use `key in dict` instead of `key in dict.keys()` ×820 || [only_rewrite] Use `key not in dict` instead of `key not in dict.keys()` ×82 || [only_reference] Use '"x-custom-context" in getter' instead of '"x-custom-context" in getter.keys()' ×1 || [only_reference] Use '"autorestore/stored_var_d" in ip.db' instead of '"autorestore/stored_var_d" in ip.db. ×1

### only_rewrite example — boto3 boto3-1.43.113/boto3/crt.py:185
message: Use `key in dict` instead of `key in dict.keys()`
```
  183|         return
  184|     invalid_crt_args = []
  185|     for param in config.DEFAULTS.keys():
  186|         val = config.get_deep_attr(param)
  187|         if (
```

### only_rewrite example — authlib authlib-1.8.0/authlib/jose/rfc7519/claims.py:107
message: Use `key in dict` instead of `key in dict.keys()`
```
  105| 
  106|         # Validate custom claims
  107|         for key in self.options.keys():
  108|             if key not in self.REGISTERED_CLAIMS:
  109|                 self._validate_claim_value(key)
```

### only_rewrite example — distro distro-1.9.0/tests/test_distro.py:1957
message: Use `key in dict` instead of `key in dict.keys()`
```
 1955|             _distro = distro.LinuxDistribution()
 1956|             info = getattr(_distro, info_method)()
 1957|             for key in info.keys():
 1958|                 try:
 1959|                     assert info[key] == getattr(_distro, attr_method)(key)
```

### only_reference example — fastapi fastapi-0.143.0/tests/test_telemetry/test_http.py:127
message: Use '"x-custom-context" in getter' instead of '"x-custom-context" in getter.keys()'
```
  125|     class HeaderPropagator(TraceContextTextMapPropagator):
  126|         def extract(self, carrier, context=None, getter=textmap.default_getter):
  127|             assert "x-custom-context" in getter.keys(carrier)
  128|             values = getter.get(carrier, "X-Custom-Context")
  129|             assert values is not None
```

### only_reference example — ipython ipython-9.17.1/tests/test_storemagic.py:97
message: Use '"autorestore/stored_var_d" in ip.db' instead of '"autorestore/stored_var_d" in ip.db.keys()'
```
   95|     try:
   96|         ip.run_line_magic("store", "stored_var_d")
   97|         assert "autorestore/stored_var_d" in ip.db.keys("autorestore/*")
   98|         ip.run_line_magic("store", "-d stored_var_d")
   99|         assert "autorestore/stored_var_d" not in ip.db.keys("autorestore/*")
```

### only_reference example — pydantic pydantic-2.14.1/pydantic/v1/utils.py:471
message: Use 'item in self' instead of 'item in self.keys()'
```
  469| 
  470|     def __contains__(self, item: Any) -> bool:
  471|         return item in self.keys()
  472| 
  473|     def __eq__(self, other: Any) -> bool:
```
