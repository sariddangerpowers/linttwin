
## biome :: style/useThrowNewError
reference: eslint, eslint:unicorn/throw-new-error | only biome: 0 | only reference: 7 | packages: 1
top messages: [only_reference] unicorn/throw-new-error: Use `new` when creating an error. ×7

### only_reference example — yargs-parser package/build/lib/yargs-parser.js:423
message: unicorn/throw-new-error: Use `new` when creating an error.
```
  421|             if (toEat === 0) {
  422|                 if (!isUndefined(argAfterEqualSign)) {
  423|                     error = Error(__('Argument unexpected for: %s', key));
  424|                 }
  425|                 setArg(key, defaultValue(key));
```

## biome :: style/useGlobalThis
reference: eslint, eslint:unicorn/prefer-global-this | only biome: 6 | only reference: 0 | packages: 4
top messages: [only_rewrite] Prefer globalThis over window, self and global. ×6

### only_rewrite example — form-data package/lib/browser.js:4
message: Prefer globalThis over window, self and global.
```
    2| 
    3| /* eslint-env browser */
    4| module.exports = typeof self === 'object' ? self.FormData : window.FormData;
```

### only_rewrite example — debug package/src/browser.js:119
message: Prefer globalThis over window, self and global.
```
  117| 	// initialized. Since we know we're in Chrome, we'll just detect this case
  118| 	// explicitly
  119| 	if (typeof window !== 'undefined' && window.process && (window.process.type === 'renderer' || window.process.__nwjs)) {
  120| 		return true;
  121| 	}
```

### only_rewrite example — pretty-format package/build/index.js:762
message: Prefer globalThis over window, self and global.
```
  760| const isWindow = val =>
  761| // eslint-disable-next-line unicorn/prefer-global-this
  762| typeof window !== 'undefined' && val === window;
  763| const SYMBOL_REGEXP = /^Symbol\((.*)\)(.*)$/;
  764| const NEWLINE_REGEXP = /\n/gi;
```

## biome :: style/useConsistentArrowReturn
reference: eslint, eslint:arrow-body-style | only biome: 0 | only reference: 6 | packages: 4
top messages: [only_reference] arrow-body-style: Unexpected block statement surrounding arrow body; move the returned val ×5 || [only_reference] arrow-body-style: Unexpected block statement surrounding arrow body; parenthesize the retu ×1

### only_reference example — commander package/lib/help.js:48
message: arrow-body-style: Unexpected block statement surrounding arrow body; move the returned value immediately after the `=>`.
```
   46|     }
   47|     if (this.sortSubcommands) {
   48|       visibleCommands.sort((a, b) => {
   49|         // @ts-ignore: because overloaded return type
   50|         return a.name().localeCompare(b.name());
```

### only_reference example — fs-extra package/lib/fs/index.js:46
message: arrow-body-style: Unexpected block statement surrounding arrow body; move the returned value immediately after the `=>`.
```
   44|   'utimes',
   45|   'writeFile'
   46| ].filter(key => {
   47|   // Some commands are not available on some systems. Ex:
   48|   // fs.cp was added in Node.js v16.7.0
```

### only_reference example — source-map package/lib/source-map-consumer.js:776
message: arrow-body-style: Unexpected block statement surrounding arrow body; parenthesize the returned value and move it immediately after the `=>`.
```
  774|             aSourceMapURL
  775|           );
  776|           return cons.then(consumer => {
  777|             return {
  778|               generatedOffset: {
```

## biome :: style/useCollapsedElseIf
reference: eslint, eslint:no-lonely-if | only biome: 3 | only reference: 3 | packages: 3
top messages: [only_reference] no-lonely-if: Unexpected if as the only statement in an else block. ×3 || [only_rewrite] This if statement can be collapsed into an else if statement. ×3

### only_rewrite example — argparse package/lib/argparse.js:3236
message: This if statement can be collapsed into an else if statement.
```
 3234|                 if (action.required) {
 3235|                     required_actions.push(_get_action_name(action))
 3236|                 } else {
 3237|                     // Convert action default now instead of doing it before
 3238|                     // parsing arguments to avoid calling convert functions
```

### only_rewrite example — yargs-parser package/build/lib/yargs-parser.js:654
message: This if statement can be collapsed into an else if statement.
```
  652|                     setConfigObject(value, fullKey);
  653|                 }
  654|                 else {
  655|                     // setting arguments via CLI takes precedence over
  656|                     // values within the config file.
```

### only_rewrite example — ws package/lib/extension.js:94
message: This if statement can be collapsed into an else if statement.
```
   92|         throw new SyntaxError(`Unexpected character at index ${i}`);
   93|       }
   94|     } else {
   95|       //
   96|       // The value of a quoted-string after unescaping must conform to the
```

### only_reference example — argparse package/lib/argparse.js:3241
message: no-lonely-if: Unexpected if as the only statement in an else block.
```
 3239|                     // twice (which may fail) if the argument was given, but
 3240|                     // only if it was defined already in the namespace
 3241|                     if (action.default !== undefined &&
 3242|                         typeof action.default === 'string' &&
 3243|                         hasattr(namespace, action.dest) &&
```

### only_reference example — yargs-parser package/build/lib/yargs-parser.js:657
message: no-lonely-if: Unexpected if as the only statement in an else block.
```
  655|                     // setting arguments via CLI takes precedence over
  656|                     // values within the config file.
  657|                     if (!hasKey(argv, fullKey.split('.')) || (checkAllAliases(fullKey, flags.arrays) && configuration['combine-arrays'])) {
  658|                         setArg(fullKey, value);
  659|                     }
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

## biome :: suspicious/noMisleadingCharacterClass
reference: eslint, eslint:no-misleading-character-class | only biome: 5 | only reference: 1 | packages: 3
top messages: [only_rewrite] A character class cannot match a joined character sequence. ×5 || [only_reference] no-misleading-character-class: Unexpected combined character in character class. ×1

### only_rewrite example — js-tokens package/index.js:4
message: A character class cannot match a joined character sequence.
```
    2| // License: MIT.
    3| var HashbangComment, Identifier, JSXIdentifier, JSXPunctuator, JSXString, JSXText, KeywordsWithExpressionAfter, KeywordsWithNoLineTerminatorAfter, LineTerminatorSequence, MultiLineComment, Newline, NumericLiteral, Punctuator, RegularExpressionLiteral, SingleLineComment, StringLiteral, Template, Toke
    4| RegularExpressionLiteral = /\/(?![*\/])(?:\[(?:[^\]\\\n\r\u2028\u2029]+|\\.)*\]?|[^\/[\\\n\r\u2028\u2029]+|\\.)*(\/[$_\u200C\u200D\p{ID_Continue}]*|\\)?/yu;
    5| Punctuator = /--|\+\+|=>|\.{3}|\??\.(?!\d)|(?:&&|\|\||\?\?|[+\-%&|^]|\*{1,2}|<{1,2}|>{1,3}|!=?|={1,2}|\/(?![\/*]))=?|[?~,:;[\](){}]/y;
    6| Identifier = /(\x23?)(?=[$_\p{ID_Start}\\])(?:[$_\u200C
```

### only_rewrite example — path-to-regexp package/dist/index.js:12
message: A character class cannot match a joined character sequence.
```
   10| const NOOP_VALUE = (value) => value;
   11| const ID_START = /^[$_\p{ID_Start}]$/u;
   12| const ID_CONTINUE = /^[$\u200c\u200d\p{ID_Continue}]$/u;
   13| const ID = /^[$_\p{ID_Start}][$\u200c\u200d\p{ID_Continue}]*$/u;
   14| /**
```

### only_reference example — ajv package/dist/runtime/quote.js:5
message: no-misleading-character-class: Unexpected combined character in character class.
```
    3| const rxEscapable = 
    4| // eslint-disable-next-line no-control-regex, no-misleading-character-class
    5| /[\\"\u0000-\u001f\u007f-\u009f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g;
    6| const escaped = {
    7|     "\b": "\\b",
```

## biome :: complexity/noUselessStringConcat
reference: eslint, eslint:no-useless-concat | only biome: 0 | only reference: 6 | packages: 2
top messages: [only_reference] no-useless-concat: Unexpected string concatenation of literals. ×6

### only_reference example — whatwg-url package/lib/URLSearchParams.js:118
message: no-useless-concat: Unexpected string concatenation of literals.
```
  116|               if (!utils.isObject(curArg)) {
  117|                 throw new globalObject.TypeError(
  118|                   "Failed to construct 'URLSearchParams': parameter 1" + " sequence" + " is not an iterable object."
  119|                 );
  120|               } else {
```

### only_reference example — minimatch package/dist/commonjs/brace-expressions.js:10
message: no-useless-concat: Unexpected string concatenation of literals.
```
    8|     '[:alnum:]': ['\\p{L}\\p{Nl}\\p{Nd}', true],
    9|     '[:alpha:]': ['\\p{L}\\p{Nl}', true],
   10|     '[:ascii:]': ['\\x' + '00-\\x' + '7f', false],
   11|     '[:blank:]': ['\\p{Zs}\\t', true],
   12|     '[:cntrl:]': ['\\p{Cc}', true],
```

## biome :: style/useDefaultSwitchClause
reference: eslint, eslint:default-case | only biome: 4 | only reference: 0 | packages: 3
top messages: [only_rewrite] Expected a default switch clause. ×4

### only_rewrite example — chalk package/source/vendor/supports-color/index.js:165
message: Expected a default switch clause.
```
  163| 		const version = Number.parseInt((env.TERM_PROGRAM_VERSION || '').split('.', 1)[0], 10);
  164| 
  165| 		switch (env.TERM_PROGRAM) {
  166| 			case 'iTerm.app': {
  167| 				return version >= 3 ? 3 : 2;
```

### only_rewrite example — color-convert package/conversions.js:82
message: Expected a default switch clause.
```
   80| 	let s;
   81| 
   82| 	switch (max) {
   83| 		case min: {
   84| 			h = 0;
```

### only_rewrite example — supports-color package/index.js:171
message: Expected a default switch clause.
```
  169| 		const version = Number((env.TERM_PROGRAM_VERSION || '').split('.', 1)[0]);
  170| 
  171| 		switch (env.TERM_PROGRAM) {
  172| 			case 'iTerm.app': {
  173| 				return version >= 3 ? 3 : 2;
```

## biome :: complexity/noUselessSwitchCase
reference: eslint, eslint:unicorn/no-useless-switch-case | only biome: 2 | only reference: 1 | packages: 2
top messages: [only_rewrite] Useless case clause. ×2 || [only_reference] unicorn/no-useless-switch-case: Useless case in switch statement. ×1

### only_rewrite example — color-convert package/conversions.js:451
message: Useless case clause.
```
  449| 	switch (i) {
  450| 		default:
  451| 		case 6:
  452| 		case 0: { r = v;  g = n;  b = wh; break;
  453| 		}
```

### only_reference example — entities package/dist/index.js:78
message: unicorn/no-useless-switch-case: Useless case in switch statement.
```
   76|         }
   77|         // biome-ignore lint/complexity/noUselessSwitchCase: we get an error for the switch not being exhaustive
   78|         case EncodingMode.Extensive:
   79|         default: {
   80|             return (level === EntityLevel.HTML ? encodeHTML : encodeXML)(input);
```

## biome :: suspicious/noConsole
reference: eslint, eslint:no-console | only biome: 3 | only reference: 0 | packages: 1
top messages: [only_rewrite] Don't use console. ×3

### only_rewrite example — debug package/src/browser.js:135
message: Don't use console.
```
  133| 	return (typeof document !== 'undefined' && document.documentElement && document.documentElement.style && document.documentElement.style.WebkitAppearance) ||
  134| 		// Is firebug? http://stackoverflow.com/a/398120/376773
  135| 		(typeof window !== 'undefined' && window.console && (window.console.firebug || (window.console.exception && window.console.table))) ||
  136| 		// Is firefox >= v31?
  137| 		// https://developer.mozilla.org/en-US/docs/Tools/Web_Console#Styling_messages
```

## biome :: correctness/noEmptyCharacterClassInRegex
reference: eslint, eslint:no-empty-character-class | only biome: 3 | only reference: 0 | packages: 2
top messages: [only_rewrite] The regular expression includes this negated empty character class. ×3

### only_rewrite example — js-tokens package/index.js:7
message: The regular expression includes this negated empty character class.
```
    5| Punctuator = /--|\+\+|=>|\.{3}|\??\.(?!\d)|(?:&&|\|\||\?\?|[+\-%&|^]|\*{1,2}|<{1,2}|>{1,3}|!=?|={1,2}|\/(?![\/*]))=?|[?~,:;[\](){}]/y;
    6| Identifier = /(\x23?)(?=[$_\p{ID_Start}\\])(?:[$_\u200C\u200D\p{ID_Continue}]+|\\u[\da-fA-F]{4}|\\u\{[\da-fA-F]+\})+/yu;
    7| StringLiteral = /(['"])(?:[^'"\\\n\r]+|(?!\1)['"]|\\(?:\r\n|[^]))*(\1)?/y;
    8| NumericLiteral = /(?:0[xX][\da-fA-F](?:_?[\da-fA-F])*|0[oO][0-7](?:_?[0-7])*|0[bB][01](?:_?[01])*)n?|0n|[1-9](?:_?\d)*n|(?:(?:0(?!\d)|0\d*[89]\d*|[1-9](?:_?\d)*)(?:\.(?:\d(?:_?\d)*)?)?|\.\d(?:_?\d)*)(?:[eE][+-]?\d(?:_?\d)*)?|0[0-7]+/y;
    9| Template = /[`}](?:[^`\\$]+|\\[^]|\$(?!\{))*(`|\$\{)?/y;
```

### only_rewrite example — postcss package/lib/parser.js:191
message: The regular expression includes this negated empty character class.
```
  189|       node.raws.right = ''
  190|     } else {
  191|       let match = text.match(/^(\s*)([^]*\S)(\s*)$/)
  192|       node.text = match[2]
  193|       node.raws.left = match[1]
```

## biome :: correctness/noInvalidConstructorSuper
reference: eslint, eslint:constructor-super | only biome: 0 | only reference: 2 | packages: 1
top messages: [only_reference] constructor-super: Unexpected duplicate 'super()'. ×2

### only_reference example — source-map package/lib/source-map-consumer.js:175
message: constructor-super: Unexpected duplicate 'super()'.
```
  173| class BasicSourceMapConsumer extends SourceMapConsumer {
  174|   constructor(aSourceMap, aSourceMapURL) {
  175|     return super(INTERNAL).then(that => {
  176|       let sourceMap = aSourceMap;
  177|       if (typeof aSourceMap === "string") {
```

## biome :: suspicious/useAwait
reference: eslint, eslint:require-await | only biome: 0 | only reference: 1 | packages: 1
top messages: [only_reference] require-await: Async arrow function has no 'await' expression. ×1

### only_reference example — p-limit package/index.js:34
message: require-await: Async arrow function has no 'await' expression.
```
   32| 	const run = async (function_, resolve, arguments_) => {
   33| 		// Execute the function and capture the result promise
   34| 		const result = (async () => function_(...arguments_))();
   35| 
   36| 		// Resolve immediately with the promise (don't wait for completion)
```

## biome :: style/noNegationElse
reference: eslint, eslint:no-negated-condition | only biome: 0 | only reference: 1 | packages: 1
top messages: [only_reference] no-negated-condition: Unexpected negated condition. ×1

### only_reference example — json5 package/lib/stringify.js:240
message: no-negated-condition: Unexpected negated condition.
```
  238|         for (let i = 0; i < value.length; i++) {
  239|             const propertyString = serializeProperty(String(i), value)
  240|             partial.push((propertyString !== undefined) ? propertyString : 'null')
  241|         }
  242| 
```

## biome :: suspicious/noFallthroughSwitchClause
reference: eslint, eslint:no-fallthrough | only biome: 1 | only reference: 0 | packages: 1
top messages: [only_rewrite] This case is falling through to the next case. ×1

### only_rewrite example — semver package/ranges/min-version.js:29
message: This case is falling through to the next case.
```
   27|       const compver = new SemVer(comparator.semver.version)
   28|       switch (comparator.operator) {
   29|         case '>':
   30|           if (compver.prerelease.length === 0) {
   31|             compver.patch++
```

## biome :: style/noYodaExpression
reference: eslint, eslint:yoda | only biome: 0 | only reference: 1 | packages: 1
top messages: [only_reference] yoda: Expected literal to be on the right side of <=. ×1

### only_reference example — source-map package/lib/base64.js:15
message: yoda: Expected literal to be on the right side of <=.
```
   13|  */
   14| exports.encode = function (number) {
   15|   if (0 <= number && number < intToCharMap.length) {
   16|     return intToCharMap[number];
   17|   }
```
