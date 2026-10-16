
## biome :: style/useNumericSeparators
reference: eslint, eslint:unicorn/numeric-separators-style | only biome: 0 | only reference: 98 | packages: 3
top messages: [only_reference] unicorn/numeric-separators-style: Invalid group length in numeric value. ×98

### only_reference example — color-convert package/conversions.js:41
message: unicorn/numeric-separators-style: Invalid group length in numeric value.
```
   39| // SRGB non-linear transform functions
   40| function srgbNonlinearTransform(c) {
   41| 	const cc = c > 0.003_130_8
   42| 		? ((1.055 * (c ** (1 / 2.4))) - 0.055)
   43| 		: c * 12.92;
```

### only_reference example — iconv-lite package/encodings/sbcs-data.js:7
message: unicorn/numeric-separators-style: Invalid group length in numeric value.
```
    5| module.exports = {
    6|   // Not supported by iconv, not sure why.
    7|   10029: "maccenteuro",
    8|   maccenteuro: {
    9|     type: "_sbcs",
```

### only_reference example — qs package/test/parse.js:437
message: unicorn/numeric-separators-style: Invalid group length in numeric value.
```
  435| 
  436|     t.test('correctly prunes undefined values when converting an array to an object', function (st) {
  437|         st.deepEqual(qs.parse('a[2]=b&a[99999999]=c'), { a: { 2: 'b', 99999999: 'c' } });
  438|         st.end();
  439|     });
```

## biome :: style/useConst
reference: eslint, eslint:prefer-const | only biome: 0 | only reference: 82 | packages: 6
top messages: [only_reference] prefer-const: 'dirname' is never reassigned. Use 'const' instead. ×7 || [only_reference] prefer-const: 'readFromStdout' is never reassigned. Use 'const' instead. ×4 || [only_reference] prefer-const: 'sharedBuffer' is never reassigned. Use 'const' instead. ×4 || [only_reference] prefer-const: 'id2' is never reassigned. Use 'const' instead. ×3

### only_reference example — chokidar package/index.js:582
message: prefer-const: 'timeoutObject' is never reassigned. Use 'const' instead.
```
  580|         }
  581|         // eslint-disable-next-line prefer-const
  582|         let timeoutObject;
  583|         const clear = () => {
  584|             const item = action.get(path);
```

### only_reference example — argparse package/lib/argparse.js:375
message: prefer-const: 'prog' is never reassigned. Use 'const' instead.
```
  373|     constructor () {
  374|         let [
  375|             prog,
  376|             indent_increment,
  377|             max_help_position,
```

### only_reference example — esbuild package/lib/main.js:193
message: prefer-const: 'buffer' is never reassigned. Use 'const' instead.
```
  191|   encodeUTF8 = (text) => Buffer.from(text);
  192|   decodeUTF8 = (bytes) => {
  193|     let { buffer, byteOffset, byteLength } = bytes;
  194|     return Buffer.from(buffer, byteOffset, byteLength).toString();
  195|   };
```

## biome :: correctness/noUndeclaredVariables
reference: eslint, eslint:no-undef | only biome: 78 | only reference: 0 | packages: 6
top messages: [only_rewrite] The arguments variable is undeclared. ×67 || [only_rewrite] The SuppressedError variable is undeclared. ×6 || [only_rewrite] The AsyncIterator variable is undeclared. ×3 || [only_rewrite] The value variable is undeclared. ×1

### only_rewrite example — convert-source-map package/index.js:34
message: The value variable is undeclared.
```
   32| 
   33| function decodeBase64WithNewBuffer(base64) {
   34|   if (typeof value === 'number') {
   35|     throw new TypeError('The value to decode must not be of type number.');
   36|   }
```

### only_rewrite example — argparse package/lib/argparse.js:380
message: The arguments variable is undeclared.
```
  378|             width,
  379|             color
  380|         ] = _parse_opts(arguments, {
  381|             prog: no_default,
  382|             indent_increment: 2,
```

### only_rewrite example — whatwg-url package/lib/URL.js:348
message: The arguments variable is undeclared.
```
  346|       }
  347|       {
  348|         let curArg = arguments[1];
  349|         if (curArg !== undefined) {
  350|           curArg = conversions["USVString"](curArg, {
```

## biome :: complexity/noUselessUndefined
reference: eslint, eslint:unicorn/no-useless-undefined | only biome: 0 | only reference: 70 | packages: 10
top messages: [only_reference] unicorn/no-useless-undefined: Do not use useless `undefined`. ×70

### only_reference example — get-stream package/source/utils.js:3
message: unicorn/no-useless-undefined: Do not use useless `undefined`.
```
    1| export const identity = value => value;
    2| 
    3| export const noop = () => undefined;
    4| 
    5| export const getContentsProperty = ({contents}) => contents;
```

### only_reference example — chokidar package/handler.js:501
message: unicorn/no-useless-undefined: Do not use useless `undefined`.
```
  499|                 }
  500|                 const wasThrottled = throttler ? throttler.clear() : false;
  501|                 resolve(undefined);
  502|                 // Files that absent in current directory snapshot
  503|                 // but present in previous emit `remove` event
```

### only_reference example — commander package/lib/command.js:473
message: unicorn/no-useless-undefined: Do not use useless `undefined`.
```
  471|     if (hasImplicitHelpCommand) {
  472|       if (this._helpCommand === undefined) {
  473|         this.helpCommand(undefined, undefined); // use default name and description
  474|       }
  475|       return this._helpCommand;
```

## biome :: style/useForOf
reference: eslint, eslint:unicorn/no-for-loop | only biome: 20 | only reference: 37 | packages: 18
top messages: [only_reference] unicorn/no-for-loop: Use a `for-of` loop instead of this `for` loop. ×37 || [only_rewrite] This for loop only uses its index to read from the iterated array. ×20

### only_rewrite example — iconv-lite package/encodings/dbcs-codec.js:107
message: This for loop only uses its index to read from the iterated array.
```
  105|   var skipEncodeChars = {}
  106|   if (codecOptions.encodeSkipVals) {
  107|     for (var i = 0; i < codecOptions.encodeSkipVals.length; i++) {
  108|       var val = codecOptions.encodeSkipVals[i]
  109|       if (typeof val === "number") { skipEncodeChars[val] = true } else {
```

### only_rewrite example — semver package/classes/range.js:209
message: This for loop only uses its index to read from the iterated array.
```
  207|     }
  208| 
  209|     for (let i = 0; i < this.set.length; i++) {
  210|       if (testSet(this.set[i], version, this.options)) {
  211|         return true
```

### only_rewrite example — readable-stream package/lib/internal/streams/readable.js:796
message: This for loop only uses its index to read from the iterated array.
```
  794|     state.pipes = []
  795|     this.pause()
  796|     for (let i = 0; i < dests.length; i++)
  797|       dests[i].emit('unpipe', this, {
  798|         hasUnpiped: false
```

### only_reference example — eslint-scope package/dist/eslint-scope.cjs:913
message: unicorn/no-for-loop: Use a `for-of` loop instead of this `for` loop.
```
  911| 
  912| 		// create an implicit global variable from assignment expression
  913| 		for (let i = 0, iz = implicit.length; i < iz; ++i) {
  914| 			const info = implicit[i];
  915| 
```

### only_reference example — argparse package/lib/argparse.js:697
message: unicorn/no-for-loop: Use a `for-of` loop instead of this `for` loop.
```
  695|         let pos_start
  696|         const action_sets = optionals.concat(positionals)
  697|         for (let i = 0; i < action_sets.length; i++) {
  698|             const [required, group] = action_sets[i]
  699|             const start = parts.length
```

### only_reference example — ajv package/dist/vocabularies/discriminator/index.js:58
message: unicorn/no-for-loop: Use a `for-of` loop instead of this `for` loop.
```
   56|             const topRequired = hasRequired(parentSchema);
   57|             let tagRequired = true;
   58|             for (let i = 0; i < oneOf.length; i++) {
   59|                 let sch = oneOf[i];
   60|                 if ((sch === null || sch === void 0 ? void 0 : sch.$ref) && !(0, util_1.schemaHasRulesButRef)(sch, it.self.RULES)) {
```

## biome :: complexity/noArguments
reference: eslint, eslint:prefer-rest-params | only biome: 52 | only reference: 0 | packages: 10
top messages: [only_rewrite] Use the rest parameters instead of arguments. ×52

### only_rewrite example — argparse package/lib/argparse.js:126
message: Use the rest parameters instead of arguments.
```
  124| function range (from, to, step = 1) {
  125|     // range(10) is equivalent to range(0, 10)
  126|     if (arguments.length === 1) [to, from] = [from, 0]
  127|     if (typeof from !== 'number' || typeof to !== 'number' || typeof step !== 'number') {
  128|         throw new TypeError('argument cannot be interpreted as an integer')
```

### only_rewrite example — ignore package/legacy.js:1184
message: Use the rest parameters instead of arguments.
```
 1182| var Ignore = /*#__PURE__*/function () {
 1183|   function Ignore() {
 1184|     var _ref5 = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {},
 1185|       _ref5$ignorecase = _ref5.ignorecase,
 1186|       ignorecase = _ref5$ignorecase === void 0 ? true : _ref5$ignorecase,
```

### only_rewrite example — readable-stream package/lib/internal/streams/end-of-stream.js:40
message: Use the rest parameters instead of arguments.
```
   38| function eos(stream, options, callback) {
   39|   var _options$readable, _options$writable
   40|   if (arguments.length === 2) {
   41|     callback = options
   42|     options = kEmptyObject
```

## biome :: suspicious/noShadowRestrictedNames
reference: eslint, eslint:no-shadow-restricted-names | only biome: 45 | only reference: 0 | packages: 13
top messages: [only_rewrite] Do not shadow the global "escape" property. ×16 || [only_rewrite] Do not shadow the global "Symbol" property. ×7 || [only_rewrite] Do not shadow the global "unescape" property. ×6 || [only_rewrite] Do not shadow the global "Promise" property. ×5

### only_rewrite example — get-stream package/source/stream.js:21
message: Do not shadow the global "toString" property.
```
   19| };
   20| 
   21| const {toString} = Object.prototype;
   22| 
   23| // The default iterable for Node.js streams does not allow for multiple readers at once, so we re-implement it
```

### only_rewrite example — cross-spawn package/lib/parse.js:5
message: Do not shadow the global "escape" property.
```
    3| const path = require('path');
    4| const resolveCommand = require('./util/resolveCommand');
    5| const escape = require('./util/escape');
    6| const readShebang = require('./util/readShebang');
    7| 
```

### only_rewrite example — entities package/dist/escape.js:120
message: Do not shadow the global "escape" property.
```
  118|  * @param data String to escape.
  119|  */
  120| export const escape = encodeXML;
  121| /**
  122|  * Escape `data` using `re`, mapping each matched character to its entity.
```

## biome :: suspicious/noShadow
reference: eslint, eslint:no-shadow | only biome: 44 | only reference: 0 | packages: 13
top messages: [only_rewrite] This variable shadows another variable with the same name in the outer scope. ×44

### only_rewrite example — acorn package/dist/bin.js:63
message: This variable shadows another variable with the same name in the outer scope.
```
   61|   var result = [], fileIdx = 0;
   62|   try {
   63|     codeList.forEach(function (code, idx) {
   64|       fileIdx = idx;
   65|       if (!tokenize) {
```

### only_rewrite example — convert-source-map package/index.js:54
message: This variable shadows another variable with the same name in the outer scope.
```
   52| 
   53|   try {
   54|     var sm = read(filename);
   55|     if (sm != null && typeof sm.catch === 'function') {
   56|       return sm.catch(throwError);
```

### only_rewrite example — argparse package/lib/argparse.js:3009
message: This variable shadows another variable with the same name in the outer scope.
```
 3007| 
 3008|         // function to convert arg_strings into an optional action
 3009|         const consume_optional = start_index => {
 3010| 
 3011|             // get the optional identified at this index
```

## biome :: style/noNestedTernary
reference: eslint, eslint:no-nested-ternary | only biome: 20 | only reference: 20 | packages: 8
top messages: [only_reference] no-nested-ternary: Do not nest ternary expressions. ×20 || [only_rewrite] Do not nest ternary expressions. ×20

### only_rewrite example — entities package/dist/escape.js:14
message: Do not nest ternary expressions.
```
   12|                 : char === 60
   13|                     ? "&lt;"
   14|                     : char === 62
   15|                         ? "&gt;"
   16|                         : "&nbsp;";
```

### only_rewrite example — ajv package/dist/compile/util.js:98
message: Do not nest ternary expressions.
```
   96|             : to instanceof codegen_1.Name
   97|                 ? (from instanceof codegen_1.Name ? mergeNames(gen, from, to) : mergeToName(gen, from, to), to)
   98|                 : from instanceof codegen_1.Name
   99|                     ? (mergeToName(gen, to, from), from)
  100|                     : mergeValues(from, to);
```

### only_rewrite example — ignore package/index.js:516
message: Do not nest ternary expressions.
```
  514|       // >   folder itself, so it requires at least one directory segment.
  515|       // 'a/**/' matches 'a/b/', 'a/x/y/' but not 'a/'
  516|       ? str.slice(index + 6) === '\\/'
  517|         ? '(?:\\/[^\\/]+)+'
  518| 
```

### only_reference example — entities package/dist/escape.js:6
message: no-nested-ternary: Do not nest ternary expressions.
```
    4|  */
    5| function getEscape(char) {
    6|     return char === 34
    7|         ? "&quot;"
    8|         : char === 38
```

### only_reference example — ajv package/dist/compile/util.js:94
message: no-nested-ternary: Do not nest ternary expressions.
```
   92| function makeMergeEvaluated({ mergeNames, mergeToName, mergeValues, resultToName, }) {
   93|     return (gen, from, to, toName) => {
   94|         const res = to === undefined
   95|             ? from
   96|             : to instanceof codegen_1.Name
```

### only_reference example — ignore package/index.js:509
message: no-nested-ternary: Do not nest ternary expressions.
```
  507| 
  508|     // Check if it is not the last `'/**'`
  509|     (_, index, str) => index + 6 < str.length
  510| 
  511|       // case: /**/ at the end of the pattern, i.e. a trailing `'/**/'`
```

## biome :: suspicious/noSparseArray
reference: eslint, eslint:no-sparse-arrays | only biome: 0 | only reference: 36 | packages: 1
top messages: [only_reference] no-sparse-arrays: Unexpected comma in middle of array. ×36

### only_reference example — qs package/test/parse.js:509
message: no-sparse-arrays: Unexpected comma in middle of array.
```
  507|     t.test('parses sparse arrays', function (st) {
  508|         /* eslint no-sparse-arrays: 0 */
  509|         st.deepEqual(qs.parse('a[4]=1&a[1]=2', { allowSparse: true }), { a: [, '2', , , '1'] });
  510|         st.deepEqual(qs.parse('a[1][b][2][c]=1', { allowSparse: true }), { a: [, { b: [, , { c: '1' }] }] });
  511|         st.deepEqual(qs.parse('a[1][2][3][c]=1', { allowSparse: true }), { a: [, [, , [, , , { c: '1' }]]] });
```

## biome :: style/useConsistentBuiltinInstantiation
reference: eslint, eslint:no-new-wrappers | only biome: 35 | only reference: 0 | packages: 10
top messages: [only_rewrite] Use new Error() instead of Error(). ×14 || [only_rewrite] Use new TypeError() instead of TypeError(). ×10 || [only_rewrite] Use new Object() instead of Object(). ×6 || [only_rewrite] Use new Array() instead of Array(). ×4

### only_rewrite example — argparse package/lib/argparse.js:880
message: Use new Array() instead of Array().
```
  878|                 return result
  879|             } else {
  880|                 return Array(tuple_size).fill(result)
  881|             }
  882|         }
```

### only_rewrite example — ignore package/legacy.js:13
message: Use new Object() instead of Object().
```
   11| function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o);
   12| function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
   13| function _iterableToArrayLimit(arr, i) { var _i = null == arr ? null : "undefined" != typeof Symbol && arr[Symbol.iterator] || arr["@@iterator"]; if (null != _i) { var _s, _e, _x, _r, _arr = [], _n 
```

### only_rewrite example — js-tokens package/index.js:23
message: Use new RegExp() instead of RegExp().
```
   21| KeywordsWithExpressionAfter = /^(?:await|case|default|delete|do|else|instanceof|new|return|throw|typeof|void|yield)$/;
   22| KeywordsWithNoLineTerminatorAfter = /^(?:return|throw|yield)$/;
   23| Newline = RegExp(LineTerminatorSequence.source);
   24| jsTokens = function*(input, {jsx = false} = {}) {
   25| 	var braces, firstCodePoint, isExpression, lastIndex, lastSignificantToken, length, match, mode, nextLastIndex, nextLastSignificantToken, parenNesting, postfixIncDec, punctuator, stack;
```

## biome :: correctness/noInvalidBuiltinInstantiation
reference: eslint, eslint:no-new-native-nonconstructor, eslint:unicorn/new-for-builtins | only biome: 0 | only reference: 33 | packages: 9
top messages: [only_reference] unicorn/new-for-builtins: Use `new Error()` instead of `Error()`. ×14 || [only_reference] unicorn/new-for-builtins: Use `new TypeError()` instead of `TypeError()`. ×10 || [only_reference] unicorn/new-for-builtins: Use `new Array()` instead of `Array()`. ×4 || [only_reference] unicorn/new-for-builtins: Use `new Object()` instead of `Object()`. ×4

### only_reference example — argparse package/lib/argparse.js:880
message: unicorn/new-for-builtins: Use `new Array()` instead of `Array()`.
```
  878|                 return result
  879|             } else {
  880|                 return Array(tuple_size).fill(result)
  881|             }
  882|         }
```

### only_reference example — js-tokens package/index.js:23
message: unicorn/new-for-builtins: Use `new RegExp()` instead of `RegExp()`.
```
   21| KeywordsWithExpressionAfter = /^(?:await|case|default|delete|do|else|instanceof|new|return|throw|typeof|void|yield)$/;
   22| KeywordsWithNoLineTerminatorAfter = /^(?:return|throw|yield)$/;
   23| Newline = RegExp(LineTerminatorSequence.source);
   24| jsTokens = function*(input, {jsx = false} = {}) {
   25| 	var braces, firstCodePoint, isExpression, lastIndex, lastSignificantToken, length, match, mode, nextLastIndex, nextLastSignificantToken, parenNesting, postfixIncDec, punctuator, stack;
```

### only_reference example — json5 package/lib/stringify.js:166
message: unicorn/new-for-builtins: Use `new TypeError()` instead of `TypeError()`.
```
  164|     function serializeObject (value) {
  165|         if (stack.indexOf(value) >= 0) {
  166|             throw TypeError('Converting circular structure to JSON5')
  167|         }
  168| 
```

## biome :: style/useBlockStatements
reference: eslint, eslint:curly | only biome: 15 | only reference: 15 | packages: 6
top messages: [only_rewrite] Block statements are preferred in this position. ×15 || [only_reference] curly: Expected { after 'if' condition. ×14 || [only_reference] curly: Expected { after 'else'. ×1

### only_rewrite example — entities package/dist/decode.js:885
message: Block statements are preferred in this position.
```
  883|                     // Handle odd trailing char.
  884|                     if (charIndexInPacked < remaining) {
  885|                         if (input.charCodeAt(index) !==
  886|                             (decodeTree[wordIndex] & 0xff))
  887|                             // eslint-disable-next-line unicorn/no-break-in-nested-loop
```

### only_rewrite example — commander package/lib/command.js:2781
message: Block statements are preferred in this position.
```
 2779|   // (https://force-color.org recent web page from 2023, does not match major javascript implementations)
 2780| 
 2781|   if (
 2782|     process.env.NO_COLOR ||
 2783|     process.env.FORCE_COLOR === '0' ||
```

### only_rewrite example — fs-extra package/lib/copy/copy.js:57
message: Block statements are preferred in this position.
```
   55|   if (srcStat.isDirectory()) return onDir(srcStat, destStat, src, dest, opts)
   56| 
   57|   if (
   58|     srcStat.isFile() ||
   59|     srcStat.isCharacterDevice() ||
```

### only_reference example — entities package/dist/decode.js:888
message: curly: Expected { after 'if' condition.
```
  886|                             (decodeTree[wordIndex] & 0xff))
  887|                             // eslint-disable-next-line unicorn/no-break-in-nested-loop
  888|                             break;
  889|                         index += 1;
  890|                     }
```

### only_reference example — commander package/lib/command.js:2788
message: curly: Expected { after 'if' condition.
```
 2786|     return false;
 2787|   if (process.env.FORCE_COLOR || process.env.CLICOLOR_FORCE !== undefined)
 2788|     return true;
 2789|   return undefined;
 2790| }
```

### only_reference example — fs-extra package/lib/copy/copy.js:61
message: curly: Expected { after 'if' condition.
```
   59|     srcStat.isCharacterDevice() ||
   60|     srcStat.isBlockDevice()
   61|   ) return onFile(srcStat, destStat, src, dest, opts)
   62| 
   63|   if (srcStat.isSymbolicLink()) return onLink(destStat, src, dest, opts)
```

## biome :: complexity/noExtraBooleanCast
reference: eslint, eslint:no-extra-boolean-cast | only biome: 28 | only reference: 0 | packages: 2
top messages: [only_rewrite] Avoid redundant double-negation. ×28

### only_rewrite example — lru-cache package/dist/commonjs/index.js:12
message: Avoid redundant double-negation.
```
   10| const warned = new Set();
   11| /* c8 ignore start */
   12| const PROCESS = (typeof process === 'object' && !!process ?
   13|     process
   14|     : {});
```

### only_rewrite example — yallist package/dist/commonjs/index.js:146
message: Avoid redundant double-negation.
```
  144|         let i = 0;
  145|         let walker = this.head;
  146|         for (; !!walker && i < n; i++) {
  147|             walker = walker.next;
  148|         }
```

## biome :: style/useTemplate
reference: eslint, eslint:prefer-template | only biome: 0 | only reference: 23 | packages: 11
top messages: [only_reference] prefer-template: Unexpected string concatenation. ×23

### only_reference example — debug package/src/browser.js:150
message: prefer-template: Unexpected string concatenation.
```
  148| 
  149| function formatArgs(args) {
  150| 	args[0] = (this.useColors ? '%c' : '') +
  151| 		this.namespace +
  152| 		(this.useColors ? ' %c' : ' ') +
```

### only_reference example — argparse package/lib/argparse.js:736
message: prefer-template: Unexpected string concatenation.
```
  734|                         const default_value = this._get_default_metavar_for_optional(action)
  735|                         const args_string = this._format_args(action, default_value)
  736|                         part = option_color + option_string + ' ' +
  737|                             t.summary_label + args_string + t.reset
  738|                     }
```

### only_reference example — ajv package/dist/compile/validate/keyword.js:114
message: prefer-template: Unexpected string concatenation.
```
  112|         const valid = def.validateSchema(schema[keyword]);
  113|         if (!valid) {
  114|             const msg = `keyword "${keyword}" value is invalid at path "${errSchemaPath}": ` +
  115|                 self.errorsText(def.validateSchema.errors);
  116|             if (opts.validateSchema === "log")
```

## biome :: suspicious/noControlCharactersInRegex
reference: eslint, eslint:no-control-regex | only biome: 22 | only reference: 0 | packages: 5
top messages: [only_rewrite] Unexpected control character in a regular expression. ×22

### only_rewrite example — argparse package/lib/argparse.js:144
message: Unexpected control character in a regular expression.
```
  142|     let result
  143|     if (!keepends) {
  144|         result = str.split(/\r\n|[\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029]/)
  145|     } else {
  146|         result = []
```

### only_rewrite example — ajv package/dist/runtime/quote.js:5
message: Unexpected control character in a regular expression.
```
    3| const rxEscapable = 
    4| // eslint-disable-next-line no-control-regex, no-misleading-character-class
    5| /[\\"\u0000-\u001f\u007f-\u009f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g;
    6| const escaped = {
    7|     "\b": "\\b",
```

### only_rewrite example — ignore package/index.js:1528
message: Unexpected control character in a regular expression.
```
 1526|   /* eslint no-control-regex: "off" */
 1527|   const makePosix = str => /^\\\\\?\\/.test(str)
 1528|   || /["<>|\u0000-\u001F]+/u.test(str)
 1529|     ? str
 1530|     : str.replace(/\\/g, '/')
```

## biome :: style/noParameterAssign
reference: eslint, eslint:no-param-reassign | only biome: 0 | only reference: 12 | packages: 6
top messages: [only_reference] no-param-reassign: Assignment to function parameter 'ext'. ×4 || [only_reference] no-param-reassign: Assignment to function parameter 'cwd'. ×2 || [only_reference] no-param-reassign: Assignment to function parameter 'v'. ×1 || [only_reference] no-param-reassign: Assignment to function parameter 'schema'. ×1

### only_reference example — locate-path package/index.js:35
message: no-param-reassign: Assignment to function parameter 'cwd'.
```
   33| ) {
   34| 	checkType(type);
   35| 	cwd = toPath(cwd);
   36| 
   37| 	const statFunction = allowSymlinks ? fsPromises.stat : fsPromises.lstat;
```

### only_reference example — argparse package/lib/argparse.js:2027
message: no-param-reassign: Assignment to function parameter 'v'.
```
 2025|         const args = [this._flags]
 2026|         const kwargs = Object.entries(this._options).map(([k, v]) => {
 2027|             if (k === 'mode') v = { value: v, [util.inspect.custom] () { return '0o' + this.value.toString(8) } }
 2028|             return [k, v]
 2029|         })
```

### only_reference example — ajv package/dist/compile/index.js:222
message: no-param-reassign: Assignment to function parameter 'schema'.
```
  220|         if (partSchema === undefined)
  221|             return;
  222|         schema = partSchema;
  223|         // TODO PREVENT_SCOPE_CHANGE could be defined in keyword def?
  224|         const schId = typeof schema === "object" && schema[this.opts.schemaId];
```

## biome :: style/useErrorCause
reference: eslint, eslint:preserve-caught-error | only biome: 10 | only reference: 0 | packages: 5
top messages: [only_rewrite] The original error is not being passed to the new `Error` object.Include the original erro ×6 || [only_rewrite] The original error is being discarded because the `catch` clause doesn't have a parameter. ×4

### only_rewrite example — argparse package/lib/argparse.js:2005
message: The original error is not being passed to the new `Error` object.Include the original error in the `cause` property to preserve it.
```
 2003|             const args = { filename: string, error: e.message }
 2004|             const message = "can't open '%(filename)s': %(error)s"
 2005|             throw new ArgumentTypeError(sub(message, args))
 2006|         }
 2007| 
```

### only_rewrite example — esbuild package/lib/main.js:2033
message: The original error is being discarded because the `catch` clause doesn't have a parameter.Specify an error object in the `catch` clause to access the original e
```
 2031| `;
 2032|           }
 2033|           throw new Error(`
 2034| You installed esbuild for another platform than the one you're currently using.
 2035| This won't work because esbuild is written with native code and needs to
```

### only_rewrite example — pretty-format package/build/index.js:909
message: The original error is not being passed to the new `Error` object.Include the original error in the `cause` property to preserve it.
```
  907|     }, config.colors);
  908|   } catch (error) {
  909|     throw new PrettyFormatPluginError(error.message, error.stack);
  910|   }
  911|   if (typeof printed !== 'string') {
```

## biome :: suspicious/noEmptyBlockStatements
reference: eslint, eslint:no-empty, eslint:no-empty-function, eslint:no-empty-static-block | only biome: 0 | only reference: 8 | packages: 1
top messages: [only_reference] no-empty-function: Unexpected empty method 'attach'. ×2 || [only_reference] no-empty-function: Unexpected empty method 'detach'. ×2 || [only_reference] no-empty-function: Unexpected empty method 'BreakStatement'. ×2 || [only_reference] no-empty-function: Unexpected empty method 'ContinueStatement'. ×2

### only_reference example — eslint-scope package/dist/eslint-scope.cjs:1390
message: no-empty-function: Unexpected empty method 'attach'.
```
 1388| 	}
 1389| 
 1390| 	attach() {} // eslint-disable-line class-methods-use-this -- Desired as instance method
 1391| 
 1392| 	detach() {} // eslint-disable-line class-methods-use-this -- Desired as instance method
```

## biome :: complexity/noUselessEscapeInRegex
reference: eslint, eslint:no-useless-escape | only biome: 0 | only reference: 8 | packages: 5
top messages: [only_reference] no-useless-escape: Unnecessary escape character: \(. ×4 || [only_reference] no-useless-escape: Unnecessary escape character: \/. ×3 || [only_reference] no-useless-escape: Unnecessary escape character: \+. ×1

### only_reference example — convert-source-map package/index.js:6
message: no-useless-escape: Unnecessary escape character: \/.
```
    4|   get: function getCommentRegex () {
    5|     // Groups: 1: media type, 2: MIME type, 3: charset, 4: encoding, 5: data.
    6|     return /^\s*?\/[\/\*][@#]\s+?sourceMappingURL=data:(((?:application|text)\/json)(?:;charset=([^;,]+?)?)?)?(?:;(base64))?,(.*?)$/mg;
    7|   }
    8| });
```

### only_reference example — cookie package/dist/index.js:68
message: no-useless-escape: Unnecessary escape character: \/.
```
   66|  * RegExp to match RFC 6265 cookie-octet values (without % to preserve roundtrip) that need no URL encoding.
   67|  */
   68| const cookieOctetRegExp = /^[!#$&'()*+\-.\/0-9:<=>?@A-Z[\]\^_`a-z{|}~]*$/;
   69| const NullObject = /* @__PURE__ */ (() => {
   70|     const C = function () { };
```

### only_reference example — iconv-lite package/encodings/utf7.js:21
message: no-useless-escape: Unnecessary escape character: \(.
```
   19| // Why scape ()?./?
   20| // eslint-disable-next-line no-useless-escape
   21| var nonDirectChars = /[^A-Za-z0-9'\(\),-\.\/:\? \n\r\t]+/g
   22| 
   23| function Utf7Encoder (options, codec) {
```

## biome :: performance/noAwaitInLoops
reference: eslint, eslint:no-await-in-loop | only biome: 3 | only reference: 4 | packages: 4
top messages: [only_reference] no-await-in-loop: Unexpected `await` inside a loop. ×4 || [only_rewrite] Avoid using await inside loops. ×3

### only_rewrite example — which package/lib/index.js:59
message: Avoid using await inside loops.
```
   57|     for (const ext of pathExt) {
   58|       const withExt = p + ext
   59|       const is = await isexe(withExt, { pathExt: pathExtExe, ignoreErrors: true })
   60|       if (is) {
   61|         if (!opt.all) {
```

### only_rewrite example — readable-stream package/lib/internal/streams/operators.js:143
message: Avoid using await inside loops.
```
  141|       while (true) {
  142|         while (queue.length > 0) {
  143|           const val = await queue[0]
  144|           if (val === kEof) {
  145|             return
```

### only_rewrite example — postcss package/lib/lazy-result.js:316
message: Avoid using await inside loops.
```
  314|           if (isPromise(promise)) {
  315|             try {
  316|               await promise
  317|             } catch (e) {
  318|               let node = stack[stack.length - 1].node
```

### only_reference example — find-up package/index.js:199
message: no-await-in-loop: Unexpected `await` inside a loop.
```
  197| 		try {
  198| 			// eslint-disable-next-line no-await-in-loop
  199| 			const entries = await fs.promises.readdir(directory, {withFileTypes: true});
  200| 			for (const entry of entries) {
  201| 				if (entry.isDirectory()) {
```

### only_reference example — readable-stream package/lib/internal/streams/from.js:80
message: no-await-in-loop: Unexpected `await` inside a loop.
```
   78|           readable.push(null)
   79|         } else {
   80|           const res = value && typeof value.then === 'function' ? await value : value
   81|           if (res === null) {
   82|             reading = false
```

### only_reference example — postcss package/lib/lazy-result.js:336
message: no-await-in-loop: Unexpected `await` inside a loop.
```
  334|               await Promise.all(roots)
  335|             } else {
  336|               await visitor(root, this.helpers)
  337|             }
  338|           } catch (e) {
```

## biome :: suspicious/noGlobalAssign
reference: eslint, eslint:no-global-assign | only biome: 7 | only reference: 0 | packages: 3
top messages: [only_rewrite] A global variable should not be reassigned. ×7

### only_rewrite example — ajv package/dist/2019.js:44
message: A global variable should not be reassigned.
```
   42| }
   43| exports.Ajv2019 = Ajv2019;
   44| module.exports = exports = Ajv2019;
   45| module.exports.Ajv2019 = Ajv2019;
   46| Object.defineProperty(exports, "__esModule", { value: true });
```

### only_rewrite example — semver package/internal/re.js:9
message: A global variable should not be reassigned.
```
    7| } = require('./constants')
    8| const debug = require('./debug')
    9| exports = module.exports = {}
   10| 
   11| // The actual regexps go on exports.re
```

### only_rewrite example — whatwg-url package/lib/utils.js:384
message: A global variable should not be reassigned.
```
  382| const asyncIteratorEOI = Symbol("async iterator end of iteration");
  383| 
  384| module.exports = exports = {
  385|   isObject,
  386|   define,
```
