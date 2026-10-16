
## oxlint :: no-redeclare
reference: eslint, eslint:no-redeclare | only oxlint: 28 | only reference: 19 | packages: 11
top messages: [only_reference] no-redeclare: 'Reflect' is already defined as a built-in global variable. ×10 || [only_rewrite] 'Symbol' is already defined as a built-in global variable. ×7 || [only_rewrite] 'escape' is already defined as a built-in global variable. ×6 || [only_reference] no-redeclare: 'global' is already defined as a built-in global variable. ×6

### only_rewrite example — cross-spawn package/lib/parse.js:5
message: 'escape' is already defined as a built-in global variable.
```
    3| const path = require('path');
    4| const resolveCommand = require('./util/resolveCommand');
    5| const escape = require('./util/escape');
    6| const readShebang = require('./util/readShebang');
    7| 
```

### only_rewrite example — json5 package/lib/parse.js:729
message: 'escape' is already defined as a built-in global variable.
```
  727| }
  728| 
  729| function escape () {
  730|     const c = peek()
  731|     switch (c) {
```

### only_rewrite example — path-to-regexp package/dist/index.js:23
message: 'escape' is already defined as a built-in global variable.
```
   21|  * Escape a regular expression string.
   22|  */
   23| function escape(str) {
   24|     return str.replace(/[.+*?^${}()[\]|/\\]/g, "\\$&");
   25| }
```

### only_reference example — estraverse package/estraverse.js:27
message: no-redeclare: 'exports' is already defined as a built-in global variable.
```
   25| /*jslint vars:false, bitwise:true*/
   26| /*jshint indent:4*/
   27| /*global exports:true*/
   28| (function clone(exports) {
   29|     'use strict';
```

### only_reference example — picomatch package/lib/utils.js:1
message: no-redeclare: 'navigator' is already defined as a built-in global variable.
```
    1| /*global navigator*/
    2| 'use strict';
    3| 
```

### only_reference example — pretty-format package/build/index.js:758
message: no-redeclare: 'window' is already defined as a built-in global variable.
```
  756| const getConstructorName = val => typeof val.constructor === 'function' && val.constructor.name || 'Object';
  757| 
  758| /* global window */
  759| /** Is val is equal to global window object? Works even if it does not exist :) */
  760| const isWindow = val =>
```

## oxlint :: unicorn/prefer-string-replace-all
reference: eslint, eslint:unicorn/prefer-string-replace-all | only oxlint: 6 | only reference: 36 | packages: 16
top messages: [only_reference] unicorn/prefer-string-replace-all: Prefer `String#replaceAll()` over `String#replace()`. ×33 || [only_rewrite] Prefer `String#replaceAll()` over `String#replace()` when using a regex with the global fl ×6 || [only_reference] unicorn/prefer-string-replace-all: Prefer `String#replaceAll()` over `String#split().join( ×3

### only_rewrite example — escape-string-regexp package/index.js:9
message: Prefer `String#replaceAll()` over `String#replace()` when using a regex with the global flag.
```
    7| 	// Use a simple backslash escape when it’s always valid, and a `\xnn` escape when the simpler form would be disallowed by Unicode patterns’ stricter grammar.
    8| 	return string
    9| 		.replace(/[|\\{}()[\]^$+*?.]/g, '\\$&')
   10| 		.replace(/-/g, '\\x2d');
   11| }
```

### only_rewrite example — argparse package/lib/textwrap.js:435
message: Prefer `String#replaceAll()` over `String#replace()` when using a regex with the global flag.
```
  433| 
  434|     if (margin) {
  435|         text = text.replace(new RegExp('^' + margin, 'mg'), '')
  436|     }
  437|     return text
```

### only_rewrite example — json5 package/lib/stringify.js:159
message: Prefer `String#replaceAll()` over `String#replace()` when using a regex with the global flag.
```
  157|         const quoteChar = quote || Object.keys(quotes).reduce((a, b) => (quotes[a] < quotes[b]) ? a : b)
  158| 
  159|         product = product.replace(new RegExp(quoteChar, 'g'), replacements[quoteChar])
  160| 
  161|         return quoteChar + product + quoteChar
```

### only_reference example — cross-spawn package/lib/util/escape.js:8
message: unicorn/prefer-string-replace-all: Prefer `String#replaceAll()` over `String#replace()`.
```
    6| function escapeCommand(arg) {
    7|     // Escape meta chars
    8|     arg = arg.replace(metaCharsRegExp, '^$1');
    9| 
   10|     return arg;
```

### only_reference example — chokidar package/index.js:52
message: unicorn/prefer-string-replace-all: Prefer `String#replaceAll()` over `String#replace()`.
```
   50|     if (path.startsWith('//'))
   51|         prepend = true;
   52|     path = path.replace(DOUBLE_SLASH_RE, '/');
   53|     if (prepend)
   54|         path = '/' + path;
```

### only_reference example — argparse package/lib/sub.js:12
message: unicorn/prefer-string-replace-all: Prefer `String#replaceAll()` over `String#replace()`.
```
   10|     const regex = /%(?:(%)|(-)?(\*)?(?:\((\w+)\))?([A-Za-z]))/g
   11| 
   12|     const result = pattern.replace(regex, function (_, is_literal, is_left_align, is_padded, name, format) {
   13|         if (is_literal) return '%'
   14| 
```

## oxlint :: sort-vars
reference: eslint, eslint:sort-vars | only oxlint: 0 | only reference: 42 | packages: 12
top messages: [only_reference] sort-vars: Variables within the same declaration block should be sorted alphabetically. ×42

### only_reference example — convert-source-map package/index.js:127
message: sort-vars: Variables within the same declaration block should be sorted alphabetically.
```
  125| 
  126| Converter.prototype.toComment = function (options) {
  127|   var encoding, content, data;
  128|   if (options != null && options.encoding === 'uri') {
  129|     encoding = '';
```

### only_reference example — fast-deep-equal package/index.js:13
message: sort-vars: Variables within the same declaration block should be sorted alphabetically.
```
   11|     if (a.constructor !== b.constructor) return false;
   12| 
   13|     var length, i, keys;
   14|     if (Array.isArray(a)) {
   15|       length = a.length;
```

### only_reference example — estraverse package/estraverse.js:35
message: sort-vars: Variables within the same declaration block should be sorted alphabetically.
```
   33|         VisitorKeys,
   34|         BREAK,
   35|         SKIP,
   36|         REMOVE;
   37| 
```

## oxlint :: no-sparse-arrays
reference: eslint, eslint:no-sparse-arrays | only oxlint: 40 | only reference: 0 | packages: 1
top messages: [only_rewrite] Unexpected comma in middle of array ×40

### only_rewrite example — qs package/test/parse.js:509
message: Unexpected comma in middle of array
```
  507|     t.test('parses sparse arrays', function (st) {
  508|         /* eslint no-sparse-arrays: 0 */
  509|         st.deepEqual(qs.parse('a[4]=1&a[1]=2', { allowSparse: true }), { a: [, '2', , , '1'] });
  510|         st.deepEqual(qs.parse('a[1][b][2][c]=1', { allowSparse: true }), { a: [, { b: [, , { c: '1' }] }] });
  511|         st.deepEqual(qs.parse('a[1][2][3][c]=1', { allowSparse: true }), { a: [, [, , [, , , { c: '1' }]]] });
```

## oxlint :: unicorn/prefer-type-error
reference: eslint, eslint:unicorn/prefer-type-error | only oxlint: 4 | only reference: 23 | packages: 5
top messages: [only_reference] unicorn/prefer-type-error: `new Error()` is too unspecific for a type check. Use `new Type ×23 || [only_rewrite] Prefer throwing a `TypeError` over a generic `Error` after a type checking if-statement ×4

### only_rewrite example — esbuild package/lib/main.js:198
message: Prefer throwing a `TypeError` over a generic `Error` after a type checking if-statement
```
  196|   encodeInvariant = 'Buffer.from("")';
  197| } else {
  198|   throw new Error("No UTF-8 codec found");
  199| }
  200| if (!(encodeUTF8("") instanceof Uint8Array))
```

### only_rewrite example — iconv-lite package/encodings/dbcs-codec.js:182
message: Prefer throwing a `TypeError` over a generic `Error` after a type checking if-statement
```
  180|       var charCode = writeTable[curAddr - 1] + 1
  181|       for (var l = 0; l < part; l++) { writeTable[curAddr++] = charCode++ }
  182|     } else { throw new Error("Incorrect type '" + typeof part + "' given in " + this.encodingName + " at chunk " + chunk[0]) }
  183|   }
  184|   if (curAddr > 0xFF) { throw new Error("Incorrect chunk in " + this.encodingName + " at addr " + chunk[0] + ": too long" + curAddr) }
```

### only_rewrite example — postcss package/lib/container.js:222
message: Prefer throwing a `TypeError` over a generic `Error` after a type checking if-statement
```
  220|     } else if (nodes.prop) {
  221|       if (typeof nodes.value === 'undefined') {
  222|         throw new Error('Value field is missed in node creation')
  223|       } else if (typeof nodes.value !== 'string') {
  224|         nodes.value = String(nodes.value)
```

### only_reference example — chokidar package/index.js:46
message: unicorn/prefer-type-error: `new Error()` is too unspecific for a type check. Use `new TypeError()` instead.
```
   44| function normalizePath(path) {
   45|     if (typeof path !== 'string')
   46|         throw new Error('string expected');
   47|     path = sp.normalize(path);
   48|     path = path.replace(/\\/g, '/');
```

### only_reference example — ajv package/dist/core.js:445
message: unicorn/prefer-type-error: `new Error()` is too unspecific for a type check. Use `new TypeError()` instead.
```
  443|                 throw new Error("schema must be object");
  444|             else if (typeof schema != "boolean")
  445|                 throw new Error("schema must be object or boolean");
  446|         }
  447|         let sch = this._cache.get(schema);
```

### only_reference example — esbuild package/lib/main.js:201
message: unicorn/prefer-type-error: `new Error()` is too unspecific for a type check. Use `new TypeError()` instead.
```
  199| }
  200| if (!(encodeUTF8("") instanceof Uint8Array))
  201|   throw new Error(`Invariant violation: "${encodeInvariant} instanceof Uint8Array" is incorrectly false
  202| 
  203| This indicates that your JavaScript environment is broken. You cannot use
```

## oxlint :: unicorn/prefer-default-parameters
reference: eslint, eslint:unicorn/prefer-default-parameters | only oxlint: 0 | only reference: 26 | packages: 9
top messages: [only_reference] unicorn/prefer-default-parameters: Prefer a default parameter over fallback expressions. ×14 || [only_reference] unicorn/prefer-default-parameters: Prefer a destructuring default over fallback expression ×9 || [only_reference] unicorn/prefer-default-parameters: Prefer default parameters over reassignment. ×3

### only_reference example — cliui package/build/lib/index.js:97
message: unicorn/prefer-default-parameters: Prefer a destructuring default over fallback expressions.
```
   95|             let str = '';
   96|             rrow.forEach((col, c) => {
   97|                 const { width } = row[c]; // the width with padding.
   98|                 const wrapWidth = this.negatePadding(row[c]); // the width without padding.
   99|                 let ts = col; // temporary string used during alignment/padding.
```

### only_reference example — commander package/lib/argument.js:13
message: unicorn/prefer-default-parameters: Prefer a default parameter over fallback expressions.
```
   11|    */
   12| 
   13|   constructor(name, description) {
   14|     this.description = description || '';
   15|     this.variadic = false;
```

### only_reference example — ajv package/dist/compile/validate/index.js:181
message: unicorn/prefer-default-parameters: Prefer a default parameter over fallback expressions.
```
  179|         gen.assign((0, codegen_1._) `${evaluated}.items`, items);
  180| }
  181| function schemaKeywords(it, types, typeErrors, errsCount) {
  182|     const { gen, schema, data, allErrors, opts, self } = it;
  183|     const { RULES } = self;
```

## oxlint :: unicorn/prefer-regexp-test
reference: eslint, eslint:unicorn/prefer-regexp-test | only oxlint: 4 | only reference: 22 | packages: 4
top messages: [only_reference] unicorn/prefer-regexp-test: Prefer `RegExp#test(…)` over `String#match(…)`. ×22 || [only_rewrite] Prefer `RegExp#test()` over `String#match()` and `RegExp#exec()`. ×4

### only_rewrite example — glob package/dist/commonjs/ignore.js:108
message: Prefer `RegExp#test()` over `String#match()` and `RegExp#exec()`.
```
  106|         const relative = (p.relative() || '.') + '/';
  107|         for (const m of this.relativeChildren) {
  108|             if (m.match(relative))
  109|                 return true;
  110|         }
```

### only_reference example — brace-expansion package/dist/commonjs/index.js:265
message: unicorn/prefer-regexp-test: Prefer `RegExp#test(…)` over `String#match(…)`.
```
  263|         if (!isSequence && !isOptions) {
  264|             // {a},b}
  265|             if (rewrites < maxRewrites && m.post.match(/,(?!,).*\}/)) {
  266|                 rewrites++;
  267|                 str = m.pre + '{' + m.body + escClose + m.post;
```

### only_reference example — glob package/dist/commonjs/ignore.js:95
message: unicorn/prefer-regexp-test: Prefer `RegExp#test(…)` over `String#match(…)`.
```
   93|         const relatives = `${relative}/`;
   94|         for (const m of this.relative) {
   95|             if (m.match(relative) || m.match(relatives))
   96|                 return true;
   97|         }
```

### only_reference example — yargs-parser package/build/lib/yargs-parser.js:192
message: unicorn/prefer-regexp-test: Prefer `RegExp#test(…)` over `String#match(…)`.
```
  190|                 // -- separated by =
  191|             }
  192|             else if (arg.match(/^--.+=/) || (!configuration['short-option-groups'] && arg.match(/^-.+=/))) {
  193|                 // Using [\s\S] instead of . because js doesn't support the
  194|                 // 'dotall' regex modifier. See:
```

## oxlint :: unicorn/no-array-callback-reference
reference: eslint, eslint:unicorn/no-array-callback-reference | only oxlint: 6 | only reference: 15 | packages: 10
top messages: [only_reference] unicorn/no-array-callback-reference: Do not pass function directly to `.forEach(…)`. ×8 || [only_rewrite] Avoid passing a function reference directly to iterator methods ×6 || [only_reference] unicorn/no-array-callback-reference: Do not pass function directly to `.every(…)`. ×1 || [only_reference] unicorn/no-array-callback-reference: Do not pass function `convertOutputFiles` directly to ×1

### only_rewrite example — chokidar package/handler.js:215
message: Avoid passing a function reference directly to iterator methods
```
  213|             // }
  214|             FsWatchInstances.delete(fullPath);
  215|             HANDLER_KEYS.forEach(clearItem(cont));
  216|             // @ts-ignore
  217|             cont.watcher = undefined;
```

### only_rewrite example — ignore package/index.js:1510
message: Avoid passing a function reference directly to iterator methods
```
 1508| 
 1509|   filter (paths) {
 1510|     return makeArray(paths).filter(this.createFilter())
 1511|   }
 1512| 
```

### only_rewrite example — minimatch package/dist/esm/index.js:123
message: Avoid passing a function reference directly to iterator methods
```
  121|         unescape: (s, options = {}) => orig.unescape(s, ext(def, options)),
  122|         escape: (s, options = {}) => orig.escape(s, ext(def, options)),
  123|         filter: (pattern, options = {}) => orig.filter(pattern, ext(def, options)),
  124|         defaults: (options) => orig.defaults(ext(def, options)),
  125|         makeRe: (pattern, options = {}) => orig.makeRe(pattern, ext(def, options)),
```

### only_reference example — ajv package/dist/compile/validate/dataType.js:34
message: unicorn/no-array-callback-reference: Do not pass function directly to `.every(…)`.
```
   32| function getJSONTypes(ts) {
   33|     const types = Array.isArray(ts) ? ts : ts ? [ts] : [];
   34|     if (types.every(rules_1.isJSONType))
   35|         return types;
   36|     throw new Error("type must be JSONType or JSONType[]: " + types.join(","));
```

### only_reference example — eslint-scope package/dist/eslint-scope.cjs:1614
message: unicorn/no-array-callback-reference: Do not pass function directly to `.forEach(…)`.
```
 1612| 
 1613| 	ArrayExpression(node) {
 1614| 		node.elements.forEach(this.visit, this);
 1615| 	}
 1616| 
```

### only_reference example — esbuild package/lib/main.js:1205
message: unicorn/no-array-callback-reference: Do not pass function `convertOutputFiles` directly to `.map(…)`.
```
 1203|       const originalErrors = result.errors.slice();
 1204|       const originalWarnings = result.warnings.slice();
 1205|       if (response.outputFiles) result.outputFiles = response.outputFiles.map(convertOutputFiles);
 1206|       if (response.metafile && response.metafile.length) result.metafile = parseJSON(response.metafile);
 1207|       if (response.mangleCache) result.mangleCache = response.mangleCache;
```

## oxlint :: unicorn/filename-case
reference: eslint, eslint:unicorn/filename-case | only oxlint: 0 | only reference: 21 | packages: 1
top messages: [only_reference]  ×21

### only_reference example — resolve package/test/module_dir/xmodules/aaa/index.js:0
message: 
```
    1| module.exports = function (x) { return x * 100; };
```

## oxlint :: capitalized-comments
reference: eslint, eslint:capitalized-comments | only oxlint: 1 | only reference: 12 | packages: 5
top messages: [only_reference] capitalized-comments: Comments should not begin with a lowercase character. ×12 || [only_rewrite] Comments should not begin with a lowercase letter ×1

### only_rewrite example — estraverse package/estraverse.js:25
message: Comments should not begin with a lowercase letter
```
   23|   THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
   24| */
   25| /*jslint vars:false, bitwise:true*/
   26| /*jshint indent:4*/
   27| /*global exports:true*/
```

### only_reference example — chokidar package/handler.js:34
message: capitalized-comments: Comments should not begin with a lowercase character.
```
   32| const KEY_RAW = 'rawEmitters';
   33| const HANDLER_KEYS = [KEY_LISTENERS, KEY_ERR, KEY_RAW];
   34| // prettier-ignore
   35| const binaryExtensions = new Set([
   36|     '3dm', '3ds', '3g2', '3gp', '7z', 'a', 'aac', 'adp', 'afdesign', 'afphoto', 'afpub', 'ai',
```

### only_reference example — minimatch package/dist/commonjs/index.js:270
message: capitalized-comments: Comments should not begin with a lowercase character.
```
  268|         this.globSet = [...new Set(this.braceExpand())];
  269|         if (options.debug) {
  270|             //oxlint-disable-next-line no-console
  271|             this.debug = (...args) => console.error(...args);
  272|         }
```

### only_reference example — lru-cache package/dist/commonjs/index.js:21
message: capitalized-comments: Comments should not begin with a lowercase character.
```
   19|     }
   20|     else {
   21|         //oxlint-disable-next-line no-console
   22|         console.error(`[${code}] ${type}: ${msg}`);
   23|     }
```

## oxlint :: prefer-template
reference: eslint, eslint:prefer-template | only oxlint: 0 | only reference: 11 | packages: 6
top messages: [only_reference] prefer-template: Unexpected string concatenation. ×11

### only_reference example — debug package/src/node.js:172
message: prefer-template: Unexpected string concatenation.
```
  170| 	if (useColors) {
  171| 		const c = this.color;
  172| 		const colorCode = '\u001B[3' + (c < 8 ? c : '8;5;' + c);
  173| 		const prefix = `  ${colorCode};1m${name} \u001B[0m`;
  174| 
```

### only_reference example — commander package/lib/help.js:170
message: prefer-template: Unexpected string concatenation.
```
  168|     return (
  169|       cmd._name +
  170|       (cmd._aliases[0] ? '|' + cmd._aliases[0] : '') +
  171|       (cmd.options.length ? ' [options]' : '') + // simplistic check for non-help option
  172|       (args ? ' ' + args : '')
```

### only_reference example — ajv package/dist/runtime/quote.js:23
message: prefer-template: Unexpected string concatenation.
```
   21|                 return typeof c === "string"
   22|                     ? c
   23|                     : "\\u" + ("0000" + a.charCodeAt(0).toString(16)).slice(-4);
   24|             })
   25|             : s) +
```

## oxlint :: no-useless-assignment
reference: eslint, eslint:no-useless-assignment | only oxlint: 2 | only reference: 9 | packages: 5
top messages: [only_reference] no-useless-assignment: The value assigned to 'offset' is not used in subsequent statements ×4 || [only_reference] no-useless-assignment: The value assigned to 'fn' is not used in subsequent statements. ×2 || [only_rewrite] This assigned value is not used in subsequent statements. ×2 || [only_reference] no-useless-assignment: The value assigned to 'patternIndex' is not used in subsequent stat ×2

### only_rewrite example — minimatch package/dist/commonjs/ast.js:150
message: This assigned value is not used in subsequent statements.
```
  148|     // (which really means one child of '')
  149|     #emptyExt = false;
  150|     id = ++ID;
  151|     get depth() {
  152|         return (this.#parent?.depth ?? -1) + 1;
```

### only_reference example — chokidar package/index.js:190
message: no-useless-assignment: The value assigned to 'path' is not used in subsequent statements.
```
  188|         this.fsw = fsw;
  189|         const watchPath = path;
  190|         this.path = path = path.replace(REPLACER_RE, '');
  191|         this.watchPath = watchPath;
  192|         this.fullWatchPath = sp.resolve(watchPath);
```

### only_reference example — glob package/dist/commonjs/walker.js:74
message: no-useless-assignment: The value assigned to 'fn' is not used in subsequent statements.
```
   72|         /* c8 ignore stop */
   73|         this.paused = false;
   74|         let fn = undefined;
   75|         while (!this.paused && (fn = this.#onResume.shift())) {
   76|             fn();
```

### only_reference example — esbuild package/lib/main.js:208
message: no-useless-assignment: The value assigned to 'offset' is not used in subsequent statements.
```
  206| `);
  207| function readUInt32LE(buffer, offset) {
  208|   return (buffer[offset++] | buffer[offset++] << 8 | buffer[offset++] << 16 | buffer[offset++] << 24) >>> 0;
  209| }
  210| function writeUInt32LE(buffer, value, offset) {
```

## oxlint :: unicorn/no-immediate-mutation
reference: eslint, eslint:unicorn/no-immediate-mutation | only oxlint: 0 | only reference: 10 | packages: 6
top messages: [only_reference] unicorn/no-immediate-mutation: Combine this initialization with the preceding declaration. ×10

### only_reference example — estraverse package/estraverse.js:59
message: unicorn/no-immediate-mutation: Combine this initialization with the preceding declaration.
```
   57|         var diff, len, i, current;
   58| 
   59|         len = array.length;
   60|         i = 0;
   61| 
```

### only_reference example — color-convert package/conversions.js:410
message: unicorn/no-immediate-mutation: Combine this initialization with the preceding declaration.
```
  408| 	let l;
  409| 
  410| 	l = (2 - s) * v;
  411| 	const lmin = (2 - s) * vmin;
  412| 	sl = s * vmin;
```

### only_reference example — ajv package/dist/core.js:251
message: unicorn/no-immediate-mutation: Combine this initialization with the preceding declaration.
```
  249|             return true;
  250|         let $schema;
  251|         $schema = schema.$schema;
  252|         if ($schema !== undefined && typeof $schema != "string") {
  253|             throw new Error("$schema must be a string");
```

## oxlint :: unicorn/new-for-builtins
reference: eslint, eslint:unicorn/new-for-builtins | only oxlint: 0 | only reference: 10 | packages: 2
top messages: [only_reference] unicorn/new-for-builtins: Use `new TypeError()` instead of `TypeError()`. ×10

### only_reference example — json5 package/lib/stringify.js:166
message: unicorn/new-for-builtins: Use `new TypeError()` instead of `TypeError()`.
```
  164|     function serializeObject (value) {
  165|         if (stack.indexOf(value) >= 0) {
  166|             throw TypeError('Converting circular structure to JSON5')
  167|         }
  168| 
```

### only_reference example — uuid package/dist/parse.js:4
message: unicorn/new-for-builtins: Use `new TypeError()` instead of `TypeError()`.
```
    2| function parse(uuid) {
    3|     if (!validate(uuid)) {
    4|         throw TypeError('Invalid UUID');
    5|     }
    6|     let v;
```

## oxlint :: block-scoped-var
reference: eslint, eslint:block-scoped-var | only oxlint: 6 | only reference: 3 | packages: 3
top messages: [only_rewrite] 'i' is used outside of binding context. ×3 || [only_rewrite] 'sm' is used outside of binding context. ×1 || [only_rewrite] 'uCode' is used outside of binding context. ×1 || [only_rewrite] 'codepoint' is used outside of binding context. ×1

### only_rewrite example — convert-source-map package/index.js:48
message: 'sm' is used outside of binding context.
```
   46| }
   47| 
   48| function readFromFileMap(sm, read) {
   49|   var r = exports.mapFileCommentRegex.exec(sm);
   50|   // for some odd reason //# .. captures in 1 and /* .. */ in 2
```

### only_rewrite example — iconv-lite package/encodings/dbcs-codec.js:440
message: 'uCode' is used outside of binding context.
```
  438|   var prevBytes = this.prevBytes; var prevOffset = this.prevBytes.length
  439|   var seqStart = -this.prevBytes.length // idx of the start of current parsed sequence.
  440|   var uCode
  441| 
  442|   for (var i = 0, j = 0; i < buf.length; i++) {
```

### only_rewrite example — tslib package/tslib.es6.js:207
message: 'i' is used outside of binding context.
```
  205| /** @deprecated */
  206| export function __spreadArrays() {
  207|     for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
  208|     for (var r = Array(s), k = 0, i = 0; i < il; i++)
  209|         for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
```

### only_reference example — tslib package/tslib.es6.js:211
message: block-scoped-var: 'r' declared on line 208 column 14 is used outside of binding context.
```
  209|         for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
  210|             r[k] = a[j];
  211|     return r;
  212| }
  213| 
```

## oxlint :: unicorn/custom-error-definition
reference: eslint, eslint:unicorn/custom-error-definition | only oxlint: 5 | only reference: 3 | packages: 5
top messages: [only_rewrite] Pass the error message to `super()` instead of setting `this.message`. ×3 || [only_reference] unicorn/custom-error-definition: Error constructors should accept an `options` parameter. ×2 || [only_rewrite] Invalid class name, use `YAMLExceptionError`. ×2 || [only_reference] unicorn/custom-error-definition: Error constructors should use a non-rest parameter named  ×1

### only_rewrite example — argparse package/lib/argparse.js:1134
message: Pass the error message to `super()` instead of setting `this.message`.
```
 1132| 
 1133|     constructor (argument, message) {
 1134|         super()
 1135|         this.name = 'ArgumentError'
 1136|         this._argument_name = _get_action_name(argument)
```

### only_rewrite example — js-yaml package/dist/js-yaml.cjs.js:1249
message: Invalid class name, use `YAMLExceptionError`.
```
 1247| * @category Main
 1248| */
 1249| var YAMLException = class YAMLException extends Error {
 1250| 	/**
 1251| 	* Optional `mark` contains source snippet data. Usually, use
```

### only_reference example — readable-stream package/lib/ours/primordials.js:13
message: unicorn/custom-error-definition: Error constructors should accept an `options` parameter.
```
   11| // This is a simplified version of AggregateError
   12| class AggregateError extends Error {
   13|   constructor(errors) {
   14|     if (!Array.isArray(errors)) {
   15|       throw new TypeError(`Expected input to be an Array, got ${typeof errors}`)
```

### only_reference example — yargs package/build/lib/yerror.js:2
message: unicorn/custom-error-definition: Error constructors should accept an `options` parameter.
```
    1| export class YError extends Error {
    2|     constructor(msg) {
    3|         super(msg || 'yargs error');
    4|         this.name = 'YError';
```

### only_reference example — postcss package/lib/css-syntax-error.js:8
message: unicorn/custom-error-definition: Error constructors should use a non-rest parameter named `options`.
```
    6| 
    7| class CssSyntaxError extends Error {
    8|   constructor(message, line, column, source, file, plugin) {
    9|     super(message)
   10|     this.name = 'CssSyntaxError'
```

## oxlint :: no-param-reassign
reference: eslint, eslint:no-param-reassign | only oxlint: 0 | only reference: 5 | packages: 3
top messages: [only_reference] no-param-reassign: Assignment to function parameter 'args'. ×3 || [only_reference] no-param-reassign: Assignment to function parameter 'children'. ×1 || [only_reference] no-param-reassign: Assignment to function parameter 'plugins'. ×1

### only_reference example — color-convert package/index.js:16
message: no-param-reassign: Assignment to function parameter 'args'.
```
   14| 
   15| 		if (arg0.length > 1) {
   16| 			args = arg0;
   17| 		}
   18| 
```

### only_reference example — readable-stream package/lib/ours/errors.js:287
message: no-param-reassign: Assignment to function parameter 'args'.
```
  285|     let msg
  286|     const len = args.length
  287|     args = (Array.isArray(args) ? args : [args]).map((a) => `"${a}"`).join(' or ')
  288|     switch (len) {
  289|       case 1:
```

### only_reference example — postcss package/lib/container.js:258
message: no-param-reassign: Assignment to function parameter 'children'.
```
  256| 
  257|   prepend(...children) {
  258|     children = children.reverse()
  259|     for (let child of children) {
  260|       let nodes = this.normalize(child, this.first, 'prepend').reverse()
```

## oxlint :: unicorn/prefer-string-starts-ends-with
reference: eslint, eslint:unicorn/prefer-string-starts-ends-with | only oxlint: 5 | only reference: 0 | packages: 3
top messages: [only_rewrite] Prefer String#startsWith over a regex with a caret. ×3 || [only_rewrite] Prefer String#endsWith over a regex with a dollar sign. ×2

### only_rewrite example — brace-expansion package/dist/commonjs/index.js:251
message: Prefer String#endsWith over a regex with a dollar sign.
```
  249|         // no need to expand pre, since it is guaranteed to be free of brace-sets
  250|         const pre = m.pre;
  251|         if (/\$$/.test(pre)) {
  252|             acc = combine(acc, pre + '{' + m.body + '}', [''], max, maxLength, dropEmpties && !m.post.length);
  253|             firstGroup = false;
```

### only_rewrite example — ignore package/index.js:1527
message: Prefer String#startsWith over a regex with a caret.
```
 1525| const setupWindows = () => {
 1526|   /* eslint no-control-regex: "off" */
 1527|   const makePosix = str => /^\\\\\?\\/.test(str)
 1528|   || /["<>|\u0000-\u001F]+/u.test(str)
 1529|     ? str
```

### only_rewrite example — yargs package/build/lib/parse-command.js:18
message: Prefer String#startsWith over a regex with a caret.
```
   16|         if (/\.+[\]>]/.test(cmd) && i === splitCommand.length - 1)
   17|             variadic = true;
   18|         if (/^\[/.test(cmd)) {
   19|             parsedCommand.optional.push({
   20|                 cmd: cmd.replace(bregex, '').split('|'),
```

## oxlint :: unicorn/no-array-method-this-argument
reference: eslint, eslint:unicorn/no-array-method-this-argument | only oxlint: 3 | only reference: 2 | packages: 2
top messages: [only_rewrite] Avoid using 'thisArg' with array iteration methods ×3 || [only_reference] unicorn/no-array-method-this-argument: Do not use the `this` argument in `Array#forEach()` ×1 || [only_reference] unicorn/no-array-method-this-argument: Do not use the `this` argument in `Array#map()`. ×1

### only_rewrite example — source-map package/lib/source-map-generator.js:238
message: Avoid using 'thisArg' with array iteration methods
```
  236| 
  237|     // Copy sourcesContents of applied map.
  238|     aSourceMapConsumer.sources.forEach(function (srcFile) {
  239|       const content = aSourceMapConsumer.sourceContentFor(srcFile);
  240|       if (content != null) {
```

### only_rewrite example — minimatch package/dist/esm/index.js:123
message: Avoid using 'thisArg' with array iteration methods
```
  121|         unescape: (s, options = {}) => orig.unescape(s, ext(def, options)),
  122|         escape: (s, options = {}) => orig.escape(s, ext(def, options)),
  123|         filter: (pattern, options = {}) => orig.filter(pattern, ext(def, options)),
  124|         defaults: (options) => orig.defaults(ext(def, options)),
  125|         makeRe: (pattern, options = {}) => orig.makeRe(pattern, ext(def, options)),
```

### only_reference example — source-map package/lib/source-map-generator.js:249
message: unicorn/no-array-method-this-argument: Do not use the `this` argument in `Array#forEach()`.
```
  247|         this.setSourceContent(srcFile, content);
  248|       }
  249|     }, this);
  250|   }
  251| 
```

## oxlint :: no-underscore-dangle
reference: eslint, eslint:no-underscore-dangle | only oxlint: 0 | only reference: 4 | packages: 1
top messages: [only_reference] no-underscore-dangle: Unexpected dangling '_' in '_end'. ×4

### only_reference example — ignore package/legacy.js:662
message: no-underscore-dangle: Unexpected dangling '_' in '_end'.
```
  660|       var _end = index;
  661|       do {
  662|         if (source[_end] === ESCAPE) {
  663|           _end++;
  664|         } else if (source[_end] === '(') {
```

## oxlint :: unicorn/require-module-specifiers
reference: eslint, eslint:unicorn/require-module-specifiers | only oxlint: 4 | only reference: 0 | packages: 3
top messages: [only_rewrite] Empty export specifier is not allowed ×4

### only_rewrite example — isexe package/dist/esm/options.js:1
message: Empty export specifier is not allowed
```
    1| export {};
    2| //# sourceMappingURL=options.js.map
```

### only_rewrite example — uuid package/dist/types.js:1
message: Empty export specifier is not allowed
```
    1| export {};
```

### only_rewrite example — yargs package/build/lib/typings/yargs-parser-types.js:1
message: Empty export specifier is not allowed
```
    1| export {};
```

## oxlint :: max-depth
reference: eslint, eslint:max-depth | only oxlint: 0 | only reference: 4 | packages: 1
top messages: [only_reference] max-depth: Blocks are nested too deeply (5). Maximum allowed is 4. ×4

### only_reference example — js-yaml package/dist/js-yaml.cjs.js:2059
message: max-depth: Blocks are nested too deeply (5). Maximum allowed is 4.
```
 2057| 		while (ch !== 0 && !isWsOrEol(ch) && !(inFlow && isFlowIndicator(ch))) {
 2058| 			if (ch === 33) if (!isNamed) {
 2059| 				tagHandle = state.input.slice(suffixStart - 1, state.position + 1);
 2060| 				if (!PATTERN_TAG_HANDLE.test(tagHandle)) throwError(state, "named tag handle cannot contain such characters");
 2061| 				isNamed = true;
```
