
## ruff :: F632
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Use `==` to compare constant literals ×2

### only_rewrite example — executing .0/tests/small_samples/4851dc1b626a95e97dbe0c53f96099d165b755dd1bd552c6ca771f7bca6d30f5.py:16
message: Use `==` to compare constant literals
```
   14| # 
   15| 
   16| if 1 < 1 > 1 == 1 >= 1 <= 1 != 1 in 1 not in 1 is 1 is not 1:
   17|     pass
```

## ruff :: F602
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Dictionary key `TargetVersion` repeated ×2

### only_rewrite example — executing .0/tests/small_samples/46597f8f896f11c5d7f432236344cc7e5645c2a39836eb6abdd2437c0422f0f4.py:95
message: Dictionary key `TargetVersion` repeated
```
   93| CACHED = 1
   94| PY36_VERSIONS = {TargetVersion.PY36, TargetVersion.PY37, TargetVersion.PY38}
   95| VERSION_TO_FEATURES: Dict[TargetVersion, Set[Feature]] = {TargetVersion.PY27: {*()}, TargetVersion.PY33: {*()}, TargetVersion.PY34: {*()}, TargetVersion.PY35: {*()}, TargetVersion: {Feature.ASYNC_IDENTIFIERS}, TargetVersion: {*()}, TargetVersion: {Feature.UNICODE_LITERALS, Feature.F_STRINGS, Feature
   96| FileMode = Mode
   97| 
```

## ruff :: F823
reference: flake8 | only ruff: 0 | only reference: 2 | packages: 2
top messages: [only_reference] local variable 'match' defined in enclosing scope on line 108 referenced before assignment ×1 || [only_reference] local variable 'match' defined in enclosing scope on line 107 referenced before assignment ×1

### only_reference example — black black-26.10.1/tests/data/cases/pattern_matching_generic.py:29
message: local variable 'match' defined in enclosing scope on line 108 referenced before assignment
```
   27|     match match:
   28|         case case:
   29|             match match:
   30|                 case case:
   31|                     pass
```

### only_reference example — ruff ates/ruff_python_formatter/resources/test/fixtures/black/cases/pattern_matching_generic.py:28
message: local variable 'match' defined in enclosing scope on line 107 referenced before assignment
```
   26|     match match:
   27|         case case:
   28|             match match:
   29|                 case case:
   30|                     pass
```

## ruff :: PLE0011
reference: pylint | only ruff: 0 | only reference: 2 | packages: 1
top messages: [only_reference] Unrecognized file option 'break' ×2

### only_reference example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/trailing_comments.py:7
message: Unrecognized file option 'break'
```
    5| i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)  # ty: ignore This shouldn't break
    6| i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)  # pyright: This shouldn't break
    7| i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)  # pylint: This shouldn't break
    8| i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)  # noqa This shouldn't break
    9| i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)  # nocoverage: This should break
```

## ruff :: PLE1206
reference: pylint | only ruff: 0 | only reference: 2 | packages: 1
top messages: [only_reference] Not enough arguments for logging format string ×2

### only_reference example — snowflake-connector-python snowflake_connector_python-4.8.0/src/snowflake/connector/converter.py:292
message: Not enough arguments for logging format string
```
  290|             return t, fraction_of_nanoseconds
  291|         except OverflowError:
  292|             logger.debug(
  293|                 "OverflowError in converting from epoch time to "
  294|                 "timestamp_ltz: %s(ms). Falling back to use struct_time."
```

## ruff :: PLE1132
reference: pylint | only ruff: 0 | only reference: 2 | packages: 1
top messages: [only_reference] Got multiple values for keyword argument 'max_length' in function call ×2

### only_reference example — transformers transformers-5.19.0/src/transformers/tokenization_utils_base.py:2513
message: Got multiple values for keyword argument 'max_length' in function call
```
 2511|             if not self._in_target_context_manager and hasattr(self, "_switch_to_input_mode"):
 2512|                 self._switch_to_input_mode()
 2513|             encodings = self._encode_plus(
 2514|                 text=text,
 2515|                 text_pair=text_pair,
```

## ruff :: SIM211
reference: flake8 | only ruff: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Use `not ...` instead of `False if ... else True` ×2

### only_rewrite example — sympy sympy-1.14.0/sympy/printing/latex.py:465
message: Use `not ...` instead of `False if ... else True`
```
  463|         # Based off of that in StrPrinter
  464|         dps = prec_to_dps(expr._prec)
  465|         strip = False if self._settings['full_prec'] else True
  466|         low = self._settings["min"] if "min" in self._settings else None
  467|         high = self._settings["max"] if "max" in self._settings else None
```

## ruff :: PLW1509
reference: pylint | only ruff: 0 | only reference: 1 | packages: 1
top messages: [only_reference] Using preexec_fn keyword which may be unsafe in the presence of threads ×1

### only_reference example — langchain langchain-1.4.5/langchain/agents/middleware/_execution.py:35
message: Using preexec_fn keyword which may be unsafe in the presence of threads
```
   33|     start_new_session: bool,
   34| ) -> subprocess.Popen[str]:
   35|     return subprocess.Popen(  # noqa: S603
   36|         list(command),
   37|         stdin=subprocess.PIPE,
```

## ruff :: SIM208
reference: flake8 | only ruff: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Use `something` instead of `not (not something)` ×1

### only_rewrite example — executing .0/tests/small_samples/28dde5e66130457326139e9f4ae62987606de2b6362b073ae3671ad38cf37046.py:1
message: Use `something` instead of `not (not something)`
```
    1| not not something
```

## ruff :: C402
reference: flake8 | only ruff: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unnecessary generator (rewrite as a dict comprehension) ×1

### only_rewrite example — executing executing-2.3.0/tests/samples/bird.py:896
message: Unnecessary generator (rewrite as a dict comprehension)
```
  894|     def names(self):
  895|         # type: () -> List[str]
  896|         rev = dict((v, k) for k, v in self.data.items())
  897|         return [safe_qualname(rev[i]) for i in range(len(rev))]
  898| 
```

## ruff :: SIM107
reference: flake8 | only ruff: 0 | only reference: 1 | packages: 1
top messages: [only_reference] Don't use return in try/except and finally ×1

### only_reference example — prompt-toolkit prompt_toolkit-3.0.53/src/prompt_toolkit/eventloop/async_generator.py:101
message: Don't use return in try/except and finally
```
   99|                 except Full:
  100|                     if quitting:
  101|                         return
  102|                     continue
  103|                 else:
```

## ruff :: PLE2515
reference: pylint | only ruff: 0 | only reference: 1 | packages: 1
top messages: [only_reference] Invalid unescaped character zero-width-space, use "\u200B" instead. ×1

### only_reference example — pip pip-26.2.1/src/pip/_internal/utils/unpacking.py:281
message: Invalid unescaped character zero-width-space, use "\u200B" instead.
```
  279| ) -> None:
  280|     """Fallback for Python without tarfile.data_filter"""
  281|     # NOTE: This function can be removed once pip requires CPython ≥ 3.12.​
  282|     # PEP 706 added tarfile.data_filter, made tarfile extraction operations more secure.
  283|     # This feature is fully supported from CPython 3.12 onward.
```

## ruff :: E401
reference: flake8 | only ruff: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Multiple imports on one line ×1

### only_rewrite example — ruff ruff-0.17.0/crates/ruff_python_parser/resources/inline/ok/import_stmt_terminator.py:1
message: Multiple imports on one line
```
    1| import a, b; import c, d
    2| import a, b
    3| c, d
```

## ruff :: PLC2401
reference: pylint | only ruff: 0 | only reference: 1 | packages: 1
top messages: [only_reference] Argument name "this_is_a_very_long_keyword_argument_asökdhflakjslaslhfdlaffahflahsöfdhasäg ×1

### only_reference example — ruff ruff-0.17.0/crates/ruff_python_formatter/resources/test/fixtures/ruff/expression/call.py:23
message: Argument name "this_is_a_very_long_keyword_argument_asökdhflakjslaslhfdlaffahflahsöfdhasägporejfäalkdsjäfalisjäfdlkasjd" contains a non-ASCII character, conside
```
   21| )
   22| f(
   23|     this_is_a_very_long_keyword_argument_asökdhflakjslaslhfdlaffahflahsöfdhasägporejfäalkdsjäfalisjäfdlkasjd=1
   24| )
   25| 
```

## ruff :: PLE0303
reference: pylint | only ruff: 0 | only reference: 1 | packages: 1
top messages: [only_reference] __len__ does not return non-negative integer ×1

### only_reference example — numpy numpy-2.5.4/numpy/_core/tests/test_array_coercion.py:642
message: __len__ does not return non-negative integer
```
  640| 
  641|         class baditem:
  642|             def __len__(self):
  643|                 obj[0][0] = 2  # replace with a different list.
  644|                 raise ValueError("not actually a sequence!")
```

## ruff :: B004
reference: flake8 | only ruff: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Using `hasattr(x, "__call__")` to test if x is callable is unreliable. Use `callable(x)` f ×1

### only_rewrite example — sympy sympy-1.14.0/sympy/polys/orderings.py:233
message: Using `hasattr(x, "__call__")` to test if x is callable is unreliable. Use `callable(x)` for consistent results.
```
  231|         except KeyError:
  232|             raise ValueError("supported monomial orderings are 'lex', 'grlex' and 'grevlex', got %r" % order)
  233|     if hasattr(order, '__call__'):
  234|         if gens is not None:
  235|             def _order(expr):
```

## oxlint :: sort-keys
reference: eslint, eslint:sort-keys | only oxlint: 426 | only reference: 1719 | packages: 48
top messages: [only_rewrite] Object keys should be sorted ×426 || [only_reference] sort-keys: Expected object keys to be in ascending order. 'chars' should be before 'type'. ×60 || [only_reference] sort-keys: Expected object keys to be in ascending order. 'code' should be before 'error'. ×30 || [only_reference] sort-keys: Expected object keys to be in ascending order. 'identify' should be before 'res ×30

### only_rewrite example — ansi-styles package/index.js:16
message: Object keys should be sorted
```
   14| const bgBlackBright = [100, 49];
   15| 
   16| const styles = {
   17| 	modifier: {
   18| 		reset: [0, 0],
```

### only_rewrite example — cross-spawn package/lib/enoent.js:6
message: Object keys should be sorted
```
    4| 
    5| function notFoundError(original, syscall) {
    6|     return Object.assign(new Error(`${syscall} ${original.command} ENOENT`), {
    7|         code: 'ENOENT',
    8|         errno: 'ENOENT',
```

### only_rewrite example — get-stream package/source/array-buffer.js:69
message: Object keys should be sorted
```
   67| const hasArrayBufferResize = () => 'resize' in ArrayBuffer.prototype;
   68| 
   69| const arrayBufferMethods = {
   70| 	init: initArrayBuffer,
   71| 	convertChunk: {
```

### only_reference example — find-up package/index.js:176
message: sort-keys: Expected object keys to be in ascending order. 'locateOptions' should be before 'paths'.
```
  174| 		maxDepth,
  175| 		paths,
  176| 		locateOptions,
  177| 		strategy,
  178| 	};
```

### only_reference example — ansi-styles package/index.js:20
message: sort-keys: Expected object keys to be in ascending order. 'bold' should be before 'reset'.
```
   18| 		reset: [0, 0],
   19| 		// 21 isn't widely supported and 22 does the same thing
   20| 		bold: [1, 22],
   21| 		dim: [2, 22],
   22| 		italic: [3, 23],
```

### only_reference example — cross-spawn package/lib/enoent.js:10
message: sort-keys: Expected object keys to be in ascending order. 'path' should be before 'syscall'.
```
    8|         errno: 'ENOENT',
    9|         syscall: `${syscall} ${original.command}`,
   10|         path: original.command,
   11|         spawnargs: original.args,
   12|     });
```

## oxlint :: unicorn/prefer-ternary
reference: eslint, eslint:unicorn/prefer-ternary | only oxlint: 50 | only reference: 330 | packages: 54
top messages: [only_reference] unicorn/prefer-ternary: This `if` statement can be replaced by a ternary expression. ×330 || [only_rewrite] Prefer ternary expressions over simple `if-else` statements. ×50

### only_rewrite example — convert-source-map package/index.js:94
message: Prefer ternary expressions over simple `if-else` statements.
```
   92| 
   93| if (typeof Buffer !== 'undefined') {
   94|   if (typeof Buffer.from === 'function') {
   95|     Converter.prototype.toBase64 = encodeBase64WithBufferFrom;
   96|   } else {
```

### only_rewrite example — debug package/src/index.js:6
message: Prefer ternary expressions over simple `if-else` statements.
```
    4|  */
    5| 
    6| if (typeof process === 'undefined' || process.type === 'renderer' || process.browser === true || process.__nwjs) {
    7| 	module.exports = require('./browser.js');
    8| } else {
```

### only_rewrite example — estraverse package/estraverse.js:43
message: Prefer ternary expressions over simple `if-else` statements.
```
   41|             if (obj.hasOwnProperty(key)) {
   42|                 val = obj[key];
   43|                 if (typeof val === 'object' && val !== null) {
   44|                     ret[key] = deepCopy(val);
   45|                 } else {
```

### only_reference example — agent-base package/dist/index.js:33
message: unicorn/prefer-ternary: This `if` statement can be replaced by a ternary expression.
```
   31|         // detect the "https" module.
   32|         const { stack } = new Error();
   33|         if (typeof stack !== 'string')
   34|             return false;
   35|         return stack
```

### only_reference example — find-up package/index.js:21
message: unicorn/prefer-ternary: This `if` statement can be replaced by a ternary expression.
```
   19| 
   20| 		const foundPath = await name(locateOptions.cwd);
   21| 		if (typeof foundPath === 'string') {
   22| 			return locatePath([foundPath], locateOptions);
   23| 		}
```

### only_reference example — ansi-styles package/index.js:161
message: unicorn/prefer-ternary: This `if` statement can be replaced by a ternary expression.
```
  159| 					}
  160| 
  161| 					if (red > 248) {
  162| 						return 231;
  163| 					}
```

## oxlint :: unicorn/prefer-string-raw
reference: eslint, eslint:unicorn/prefer-string-raw | only oxlint: 9 | only reference: 70 | packages: 12
top messages: [only_reference] unicorn/prefer-string-raw: `String.raw` should be used to avoid escaping `\`. ×70 || [only_rewrite] `String.raw` should be used to avoid escaping `\`. ×9

### only_rewrite example — ajv package/dist/runtime/quote.js:13
message: `String.raw` should be used to avoid escaping `\`.
```
   11|     "\r": "\\r",
   12|     '"': '\\"',
   13|     "\\": "\\\\",
   14| };
   15| function quote(s) {
```

### only_rewrite example — json5 package/lib/parse.js:1085
message: `String.raw` should be used to avoid escaping `\`.
```
 1083|         "'": "\\'",
 1084|         '"': '\\"',
 1085|         '\\': '\\\\',
 1086|         '\b': '\\b',
 1087|         '\f': '\\f',
```

### only_rewrite example — picomatch package/lib/parse.js:643
message: `String.raw` should be used to avoid escaping `\`.
```
  641|       } else {
  642|         output = output.replace(/\\+/g, m => {
  643|           return m.length % 2 === 0 ? '\\\\' : (m ? '\\' : '');
  644|         });
  645|       }
```

### only_reference example — ansi-regex package/index.js:7
message: unicorn/prefer-string-raw: `String.raw` should be used to avoid escaping `\`.
```
    5| 	// OSC sequences only: ESC ] ... ST (or the C1 introducer 0x9d ... ST)
    6| 	// The payload stops at the first terminator character rather than scanning ahead for one, so an unterminated `ESC ]` cannot rescan the rest of the input. Terminals likewise abort a control string on an unexpected ESC. The payload also stops at 0x9d so an unterminated C1 OSC cannot swallow the next
    7| 	const osc = `(?:(?:\\u001B\\]|\\u009D)[^\\u0007\\u001B\\u009C\\u009D]*${ST})`;
    8| 
    9| 	// CSI and related: ESC/C1, optional intermediates, optional params (supports ; and :) then final byte
```

### only_reference example — ignore package/index.js:83
message: unicorn/prefer-string-raw: `String.raw` should be used to avoid escaping `\`.
```
   81|   alnum: '0-9A-Za-z',
   82|   alpha: 'A-Za-z',
   83|   blank: ' \\t',
   84|   cntrl: '\\x00-\\x1f\\x7f',
   85|   digit: '0-9',
```

### only_reference example — path-to-regexp package/dist/index.js:77
message: unicorn/prefer-string-raw: `String.raw` should be used to avoid escaping `\`.
```
   75|             if (value === "\\") {
   76|                 if (index === chars.length) {
   77|                     throw new PathError(`Unexpected end after \\ at index ${index}`, str);
   78|                 }
   79|                 path += chars[index++];
```

## oxlint :: no-unused-vars
reference: eslint, eslint:no-unused-vars | only oxlint: 11 | only reference: 56 | packages: 8
top messages: [only_reference] no-unused-vars: '_i' is defined but never used. ×32 || [only_reference] no-unused-vars: '_default' is assigned a value but never used. ×7 || [only_reference] no-unused-vars: '_' is assigned a value but never used. ×6 || [only_rewrite] Variable 'Duplex' is declared but never used. Unused variables should start with a '_'. ×4

### only_rewrite example — ajv package/dist/compile/util.js:92
message: Parameter 'mergeNames' is declared but never used. Unused parameters should start with a '_'.
```
   90| }
   91| exports.eachItem = eachItem;
   92| function makeMergeEvaluated({ mergeNames, mergeToName, mergeValues, resultToName, }) {
   93|     return (gen, from, to, toName) => {
   94|         const res = to === undefined
```

### only_rewrite example — ws package/lib/sender.js:5
message: Variable 'Duplex' is declared but never used. Unused variables should start with a '_'.
```
    3| 'use strict';
    4| 
    5| const { Duplex } = require('stream');
    6| const { randomFillSync } = require('crypto');
    7| const {
```

### only_reference example — ajv package/dist/compile/codegen/index.js:36
message: no-unused-vars: '_names' is defined but never used.
```
   34|         return this;
   35|     }
   36|     optimizeNames(_names, _constants) {
   37|         return this;
   38|     }
```

### only_reference example — esbuild package/install.js:16
message: no-unused-vars: '__toESM' is assigned a value but never used.
```
   14|   return to;
   15| };
   16| var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
   17|   // If the importer is in node compatibility mode or this is not an ESM
   18|   // file that has been converted to a CommonJS file using a Babel-
```

### only_reference example — minipass package/dist/commonjs/index.js:119
message: no-unused-vars: '_er' is defined but never used.
```
  117|     // only here for the prototype
  118|     /* c8 ignore start */
  119|     proxyErrors(_er) { }
  120|     /* c8 ignore stop */
  121|     end() {
```

## oxlint :: unicorn/prefer-spread
reference: eslint, eslint:unicorn/prefer-spread | only oxlint: 36 | only reference: 20 | packages: 11
top messages: [only_rewrite] Prefer the spread operator (`...`) over array.concat() ×36 || [only_reference] unicorn/prefer-spread: Prefer the spread operator over `Array#concat(…)`. ×20

### only_rewrite example — commander package/lib/command.js:2141
message: Prefer the spread operator (`...`) over array.concat()
```
 2139|           .filter((option) => option.long)
 2140|           .map((option) => option.long);
 2141|         candidateFlags = candidateFlags.concat(moreFlags);
 2142|         command = command.parent;
 2143|       } while (command && !command._enablePositionalOptions);
```

### only_rewrite example — argparse package/lib/argparse.js:3193
message: Prefer the spread operator (`...`) over array.concat()
```
 3191|                 const strings = arg_strings.slice(start_index, next_option_string_index)
 3192|                 extras = extras.concat(strings)
 3193|                 extras_pattern = extras_pattern.concat(
 3194|                     arg_strings_pattern.slice(start_index, next_option_string_index).split(''))
 3195|                 start_index = next_option_string_index
```

### only_rewrite example — json-schema-traverse package/spec/fixtures/schema.js:68
message: Prefer the spread operator (`...`) over array.concat()
```
   66| 
   67|   // schema, jsonPtr, rootSchema, parentJsonPtr, parentKeyword, parentSchema, keyIndex
   68|   expectedCalls: [[schema, '', schema, undefined, undefined, undefined, undefined]]
   69|     .concat(expectedCalls('additionalItems'))
   70|     .concat(expectedCalls('items'))
```

### only_reference example — json-schema-traverse package/spec/fixtures/schema.js:71
message: unicorn/prefer-spread: Prefer the spread operator over `Array#concat(…)`.
```
   69|     .concat(expectedCalls('additionalItems'))
   70|     .concat(expectedCalls('items'))
   71|     .concat(expectedCalls('contains'))
   72|     .concat(expectedCalls('additionalProperties'))
   73|     .concat(expectedCalls('propertyNames'))
```

### only_reference example — yargs package/build/lib/command.js:280
message: unicorn/prefer-spread: Prefer the spread operator over `Array#concat(…)`.
```
  278|             .getMiddleware()
  279|             .slice(0)
  280|             .concat(commandHandler.middlewares);
  281|         const maybePromiseArgv = applyMiddleware(innerArgv, yargs, middlewares, true);
  282|         return isPromise(maybePromiseArgv)
```

## oxlint :: unicorn/prefer-logical-operator-over-ternary
reference: eslint, eslint:unicorn/prefer-logical-operator-over-ternary | only oxlint: 0 | only reference: 53 | packages: 7
top messages: [only_reference] unicorn/prefer-logical-operator-over-ternary: Prefer using optional chaining over a ternar ×38 || [only_reference] unicorn/prefer-logical-operator-over-ternary: Prefer using a logical operator over a terna ×15

### only_reference example — chokidar package/index.js:716
message: unicorn/prefer-logical-operator-over-ternary: Prefer using a logical operator over a ternary.
```
  714|         const fullPath = sp.resolve(path);
  715|         isDirectory =
  716|             isDirectory != null ? isDirectory : this._watched.has(path) || this._watched.has(fullPath);
  717|         // prevent duplicate handling in case of arriving here nearly simultaneously
  718|         // via multiple paths (such as _handleFile and _handleDir)
```

### only_reference example — fs-extra package/lib/copy/copy-sync.js:15
message: unicorn/prefer-logical-operator-over-ternary: Prefer using a logical operator over a ternary.
```
   13| 
   14|   opts = opts || {}
   15|   opts.clobber = 'clobber' in opts ? !!opts.clobber : true // default to true for now
   16|   opts.overwrite = 'overwrite' in opts ? !!opts.overwrite : opts.clobber // overwrite falls back to clobber
   17| 
```

### only_reference example — picomatch package/lib/parse.js:453
message: unicorn/prefer-logical-operator-over-ternary: Prefer using a logical operator over a ternary.
```
  451| 
  452|   const append = token => {
  453|     state.output += token.output != null ? token.output : token.value;
  454|     consume(token.value);
  455|   };
```
