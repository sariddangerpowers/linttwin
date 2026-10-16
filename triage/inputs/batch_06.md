
## ruff :: PLW1641
reference: pylint | only ruff: 1 | only reference: 9 | packages: 9
top messages: [only_reference] Implementing __eq__ without also implementing __hash__ ×9 || [only_rewrite] Object does not implement `__hash__` method ×1

### only_rewrite example — pymupdf pymupdf-1.28.2/src/__init__.py:8739
message: Object does not implement `__hash__` method
```
 8737| 
 8738| 
 8739| class Matrix:
 8740| 
 8741|     def __abs__(self):
```

### only_reference example — asn1crypto asn1crypto-1.5.1/asn1crypto/util.py:118
message: Implementing __eq__ without also implementing __hash__
```
  116|         return num
  117| 
  118|     class timezone(tzinfo):  # noqa
  119|         """
  120|         Implements datetime.timezone for py2.
```

### only_reference example — grpcio grpcio-1.84.0/src/python/grpcio/grpc/aio/_metadata.py:37
message: Implementing __eq__ without also implementing __hash__
```
   35| 
   36| 
   37| class Metadata(Collection[MetadatumType]):  # noqa: PLW1641
   38|     """Metadata abstraction for the asynchronous calls and interceptors.
   39| 
```

### only_reference example — jsonschema jsonschema-4.26.0/jsonschema/exceptions.py:219
message: Implementing __eq__ without also implementing __hash__
```
  217| 
  218| @define(slots=False)
  219| class _RefResolutionError(Exception):  # noqa: PLW1641
  220|     """
  221|     A ref could not be resolved.
```

## ruff :: B012
reference: flake8 | only ruff: 1 | only reference: 9 | packages: 3
top messages: [only_reference] return/continue/break inside finally blocks cause exceptions to be silenced. Exceptions sh ×9 || [only_rewrite] `return` inside `finally` blocks cause exceptions to be silenced ×1

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:61
message: `return` inside `finally` blocks cause exceptions to be silenced
```
   59|             global_access(local, val=autre)
   60|         finally:
   61|             return local
   62|     
   63|     def static_method():
```

### only_reference example — multiprocess multiprocess-0.70.19/pypy3.10/multiprocess/connection.py:321
message: return/continue/break inside finally blocks cause exceptions to be silenced. Exceptions should be silenced in except blocks. Control statements can be moved out
```
  319|                             return f
  320|                         elif err == _winapi.ERROR_MORE_DATA:
  321|                             return self._get_more_data(ov, maxsize)
  322|                 except OSError as e:
  323|                     if e.winerror == _winapi.ERROR_BROKEN_PIPE:
```

### only_reference example — prompt-toolkit prompt_toolkit-3.0.53/src/prompt_toolkit/eventloop/async_generator.py:101
message: return/continue/break inside finally blocks cause exceptions to be silenced. Exceptions should be silenced in except blocks. Control statements can be moved out
```
   99|                 except Full:
  100|                     if quitting:
  101|                         return
  102|                     continue
  103|                 else:
```

## ruff :: PLC0132
reference: pylint | only ruff: 10 | only reference: 0 | packages: 4
top messages: [only_rewrite] `NewType` name `str30` does not match assigned variable name `str3050` ×2 || [only_rewrite] `TypeVar` name `myvar` does not match assigned variable name `x` ×1 || [only_rewrite] `NewType` name `NewStr` does not match assigned variable name `new_type` ×1 || [only_rewrite] `TypeVar` name `T` does not match assigned variable name `T1` ×1

### only_rewrite example — jedi jedi-0.20.1/test/test_api/test_interpreter.py:540
message: `TypeVar` name `myvar` does not match assigned variable name `x`
```
  538| def test_type_var():
  539|     """This was an issue before, see Github #1369"""
  540|     x = typing.TypeVar('myvar')  # type: ignore[misc]
  541|     def_, = jedi.Interpreter('x', [locals()]).infer()
  542|     assert def_.name == 'TypeVar'
```

### only_rewrite example — pydantic pydantic-2.14.1/tests/test_json_schema.py:3330
message: `NewType` name `NewStr` does not match assigned variable name `new_type`
```
 3328| 
 3329| def test_new_type():
 3330|     new_type = NewType('NewStr', str)
 3331| 
 3332|     class Model(BaseModel):
```

### only_rewrite example — typing-extensions typing_extensions-4.16.0/src/test_typing_extensions.py:6715
message: `TypeVar` name `T` does not match assigned variable name `T1`
```
 6713|             class D(Protocol[Unpack[Ts], int]): pass
 6714| 
 6715|         T1 = TypeVar('T')
 6716|         T2 = TypeVar('T')
 6717|         class C(Generic[T1, T2, Unpack[Ts]]): pass
```

## ruff :: F722
reference: flake8 | only ruff: 1 | only reference: 9 | packages: 3
top messages: [only_reference] syntax error in forward annotation 'str\n    | list[str]\n' ×4 || [only_reference] syntax error in forward annotation "one of 'bar', 'baz'" ×3 || [only_reference] syntax error in forward annotation '^xxx\\d{3}$' ×2 || [only_rewrite] Syntax error in forward annotation: Unexpected token at the end of an expression ×1

### only_rewrite example — ruff ates/ruff_python_formatter/resources/test/fixtures/ruff/statement/long_type_annotations.py:90
message: Syntax error in forward annotation: Unexpected token at the end of an expression
```
   88| x16: None | Literal[
   89|     "split",
   90|     "a bit longer",
   91|     "records",
   92|     "index",
```

### only_reference example — langchain-core langchain_core-1.6.10/tests/unit_tests/utils/test_function_calling.py:57
message: syntax error in forward annotation "one of 'bar', 'baz'"
```
   55|     def dummy_function(
   56|         arg1: ExtensionsAnnotated[int, "foo"],
   57|         arg2: ExtensionsAnnotated[Literal["bar", "baz"], "one of 'bar', 'baz'"],
   58|     ) -> None:
   59|         """Dummy function."""
```

### only_reference example — ruff /ruff_python_formatter/resources/test/fixtures/ruff/statement/return_type_no_parameters.py:62
message: syntax error in forward annotation 'str\n    | list[str]\n'
```
   60| #########################################################################################
   61| 
   62| def test_return_multiline_string_type_annotation() -> """str
   63|     | list[str]
   64| """:
```

### only_reference example — pydantic pydantic-2.14.1/tests/test_types.py:408
message: syntax error in forward annotation '^xxx\\d{3}$'
```
  406|         str_strip_enabled: constr(strip_whitespace=True)
  407|         str_strip_disabled: constr(strip_whitespace=False)
  408|         str_regex: constr(pattern=r'^xxx\d{3}$') = ...
  409|         str_min_length: constr(min_length=5) = ...
  410|         str_email: EmailStr = ...
```

## ruff :: B011
reference: flake8 | only ruff: 10 | only reference: 0 | packages: 2
top messages: [only_rewrite] Do not `assert False` (`python -O` removes these calls), raise `AssertionError()` ×10

### only_rewrite example — executing .0/tests/small_samples/5da4523399bd1a8477d2d02970672787c08a73c1c5f0268b0d08de4c35a7f5a0.py:16
message: Do not `assert False` (`python -O` removes these calls), raise `AssertionError()`
```
   14| # 
   15| 
   16| assert False, 'Can this happen?'
   17| nodes
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/matrices/tests/test_xxm.py:255
message: Do not `assert False` (`python -O` removes these calls), raise `AssertionError()`
```
  253| 
  254|     else:
  255|         assert False, "Unknown GROUND_TYPES: %s" % GROUND_TYPES
  256| 
  257|     for domain in supported:
```

## ruff :: PLC0105
reference: pylint | only ruff: 7 | only reference: 2 | packages: 6
top messages: [only_rewrite] `TypeVar` name "_DecodeText" does not reflect its covariance; consider renaming it to "_De ×2 || [only_rewrite] `TypeVar` name "HTTPResponseType" does not reflect its covariance; consider renaming it to ×1 || [only_rewrite] `TypeVar` name "HTTPRequestType" does not reflect its covariance; consider renaming it to  ×1 || [only_reference] Type variable name does not reflect variance. "Input" is contravariant, use "Input_contra" ×1

### only_rewrite example — azure-core azure_core-1.41.0/azure/core/pipeline/__init__.py:40
message: `TypeVar` name "HTTPResponseType" does not reflect its covariance; consider renaming it to "HTTPResponseType_co"
```
   38| )
   39| 
   40| HTTPResponseType = TypeVar("HTTPResponseType", covariant=True)  # pylint: disable=typevar-name-incorrect-variance
   41| HTTPRequestType = TypeVar("HTTPRequestType", covariant=True)  # pylint: disable=typevar-name-incorrect-variance
   42| 
```

### only_rewrite example — aiohttp aiohttp-3.14.5/aiohttp/client_ws.py:50
message: `TypeVar` name "_DecodeText" does not reflect its covariance; consider renaming it to "_DecodeText_co"
```
   48| # TypeVar for whether text messages are decoded to str (True) or kept as bytes (False)
   49| # Covariant because it only affects return types, not input types
   50| _DecodeText = TypeVar("_DecodeText", bound=bool, covariant=True, default=Literal[True])
   51| 
   52| 
```

### only_rewrite example — mcp mcp-2.3.0/src/mcp/shared/context.py:24
message: `TypeVar` name "TransportT" does not reflect its covariance; consider renaming it to "TransportT_co"
```
   22| __all__ = ["BaseContext"]
   23| 
   24| TransportT = TypeVar("TransportT", bound=TransportContext, default=TransportContext, covariant=True)
   25| 
   26| 
```

### only_reference example — langchain-core langchain_core-1.6.10/langchain_core/runnables/utils.py:45
message: Type variable name does not reflect variance. "Input" is contravariant, use "Input_contra" instead
```
   43|     from langchain_core.runnables.schema import StreamEvent
   44| 
   45| Input = TypeVar("Input", contravariant=True)  # noqa: PLC0105
   46| # Output type should implement __concat__, as eg str, list, dict do
   47| Output = TypeVar("Output", covariant=True)  # noqa: PLC0105
```

## ruff :: PLW3301
reference: pylint | only ruff: 9 | only reference: 0 | packages: 5
top messages: [only_rewrite] Nested `max` calls can be flattened ×5 || [only_rewrite] Nested `min` calls can be flattened ×4

### only_rewrite example — coverage coverage-7.16.2/coverage/lcovreport.py:86
message: Nested `min` calls can be flattened
```
   84|     functions = [
   85|         (
   86|             min(region.start, min(region.lines)),  # pylint: disable=nested-min-max
   87|             max(region.start, max(region.lines)),  # pylint: disable=nested-min-max
   88|             region,
```

### only_rewrite example — prompt-toolkit prompt_toolkit-3.0.53/src/prompt_toolkit/layout/dimension.py:157
message: Nested `max` calls can be flattened
```
  155|         # explicitly pass dimensions.
  156|         max_ = min(d.max for d in dimensions)
  157|         max_ = max(max_, max(d.preferred for d in dimensions))
  158| 
  159|         # Make sure that min>=max. In some scenarios, when certain min..max
```

### only_rewrite example — mypy mypy-2.4.0/mypy/report.py:903
message: Nested `max` calls can be flattened
```
  901|         output_files = sorted(self.files, key=lambda x: x.module)
  902|         report_file = os.path.join(self.output_dir, "lineprecision.txt")
  903|         width = max(4, max(len(info.module) for info in output_files))
  904|         titles = ("Lines", "Precise", "Imprecise", "Any", "Empty", "Unanalyzed")
  905|         widths = (width,) + tuple(len(t) for t in titles)
```

## ruff :: PLW0129
reference: pylint | only ruff: 8 | only reference: 0 | packages: 2
top messages: [only_rewrite] Asserting on a non-empty string literal will always pass ×8

### only_rewrite example — aiohttp aiohttp-3.14.5/tests/test_web_functional.py:644
message: Asserting on a non-empty string literal will always pass
```
  642|     async def handler(request):
  643|         data = await request.post()
  644|         assert b"123", data["name"]
  645|         return web.Response()
  646| 
```

### only_rewrite example — ruff uff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/expression/fstring.py:590
message: Asserting on a non-empty string literal will always pass
```
  588| 
  589| # Assert statements
  590| assert f"aaaaaaaaa{
  591|         expression}bbbbbbbbbbbb", f"cccccccccc{
  592|                 expression}dddddddddd"
```

## ruff :: C414
reference: flake8 | only ruff: 8 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary `tuple()` call within `list()` ×8

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:72
message: Unnecessary `tuple()` call within `list()`
```
   70|         @empty_decorator  # 0
   71|         @decorator_with_args(tester('123'), x=int())  # 1
   72|         @tester(list(tuple([1, 2])))  # 2!
   73|         @tester(  # 3!
   74|             list(
```

## ruff :: C409
reference: flake8 | only ruff: 8 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary list literal passed to `tuple()` (rewrite as a tuple literal) ×8

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:72
message: Unnecessary list literal passed to `tuple()` (rewrite as a tuple literal)
```
   70|         @empty_decorator  # 0
   71|         @decorator_with_args(tester('123'), x=int())  # 1
   72|         @tester(list(tuple([1, 2])))  # 2!
   73|         @tester(  # 3!
   74|             list(
```

## ruff :: SIM223
reference: flake8 | only ruff: 8 | only reference: 0 | packages: 3
top messages: [only_rewrite] Use `False` instead of `False and ...` ×6 || [only_rewrite] Use `0` instead of `0 and ...` ×1 || [only_rewrite] Use `False` instead of `... and False` ×1

### only_rewrite example — executing .0/tests/small_samples/339587c1bea1dae03e45ad87a1c245a4e7a3d719968e39e572cb987ee055ad50.py:16
message: Use `0` instead of `0 and ...`
```
   14| # 
   15| 
   16| print(0 and foo)
```

### only_rewrite example — pymupdf pymupdf-1.28.2/src/__init__.py:8658
message: Use `False` instead of `False and ...`
```
 8656|             return None
 8657|         CheckParent(self)
 8658|         if 0 and g_use_extra:
 8659|             val = extra.Link_next( self.this)
 8660|         else:
```

### only_rewrite example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/expression/unary.py:198
message: Use `False` instead of `False and ...`
```
  196| 
  197| # Regression tests for https://github.com/astral-sh/ruff/issues/19226
  198| if '' and (not #
  199| 0):
  200|     pass
```

## ruff :: PLR0206
reference: pylint | only ruff: 1 | only reference: 7 | packages: 1
top messages: [only_reference] Cannot have defined parameters for properties ×7 || [only_rewrite] Cannot have defined parameters for properties ×1

### only_rewrite example — scikit-learn scikit_learn-1.9.1/sklearn/utils/deprecation.py:108
message: Cannot have defined parameters for properties
```
  106|         @property
  107|         @functools.wraps(prop.fget)
  108|         def wrapped(*args, **kwargs):
  109|             warnings.warn(msg, category=FutureWarning)
  110|             return prop.fget(*args, **kwargs)
```

### only_reference example — scikit-learn scikit_learn-1.9.1/sklearn/tests/test_metaestimators.py:112
message: Cannot have defined parameters for properties
```
  110| 
  111|         @hides
  112|         def inverse_transform(self, X, *args, **kwargs):
  113|             self._check_fit()
  114|             return X
```

## ruff :: F402
reference: flake8 | only ruff: 1 | only reference: 6 | packages: 6
top messages: [only_reference] import 'header' from line 30 shadowed by loop variable ×2 || [only_rewrite] Import `token` from line 3 shadowed by loop variable ×1 || [only_reference] import 'e' from line 28 shadowed by loop variable ×1 || [only_reference] import 'j' from line 5 shadowed by loop variable ×1

### only_rewrite example — asttokens asttokens-3.0.2/tests/test_asttokens.py:46
message: Import `token` from line 3 shadowed by loop variable
```
   44|       def tokens_iter():
   45|         # force nonlocal into scope
   46|         for token in asttokens.util.generate_tokens(source):
   47|           yield token
   48|         self.was_called = True
```

### only_reference example — httplib2 httplib2-0.32.0/httplib2/__init__.py:451
message: import 'header' from line 30 shadowed by loop variable
```
  449|             if vary:
  450|                 vary_headers = vary.lower().replace(" ", "").split(",")
  451|                 for header in vary_headers:
  452|                     key = "-varied-%s" % header
  453|                     try:
```

### only_reference example — more-itertools more_itertools-11.2.0/more_itertools/more.py:4541
message: import 'e' from line 28 shadowed by loop variable
```
 4539|     try:
 4540|         i = 0
 4541|         for e in element:
 4542|             i = pool.index(e, i)
 4543|             occupations[i] += 1
```

### only_reference example — mpmath mpmath-1.4.1/mpmath/tests/test_linalg.py:307
message: import 'j' from line 5 shadowed by loop variable
```
  305|             flg = False
  306|             dtype = 'complex'
  307|             for j in range(n):
  308|                 for i in range(m):
  309|                     val = nint(lowlimit + (uplimit-lowlimit)*rand())
```

## ruff :: B031
reference: flake8 | only ruff: 0 | only reference: 7 | packages: 2
top messages: [only_reference] Using the generator returned from `itertools.groupby()` more than once will do nothing on  ×7

### only_reference example — fsspec fsspec-2026.9.0/fsspec/caching.py:196
message: Using the generator returned from `itertools.groupby()` more than once will do nothing on the second usage. Save the result to a list, if the result is needed m
```
  194|             _blocks = tuple(map(itemgetter(1), _blocks))
  195|             # Compute start of first block
  196|             sstart = _blocks[0] * self.blocksize
  197|             # Compute the end of the last block. Last block may not be full size.
  198|             send = min(_blocks[-1] * self.blocksize + self.blocksize, self.size)
```

### only_reference example — networkx networkx-3.7/networkx/generators/tests/test_atlas.py:70
message: Using the generator returned from `itertools.groupby()` more than once will do nothing on the second usage. Save the result to a list, if the result is needed m
```
   68|         for n, group in groupby(self.GAG, key=nx.number_of_nodes):
   69|             for m, group in groupby(group, key=nx.number_of_edges):
   70|                 for G1, G2 in pairwise(group):
   71|                     if (G1.name, G2.name) in exceptions:
   72|                         continue
```

## ruff :: PLE0307
reference: pylint | only ruff: 1 | only reference: 6 | packages: 5
top messages: [only_reference] __str__ does not return str ×6 || [only_rewrite] `__str__` does not return `str` ×1

### only_rewrite example — ipython ipython-9.17.1/tests/test_pretty.py:193
message: `__str__` does not return `str`
```
  191| class BadException(Exception):
  192|     def __str__(self):
  193|         return -1
  194| 
  195| 
```

### only_reference example — ipython ipython-9.17.1/tests/test_pretty.py:192
message: __str__ does not return str
```
  190| 
  191| class BadException(Exception):
  192|     def __str__(self):
  193|         return -1
  194| 
```

### only_reference example — pexpect pexpect-4.9.0/pexpect/screen.py:125
message: __str__ does not return str
```
  123|         __unicode__ = _unicode
  124| 
  125|         def __str__(self):
  126|             '''This returns a printable representation of the screen. The end of
  127|             each screen line is terminated by a newline. '''
```

### only_reference example — pytz pytz-2026.5/pytz/tzinfo.py:75
message: __str__ does not return str
```
   73|     zone = None
   74| 
   75|     def __str__(self):
   76|         return self.zone
   77| 
```

## ruff :: B019
reference: flake8 | only ruff: 0 | only reference: 6 | packages: 4
top messages: [only_reference] Use of `functools.lru_cache`, `functools.cache` or `async_lru.alru_cache` on methods can l ×6

### only_reference example — anyio anyio-4.15.1/tests/test_functools.py:332
message: Use of `functools.lru_cache`, `functools.cache` or `async_lru.alru_cache` on methods can lead to memory leaks. The cache may retain instance references, prevent
```
  330|     async def test_cached_instance_method(self) -> None:
  331|         class Foo:
  332|             @lru_cache
  333|             async def instance_method(self, x: int) -> int:
  334|                 return x
```

### only_reference example — importlib-metadata importlib_metadata-9.0.1/importlib_metadata/__init__.py:840
message: Use of `functools.lru_cache`, `functools.cache` or `async_lru.alru_cache` on methods can lead to memory leaks. The cache may retain instance references, prevent
```
  838| 
  839|     @_clear_after_fork  # type: ignore[misc]
  840|     @functools.lru_cache
  841|     def __new__(cls, root):
  842|         return super().__new__(cls)
```

### only_reference example — matplotlib matplotlib-3.11.2/lib/matplotlib/texmanager.py:109
message: Use of `functools.lru_cache`, `functools.cache` or `async_lru.alru_cache` on methods can lead to memory leaks. The cache may retain instance references, prevent
```
  107|     }
  108| 
  109|     @functools.lru_cache  # Always return the same instance.
  110|     def __new__(cls):
  111|         cls._cache_dir.mkdir(parents=True, exist_ok=True)
```

## ruff :: PLE0101
reference: pylint | only ruff: 3 | only reference: 3 | packages: 3
top messages: [only_rewrite] Explicit return in `__init__` ×3 || [only_reference] Explicit return in __init__ ×3

### only_rewrite example — alembic alembic-1.20.0/alembic/ddl/impl.py:81
message: Explicit return in `__init__`
```
   79|         if "__dialect__" in dict_:
   80|             _impls[dict_["__dialect__"]] = cls  # type: ignore[assignment]
   81|         return newtype
   82| 
   83| 
```

### only_rewrite example — pyzmq pyzmq-27.2.0/zmq/asyncio.py:192
message: Explicit return in `__init__`
```
  190|     def __init__(self, selector: selectors.BaseSelector | None = None) -> None:
  191|         _deprecated()
  192|         return super().__init__(selector)
  193| 
  194| 
```

### only_rewrite example — scipy scipy-1.18.1/scipy/stats/_distribution_infrastructure.py:4455
message: Explicit return in `__init__`
```
 4453| 
 4454|     def __init__(self, X, /, *args, lb=-np.inf, ub=np.inf, **kwargs):
 4455|         return super().__init__(X, *args, lb=lb, ub=ub, **kwargs)
 4456| 
 4457|     def _process_parameters(self, lb=None, ub=None, **params):
```

### only_reference example — alembic alembic-1.20.0/alembic/ddl/impl.py:72
message: Explicit return in __init__
```
   70| 
   71| class ImplMeta(type):
   72|     def __init__(
   73|         cls,
   74|         classname: str,
```

### only_reference example — pyzmq pyzmq-27.2.0/zmq/asyncio.py:190
message: Explicit return in __init__
```
  188|     """
  189| 
  190|     def __init__(self, selector: selectors.BaseSelector | None = None) -> None:
  191|         _deprecated()
  192|         return super().__init__(selector)
```

### only_reference example — scipy scipy-1.18.1/scipy/stats/_distribution_infrastructure.py:4454
message: Explicit return in __init__
```
 4452|                           _Parameterization(_ub_param)]
 4453| 
 4454|     def __init__(self, X, /, *args, lb=-np.inf, ub=np.inf, **kwargs):
 4455|         return super().__init__(X, *args, lb=lb, ub=ub, **kwargs)
 4456| 
```

## ruff :: B010
reference: flake8 | only ruff: 4 | only reference: 2 | packages: 4
top messages: [only_rewrite] Do not call `setattr` with a constant attribute value. It is not any safer than normal pro ×4 || [only_reference] Do not call setattr with a constant attribute value, it is not any safer than normal prope ×2

### only_rewrite example — asttokens asttokens-3.0.2/asttokens/util.py:466
message: Do not call `setattr` with a constant attribute value. It is not any safer than normal property access.
```
  464|     for part in joinedstr.values:
  465|       # The ast positions of the FormattedValues/Constant nodes span the full f-string, which is weird.
  466|       setattr(part, '_broken_positions', True)  # use setattr for mypy
  467| 
  468|       if isinstance(part, ast.FormattedValue):
```

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/rust.py:258
message: Do not call `setattr` with a constant attribute value. It is not any safer than normal property access.
```
  256|         self._assumptions = expr._assumptions
  257|         if self.explicit:
  258|             setattr(self, 'precedence', PRECEDENCE["Func"] + 10)
  259| 
  260|     @property
```

### only_reference example — sqlparse sqlparse-0.6.0/sqlparse/sql.py:169
message: Do not call setattr with a constant attribute value, it is not any safer than normal property access.
```
  167|     def __init__(self, tokens=None):
  168|         self.tokens = tokens or []
  169|         [setattr(token, 'parent', self) for token in self.tokens]
  170|         super().__init__(None, ''.join(token.value for token in self.tokens))
  171|         self.is_group = True
```

### only_reference example — scikit-learn scikit_learn-1.9.1/sklearn/utils/_repr_html/base.py:95
message: Do not call setattr with a constant attribute value, it is not any safer than normal property access.
```
   93|     @_doc_link_template.setter
   94|     def _doc_link_template(self, value):
   95|         setattr(self, "__doc_link_template", value)
   96| 
   97|     def _get_doc_link(self):
```

## ruff :: N812
reference: flake8 | only ruff: 6 | only reference: 0 | packages: 3
top messages: [only_rewrite] Lowercase `mpz` imported as non-lowercase `GMPYInteger` ×2 || [only_rewrite] Lowercase `specializer` imported as non-lowercase `cffSpecializer` ×1 || [only_rewrite] Lowercase `errors` imported as non-lowercase `varLibErrors` ×1 || [only_rewrite] Lowercase `deque` imported as non-lowercase `Deque` ×1

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/ttLib/scaleUpem.py:11
message: Lowercase `specializer` imported as non-lowercase `cffSpecializer`
```
    9| import fontTools.ttLib.tables.otTables as otTables
   10| from fontTools.cffLib import VarStoreData
   11| import fontTools.cffLib.specializer as cffSpecializer
   12| from fontTools.varLib import builder  # for VarData.calculateNumShorts
   13| from fontTools.varLib.multiVarStore import OnlineMultiVarStoreBuilder
```

### only_rewrite example — executing executing-2.3.0/tests/samples/utils.py:26
message: Lowercase `deque` imported as non-lowercase `Deque`
```
   24|     from typing import Deque
   25| except ImportError:
   26|     from collections import deque as Deque
   27| 
   28| try:
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/tests/test_rootoftools.py:6
message: Lowercase `_pure_key_dict` imported as non-lowercase `D`
```
    4| import sympy.polys.rootoftools as rootoftools
    5| from sympy.polys.rootoftools import (rootof, RootOf, CRootOf, RootSum,
    6|     _pure_key_dict as D)
    7| 
    8| from sympy.polys.polyerrors import (
```

## ruff :: PLW0211
reference: pylint | only ruff: 5 | only reference: 1 | packages: 4
top messages: [only_rewrite] First argument of a static method should not be named `self` ×5 || [only_reference] Static method with 'cls' as first argument ×1

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/misc/textTools.py:19
message: First argument of a static method should not be named `self`
```
   17|         return blob
   18| 
   19|     def __new__(self, content):
   20|         return str.__new__(self, self.transcode(content))
   21| 
```

### only_rewrite example — ipython ipython-9.17.1/tests/test_guarded_eval.py:329
message: First argument of a static method should not be named `self`
```
  327| 
  328| class InitReturnsFrozenset:
  329|     def __new__(self) -> frozenset:  # type:ignore[misc]
  330|         return frozenset()
  331| 
```

### only_rewrite example — sympy sympy-1.14.0/sympy/tensor/array/sparse_ndim_array.py:13
message: First argument of a static method should not be named `self`
```
   11| class SparseNDimArray(NDimArray):
   12| 
   13|     def __new__(self, *args, **kwargs):
   14|         return ImmutableSparseNDimArray(*args, **kwargs)
   15| 
```

### only_reference example — sqlalchemy sqlalchemy-2.1.4/test/ext/test_extendedattr.py:163
message: Static method with 'cls' as first argument
```
  161|             # This proves that a staticmethod will work here; don't
  162|             # flatten this back to a class assignment!
  163|             def __sa_instrumentation_manager__(cls):
  164|                 return MyTypesManager(cls)
  165| 
```

## ruff :: PLE1205
reference: pylint | only ruff: 0 | only reference: 6 | packages: 2
top messages: [only_reference] Too many arguments for logging format string ×6

### only_reference example — litellm litellm-1.105.0/litellm/proxy/hooks/parallel_request_limiter.py:800
message: Too many arguments for logging format string
```
  798|             return _user_id_rate_limits.model_dump()
  799|         except Exception as e:
  800|             verbose_proxy_logger.debug("Parallel Request Limiter: Error getting user object", str(e))
  801|             return None
  802| 
```

### only_reference example — poetry-core poetry_core-2.5.0/src/poetry/core/_vendor/lark/lark.py:469
message: Too many arguments for logging format string
```
  467|                     self.save(f, _LOAD_ALLOWED_OPTIONS)
  468|             except IOError as e:
  469|                 logger.exception("Failed to save Lark to cache: %r.", cache_fn, e)
  470| 
  471|     if __doc__:
```

## ruff :: C417
reference: flake8 | only ruff: 0 | only reference: 6 | packages: 2
top messages: [only_reference] Unnecessary use of map - use a list comprehension instead. ×5 || [only_reference] Unnecessary use of map - use a generator expression instead. ×1

### only_reference example — six six-1.17.0/test_six.py:231
message: Unnecessary use of map - use a generator expression instead.
```
  229| def test_map():
  230|     from six.moves import map
  231|     assert six.advance_iterator(map(lambda x: x + 1, range(2))) == 1
  232| 
  233| 
```

### only_reference example — scipy scipy-1.18.1/scipy/interpolate/_fitpack_impl.py:313
message: Unnecessary use of map - use a list comprehension instead.
```
  311|         parametric = False
  312|     if parametric:
  313|         return list(map(lambda c, x=x, t=t, k=k, der=der:
  314|                         splev(x, [t, c, k], der, ext), c))
  315|     else:
```
