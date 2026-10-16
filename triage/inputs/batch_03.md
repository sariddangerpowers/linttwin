
## ruff :: B015
reference: flake8 | only ruff: 269 | only reference: 0 | packages: 17
top messages: [only_rewrite] Pointless comparison. Did you mean to assign a value? Otherwise, prepend `assert` or remov ×269

### only_rewrite example — attrs attrs-26.1.0/tests/test_next_gen.py:79
message: Pointless comparison. Did you mean to assign a value? Otherwise, prepend `assert` or remove it.
```
   77|         """
   78|         with pytest.raises(TypeError):
   79|             C("1", 2) < C("2", 3)
   80| 
   81|         @attrs.define(order=True)
```

### only_rewrite example — asyncpg asyncpg-0.32.0/tests/test_record.py:278
message: Pointless comparison. Did you mean to assign a value? Otherwise, prepend `assert` or remove it.
```
  276|         with self.assertRaisesRegex(
  277|                 TypeError, "unorderable|'<' not supported"):
  278|             r1 < r8
  279| 
  280|         self.assertEqual(
```

### only_rewrite example — cffi cffi-2.1.1/src/c/test_c.py:2449
message: Pointless comparison. Did you mean to assign a value? Otherwise, prepend `assert` or remove it.
```
 2447|     assert (q != p) is True
 2448|     if strict_compare:
 2449|         with pytest.raises(TypeError): p < q
 2450|         with pytest.raises(TypeError): p <= q
 2451|         with pytest.raises(TypeError): q < p
```

## ruff :: B028
reference: flake8 | only ruff: 259 | only reference: 0 | packages: 16
top messages: [only_rewrite] No explicit `stacklevel` keyword argument found ×259

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/legacy.py:33
message: No explicit `stacklevel` keyword argument found
```
   31|     """
   32|     if len(kwargs):
   33|         warn(
   34|             f"charset-normalizer disregard arguments '{','.join(list(kwargs.keys()))}' in legacy function detect()"
   35|         )
```

### only_rewrite example — fonttools fonttools-4.66.1/Lib/fontTools/ufoLib/glifLib.py:1607
message: No explicit `stacklevel` keyword argument found
```
 1605|     except TypeError:
 1606|         pen.beginPath()
 1607|         warn(
 1608|             "The beginPath method needs an identifier kwarg. The contour's identifier value has been discarded.",
 1609|             DeprecationWarning,
```

### only_rewrite example — ipython ipython-9.17.1/IPython/core/magics/pylab.py:166
message: No explicit `stacklevel` keyword argument found
```
  164|         print("Populating the interactive namespace from numpy and matplotlib")
  165|         if clobbered:
  166|             warn("pylab import has clobbered these variables: %s"  % clobbered +
  167|             "\n`%matplotlib` prevents importing * from pylab and numpy"
  168|             )
```

## ruff :: PLC0207
reference: pylint | only ruff: 133 | only reference: 92 | packages: 48
top messages: [only_rewrite] String is split more times than necessary ×133 || [only_reference] Use str(candidate).split('+', maxsplit=1)[0] instead ×4 || [only_reference] Use status.split(' ', maxsplit=1)[0] instead ×4 || [only_reference] Use path.split('/files', maxsplit=1)[0] instead ×4

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/noxfile.py:83
message: String is split more times than necessary
```
   81|     simply reset the state and pull.
   82|     """
   83|     expected_directory = git_url.split("/")[-1]
   84| 
   85|     if expected_directory.endswith(".git"):
```

### only_rewrite example — babel babel-2.18.0/babel/plural.py:361
message: String is split more times than necessary
```
  359| 
  360| def tokenize_rule(s: str) -> list[tuple[str, str]]:
  361|     s = s.split('@')[0]
  362|     result: list[tuple[str, str]] = []
  363|     pos = 0
```

### only_rewrite example — azure-core azure_core-1.41.0/tests/specs_sdk/modeltypes/modeltypes/_utils/model_base.py:362
message: String is split more times than necessary
```
  360|     models.update({k: v for k, v in sys.modules[module_end].__dict__.items() if isinstance(v, type)})
  361|     if isinstance(model_name, str):
  362|         model_name = model_name.split(".")[-1]
  363|     if model_name not in models:
  364|         return model_name
```

### only_reference example — aiobotocore aiobotocore-3.9.2/scripts/changelog.py:189
message: Use __doc__.split('\n\n', maxsplit=1)[0] instead
```
  187| 
  188| def _main(argv: list[str] | None = None) -> int:
  189|     parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
  190|     sub = parser.add_subparsers(dest="cmd", required=True)
  191| 
```

### only_reference example — chardet chardet-7.6.0/scripts/tests/test_exclusions.py:292
message: Use _document(tag, count=20).split('. ', maxsplit=1)[0] instead
```
  290|     # reproduced, and the article is mostly its own work.
  291|     borrowed = " ".join(
  292|         _document(tag, count=20).split(". ")[0] + "."
  293|         for tag in ("alpha", "beta", "gamma", "delta")
  294|     )
```

### only_reference example — babel babel-2.18.0/tests/messages/test_checkers.py:87
message: Use _locale.split('_', maxsplit=1)[0] instead
```
   85|         if _locale in ['nn', 'no']:
   86|             _locale = 'nn_NO'
   87|             num_plurals = PLURALS[_locale.split('_')[0]][0]
   88|             plural_expr = PLURALS[_locale.split('_')[0]][1]
   89|         else:
```

## ruff :: PLR0912
reference: pylint | only ruff: 179 | only reference: 33 | packages: 48
top messages: [only_rewrite] Too many branches (13 > 12) ×75 || [only_rewrite] Too many branches (14 > 12) ×16 || [only_rewrite] Too many branches (16 > 12) ×10 || [only_rewrite] Too many branches (15 > 12) ×10

### only_rewrite example — babel babel-2.18.0/babel/dates.py:565
message: Too many branches (13 > 12)
```
  563| 
  564| 
  565| def get_timezone_name(
  566|     dt_or_tzinfo: _DtOrTzinfo = None,
  567|     width: Literal['long', 'short'] = 'long',
```

### only_rewrite example — dill dill-0.4.1/dill/__diff.py:81
message: Too many branches (13 > 12)
```
   79| 
   80| 
   81| def memorise(obj, force=False):
   82|     """
   83|     Adds an object to the memo, and recursively adds all the objects
```

### only_rewrite example — distlib distlib-0.4.3/distlib/scripts.py:185
message: Too many branches (13 > 12)
```
  183|         return result
  184| 
  185|     def _get_shebang(self, encoding, post_interp=b'', options=None):
  186|         enquote = True
  187|         if self.executable:
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/catalog/_create.py:39
message: Too many branches (31/12)
```
   37| 
   38| 
   39| def _create_table(  # noqa: PLR0912,PLR0915
   40|     database: str,
   41|     table: str,
```

### only_reference example — pydantic-settings pydantic_settings-2.15.0/tests/test_docs.py:60
message: Too many branches (17/12)
```
   58| @pytest.mark.skipif(bool(skip_reason), reason=skip_reason or 'not skipping')
   59| @pytest.mark.parametrize('example', list(find_examples(str(DOCS_ROOT), skip=sys.platform == 'win32')), ids=str)
   60| def test_docs_examples(  # noqa C901
   61|     example: CodeExample, eval_example: EvalExample, tmp_path: Path, mocker, docs_test_env
   62| ):
```

### only_reference example — narwhals narwhals-2.27.1/src/narwhals/_interchange/dataframe.py:29
message: Too many branches (18/12)
```
   27| 
   28| 
   29| def map_interchange_dtype_to_narwhals_dtype(  # noqa: C901, PLR0911, PLR0912
   30|     interchange_dtype: tuple[DtypeKind, int, Any, Any],
   31| ) -> DType:
```

## ruff :: PLW2901
reference: pylint | only ruff: 146 | only reference: 63 | packages: 46
top messages: [only_rewrite] `with` statement variable `im` overwritten by assignment target ×15 || [only_rewrite] `for` loop variable `chunk` overwritten by assignment target ×13 || [only_rewrite] Outer `with` statement variable `conn` overwritten by inner `with` statement target ×11 || [only_rewrite] `with` statement variable `match` overwritten by assignment target ×10

### only_rewrite example — anyio anyio-4.15.1/tests/test_taskgroups.py:1576
message: Outer `with` statement variable `tg` overwritten by inner `with` statement target
```
 1574|         tg.start_soon(set_event)
 1575| 
 1576|         async with create_task_group() as tg:
 1577|             tg.start_soon(never_cancel_task)
 1578|             tg.cancel_scope.cancel()
```

### only_rewrite example — click click-8.5.0/src/click/shell_completion.py:727
message: `with` statement variable `ctx` overwritten by assignment target
```
  725|                         name, args, parent=ctx, resilient_parsing=True
  726|                     ) as sub_ctx:
  727|                         ctx = sub_ctx
  728|                         args = ctx._protected_args + ctx.args
  729|                 else:
```

### only_rewrite example — ghapi ghapi-2.1.4/ghapi/core.py:221
message: `with` statement variable `clone_dir` overwritten by assignment target
```
  219|         token = self.headers['Authorization'].split('token ')[1]
  220|         _run_subp(['git', 'clone', f'https://{token}@gist.github.com/{gist.id}.git', clone_dir])
  221|         clone_dir, img_paths = Path(clone_dir), L(img_paths).map(Path)
  222|         for o in img_paths: shutil.copy2(o, clone_dir/o.name)
  223|         _run_subp(['git', '-C', clone_dir, 'add', '.'])
```

### only_reference example — attrs attrs-26.1.0/src/attr/_make.py:333
message: Redefining 'a' from loop (line 329)
```
  331|                 continue
  332| 
  333|             a = a.evolve(inherited=True)  # noqa: PLW2901
  334|             base_attrs.append(a)
  335|             base_attr_map[a.name] = base_cls
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/element.py:2709
message: Redefining 'element' from loop (line 2707)
```
 2707|         for event, element in self._event_stream(iterator):
 2708|             if event in (Tag.START_ELEMENT_EVENT, Tag.EMPTY_ELEMENT_EVENT):
 2709|                 element = cast(Tag, element)
 2710|                 piece = element._format_tag(eventual_encoding, formatter, opening=True)
 2711|             elif event is Tag.END_ELEMENT_EVENT:
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/neptune/_gremlin_parser.py:74
message: Redefining 'k' from loop (line 71)
```
   72|             # If the key is a Vertex or an Edge do special processing
   73|             if isinstance(k, (gremlin.Vertex, gremlin.Edge)):
   74|                 k = k.id  # noqa: PLW2901
   75| 
   76|             # If the value is a list do special processing to make it a scalar if the list is of length 1
```

## ruff :: B904
reference: flake8 | only ruff: 190 | only reference: 18 | packages: 38
top messages: [only_rewrite] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from N ×190 || [only_reference] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from N ×18

### only_rewrite example — backoff backoff-2.2.1/backoff/_async.py:169
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
```
  167|                 except StopIteration:
  168|                     await _call_handlers(on_giveup, **details, exception=e)
  169|                     raise e
  170| 
  171|                 await _call_handlers(on_backoff, **details, wait=seconds,
```

### only_rewrite example — distlib distlib-0.4.3/distlib/compat.py:1023
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
```
 1021|                 v = ValueError('Cannot resolve %r: %s' % (s, e))
 1022|                 v.__cause__, v.__traceback__ = e, tb
 1023|                 raise v
 1024| 
 1025|         def ext_convert(self, value):
```

### only_rewrite example — azure-core azure_core-1.41.0/azure/core/exceptions.py:103
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
```
  101|     except AttributeError:  # Python 2
  102|         error.__traceback__ = exc_traceback
  103|         raise error  # pylint: disable=raise-missing-from
  104| 
  105| 
```

### only_reference example — email-validator email_validator-2.3.0/email_validator/deliverability.py:90
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling.  See https
```
   88| 
   89|                 if not any(is_global_addr(r.address) for r in response):
   90|                     raise dns.resolver.NoAnswer  # fall back to AAAA
   91| 
   92|                 deliverability_info["mx"] = [(0, domain)]
```

### only_reference example — exceptiongroup exceptiongroup-1.3.1/tests/test_exceptions.py:703
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling.  See https
```
  701|             except EG as nested:
  702|                 try:
  703|                     raise ValueError(1)
  704|                 except ValueError as ve:
  705|                     raise EG("eg", [ve, nested])
```

### only_reference example — gitpython gitpython-3.2.0/git/objects/submodule/base.py:886
message: Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling.  See https
```
  884|                             or os.listdir(checkout_module_abspath)
  885|                         ):
  886|                             raise OSError(
  887|                                 "Module directory at %r does already exist and is non-empty" % checkout_module_abspath
  888|                             )
```

## ruff :: PLR1714
reference: pylint | only ruff: 115 | only reference: 73 | packages: 55
top messages: [only_rewrite] Consider merging multiple comparisons. Use a `set` if the elements are hashable. ×26 || [only_rewrite] Consider merging multiple comparisons. ×10 || [only_reference] Consider merging these comparisons with 'in' by using 'axis in (-1, a.ndim - 1)'. Use a se ×8 || [only_rewrite] Consider merging multiple comparisons: `cp in {0, 0xFFFD}`. ×5

### only_rewrite example — cloudpickle cloudpickle-3.1.2/cloudpickle/cloudpickle.py:223
message: Consider merging multiple comparisons: `module_name in {"__main__", "__mp_main__"}`.
```
  221|         # sys.modules
  222|         if (
  223|             module_name == "__main__"
  224|             or module_name == "__mp_main__"
  225|             or module is None
```

### only_rewrite example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/md.py:375
message: Consider merging multiple comparisons: `character not in {"\x1a", "\ufeff"}`.
```
  373| 
  374|         if (
  375|             not info.printable
  376|             and not info.space
  377|             and character != "\x1a"
```

### only_rewrite example — google-api-python-client google_api_python_client-2.201.0/googleapiclient/mimeparse.py:99
message: Consider merging multiple comparisons: `type in (target_type, "*")`. Use a `set` if the elements are hashable.
```
   97|     (target_type, target_subtype, target_params) = parse_media_range(mime_type)
   98|     for type, subtype, params in parsed_ranges:
   99|         type_match = type == target_type or type == "*" or target_type == "*"
  100|         subtype_match = (
  101|             subtype == target_subtype or subtype == "*" or target_subtype == "*"
```

### only_reference example — distlib distlib-0.4.3/distlib/util.py:1868
message: Consider merging these comparisons with 'in' by using 'repository not in (result['server'], result['repository'])'. Use a set instead if elements are hashable.
```
 1866|                         if (server == 'pypi' and repository in (self.DEFAULT_REPOSITORY, 'pypi')):
 1867|                             result['repository'] = self.DEFAULT_REPOSITORY
 1868|                         elif (result['server'] != repository and result['repository'] != repository):
 1869|                             result = {}
 1870|             elif 'server-login' in sections:
```

### only_reference example — cffi cffi-2.1.1/testing/embedding/test_basic.py:50
message: Consider merging these comparisons with 'in' by using 'sys.platform in ('win32', 'darwin')'. Use a set instead if elements are hashable.
```
   48|         check_lib_python_found(str(embedding_path))
   49|         self._path = embedding_path / meth.__name__
   50|         if sys.platform == "win32" or sys.platform == "darwin":
   51|             self._compiled_modules.clear()   # workaround
   52| 
```

### only_reference example — docutils docutils-0.23/docutils/parsers/rst/tableparser.py:84
message: Consider merging these comparisons with 'in' by using 'self.head_body_sep in (0, len(self.block) - 1)'. Use a set instead if elements are hashable.
```
   82|                     self.head_body_sep = i
   83|                     self.block[i] = line.replace('=', '-')
   84|         if self.head_body_sep == 0 or self.head_body_sep == (len(self.block)
   85|                                                              - 1):
   86|             raise TableMarkupError('The head/body row separator may not be '
```

## ruff :: B014
reference: flake8 | only ruff: 0 | only reference: 187 | packages: 51
top messages: [only_reference] Redundant exception types in `except (ModuleNotFoundError, ImportError):`.  Write `except  ×18 || [only_reference] Redundant exception types in `except (OSError, IOError):`.  Write `except OSError:`, which ×10 || [only_reference] Redundant exception types in `except (FileNotFoundError, OSError):`.  Write `except OSErro ×9 || [only_reference] Redundant exception types in `except (ProcessLookupError, OSError):`.  Write `except OSErr ×6

### only_reference example — charset-normalizer charset_normalizer-3.5.2/src/charset_normalizer/api.py:275
message: Redundant exception types in `except (ModuleNotFoundError, ImportError):`.  Write `except ImportError:`, which catches exactly the same exceptions.
```
  273|         try:
  274|             is_multi_byte_decoder: bool = is_multi_byte_encoding(encoding_iana)
  275|         except (ModuleNotFoundError, ImportError):  # Defensive:
  276|             logger.log(
  277|                 TRACE,
```

### only_reference example — chardet chardet-7.6.0/src/chardet/models/__init__.py:305
message: Redundant exception types in `except (FileNotFoundError, OSError):`.  Write `except OSError:`, which catches exactly the same exceptions.
```
  303|             files.joinpath("models.bin").read_bytes()
  304|         ).digest()
  305|     except (FileNotFoundError, OSError):
  306|         data = b""
  307|         models_digest = b""
```

### only_reference example — dill dill-0.4.1/dill/_dill.py:891
message: Redundant exception types in `except (IOError, FileNotFoundError):`.  Write `except IOError:`, which catches exactly the same exceptions.
```
  889|             else:
  890|                 f = open(name, mode)
  891|         except (IOError, FileNotFoundError):
  892|             err = sys.exc_info()[1]
  893|             raise UnpicklingError(err)
```

## ruff :: SIM401
reference: flake8 | only ruff: 65 | only reference: 119 | packages: 43
top messages: [only_reference] Use 'length = subs.get(self.length, self.length)' instead of an if-block ×9 || [only_reference] Use 'a = rout.get("result", rout['name'])' instead of an if-block ×8 || [only_rewrite] Use `self.stage_info.get("region", None)` instead of an `if` block ×6 || [only_rewrite] Use `response.headers.get(GCS_METADATA_MATDESC_KEY, None)` instead of an `if` block ×4

### only_rewrite example — awswrangler awswrangler-3.17.1/awswrangler/redshift/_utils.py:290
message: Use `_varchar_lengths.get(col_name, varchar_lengths_default)` instead of an `if` block
```
  288|     redshift_types: dict[str, str] = {}
  289|     for col_name, col_type in athena_types.items():
  290|         length: int = _varchar_lengths[col_name] if col_name in _varchar_lengths else varchar_lengths_default
  291|         redshift_types[col_name] = _data_types.athena2redshift(dtype=col_type, varchar_length=length)
  292|     _logger.debug("Converted redshift types: %s", redshift_types)
```

### only_rewrite example — distlib distlib-0.4.3/distlib/compat.py:544
message: Use `self.get(key, default)` instead of an `if` block
```
  542| 
  543|         def get(self, key, default=None):
  544|             return self[key] if key in self else default
  545| 
  546|         def __len__(self):
```

### only_rewrite example — alembic alembic-1.20.0/alembic/testing/fixtures.py:377
message: Use `compare.get("name", column.name)` instead of an `if` block
```
  375|         eq_(
  376|             new_col["name"],
  377|             compare["name"] if "name" in compare else column.name,
  378|         )
  379|         self._compare_type(
```

### only_reference example — authlib authlib-1.8.0/authlib/jose/rfc7516/jwe.py:317
message: Use 'cek = preset.get("cek", None)' instead of an if-block
```
  315|         # step 3: Encrypt the CEK with the recipient's public key
  316|         preset = alg.generate_preset(enc, keys[0])
  317|         if "cek" in preset:
  318|             cek = preset["cek"]
  319|         else:
```

### only_reference example — docker docker-7.2.0/docker/utils/utils.py:147
message: Use 'mode = v.get("mode", "rw")' instead of an if-block
```
  145|             if 'ro' in v:
  146|                 mode = 'ro' if v['ro'] else 'rw'
  147|             elif 'mode' in v:
  148|                 mode = v['mode']
  149|             else:
```

### only_reference example — dill dill-0.4.1/dill/_dill.py:1580
message: Use 'postproc = pickler._postproc.get(id(f), next(iter(pickler._postproc.values()), None))' instead of an if-block
```
 1578|         return
 1579|     if is_dill(pickler, child=True):
 1580|         if id(f) in pickler._postproc:
 1581|             # Already seen. Add to its postprocessing.
 1582|             postproc = pickler._postproc[id(f)]
```

## ruff :: PLE0237
reference: pylint | only ruff: 0 | only reference: 184 | packages: 10
top messages: [only_reference] Assigning to attribute '_shape' not defined in class slots ×13 || [only_reference] Assigning to attribute 'seconds' not defined in class slots ×9 || [only_reference] Assigning to attribute 'nanos' not defined in class slots ×9 || [only_reference] Assigning to attribute '_maint_notifications_pool_handler' not defined in class slots ×5

### only_reference example — google-crc32c google_crc32c-1.9.0/src/google_crc32c/_checksum.py:31
message: Assigning to attribute '_crc' not defined in class slots
```
   29| 
   30|     def __init__(self, initial_value=b""):
   31|         self._crc = 0
   32|         if initial_value != b"":
   33|             self.update(initial_value)
```

### only_reference example — google-api-core google_api_core-2.42.0/google/api_core/datetime_helpers.py:197
message: Assigning to attribute '_nanosecond' not defined in class slots
```
  195|             kw["microsecond"] = nanos // 1000
  196|         inst = datetime.datetime.__new__(cls, *args, **kw)
  197|         inst._nanosecond = nanos or 0
  198|         return inst
  199| 
```

### only_reference example — packaging packaging-26.3/tests/test_requirements.py:836
message: Assigning to attribute 'nonexistent' not defined in class slots
```
  834|     assert not hasattr(r, "__dict__")
  835|     with pytest.raises(AttributeError):
  836|         r.nonexistent = 1  # type: ignore[attr-defined]
  837| 
  838| 
```

## ruff :: PLC0205
reference: pylint | only ruff: 90 | only reference: 90 | packages: 15
top messages: [only_rewrite] Class `__slots__` should be a non-string iterable ×90 || [only_reference] Class __slots__ should be a non-string iterable ×90

### only_rewrite example — click click-8.5.0/tests/test_utils/test__detect_program_name.py:9
message: Class `__slots__` should be a non-string iterable
```
    7| 
    8| class MockMain:
    9|     __slots__ = "__package__"
   10| 
   11|     def __init__(self, package_name):
```

### only_rewrite example — dill dill-0.4.1/dill/tests/test_classdef.py:231
message: Class `__slots__` should be a non-string iterable
```
  229| 
  230| class Y2(object):
  231|   __slots__ = 'y'
  232|   def __init__(self, y):
  233|     self.y = y
```

### only_rewrite example — gitdb gitdb-4.0.12/gitdb/stream.py:560
message: Class `__slots__` should be a non-string iterable
```
  558|     """Simple stream writer which produces a sha whenever you like as it degests
  559|     everything it is supposed to write"""
  560|     __slots__ = "sha1"
  561| 
  562|     def __init__(self):
```

### only_reference example — click click-8.5.0/tests/test_utils/test__detect_program_name.py:8
message: Class __slots__ should be a non-string iterable
```
    6| 
    7| 
    8| class MockMain:
    9|     __slots__ = "__package__"
   10| 
```

### only_reference example — dill dill-0.4.1/dill/tests/test_classdef.py:230
message: Class __slots__ should be a non-string iterable
```
  228| y = Y(value)
  229| 
  230| class Y2(object):
  231|   __slots__ = 'y'
  232|   def __init__(self, y):
```

### only_reference example — gitdb gitdb-4.0.12/gitdb/stream.py:556
message: Class __slots__ should be a non-string iterable
```
  554| #{ W Streams
  555| 
  556| class Sha1Writer:
  557| 
  558|     """Simple stream writer which produces a sha whenever you like as it degests
```

## ruff :: SIM110
reference: flake8 | only ruff: 91 | only reference: 78 | packages: 60
top messages: [only_rewrite] Use `return all(isinstance(value, numberTypes) for value in values)` instead of `for` loop ×3 || [only_rewrite] Use `return all(fontInfoWOFFMetadataTextValue(text) for text in value["text"])` instead of ×3 || [only_reference] Use 'return any(item[0].lower() == k.lower() and item[1] == v for (k, v) in self.__iter__( ×2 || [only_reference] Use 'return any('location' not in val.serialization for (member, val) in shape.members.ite ×2

### only_rewrite example — asn1crypto asn1crypto-1.5.1/asn1crypto/x509.py:965
message: Use `return all(other[index] == self_rdn for index, self_rdn in enumerate(self))` instead of `for` loop
```
  963|             return False
  964| 
  965|         for index, self_rdn in enumerate(self):
  966|             if other[index] != self_rdn:
  967|                 return False
```

### only_rewrite example — boto3 boto3-1.43.113/boto3/resources/response.py:26
message: Use `return all(element is not None for element in iterable)` instead of `for` loop
```
   24|     against None, so 0 and False are allowable values.
   25|     """
   26|     for element in iterable:
   27|         if element is None:
   28|             return False
```

### only_rewrite example — distlib distlib-0.4.3/distlib/metadata.py:534
message: Use `return all(scheme.is_valid_matcher(v.split(';')[0]) for v in value)` instead of `for` loop
```
  532| 
  533|         def are_valid_constraints(value):
  534|             for v in value:
  535|                 if not scheme.is_valid_matcher(v.split(';')[0]):
  536|                     return False
```

### only_reference example — boto3 boto3-1.43.113/boto3/docs/method.py:73
message: Use 'return any(identifier.path and '[]' in identifier.path for identifier in resource.identifiers)'
```
   71| 
   72| def _method_returns_resource_list(resource):
   73|     for identifier in resource.identifiers:
   74|         if identifier.path and '[]' in identifier.path:
   75|             return True
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/filter.py:464
message: Use 'return any(any((x.exclude_everything for x in ruleset)) for ruleset in self.attribute_rules.values())'
```
  462|         if any(x.exclude_everything for x in self.name_rules):
  463|             return True
  464|         for ruleset in self.attribute_rules.values():
  465|             if any(x.exclude_everything for x in ruleset):
  466|                 return True
```

### only_reference example — aiobotocore aiobotocore-3.9.2/aiobotocore/_helpers.py:12
message: Use 'return any(await resolve_awaitable(item) for item in items)'
```
   10| 
   11| async def async_any(items):
   12|     for item in items:
   13|         if await resolve_awaitable(item):
   14|             return True
```

## ruff :: SIM102
reference: flake8 | only ruff: 37 | only reference: 131 | packages: 54
top messages: [only_reference] Use a single if-statement instead of nested if-statements ×131 || [only_rewrite] Use a single `if` statement instead of nested `if` statements ×37

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/footnotes.py:163
message: Use a single `if` statement instead of nested `if` statements
```
  161|         def finder(element):
  162|             for child in element:
  163|                 if child.text:
  164|                     if child.text.find(self.getConfig("PLACE_MARKER")) > -1:
  165|                         return child, element, True
```

### only_rewrite example — executing executing-2.3.0/tests/test_main.py:1179
message: Use a single `if` statement instead of nested `if` statements
```
 1177|         lineno = None
 1178|         for inst_index, inst in enumerate(instructions):
 1179|             if hasattr(self, "start_time"):
 1180|                 if time.time() - self.start_time > 45 * 60:
 1181|                     # Avoid travis time limit of 50 minutes
```

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/rootisolation.py:1173
message: Use a single `if` statement instead of nested `if` statements
```
 1171|                 Q.append(cls)
 1172| 
 1173|         if 0 in indices:
 1174|             if indices[0] % 2 == 1:
 1175|                 f1_sgn = -f1_sgn
```

### only_reference example — awswrangler awswrangler-3.17.1/awswrangler/athena/_cache.py:215
message: Use a single if-statement instead of nested if-statements
```
  213|                         query_execution_payload=query_info,
  214|                     )
  215|         elif statement_type == "DML" and not query_info["Query"].startswith("INSERT"):
  216|             if _compare_query_string(sql=comparable_sql, other=query_info["Query"]):
  217|                 return _CacheInfo(
```

### only_reference example — babel babel-2.18.0/babel/messages/catalog.py:586
message: Use a single if-statement instead of nested if-statements
```
  584|             elif name == 'pot-creation-date':
  585|                 self.creation_date = _parse_datetime_header(value)
  586|             elif name == 'po-revision-date':
  587|                 # Keep the value if it's not the default one
  588|                 if 'YEAR' not in value:
```

### only_reference example — gitdb gitdb-4.0.12/gitdb/util.py:382
message: Use a single if-statement instead of nested if-statements
```
  380|         if self._write and successful:
  381|             # on windows, rename does not silently overwrite the existing one
  382|             if sys.platform == "win32":
  383|                 if isfile(self._filepath):
  384|                     remove(self._filepath)
```

## ruff :: SIM201
reference: flake8 | only ruff: 24 | only reference: 139 | packages: 42
top messages: [only_reference] Use 'self != other' instead of 'not self == other' ×113 || [only_rewrite] Use `hm != hlastm` instead of `not hm == hlastm` ×3 || [only_reference] Use 'self.__class__ != other.__class__' instead of 'not self.__class__ == other.__class__' ×2 || [only_reference] Use 'len(w) != m' instead of 'not len(w) == m' ×2

### only_rewrite example — awscli awscli-1.46.1/awscli/customizations/utils.py:133
message: Use `key_group != current_group` instead of `not key_group == current_group`
```
  131|         if current_group is None:
  132|             current_group = key_group
  133|         elif not key_group == current_group:
  134|             raise ValueError('The key "%s" cannot be specified when one '
  135|                              'of the following keys are also specified: '
```

### only_rewrite example — asttokens asttokens-3.0.2/asttokens/mark_tokens.py:473
message: Use `first_token.string != 'async'` instead of `not first_token.string == 'async'`
```
  471|     self, node: AstNode, first_token: util.Token, last_token: util.Token
  472|   ) -> Tuple[util.Token, util.Token]:
  473|     if not first_token.string == 'async':
  474|       first_token = self._code.prev_token(first_token)
  475|     return (first_token, last_token)
```

### only_rewrite example — markdown markdown-3.11.1/markdown/extensions/md_in_html.py:293
message: Use `self.rawdata[i:i + 9] != '<![CDATA['` instead of `not self.rawdata[i:i + 9] == '<![CDATA['`
```
  291|     def parse_html_declaration(self, i: int) -> int:
  292|         if self.at_line_start() or self.intail or self.mdstack:
  293|             if self.rawdata[i:i+3] == '<![' and not self.rawdata[i:i+9] == '<![CDATA[':
  294|                 # We have encountered the bug in #1534 (Python bug `gh-77057`).
  295|                 # Provide an override until we drop support for Python < 3.13.
```

### only_reference example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:1726
message: Use 'self != other' instead of 'not self == other'
```
 1724| 
 1725|     def __ne__(self, other):
 1726|         return not self == other
 1727| 
 1728|     def __eq__(self, other):
```

### only_reference example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/element.py:2625
message: Use 'self != other' instead of 'not self == other'
```
 2623|         """Returns true iff this Tag is not identical to `other`,
 2624|         as defined in __eq__."""
 2625|         return not self == other
 2626| 
 2627|     def __repr__(self) -> str:
```

### only_reference example — distlib distlib-0.4.3/distlib/compat.py:873
message: Use 'self != other' instead of 'not self == other'
```
  871| 
  872|         def __ne__(self, other):
  873|             return not self == other
  874| 
  875|         # -- the following methods are only used in Python 2.7 --
```

## ruff :: E722
reference: flake8 | only ruff: 9 | only reference: 152 | packages: 32
top messages: [only_reference] do not use bare 'except' ×152 || [only_rewrite] Do not use bare `except` ×9

### only_rewrite example — executing executing-2.3.0/tests/samples/bird.py:963
message: Do not use bare `except`
```
  961|             try:
  962|                 length = len(val)
  963|             except:
  964|                 pass
  965|             else:
```

### only_reference example — gitdb gitdb-4.0.12/gitdb/db/loose.py:207
message: do not use bare 'except'
```
  205|                     writer.close()
  206|             # END assure target stream is closed
  207|         except:
  208|             if tmp_path:
  209|                 remove(tmp_path)
```

### only_reference example — alembic alembic-1.20.0/alembic/util/messaging.py:59
message: do not use bare 'except'
```
   57|     try:
   58|         yield
   59|     except:
   60|         if not quiet:
   61|             write_outstream(sys.stdout, "  FAILED\n")
```

### only_reference example — google-api-python-client google_api_python_client-2.201.0/googleapiclient/http.py:1167
message: do not use bare 'except'
```
 1165|                     self.resumable_uri, method="PUT", body=data, headers=headers
 1166|                 )
 1167|             except:
 1168|                 self._in_error_state = True
 1169|                 raise
```

## ruff :: B023
reference: flake8 | only ruff: 156 | only reference: 0 | packages: 14
top messages: [only_rewrite] Function definition does not bind loop variable `q` ×15 || [only_rewrite] Function definition does not bind loop variable `xK` ×12 || [only_rewrite] Function definition does not bind loop variable `not_basis` ×10 || [only_rewrite] Function definition does not bind loop variable `wrong_delta` ×10

### only_rewrite example — coverage coverage-7.16.2/tests/test_context.py:84
message: Function definition does not bind loop variable `combined`
```
   82|             def assert_combined_lines(filename: str, context: str, lines: list[TLineNo]) -> None:
   83|                 # pylint: disable=cell-var-from-loop
   84|                 combined.set_query_context(context)
   85|                 assert combined.lines(filename) == lines
   86| 
```

### only_rewrite example — h11 h11-0.16.0/h11/tests/test_connection.py:638
message: Function definition does not bind loop variable `req`
```
  636|         def setup() -> ConnectionPair:
  637|             p = ConnectionPair()
  638|             p.send(CLIENT, req)
  639|             # No switch-related state change stuff yet; the client has to
  640|             # finish the request before that kicks in
```

### only_rewrite example — fonttools fonttools-4.66.1/Tests/varLib/instancer/instancer_test.py:2092
message: Function definition does not bind loop variable `segments`
```
 2090|             def make():
 2091|                 f = ttLib.TTFont(AVAR2_SUBSET_PATH, recalcTimestamp=False)
 2092|                 for tag, seg in segments.items():
 2093|                     f["avar"].segments[tag] = dict(seg)
 2094|                 return f
```

## ruff :: W292
reference: flake8 | only ruff: 153 | only reference: 0 | packages: 2
top messages: [only_rewrite] No newline at end of file ×153

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/recursion.py:3
message: No newline at end of file
```
    1| """ For issue #25 """
    2| class Base(object):
    3|     pass
```

### only_rewrite example — executing .0/tests/small_samples/a9cf2f563ac80ad0066c4ef3ac10fa2f146252db49b3a0a9cb69e0c03e07827b.py:18
message: No newline at end of file
```
   16| def call_errorfunc():
   17|     global _errok, _token, _restart
   18|     del _errok, _token, _restart
```

## ruff :: PLR1730
reference: pylint | only ruff: 144 | only reference: 0 | packages: 37
top messages: [only_rewrite] Replace `if` statement with `max` call ×11 || [only_rewrite] Replace `if` statement with `max_extent = max(max_extent, current_col)` ×10 || [only_rewrite] Replace `if` statement with `start = max(start, 0)` ×4 || [only_rewrite] Replace `if` statement with `self.maxDegree = max(self.maxDegree, dash_count)` ×3

### only_rewrite example — aioitertools aioitertools-0.13.0/aioitertools/builtins.py:267
message: Replace `if` statement with `value = max(value, item)`
```
  265|     else:
  266|         async for item in it:
  267|             if item > value:
  268|                 value = item
  269| 
```

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/formatter.py:129
message: Replace `if` statement with `indent = max(indent, 0)`
```
  127|         indent_str: str
  128|         if isinstance(indent, int):
  129|             if indent < 0:
  130|                 indent = 0
  131|             indent_str = " " * indent
```

### only_rewrite example — google-api-python-client google_api_python_client-2.201.0/googleapiclient/channel.py:305
message: Replace `if` statement with `expiration_ms = max(expiration_ms, 0)`
```
  303|             delta.microseconds / 1000 + (delta.seconds + delta.days * 24 * 3600) * 1000
  304|         )
  305|         if expiration_ms < 0:
  306|             expiration_ms = 0
  307| 
```

## ruff :: F405
reference: flake8 | only ruff: 92 | only reference: 51 | packages: 4
top messages: [only_rewrite] `beta` may be undefined, or defined from star imports ×49 || [only_reference] 'beta' may be undefined, or defined from star imports: .mtrand ×49 || [only_rewrite] `Literal` may be undefined, or defined from star imports ×24 || [only_rewrite] `UserAPIKeyAuth` may be undefined, or defined from star imports ×13

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python3/astroid/module.py:35
message: `XXXError` may be undefined, or defined from star imports
```
   33|             pass
   34|         except (NameError, TypeError):
   35|             raise XXXError()
   36|         except:
   37|             raise
```

### only_rewrite example — litellm litellm-1.105.0/litellm/llms/openai/responses/transformation.py:847
message: `Literal` may be undefined, or defined from star imports
```
  845|         include: list[str] | None = None,
  846|         limit: int = 20,
  847|         order: Literal["asc", "desc"] = "desc",
  848|     ) -> tuple[str, dict]:
  849|         encoded_response_id: Final = encode_url_path_segment(response_id, field_name="response_id")
```

### only_rewrite example — numpy numpy-2.5.4/numpy/_core/__init__.py:155
message: `memmap` may be undefined, or defined from star imports
```
  153|     "abs", "acos", "acosh", "asin", "asinh", "atan", "atanh", "atan2",
  154|     "bitwise_invert", "bitwise_left_shift", "bitwise_right_shift", "concat",
  155|     "pow", "permute_dims", "memmap", "sctypeDict", "record", "recarray"
  156| ]
  157| __all__ += numeric.__all__
```

### only_reference example — numpy numpy-2.5.4/numpy/_core/__init__.py:161
message: 'memmap' may be undefined, or defined from star imports: .einsumfunc, .fromnumeric, .function_base, .getlimits, .memmap, .numeric, .shape_base
```
  159| __all__ += getlimits.__all__
  160| __all__ += shape_base.__all__
  161| __all__ += einsumfunc.__all__
  162| 
  163| 
```

### only_reference example — scipy scipy-1.18.1/scipy/stats/distributions.py:24
message: 'rv_histogram' may be undefined, or defined from star imports: ._continuous_distns, ._discrete_distns
```
   22| __all__ += _continuous_distns._distn_names
   23| __all__ += ['levy_stable']
   24| __all__ += _discrete_distns._distn_names
```

## ruff :: B007
reference: flake8 | only ruff: 125 | only reference: 14 | packages: 16
top messages: [only_rewrite] Loop control variable `i` not used within loop body ×51 || [only_rewrite] Loop control variable `event` not used within loop body ×24 || [only_rewrite] Loop control variable `chunk` not used within loop body ×12 || [only_reference] Loop control variable 'x' not used within the loop body. If this is intended, start the na ×7

### only_rewrite example — aiobotocore aiobotocore-3.9.2/tests/botocore_tests/unit/test_httpchecksum.py:629
message: Loop control variable `chunk` not used within loop body
```
  627|         wrapper = make_wrapper("duorhq==")
  628|         with pytest.raises(FlexibleChecksumError):
  629|             async for chunk in wrapper:
  630|                 pass
  631| 
```

### only_rewrite example — asttokens asttokens-3.0.2/tests/testdata/python2/astroid/nonregr.py:15
message: Loop control variable `k` not used within loop body
```
   13| 
   14| def toto(value):
   15|     for k, v in value:
   16|         print(v.get('yo'))
   17| 
```

### only_rewrite example — httpcore httpcore-1.0.9/tests/test_models.py:188
message: Loop control variable `chunk` not used within loop body
```
  186|     # Once we've streamed the response, we can't access the stream again.
  187|     with pytest.raises(RuntimeError):
  188|         async for chunk in response.aiter_stream():
  189|             pass  # pragma: nocover
```

### only_reference example — more-itertools more_itertools-11.2.0/more_itertools/more.py:4716
message: Loop control variable 'i' not used within the loop body. If this is intended, start the name with an underscore.
```
 4714| 
 4715|     for item in zip(*iterables, strict=strict):
 4716|         for i, new_item[i] in zip(iterable_positions, item):
 4717|             pass
 4718|         yield tuple(new_item)
```

### only_reference example — ruff ruff-0.17.0/crates/ruff_python_parser/resources/inline/ok/for_in_target_valid_expr.py:1
message: Loop control variable 'd' not used within the loop body. If this is intended, start the name with an underscore.
```
    1| for d[x in y] in target: ...
    2| for (x in y)[0] in iter: ...
    3| for (x in y).attr in iter: ...
```

### only_reference example — black black-26.10.1/tests/data/cases/bracketmatch.py:1
message: Loop control variable 'x' not used within the loop body. If this is intended, start the name with an underscore.
```
    1| for ((x in {}) or {})['a'] in x:
    2|     pass
    3| pem_spam = lambda l, spam = {
```

## ruff :: PLR0022
reference: pylint | only ruff: 0 | only reference: 136 | packages: 2
top messages: [only_reference] Useless option value for 'disable', 'bad-continuation' was removed from pylint, see https: ×136

### only_reference example — fsspec fsspec-2026.9.0/fsspec/implementations/smb.py:17
message: Useless option value for 'disable', 'bad-continuation' was removed from pylint, see https://github.com/pylint-dev/pylint/pull/3571.
```
   15| from ..utils import infer_storage_options
   16| 
   17| # ! pylint: disable=bad-continuation
   18| 
   19| 
```

### only_reference example — google-cloud-aiplatform google_cloud_aiplatform-2.4.0/agentplatform/model_garden/_model_garden.py:15
message: Useless option value for 'disable', 'bad-continuation' was removed from pylint, see https://github.com/pylint-dev/pylint/pull/3571.
```
   13| # limitations under the License.
   14| #
   15| # pylint: disable=bad-continuation, line-too-long, protected-access
   16| """Class for interacting with Model Garden OSS models."""
   17| 
```

## ruff :: PLR1704
reference: pylint | only ruff: 17 | only reference: 101 | packages: 27
top messages: [only_reference] Redefining argument with the local name 'a' ×13 || [only_reference] Redefining argument with the local name 'f' ×13 || [only_reference] Redefining argument with the local name 'x' ×8 || [only_rewrite] Redefining argument with the local name `r_multi_db` ×6

### only_rewrite example — beautifulsoup4 beautifulsoup4-4.15.0/bs4/filter.py:631
message: Redefining argument with the local name `attr_value`
```
  629|         def _match_attribute_value_helper(attr_values: Sequence[Optional[str]]) -> bool:
  630|             for rule in rules:
  631|                 for attr_value in attr_values:
  632|                     if rule.matches_string(attr_value):
  633|                         return True
```

### only_rewrite example — alembic alembic-1.20.0/alembic/util/langhelpers.py:403
message: Redefining argument with the local name `qualifier`
```
  401|             results_by_subgroup: dict[str, PriorityDispatchResult] = {}
  402|             for priority in DispatchPriority:
  403|                 for qualifier in qualifiers:
  404|                     for fn, subgroup in self._registry.get(
  405|                         (target, qualifier, priority), ()
```

### only_rewrite example — fsspec fsspec-2026.9.0/fsspec/spec.py:1725
message: Redefining argument with the local name `prefix`
```
 1723|         def format_bytes(n: int) -> str:
 1724|             """Format bytes as text."""
 1725|             for prefix, k in (
 1726|                 ("P", 2**50),
 1727|                 ("T", 2**40),
```

### only_reference example — asn1crypto asn1crypto-1.5.1/asn1crypto/core.py:341
message: Redefining argument with the local name 'class_'
```
  339|                 if len(explicit) == 2 and isinstance(explicit[1], int_types):
  340|                     explicit = (explicit, )
  341|                 for class_, tag in explicit:
  342|                     invalid_class = None
  343|                     if isinstance(class_, int_types):
```

### only_reference example — click click-8.5.0/src/click/formatting.py:100
message: Redefining argument with the local name 'text'
```
   98| 
   99|     rv = []
  100|     for indent, raw, text in p:
  101|         with wrapper.extra_indent(" " * indent):
  102|             if raw:
```

### only_reference example — distlib distlib-0.4.3/distlib/version.py:112
message: Redefining argument with the local name 's'
```
  110|         if r.constraints:
  111|             # import pdb; pdb.set_trace()
  112|             for op, s in r.constraints:
  113|                 if s.endswith('.*'):
  114|                     if op not in ('==', '!='):
```
