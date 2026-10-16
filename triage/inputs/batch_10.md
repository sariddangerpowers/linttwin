
## oxlint :: unicorn/prefer-at
reference: eslint, eslint:unicorn/prefer-at | only oxlint: 2 | only reference: 1 | packages: 3
top messages: [only_rewrite] Prefer `.at()` over `slice()[0]`. ×1 || [only_rewrite] Prefer `.at()` over `[index]`. ×1 || [only_reference] unicorn/prefer-at: Prefer `.at(…)` over the first element from `.slice(…)`. ×1

### only_rewrite example — commander package/lib/command.js:377
message: Prefer `.at()` over `slice()[0]`.
```
  375|    */
  376|   addArgument(argument) {
  377|     const previousArgument = this.registeredArguments.slice(-1)[0];
  378|     if (previousArgument?.variadic) {
  379|       throw new Error(
```

### only_rewrite example — source-map package/lib/source-node.js:282
message: Prefer `.at()` over `[index]`.
```
  280|    */
  281|   replaceRight(aPattern, aReplacement) {
  282|     const lastChild = this.children[this.children.length - 1];
  283|     if (lastChild[isSourceNode]) {
  284|       lastChild.replaceRight(aPattern, aReplacement);
```

### only_reference example — yargs-parser package/build/lib/yargs-parser.js:318
message: unicorn/prefer-at: Prefer `.at(…)` over the first element from `.slice(…)`.
```
  316|                     }
  317|                 }
  318|                 key = arg.slice(-1)[0];
  319|                 if (!broken && key !== '-') {
  320|                     if (checkAllAliases(key, flags.arrays)) {
```

## oxlint :: sort-imports
reference: eslint, eslint:sort-imports | only oxlint: 0 | only reference: 3 | packages: 1
top messages: [only_reference] sort-imports: Imports should be sorted alphabetically. ×2 || [only_reference] sort-imports: Expected 'multiple' syntax before 'single' syntax. ×1

### only_reference example — yargs-parser package/build/lib/index.js:11
message: sort-imports: Expected 'multiple' syntax before 'single' syntax.
```
    9| /* eslint-disable n/no-unpublished-import */
   10| import { format } from 'util';
   11| import { normalize, resolve } from 'path';
   12| import { camelCase, decamelize, looksLikeNumber } from './string-utils.js';
   13| import { YargsParser } from './yargs-parser.js';
```

## oxlint :: no-loop-func
reference: eslint, eslint:no-loop-func | only oxlint: 0 | only reference: 3 | packages: 1
top messages: [only_reference] no-loop-func: Function declared in a loop contains unsafe references to variable(s) 'done' ×3

### only_reference example — tslib package/tslib.es6.js:76
message: no-loop-func: Function declared in a loop contains unsafe references to variable(s) 'done'.
```
   74|         for (var p in contextIn) context[p] = p === "access" ? {} : contextIn[p];
   75|         for (var p in contextIn.access) context.access[p] = contextIn.access[p];
   76|         context.addInitializer = function (f) { if (done) throw new TypeError("Cannot add initializers after decoration has completed"); extraInitializers.push(accept(f || null)); };
   77|         var result = (0, decorators[i])(kind === "accessor" ? { get: descriptor.get, set: descriptor.set } : descriptor[key], context);
   78|         if (kind === "accessor") {
```

## oxlint :: unicorn/no-nested-ternary
reference: eslint, eslint:unicorn/no-nested-ternary | only oxlint: 1 | only reference: 1 | packages: 1
top messages: [only_reference] unicorn/no-nested-ternary: Do not nest ternary expressions. ×1 || [only_rewrite] Unexpected deeply nested ternary expression. ×1

### only_rewrite example — entities package/dist/escape.js:14
message: Unexpected deeply nested ternary expression.
```
   12|                 : char === 60
   13|                     ? "&lt;"
   14|                     : char === 62
   15|                         ? "&gt;"
   16|                         : "&nbsp;";
```

### only_reference example — entities package/dist/escape.js:10
message: unicorn/no-nested-ternary: Do not nest ternary expressions.
```
    8|         : char === 38
    9|             ? "&amp;"
   10|             : char === 39
   11|                 ? "&apos;"
   12|                 : char === 60
```

## oxlint :: no-lonely-if
reference: eslint, eslint:no-lonely-if | only oxlint: 0 | only reference: 2 | packages: 2
top messages: [only_reference] no-lonely-if: Unexpected if as the only statement in an else block. ×2

### only_reference example — ajv package/dist/runtime/parseJson.js:165
message: no-lonely-if: Unexpected if as the only statement in an else block.
```
  163|         }
  164|         else {
  165|             if (c.charCodeAt(0) >= 0x20) {
  166|                 str += c;
  167|             }
```

### only_reference example — ws package/lib/extension.js:100
message: no-lonely-if: Unexpected if as the only statement in an else block.
```
   98|       // Ref: https://tools.ietf.org/html/rfc6455#section-9.1
   99|       //
  100|       if (isEscaping) {
  101|         if (tokenChars[code] !== 1) {
  102|           throw new SyntaxError(`Unexpected character at index ${i}`);
```

## oxlint :: unicorn/prefer-includes
reference: eslint, eslint:unicorn/prefer-includes | only oxlint: 0 | only reference: 2 | packages: 2
top messages: [only_reference] unicorn/prefer-includes: Use `.includes()` instead of `.some()` when checking value existe ×2

### only_reference example — ajv package/dist/vocabularies/jtd/properties.js:81
message: unicorn/prefer-includes: Use `.includes()` instead of `.some()` when checking value existence.
```
   79|         const schema = parentSchema[keyword];
   80|         const allPs = schema ? (0, code_1.allSchemaProperties)(schema) : [];
   81|         if (it.jtdDiscriminator && allPs.some((p) => p === it.jtdDiscriminator)) {
   82|             throw new Error(`JTD: discriminator tag used in ${keyword}`);
   83|         }
```

### only_reference example — picomatch package/lib/parse.js:301
message: unicorn/prefer-includes: Use `.includes()` instead of `.some()` when checking value existence.
```
  299|   if (branches.length > 1) {
  300|     if (
  301|       branches.some(branch => branch === '') ||
  302|       branches.some(branch => /^[*?]+$/.test(branch)) ||
  303|       hasRepeatedCharPrefixOverlap(branches)
```

## oxlint :: max-statements
reference: eslint, eslint:max-statements | only oxlint: 1 | only reference: 1 | packages: 1
top messages: [only_reference] max-statements: Arrow function has too many statements (15). Maximum allowed is 10. ×1 || [only_rewrite] function has too many statements (15). Maximum allowed is 10. ×1

### only_rewrite example — ignore package/index.js:1077
message: function has too many statements (15). Maximum allowed is 10.
```
 1075| }
 1076| 
 1077| const createRule = ({
 1078|   pattern,
 1079|   mark
```

### only_reference example — ignore package/index.js:1080
message: max-statements: Arrow function has too many statements (15). Maximum allowed is 10.
```
 1078|   pattern,
 1079|   mark
 1080| }, ignoreCase) => {
 1081|   // Git drops a BOM before it reads the first line, so before anything else.
 1082|   let body = pattern[0] === BOM
```

## oxlint :: max-lines-per-function
reference: eslint, eslint:max-lines-per-function | only oxlint: 1 | only reference: 1 | packages: 1
top messages: [only_reference] max-lines-per-function: Arrow function has too many lines (58). Maximum allowed is 50. ×1 || [only_rewrite] The function has too many lines (58). Maximum allowed is 50. ×1

### only_rewrite example — ignore package/index.js:1077
message: The function has too many lines (58). Maximum allowed is 50.
```
 1075| }
 1076| 
 1077| const createRule = ({
 1078|   pattern,
 1079|   mark
```

### only_reference example — ignore package/index.js:1080
message: max-lines-per-function: Arrow function has too many lines (58). Maximum allowed is 50.
```
 1078|   pattern,
 1079|   mark
 1080| }, ignoreCase) => {
 1081|   // Git drops a BOM before it reads the first line, so before anything else.
 1082|   let body = pattern[0] === BOM
```

## oxlint :: no-control-regex
reference: eslint, eslint:no-control-regex | only oxlint: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unexpected control characters ×1 || [only_rewrite] Unexpected control character ×1

### only_rewrite example — ignore package/index.js:1528
message: Unexpected control characters
```
 1526|   /* eslint no-control-regex: "off" */
 1527|   const makePosix = str => /^\\\\\?\\/.test(str)
 1528|   || /["<>|\u0000-\u001F]+/u.test(str)
 1529|     ? str
 1530|     : str.replace(/\\/g, '/')
```

## oxlint :: unicorn/prefer-top-level-await
reference: eslint, eslint:unicorn/prefer-top-level-await | only oxlint: 1 | only reference: 1 | packages: 1
top messages: [only_reference] unicorn/prefer-top-level-await: Prefer top-level await over using a promise chain. ×1 || [only_rewrite] Prefer top-level await over using a promise chain. ×1

### only_rewrite example — lru-cache package/dist/esm/diagnostics-channel.js:13
message: Prefer top-level await over using a promise chain.
```
   11| export let metrics = dummy;
   12| export let tracing = dummy;
   13| import('node:diagnostics_channel')
   14|     .then(dc => {
   15|     metrics = dc.channel('lru-cache:metrics');
```

### only_reference example — lru-cache package/dist/esm/diagnostics-channel.js:18
message: unicorn/prefer-top-level-await: Prefer top-level await over using a promise chain.
```
   16|     tracing = dc.tracingChannel('lru-cache');
   17| })
   18|     .catch(() => { });
   19| //# sourceMappingURL=diagnostics-channel-esm.mjs.map
```

## oxlint :: unicorn/catch-error-name
reference: eslint, eslint:unicorn/catch-error-name | only oxlint: 0 | only reference: 2 | packages: 1
top messages: [only_reference] unicorn/catch-error-name: The catch parameter `_err` should be named `error_`. ×1 || [only_reference] unicorn/catch-error-name: The catch parameter `_err` should be named `error`. ×1

### only_reference example — yargs package/build/lib/command.js:259
message: unicorn/catch-error-name: The catch parameter `_err` should be named `error_`.
```
  257|                         yargs.getInternalMethods().getUsageInstance().fail(null, error);
  258|                     }
  259|                     catch (_err) {
  260|                     }
  261|                 });
```

## oxlint :: unicorn/prefer-global-this
reference: eslint, eslint:unicorn/prefer-global-this | only oxlint: 2 | only reference: 0 | packages: 1
top messages: [only_rewrite] Prefer `globalThis` over environment-specific global aliases like `window`, `self`, and `g ×2

### only_rewrite example — tslib package/tslib.js:49
message: Prefer `globalThis` over environment-specific global aliases like `window`, `self`, and `global`.
```
   47| var __rewriteRelativeImportExtension;
   48| (function (factory) {
   49|     var root = typeof global === "object" ? global : typeof self === "object" ? self : typeof this === "object" ? this : {};
   50|     if (typeof define === "function" && define.amd) {
   51|         define("tslib", ["exports"], function (exports) { factory(createExporter(root, createExporter(exports))); });
```

## oxlint :: unicorn/no-abusive-eslint-disable
reference: eslint, eslint:unicorn/no-abusive-eslint-disable | only oxlint: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unexpected `eslint-disable` comment that does not specify any rules to disable. ×1

### only_rewrite example — has-flag package/index.js:1
message: Unexpected `eslint-disable` comment that does not specify any rules to disable.
```
    1| import process from 'process'; // eslint-disable-line node/prefer-global/process
    2| 
    3| export default function hasFlag(flag, argv = process.argv) {
```

## oxlint :: class-methods-use-this
reference: eslint, eslint:class-methods-use-this | only oxlint: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Expected method `errorsText` to have this. ×1

### only_rewrite example — ajv package/dist/core.js:392
message: Expected method `errorsText` to have this.
```
  390|         return this;
  391|     }
  392|     errorsText(errors = this.errors, // optional array of validation errors
  393|     { separator = ", ", dataVar = "data" } = {} // optional options with properties `separator` and `dataVar`
  394|     ) {
```

## oxlint :: unicorn/prefer-native-coercion-functions
reference: eslint, eslint:unicorn/prefer-native-coercion-functions | only oxlint: 0 | only reference: 1 | packages: 1
top messages: [only_reference] unicorn/prefer-native-coercion-functions: method 'RFC3986' is equivalent to `String`. Use  ×1

### only_reference example — qs package/lib/formats.js:17
message: unicorn/prefer-native-coercion-functions: method 'RFC3986' is equivalent to `String`. Use `String` directly.
```
   15|             return replace.call(value, percentTwenties, '+');
   16|         },
   17|         RFC3986: function (value) {
   18|             return String(value);
   19|         }
```

## oxlint :: unicorn/explicit-length-check
reference: eslint, eslint:unicorn/explicit-length-check | only oxlint: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] Use `.length > 0` when checking length is not zero. ×1

### only_rewrite example — yargs package/build/lib/argsert.js:20
message: Use `.length > 0` when checking length is not zero.
```
   18|         while (args.length && args[args.length - 1] === undefined)
   19|             args.pop();
   20|         const length = _length || args.length;
   21|         if (length < parsed.demanded.length) {
   22|             throw new YError(`Not enough arguments provided. Expected ${parsed.demanded.length} but received ${args.length}.`);
```

## oxlint :: max-params
reference: eslint, eslint:max-params | only oxlint: 0 | only reference: 1 | packages: 1
top messages: [only_reference] max-params: Method '__n' has too many parameters (4). Maximum allowed is 3. ×1

### only_reference example — yargs package/lib/platform-shims/browser.mjs:77
message: max-params: Method '__n' has too many parameters (4). Maximum allowed is 3.
```
   75|       return sprintf(str[0], ...args);
   76|     },
   77|     __n: (str1, str2, count, ...args) => {
   78|       if (count === 1) {
   79|         return sprintf(str1, ...args);
```

## oxlint :: unicorn/no-process-exit
reference: eslint, eslint:unicorn/no-process-exit | only oxlint: 0 | only reference: 1 | packages: 1
top messages: [only_reference] unicorn/no-process-exit: Only use `process.exit()` in CLI apps. Throw an error instead. ×1

### only_reference example — yargs package/lib/platform-shims/esm.mjs:50
message: unicorn/no-process-exit: Only use `process.exit()` in CLI apps. Throw an error instead.
```
   48|     exit: (code) => {
   49|       // eslint-disable-next-line n/no-process-exit
   50|       process.exit(code);
   51|     },
   52|     nextTick: process.nextTick,
```

## biome :: complexity/noCommaOperator
reference: eslint, eslint:no-sequences | only biome: 782 | only reference: 1 | packages: 13
top messages: [only_rewrite] The comma operator is disallowed. ×782 || [only_reference] no-sequences: Unexpected use of comma operator. ×1

### only_rewrite example — ajv package/dist/core.js:107
message: The comma operator is disallowed.
```
  105|         const formatOpt = opts.validateFormats;
  106|         opts.validateFormats = false;
  107|         this.RULES = (0, rules_1.getRules)();
  108|         checkOptions.call(this, removedOptions, opts, "NOT SUPPORTED");
  109|         checkOptions.call(this, deprecatedOptions, opts, "DEPRECATED", "warn");
```

### only_rewrite example — ignore package/legacy.js:13
message: The comma operator is disallowed.
```
   11| function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o);
   12| function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
   13| function _iterableToArrayLimit(arr, i) { var _i = null == arr ? null : "undefined" != typeof Symbol && arr[Symbol.iterator] || arr["@@iterator"]; if (null != _i) { var _s, _e, _x, _r, _arr = [], _n 
```

### only_rewrite example — balanced-match package/dist/commonjs/index.js:7
message: The comma operator is disallowed.
```
    5|     const ma = a instanceof RegExp ? maybeMatch(a, str) : a;
    6|     const mb = b instanceof RegExp ? maybeMatch(b, str) : b;
    7|     const r = ma !== null && mb != null && (0, exports.range)(ma, mb, str);
    8|     return (r && {
    9|         start: r[0],
```

### only_reference example — signal-exit package/dist/cjs/index.js:252
message: no-sequences: Unexpected use of comma operator.
```
  250| // wrap so that we call the method on the actual handler, without
  251| // exporting it directly.
  252| _a = signalExitWrap(processOk(process) ? new SignalExit(process) : new SignalExitFallback()), 
  253| /**
  254|  * Called when the process is exiting, whether via signal, explicit
```

## biome :: complexity/useMaxParams
reference: eslint, eslint:max-params | only biome: 0 | only reference: 267 | packages: 40
top messages: [only_reference] max-params: Arrow function has too many parameters (4). Maximum allowed is 3. ×41 || [only_reference] max-params: Function has too many parameters (4). Maximum allowed is 3. ×16 || [only_reference] max-params: Constructor has too many parameters (4). Maximum allowed is 3. ×15 || [only_reference] max-params: Method 'backgroundFetch' has too many parameters (4). Maximum allowed is 3. ×8

### only_reference example — get-stream package/source/contents.js:72
message: max-params: Arrow function has too many parameters (4). Maximum allowed is 3.
```
   70| };
   71| 
   72| const addNewChunk = (convertedChunk, state, addChunk, newLength) => {
   73| 	state.contents = addChunk(convertedChunk, state, newLength);
   74| 	state.length = newLength;
```

### only_reference example — chalk package/source/utilities.js:21
message: max-params: Function 'stringEncaseCRLFWithFirstIndex' has too many parameters (4). Maximum allowed is 3.
```
   19| }
   20| 
   21| export function stringEncaseCRLFWithFirstIndex(string, prefix, postfix, index) {
   22| 	let endIndex = 0;
   23| 	let returnValue = '';
```

### only_reference example — eslint-scope package/dist/eslint-scope.cjs:355
message: max-params: Constructor has too many parameters (4). Maximum allowed is 3.
```
  353|  */
  354| class ParameterDefinition extends Definition {
  355| 	constructor(name, node, index, rest) {
  356| 		super(Variable.Parameter, name, node, null, index, null);
  357| 
```

## biome :: correctness/noUnusedVariables
reference: eslint, eslint:no-unused-vars | only biome: 5 | only reference: 174 | packages: 16
top messages: [only_reference] no-unused-vars: '_i' is defined but never used. ×32 || [only_reference] no-unused-vars: 'pkg' is defined but never used. ×24 || [only_reference] no-unused-vars: 'res' is defined but never used. ×20 || [only_reference] no-unused-vars: '_' is defined but never used. ×11

### only_rewrite example — iconv-lite package/encodings/dbcs-codec.js:286
message: This variable uCode is unused.
```
  284|     if (nextChar === -1) {
  285|       if (i == str.length) break
  286|       var uCode = str.charCodeAt(i++)
  287|     } else {
  288|       var uCode = nextChar
```

### only_rewrite example — readable-stream package/lib/internal/streams/operators.js:196
message: This variable unused is unused.
```
  194| }
  195| async function some(fn, options = undefined) {
  196|   for await (const unused of filter.call(this, fn, options)) {
  197|     return true
  198|   }
```

### only_rewrite example — resolve package/lib/async.js:317
message: This function onfile is unused.
```
  315|         }
  316| 
  317|         function onfile(err, m, pkg) {
  318|             if (err) return cb(err);
  319|             if (m) return cb(null, m, pkg);
```

### only_reference example — eslint-scope package/dist/eslint-scope.cjs:680
message: no-unused-vars: 'ref' is defined but never used.
```
  678| 	// References in default parameters isn't resolved to variables which are in their function body.
  679| 	// eslint-disable-next-line class-methods-use-this, no-unused-vars  -- Desired as instance method with signature
  680| 	__isValidResolution(ref, variable) {
  681| 		return true;
  682| 	}
```

### only_reference example — chokidar package/index.js:3
message: no-unused-vars: 'Stats' is defined but never used.
```
    1| /*! chokidar - MIT License (c) 2012 Paul Miller (paulmillr.com) */
    2| import { EventEmitter } from 'node:events';
    3| import { stat as statcb, Stats } from 'node:fs';
    4| import { readdir, stat } from 'node:fs/promises';
    5| import * as sp from 'node:path';
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

## biome :: style/useNumberNamespace
reference: eslint, eslint:unicorn/prefer-number-properties | only biome: 110 | only reference: 39 | packages: 26
top messages: [only_rewrite] Use Number.POSITIVE_INFINITY instead of the equivalent global. ×69 || [only_reference] unicorn/prefer-number-properties: Prefer `Number.isNaN` over `isNaN`. ×29 || [only_rewrite] Use Number.parseInt instead of the equivalent global. ×19 || [only_rewrite] Use Number.NaN instead of the equivalent global. ×16

### only_rewrite example — agent-base package/dist/index.js:50
message: Use Number.POSITIVE_INFINITY instead of the equivalent global.
```
   48|         // need to create a fake socket because Node.js native connection pooling
   49|         // will never be invoked.
   50|         if (this.maxSockets === Infinity && this.maxTotalSockets === Infinity) {
   51|             return null;
   52|         }
```

### only_rewrite example — form-data package/lib/form_data.js:139
message: Use Number.POSITIVE_INFINITY instead of the equivalent global.
```
  137|     // Fix it when node fixes it.
  138|     // https://github.com/joyent/node/issues/7819
  139|     if (value.end != undefined && value.end != Infinity && value.start != undefined) {
  140|       // when end specified
  141|       // no need to calculate range
```

### only_rewrite example — debug package/src/browser.js:138
message: Use Number.parseInt instead of the equivalent global.
```
  136| 		// Is firefox >= v31?
  137| 		// https://developer.mozilla.org/en-US/docs/Tools/Web_Console#Styling_messages
  138| 		(typeof navigator !== 'undefined' && navigator.userAgent && (m = navigator.userAgent.toLowerCase().match(/firefox\/(\d+)/)) && parseInt(m[1], 10) >= 31) ||
  139| 		// Double check webkit in userAgent just in case we are in a worker
  140| 		(typeof navigator !== 'undefined' && navigator.userAgent && navigator.userAgent.toLowerCase().match(/applewebkit\/(\d+)/));
```

### only_reference example — is-number package/index.js:15
message: unicorn/prefer-number-properties: Prefer `Number.isFinite` over `isFinite`.
```
   13|   }
   14|   if (typeof num === 'string' && num.trim() !== '') {
   15|     return Number.isFinite ? Number.isFinite(+num) : isFinite(+num);
   16|   }
   17|   return false;
```

### only_reference example — argparse package/lib/argparse.js:2734
message: unicorn/prefer-number-properties: Prefer `Number.isNaN` over `isNaN`.
```
 2732|             }
 2733|             const result = _string_to_number(x)
 2734|             if (isNaN(result)) {
 2735|                 throw new TypeError(sub('could not convert string to float: %r', x))
 2736|             }
```

### only_reference example — esbuild package/install.js:173
message: unicorn/prefer-number-properties: Prefer `Number.isNaN` over `isNaN`.
```
  171|     let size = parseInt(str(offset + 124, 12), 8);
  172|     offset += 512;
  173|     if (!isNaN(size) && size >= 0) {
  174|       if (name === subpath) return buffer.subarray(offset, offset + size);
  175|       offset += size + 511 & ~511;
```
