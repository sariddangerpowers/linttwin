
## ruff :: PLE0604
reference: pylint | only ruff: 5 | only reference: 18 | packages: 4
top messages: [only_reference] Invalid object 'Feature' in __all__, must contain only strings ×16 || [only_rewrite] Invalid object in `__all__`, must contain only strings ×5 || [only_reference] Invalid object 'SnowflakeConnection' in __all__, must contain only strings ×2

### only_rewrite example — frozenlist frozenlist-1.8.0/packaging/pep517_backend/_backend.py:52
message: Invalid object in `__all__`, must contain only strings
```
   50| from ._transformers import sanitize_rst_roles
   51| 
   52| __all__ = (  # noqa: WPS410
   53|     'build_sdist',
   54|     'build_wheel',
```

### only_rewrite example — google-cloud-aiplatform google_cloud_aiplatform-2.4.0/google/cloud/aiplatform/compat/__init__.py:291
message: Invalid object in `__all__`, must contain only strings
```
  289|     types.vizier_service = types.vizier_service_v1
  290| 
  291| __all__ = (
  292|     DEFAULT_VERSION,
  293|     V1BETA1,
```

### only_rewrite example — propcache propcache-0.5.4/packaging/pep517_backend/_backend.py:53
message: Invalid object in `__all__`, must contain only strings
```
   51| from ._transformers import sanitize_rst_roles
   52| 
   53| __all__ = (  # noqa: WPS410
   54|     'build_sdist',
   55|     'build_wheel',
```

### only_reference example — snowflake-connector-python snowflake_connector_python-4.8.0/src/snowflake/connector/aio/__init__.py:10
message: Invalid object 'SnowflakeConnection' in __all__, must contain only strings
```
    8| 
    9| __all__ = [
   10|     SnowflakeConnection,
   11|     SnowflakeCursor,
   12|     DictCursor,
```

### only_reference example — google-cloud-aiplatform google_cloud_aiplatform-2.4.0/vertexai/resources/preview/feature_store/__init__.py:54
message: Invalid object 'Feature' in __all__, must contain only strings
```
   52| 
   53| __all__ = (
   54|     Feature,
   55|     FeatureGroup,
   56|     FeatureGroupBigQuerySource,
```

## ruff :: B911
reference: flake8 | only ruff: 0 | only reference: 20 | packages: 6
top messages: [only_reference] `itertools.batched()` without an explicit `strict=` parameter. ×20

### only_reference example — anyio anyio-4.15.1/tests/test_itertools.py:154
message: `itertools.batched()` without an explicit `strict=` parameter.
```
  152|     async def test_basic_cases(self) -> None:
  153|         for iterator in (
  154|             batched([1, 2, 3, 4, 5], 2),
  155|             batched(aiter_from([1, 2, 3, 4, 5]), 2),
  156|         ):
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/scaleUpem.py:177
message: `itertools.batched()` without an explicit `strict=` parameter.
```
  175|                     if vec:
  176|                         m = len(vec) // varData.VarRegionCount
  177|                         vec = list(batched(vec, m))
  178|                         vec = [Vector(v) for v in vec]
  179|                         component.axisValuesVarIndex = storeBuilder.storeDeltas(vec)
```

### only_reference example — more-itertools more_itertools-11.2.0/more_itertools/recipes.py:1032
message: `itertools.batched()` without an explicit `strict=` parameter.
```
 1030|     """
 1031|     if isinstance(shape, int):
 1032|         return batched(chain.from_iterable(matrix), shape)
 1033|     first_dim, *dims = shape
 1034|     scalar_stream = _flatten_tensor(matrix)
```

## ruff :: PLR1733
reference: pylint | only ruff: 16 | only reference: 4 | packages: 11
top messages: [only_rewrite] Unnecessary lookup of dictionary value by key ×16 || [only_reference] Unnecessary dictionary index lookup, use 'xref_entry' instead ×3 || [only_reference] Unnecessary dictionary index lookup, use 'nbrdict' instead ×1

### only_rewrite example — fastapi fastapi-0.143.0/fastapi/utils.py:114
message: Unnecessary lookup of dictionary value by key
```
  112|             key in main_dict
  113|             and isinstance(main_dict[key], list)
  114|             and isinstance(update_dict[key], list)
  115|         ):
  116|             main_dict[key] = main_dict[key] + update_dict[key]
```

### only_rewrite example — awscli awscli-1.46.1/awscli/botocore/stub.py:402
message: Unnecessary lookup of dictionary value by key
```
  400|         # Validate the parameters are equal
  401|         for param, value in expected_params.items():
  402|             if param not in params or expected_params[param] != params[param]:
  403|                 raise StubAssertionError(
  404|                     operation_name=model.name,
```

### only_rewrite example — botocore botocore-1.43.113/botocore/stub.py:402
message: Unnecessary lookup of dictionary value by key
```
  400|         # Validate the parameters are equal
  401|         for param, value in expected_params.items():
  402|             if param not in params or expected_params[param] != params[param]:
  403|                 raise StubAssertionError(
  404|                     operation_name=model.name,
```

### only_reference example — networkx networkx-3.7/networkx/algorithms/community/modularity_max.py:100
message: Unnecessary dictionary index lookup, use 'nbrdict' instead
```
   98|     for u, nbrdict in dq_dict.items():
   99|         for v, wt in nbrdict.items():
  100|             dq_dict[u][v] = q0 * wt - resolution * (a[u] * b[v] + b[u] * a[v])
  101| 
  102|     # Use -dq to get a max_heap instead of a min_heap
```

### only_reference example — pypdf pypdf-6.20.1/pypdf/_reader.py:758
message: Unnecessary dictionary index lookup, use 'xref_entry' instead
```
  756|                     if pid == xref_id - self.xref_index:
  757|                         # fixing index item per item is required for revised PDF.
  758|                         self.xref[gen][pid] = self.xref[gen][xref_id]
  759|                         del self.xref[gen][xref_id]
  760|                     # if not, then either it's just plain wrong, or the
```

## ruff :: F601
reference: flake8 | only ruff: 9 | only reference: 11 | packages: 8
top messages: [only_reference] dictionary key 'xx' repeated with different values ×3 || [only_reference] dictionary key 'foo' repeated with different values ×3 || [only_reference] dictionary key 'x' repeated with different values ×3 || [only_rewrite] Dictionary key literal `"xxxxxxxx"` repeated ×3

### only_rewrite example — google-api-core google_api_core-2.42.0/google/api_core/operations_v1/transports/rest_asyncio.py:155
message: Dictionary key literal repeated
```
  153|             "google.api_core.client_options.ClientOptions.client_cert_source": client_cert_source_for_mtls,
  154|             # TODO(https://github.com/googleapis/python-api-core/issues/718): Add support for `client_cert_source` to async REST transport.
  155|             "google.api_core.client_options.ClientOptions.client_cert_source": client_cert_source_for_mtls,
  156|         }
  157|         provided_unsupported_params = [
```

### only_rewrite example — fonttools fonttools-4.66.1/Tests/ufoLib/testSupport.py:598
message: Dictionary key literal `"openTypeNameCompatibleFullName"` repeated
```
  596|     "openTypeNamePreferredFamilyName": "Some Font (Preferred Family Name)",
  597|     "openTypeNamePreferredSubfamilyName": "Regular (Preferred Subfamily Name)",
  598|     "openTypeNameCompatibleFullName": "Some Font Regular (Compatible Full Name)",
  599|     "openTypeNameUniqueID": "OpenType name Table Unique ID",
  600|     "openTypeNameVersion": "OpenType name Table Version",
```

### only_rewrite example — ipython ipython-9.17.1/IPython/core/logger.py:139
message: Dictionary key literal `False` repeated (`False` hashes to the same value as `0`)
```
  137|                              'not with: %s' % val)
  138| 
  139|         label = {0:'OFF',1:'ON',False:'OFF',True:'ON'}
  140| 
  141|         if self.logfile is None:
```

### only_reference example — fonttools fonttools-4.66.1/Tests/ufoLib/testSupport.py:631
message: dictionary key 'fullName' repeated with different values
```
  629|     "fondID": 15000,
  630|     "fondName": "SomeFont Regular (FOND Name)",
  631|     "fullName": "Some Font Regular (Compatible Full Name)",
  632|     "notice": "Some Font by Some Designer for Some Foundry.",
  633|     "designer": "Some Designer",
```

### only_reference example — networkx networkx-3.7/networkx/algorithms/tests/test_planarity.py:500
message: dictionary key 1 repeated with different values
```
  498|         embedding = nx.PlanarEmbedding(
  499|             {
  500|                 1: {2: {"cw": 2, "ccw": 2}},
  501|                 2: {1: {"cw": 1, "ccw": 1}},
  502|                 1: {3: {}},
```

### only_reference example — black black-26.10.1/tests/data/cases/preview_long_strings__regression.py:148
message: dictionary key 'xx' repeated with different values
```
  146|         ),
  147| 
  148| xxxxxxx = { 'xx' : 'xxxx xxxxxxx xxxxxxxxx -x xxx -x /xxx/{0} -x xxx,xxx -xx {1} \
  149| -xx {1} -xx xxx=xxx_xxxx,xxx_xx,xxx_xxx,xxx_xxxx,xxx_xx,xxx_xxx |\
  150|  xxxxxx -x xxxxxxxx -x xxxxxxxx -x',
```

## ruff :: PLR1736
reference: pylint | only ruff: 13 | only reference: 7 | packages: 8
top messages: [only_rewrite] List index lookup in `enumerate()` loop ×13 || [only_reference] Unnecessary list index lookup, use 'ts' instead ×4 || [only_reference] Unnecessary list index lookup, use 'term' instead ×1 || [only_reference] Unnecessary list index lookup, use 'j' instead ×1

### only_rewrite example — pyasn1 pyasn1-0.6.4/pyasn1/codec/ber/decoder.py:885
message: List index lookup in `enumerate()` loop
```
  883|                                         containerValue):
  884| 
  885|                                     stream = asSeekableStream(containerValue[pos].asOctets())
  886| 
  887|                                     for component in decodeFun(stream, asn1Spec=openType, **options):
```

### only_rewrite example — pymupdf pymupdf-1.28.2/src/table.py:1719
message: List index lookup in `enumerate()` loop
```
 1717|                 if cell is not None:
 1718|                     cells[i][j] = extract_cells(
 1719|                         self.textpage, cell_boxes[i][j], markdown=True
 1720|                     )
 1721| 
```

### only_rewrite example — redis redis-8.1.0/redis/utils.py:341
message: List index lookup in `enumerate()` loop
```
  339| 
  340|     for i, ver in enumerate(num_versions1):
  341|         if num_versions1[i] > num_versions2[i]:
  342|             return -1
  343|         elif num_versions1[i] < num_versions2[i]:
```

### only_reference example — pandas pandas-3.0.6/pandas/tests/indexes/datetimes/test_iter.py:23
message: Unnecessary list index lookup, use 'ts' instead
```
   21|         )
   22|         for i, ts in enumerate(index):
   23|             assert ts == index[i]  # noqa: PLR1736 (unnecessary-list-index-lookup)
   24| 
   25|     def test_iter_readonly(self):
```

### only_reference example — sympy sympy-1.14.0/sympy/vector/functions.py:502
message: Unnecessary list index lookup, use 'term' instead
```
  500|     for i, term in enumerate(vlist):
  501|         for j in range(i):
  502|             term -= ortho_vlist[j].projection(vlist[i])
  503|         # TODO : The following line introduces a performance issue
  504|         # and needs to be changed once a good solution for issue #10279 is
```

## ruff :: C408
reference: flake8 | only ruff: 19 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary `dict()` call (rewrite as a literal) ×19

### only_rewrite example — executing executing-2.3.0/tests/samples/bird.py:84
message: Unnecessary `dict()` call (rewrite as a literal)
```
   82|         self._last_call_id = None
   83|         self._ipython_cell_value = None
   84|         self.num_samples = num_samples or dict(
   85|             big=dict(
   86|                 attributes=50,
```

## ruff :: B024
reference: flake8 | only ruff: 18 | only reference: 0 | packages: 8
top messages: [only_rewrite] `ExtendableOutputFunction` is an abstract base class, but it has no abstract methods or pr ×1 || [only_rewrite] `KeySerializationEncryption` is an abstract base class, but it has no abstract methods or  ×1 || [only_rewrite] `Event` is an abstract base class, but it has no abstract methods or properties ×1 || [only_rewrite] `Outcome` is an abstract base class, but it has no abstract methods or properties ×1

### only_rewrite example — cryptography cryptography-50.0.2/src/cryptography/hazmat/primitives/hashes.py:96
message: `ExtendableOutputFunction` is an abstract base class, but it has no abstract methods or properties
```
   94| 
   95| 
   96| class ExtendableOutputFunction(metaclass=abc.ABCMeta):
   97|     """
   98|     An interface for extendable output functions.
```

### only_rewrite example — h11 h11-0.16.0/h11/_events.py:32
message: `Event` is an abstract base class, but it has no abstract methods or properties
```
   30| 
   31| 
   32| class Event(ABC):
   33|     """
   34|     Base class for h11 events.
```

### only_rewrite example — grpcio grpcio-1.84.0/src/python/grpcio/grpc/framework/foundation/callable_util.py:25
message: `Outcome` is an abstract base class, but it has no abstract methods or properties
```
   23| 
   24| 
   25| class Outcome(ABC):
   26|     """A sum type describing the outcome of some call.
   27| 
```

## ruff :: N807
reference: flake8 | only ruff: 17 | only reference: 0 | packages: 8
top messages: [only_rewrite] Function name should not start and end with `__` ×17

### only_rewrite example — attrs attrs-26.1.0/src/attr/__init__.py:87
message: Function name should not start and end with `__`
```
   85|     """
   86| 
   87|     def __getattr__(name: str) -> str:
   88|         if name not in ("__version__", "__version_info__"):
   89|             msg = f"module {mod_name} has no attribute {name}"
```

### only_rewrite example — anyio anyio-4.15.1/src/anyio/_lazyimport.py:33
message: Function name should not start and end with `__`
```
   31|         return False
   32| 
   33|     def __getattr__(name: str) -> Any:
   34|         if new_name := deprecated_aliases.get(name):
   35|             emit_deprecation_warning(module_name, name, new_name)
```

### only_rewrite example — huggingface-hub huggingface_hub-2.2.0/src/huggingface_hub/__init__.py:1220
message: Function name should not start and end with `__`
```
 1218|     attr_to_modules = {attr: mod for mod, attrs in submod_attrs.items() for attr in attrs}
 1219| 
 1220|     def __getattr__(name):
 1221|         if name in submodules:
 1222|             try:
```

## ruff :: N814
reference: flake8 | only ruff: 1 | only reference: 16 | packages: 7
top messages: [only_reference] camelcase 'ConstantKernel' imported as constant 'C' ×5 || [only_reference] camelcase '_TypedColumnClauseArgument' imported as constant '_TCCA' ×5 || [only_reference] camelcase 'RedirectingFinder' imported as constant 'F' ×1 || [only_reference] camelcase 'LayoutDimension' imported as constant 'D' ×1

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/tests/test_pythonrational.py:3
message: Camelcase `PythonRational` imported as constant `QQ`
```
    1| """Tests for PythonRational type. """
    2| 
    3| from sympy.polys.domains import PythonRational as QQ
    4| from sympy.testing.pytest import raises
    5| 
```

### only_reference example — editables editables-0.6/tests/test_redirects.py:5
message: camelcase 'RedirectingFinder' imported as constant 'F'
```
    3| import sys
    4| 
    5| from editables.redirector import RedirectingFinder as F
    6| 
    7| 
```

### only_reference example — prompt-toolkit prompt_toolkit-3.0.53/examples/full-screen/pager.py:12
message: camelcase 'LayoutDimension' imported as constant 'D'
```
   10| from prompt_toolkit.layout.containers import HSplit, Window
   11| from prompt_toolkit.layout.controls import FormattedTextControl
   12| from prompt_toolkit.layout.dimension import LayoutDimension as D
   13| from prompt_toolkit.layout.layout import Layout
   14| from prompt_toolkit.lexers import PygmentsLexer
```

### only_reference example — requests-toolbelt requests-toolbelt-1.0.0/requests_toolbelt/adapters/x509.py:31
message: camelcase 'PROTOCOL_SSLv23' imported as constant 'PROTOCOL'
```
   29|     from _ssl import PROTOCOL_TLS as PROTOCOL
   30| except ImportError:
   31|     from _ssl import PROTOCOL_SSLv23 as PROTOCOL
   32| 
   33| 
```

## ruff :: B026
reference: flake8 | only ruff: 17 | only reference: 0 | packages: 1
top messages: [only_rewrite] Star-arg unpacking after a keyword argument is strongly discouraged ×17

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/pretty/pretty.py:358
message: Star-arg unpacking after a keyword argument is strongly discouraged
```
  356| 
  357|         f = prettyForm(
  358|             binding=prettyForm.FUNC, *self._print(deriv.expr).parens())
  359| 
  360|         pform = prettyForm(deriv_symbol)
```

## ruff :: B020
reference: flake8 | only ruff: 12 | only reference: 4 | packages: 9
top messages: [only_reference] Found for loop that reassigns the iterable it is iterating with each iterable value. ×4 || [only_rewrite] Loop control variable `self` overrides iterable it iterates ×3 || [only_rewrite] Loop control variable `x` overrides iterable it iterates ×3 || [only_rewrite] Loop control variable `f` overrides iterable it iterates ×2

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/__init__.py:469
message: Loop control variable `self` overrides iterable it iterates
```
  467|             self.original_encoding,
  468|             self.declared_html_encoding,
  469|             self.contains_replacement_characters,
  470|         ) in self.builder.prepare_markup(
  471|             markup, from_encoding, exclude_encodings=exclude_encodings
```

### only_rewrite example — google-cloud-aiplatform google_cloud_aiplatform-2.4.0/google/cloud/aiplatform/_streaming_prediction.py:189
message: Loop control variable `tensor_list` overrides iterable it iterates
```
  187|     parameters_tensor = value_to_tensor(parameters) if parameters else None
  188|     async for (
  189|         tensor_list
  190|     ) in predict_stream_of_tensor_lists_from_single_tensor_list_async(
  191|         prediction_service_async_client=prediction_service_async_client,
```

### only_rewrite example — executing executing-2.3.0/tests/samples/tracer.py:339
message: Loop control variable `node` overrides iterable it iterates
```
  337|             frame = frame.f_back
  338| 
  339|         for node in ancestors(node):
  340|             if isinstance(node, (ast.FunctionDef, ast.Lambda)):
  341|                 break
```

### only_reference example — transformers transformers-5.19.0/src/transformers/models/granitemoe_swa/modular_granitemoe_swa.py:192
message: Found for loop that reassigns the iterable it is iterating with each iterable value.
```
  190|         # (`self.rotary_emb`, built by the parent at the global theta, is left in place but unused.)
  191|         self.rotary_embs = nn.ModuleList()
  192|         for theta in sorted({theta for theta in config.layer_rope_theta if theta}):
  193|             theta_config = copy.deepcopy(config)
  194|             theta_config.rope_parameters = {**config.rope_parameters, "rope_theta": theta}
```

## ruff :: PLC0208
reference: pylint | only ruff: 0 | only reference: 16 | packages: 11
top messages: [only_reference] Use a sequence type when iterating over values ×16

### only_reference example — asyncpg asyncpg-0.32.0/tests/test_connect.py:1658
message: Use a sequence type when iterating over values
```
 1656| 
 1657|     async def test_connect_args_validation(self):
 1658|         for val in {-1, 'a', True, False, 0}:
 1659|             with self.assertRaisesRegex(ValueError, 'greater than 0'):
 1660|                 await asyncpg.connect(command_timeout=val)
```

### only_reference example — anthropic anthropic-1.13.0/src/anthropic/lib/tools/_toolsets/_security.py:137
message: Use a sequence type when iterating over values
```
  135|     """Whether `candidate`, normalised as text, is `directory` (as written or as it resolves) or below it."""
  136|     text = os.path.normcase(os.path.normpath(candidate))
  137|     for base in {directory, str(realpath_lenient(directory))}:
  138|         base = os.path.normcase(os.path.normpath(base))
  139|         if text == base or text.startswith(base.rstrip("/\\") + os.sep):
```

### only_reference example — fonttools fonttools-4.66.1/Tests/feaLib/builder_test.py:1255
message: Use a sequence type when iterating over values
```
 1253|         self.check_fea2fea_file(name)
 1254| 
 1255|         for line, sub in {(3, "sub"), (8, "pos"), (13, "sub")}:
 1256|             captor.assertRegex(
 1257|                 f'{name}.fea:{line}:12: Ambiguous "ignore {sub}", there should be least one marked glyph'
```

## ruff :: E711
reference: flake8 | only ruff: 15 | only reference: 1 | packages: 3
top messages: [only_rewrite] Comparison to `None` should be `cond is not None` ×10 || [only_rewrite] Comparison to `None` should be `cond is None` ×5 || [only_reference] comparison to None should be 'if cond is None:' ×1

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:706
message: Comparison to `None` should be `cond is None`
```
  704|             isinstance(x.parent, ast.AnnAssign)
  705|             and x.parent.target == x
  706|             and x.parent.value == None
  707|         ):
  708|             return True
```

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/fortran.py:387
message: Comparison to `None` should be `cond is not None`
```
  385|     def _print_sum_(self, sm):
  386|         params = self._print(sm.array)
  387|         if sm.dim != None: # Must use '!= None', cannot use 'is not None'
  388|             params += ', ' + self._print(sm.dim)
  389|         if sm.mask != None: # Must use '!= None', cannot use 'is not None'
```

### only_reference example — fonttools fonttools-4.66.1/Lib/fontTools/designspaceLib/__init__.py:2493
message: comparison to None should be 'if cond is None:'
```
 2491|             except ValueError:
 2492|                 self.log.warning("ValueError in readLocation yValue %3.3f", yValue)
 2493|             if userValue is None == xValue is None:
 2494|                 raise DesignSpaceDocumentError(
 2495|                     f'Exactly one of uservalue="" or xvalue="" must be provided for location dimension "{dimName}"'
```

## ruff :: B002
reference: flake8 | only ruff: 16 | only reference: 0 | packages: 3
top messages: [only_rewrite] Python does not support the unary prefix decrement operator (`--`) ×16

### only_rewrite example — mpmath mpmath-1.4.1/mpmath/tests/test_special.py:11
message: Python does not support the unary prefix decrement operator (`--`)
```
    9|     assert nan != nan
   10|     assert isnan(nan)
   11|     assert --inf == inf
   12|     assert abs(inf) == inf
   13|     assert abs(-inf) == inf
```

### only_rewrite example — pyparsing pyparsing-3.3.3/tests/test_unit.py:11613
message: Python does not support the unary prefix decrement operator (`--`)
```
11611|         self.assertEqual(expr.parse_string("1-(2-3)", parse_all=True)[0], 2)
11612|         # complicated math expressions – same as Python expressions
11613|         self.assertEqual(expr.parse_string("1----3", parse_all=True)[0], 1 - ---3)
11614|         self.assertEqual(expr.parse_string("1+2*3", parse_all=True)[0], 1 + 2 * 3)
11615|         self.assertEqual(expr.parse_string("1*2+3", parse_all=True)[0], 1 * 2 + 3)
```

### only_rewrite example — sympy sympy-1.14.0/sympy/core/tests/test_power.py:87
message: Python does not support the unary prefix decrement operator (`--`)
```
   85| 
   86| def test_issue_3866():
   87|     assert --sqrt(sqrt(5) - 1) == sqrt(sqrt(5) - 1)
   88| 
   89| 
```

## ruff :: PLW0127
reference: pylint | only ruff: 15 | only reference: 0 | packages: 9
top messages: [only_rewrite] Self-assignment of variable `resp` ×3 || [only_rewrite] Self-assignment of variable `a4` ×2 || [only_rewrite] Self-assignment of variable `X` ×2 || [only_rewrite] Self-assignment of variable `round` ×1

### only_rewrite example — azure-storage-blob azure_storage_blob-12.31.0/tests/test_large_block_blob.py:117
message: Self-assignment of variable `resp`
```
  115|         for i in range(5):
  116|             stream = BytesIO(bytearray(LARGE_BLOCK_SIZE))
  117|             resp = resp = blob.stage_block("block {0}".format(i).encode("utf-8"), stream, length=LARGE_BLOCK_SIZE)
  118|             assert resp is not None
  119|             assert "content_md5" in resp
```

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/misc/py23.py:57
message: Self-assignment of variable `round`
```
   55| open = open
   56| range = range
   57| round = round3 = round
   58| unichr = chr
   59| unicode = str
```

### only_rewrite example — mpmath mpmath-1.4.1/demo/sofa.py:51
message: Self-assignment of variable `i`
```
   49|         i = [0, φ, α]
   50|     else:
   51|         i = i = [0, α]
   52|     return 1 - quad(lambda x: f(x)*sin(x), i)
   53| 
```

## ruff :: B021
reference: flake8 | only ruff: 13 | only reference: 0 | packages: 3
top messages: [only_rewrite] f-string used as docstring. Python will interpret this as a joined string, rather than a d ×13

### only_rewrite example — executing .0/tests/small_samples/206e0609ff0589a0a32422ee902f09156af91746e27157c32c9595d12072f92a.py:1
message: f-string used as docstring. Python will interpret this as a joined string, rather than a docstring.
```
    1| f'\n\n        subroutine {fprefix}_input_{fsuffix}(c, o, n)\n          character*{clength}, intent(in) :: c\n          integer n\n          !f2py integer, depend(c), intent(hide) :: n = slen(c)\n          integer*1, dimension(n) :: o\n          !f2py intent(out) o\n          o = transfer(c, o)\n    
```

### only_rewrite example — ruff uff-0.17.0/crates/ruff_python_parser/resources/inline/ok/fstring_format_spec_terminator.py:1
message: f-string used as docstring. Python will interpret this as a joined string, rather than a docstring.
```
    1| f"hello {x:} world"
    2| f"hello {x:.3f} world"
```

### only_rewrite example — black black-26.10.1/tests/data/cases/fstring.py:1
message: f-string used as docstring. Python will interpret this as a joined string, rather than a docstring.
```
    1| f"f-string without formatted values is just a string"
    2| f"{{NOT a formatted value}}"
    3| f"{{NOT 'a' \"formatted\" \"value\"}}"
```

## ruff :: PLW0602
reference: pylint | only ruff: 8 | only reference: 4 | packages: 10
top messages: [only_reference] Using global for '_g_thread_data' but no assignment is done ×2 || [only_rewrite] Using global for `_DEFAULT_INTEGRATIONS` but no assignment is done ×2 || [only_rewrite] Using global for `Person` but no assignment is done ×1 || [only_rewrite] Using global for `time` but no assignment is done ×1

### only_rewrite example — dill dill-0.4.1/dill/tests/test_session.py:123
message: Using global for `Person` but no assignment is done
```
  121|     try:
  122|         main_dict = __main__.__dict__
  123|         global Person, person, Calendar, CalendarSubclass, cal, selfref
  124| 
  125|         for obj in ('json', 'url', 'local_mod', 'sax', 'dom'):
```

### only_rewrite example — jedi jedi-0.20.1/test/completion/complex.py:6
message: Using global for `time` but no assignment is done
```
    4| 
    5| class Foo(object):
    6|     global time
    7|     asdf = time
    8| 
```

### only_rewrite example — executing .0/tests/small_samples/6602443ba655e0e139cfb923d581f8da91071d631a42f81253c1e47fdc952da3.py:19
message: Using global for `keyring` but no assignment is done
```
   17| 
   18| def get_keyring_auth():
   19|     global keyring
```

### only_reference example — litellm litellm-1.105.0/litellm/litellm_core_utils/litellm_logging.py:557
message: Using global for 'supabaseClient' but no assignment is done
```
  555| 
  556| class Logging(LiteLLMLoggingBaseClass):
  557|     global \
  558|         supabaseClient, \
  559|         promptLayerLogger, \
```

### only_reference example — paramiko paramiko-5.0.0/paramiko/util.py:233
message: Using global for '_g_thread_data' but no assignment is done
```
  231| 
  232| def get_thread_id():
  233|     global _g_thread_data, _g_thread_counter, _g_thread_lock  # noqa
  234|     try:
  235|         return _g_thread_data.id
```

### only_reference example — setuptools setuptools-84.0.0/setuptools/tests/test_setuptools.py:54
message: Using global for 'z' but no assignment is done
```
   52| 
   53|         def f1():
   54|             global x, y, z  # noqa: PLW0602 # global kept to exercise extract_constant
   55|             x = "test"
   56|             y = z  # pyright: ignore[reportUnboundVariable] # Explicitly testing for this runtime issue
```

## ruff :: B027
reference: flake8 | only ruff: 4 | only reference: 8 | packages: 7
top messages: [only_reference] prereleases is an empty method in an abstract base class, but has no abstract decorator. C ×4 || [only_rewrite] `BaseLLMObsOTELAttributes.set_messages` is an empty method in an abstract base class, but  ×2 || [only_rewrite] `_HttpResponseBase.encoding` is an empty method in an abstract base class, but has no abst ×1 || [only_reference] encoding is an empty method in an abstract base class, but has no abstract decorator. Cons ×1

### only_rewrite example — azure-core azure_core-1.41.0/azure/core/rest/_rest_py3.py:265
message: `_HttpResponseBase.encoding` is an empty method in an abstract base class, but has no abstract decorator
```
  263|         """
  264| 
  265|     @encoding.setter
  266|     def encoding(self, value: Optional[str]) -> None:
  267|         """Sets the response encoding.
```

### only_rewrite example — litellm litellm-1.105.0/litellm/integrations/opentelemetry_utils/base_otel_llm_obs_attributes.py:9
message: `BaseLLMObsOTELAttributes.set_messages` is an empty method in an abstract base class, but has no abstract decorator
```
    7| 
    8| class BaseLLMObsOTELAttributes(ABC):
    9|     @staticmethod
   10|     def set_messages(span: "Span", kwargs: dict[str, Any]):
   11|         pass
```

### only_rewrite example — virtualenv virtualenv-21.14.7/src/virtualenv/activation/activator.py:39
message: `Activator.add_parser_arguments` is an empty method in an abstract base class, but has no abstract decorator
```
   37|         return True
   38| 
   39|     @classmethod  # ruff:ignore[empty-method-without-abstract-decorator]
   40|     def add_parser_arguments(cls, parser: ArgumentParser, interpreter: PythonInfo) -> None:
   41|         """Add CLI arguments for this activation script.
```

### only_reference example — azure-core azure_core-1.41.0/azure/core/rest/_rest_py3.py:266
message: encoding is an empty method in an abstract base class, but has no abstract decorator. Consider adding @abstractmethod.
```
  264| 
  265|     @encoding.setter
  266|     def encoding(self, value: Optional[str]) -> None:
  267|         """Sets the response encoding.
  268| 
```

### only_reference example — packaging packaging-26.3/src/packaging/specifiers.py:179
message: prereleases is an empty method in an abstract base class, but has no abstract decorator. Consider adding @abstractmethod.
```
  177| 
  178|     @prereleases.setter  # noqa: B027
  179|     def prereleases(self, value: bool) -> None:
  180|         """Setter for :attr:`prereleases`.
  181| 
```

### only_reference example — litellm litellm-1.105.0/litellm/integrations/opentelemetry_utils/base_otel_llm_obs_attributes.py:10
message: set_messages is an empty method in an abstract base class, but has no abstract decorator. Consider adding @abstractmethod.
```
    8| class BaseLLMObsOTELAttributes(ABC):
    9|     @staticmethod
   10|     def set_messages(span: "Span", kwargs: dict[str, Any]):
   11|         pass
   12| 
```

## ruff :: SIM101
reference: flake8 | only ruff: 5 | only reference: 7 | packages: 7
top messages: [only_rewrite] Multiple `isinstance` calls for `node`, merge into a single call ×4 || [only_reference] Multiple isinstance-calls which can be merged into a single call for variable 'expr' ×2 || [only_reference] Multiple isinstance-calls which can be merged into a single call for variable 'name' ×1 || [only_rewrite] Multiple `isinstance` calls for `logging_result`, merge into a single call ×1

### only_rewrite example — asttokens asttokens-3.0.2/asttokens/mark_tokens.py:303
message: Multiple `isinstance` calls for `node`, merge into a single call
```
  301|     self, node: AstNode, first_token: util.Token, last_token: util.Token
  302|   ) -> Tuple[util.Token, util.Token]:
  303|     assert isinstance(node, ast.Tuple) or isinstance(node, AstroidBaseContainer)
  304|     # It's a bare tuple if the first token belongs to the first child. The first child may
  305|     # include extraneous parentheses (which don't create new nodes), so account for those too.
```

### only_rewrite example — litellm litellm-1.105.0/litellm/litellm_core_utils/litellm_logging.py:2577
message: Multiple `isinstance` calls for `logging_result`, merge into a single call
```
 2575|         """
 2576|         if (
 2577|             isinstance(logging_result, ModelResponse)
 2578|             or isinstance(logging_result, ModelResponseStream)
 2579|             or isinstance(logging_result, EmbeddingResponse)
```

### only_reference example — alembic alembic-1.20.0/alembic/ddl/mysql.py:108
message: Multiple isinstance-calls which can be merged into a single call for variable 'expr'
```
  106|         # lib/sqlalchemy/dialects/mysql/base.py#L2191
  107|         if is_index and (
  108|             isinstance(expr, elements.BinaryExpression)
  109|             or (
  110|                 isinstance(expr, elements.UnaryExpression)
```

### only_reference example — cffi cffi-2.1.1/src/cffi/api.py:137
message: Multiple isinstance-calls which can be merged into a single call for variable 'name'
```
  135|         library we only look for the actual (untyped) symbols.
  136|         """
  137|         if not (isinstance(name, basestring) or
  138|                 name is None or
  139|                 isinstance(name, self.CData)):
```

### only_reference example — litellm litellm-1.105.0/litellm/proxy/_experimental/mcp_server/utils.py:848
message: Multiple isinstance-calls which can be merged into a single call for variable 'value'
```
  846|     if path_depth > MAX_STRUCTURED_CONTENT_SCAN_DEPTH:
  847|         return None
  848|     if isinstance(value, bool) or value is None or isinstance(value, str):
  849|         return ()
  850|     if isinstance(value, (int, float)):
```

## ruff :: PLW0128
reference: pylint | only ruff: 12 | only reference: 0 | packages: 7
top messages: [only_rewrite] Redeclared variable `resp` in assignment ×3 || [only_rewrite] Redeclared variable `X` in assignment ×2 || [only_rewrite] Redeclared variable `i` in assignment ×1 || [only_rewrite] Redeclared variable `linker` in assignment ×1

### only_rewrite example — azure-storage-blob azure_storage_blob-12.31.0/tests/test_large_block_blob.py:117
message: Redeclared variable `resp` in assignment
```
  115|         for i in range(5):
  116|             stream = BytesIO(bytearray(LARGE_BLOCK_SIZE))
  117|             resp = resp = blob.stage_block("block {0}".format(i).encode("utf-8"), stream, length=LARGE_BLOCK_SIZE)
  118|             assert resp is not None
  119|             assert "content_md5" in resp
```

### only_rewrite example — mpmath mpmath-1.4.1/demo/sofa.py:51
message: Redeclared variable `i` in assignment
```
   49|         i = [0, φ, α]
   50|     else:
   51|         i = i = [0, α]
   52|     return 1 - quad(lambda x: f(x)*sin(x), i)
   53| 
```

### only_rewrite example — numpy numpy-2.5.4/vendored-meson/meson/mesonbuild/compilers/detect.py:508
message: Redeclared variable `linker` in assignment
```
  506|             cls = c.IntelLLVMClCCompiler if lang == 'c' else cpp.IntelLLVMClCPPCompiler
  507|             env.add_lang_args(cls.language, cls, for_machine)
  508|             linker = linker = guess_win_linker(
  509|                     env, ['link'], cls, version,
  510|                     for_machine)
```

## ruff :: E702
reference: flake8 | only ruff: 12 | only reference: 0 | packages: 1
top messages: [only_rewrite] Multiple statements on one line (semicolon) ×12

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:58
message: Multiple statements on one line (semicolon)
```
   56|     def test_semicolons(self):
   57|         # fmt: off
   58|         tester(1); tester(2); tester(3)
   59|         tester(9
   60|                ); tester(
```

## ruff :: PLR0133
reference: pylint | only ruff: 12 | only reference: 0 | packages: 2
top messages: [only_rewrite] Two constants compared in a comparison, consider replacing `1 < 1` ×9 || [only_rewrite] Two constants compared in a comparison, consider replacing `1 < 3` ×3

### only_rewrite example — executing .0/tests/small_samples/4851dc1b626a95e97dbe0c53f96099d165b755dd1bd552c6ca771f7bca6d30f5.py:16
message: Two constants compared in a comparison, consider replacing `1 < 1`
```
   14| # 
   15| 
   16| if 1 < 1 > 1 == 1 >= 1 <= 1 != 1 in 1 not in 1 is 1 is not 1:
   17|     pass
```

### only_rewrite example — pytest pytest-9.1.1/testing/test_assertrewrite.py:894
message: Two constants compared in a comparison, consider replacing `1 < 3`
```
  892| 
  893|         def f2() -> None:
  894|             assert 1 < 3 < 5 <= 4 < 7
  895| 
  896|         assert getmsg(f2) == "assert 5 <= 4"
```
