# Long-tail triage tally

Counts from: re-run /root/lt-tail/rerun. Rules: 271.


## ruff: 163 rules, 312435 disagreements (25878 only-ruff, 286557 only-reference)

| Class | Rules | Disagreements | Share | only-rewrite | only-reference |
|---|---:|---:|---:|---:|---:|
| BUG | 8 | 10365 | 3.3% | 52 | 10313 |
| TRACKED | 10 | 7987 | 2.6% | 1297 | 6690 |
| REF | 37 | 3321 | 1.1% | 1095 | 2226 |
| DOC | 75 | 124506 | 39.9% | 17515 | 106991 |
| LAG | 5 | 368 | 0.1% | 362 | 6 |
| CFG | 16 | 161563 | 51.7% | 3407 | 158156 |
| ANCHOR | 10 | 4294 | 1.4% | 2122 | 2172 |
| UNCLEAR | 2 | 31 | 0.0% | 28 | 3 |

## oxlint: 60 rules, 5629 disagreements (2687 only-oxlint, 2942 only-reference)

| Class | Rules | Disagreements | Share | only-rewrite | only-reference |
|---|---:|---:|---:|---:|---:|
| BUG | 22 | 497 | 8.8% | 67 | 430 |
| TRACKED | 6 | 2079 | 36.9% | 1969 | 110 |
| REF | 1 | 4 | 0.1% | 0 | 4 |
| DOC | 6 | 148 | 2.6% | 65 | 83 |
| LAG | 14 | 664 | 11.8% | 107 | 557 |
| CFG | 1 | 10 | 0.2% | 0 | 10 |
| GAP | 1 | 2 | 0.0% | 2 | 0 |
| ANCHOR | 8 | 2217 | 39.4% | 472 | 1745 |
| UNCLEAR | 1 | 8 | 0.1% | 5 | 3 |

## biome: 48 rules, 11634 disagreements (1881 only-biome, 9753 only-reference)

| Class | Rules | Disagreements | Share | only-rewrite | only-reference |
|---|---:|---:|---:|---:|---:|
| BUG | 14 | 7384 | 63.5% | 318 | 7066 |
| TRACKED | 1 | 70 | 0.6% | 0 | 70 |
| REF | 1 | 2 | 0.0% | 0 | 2 |
| DOC | 15 | 3249 | 27.9% | 895 | 2354 |
| LAG | 5 | 643 | 5.5% | 497 | 146 |
| CFG | 5 | 150 | 1.3% | 117 | 33 |
| ANCHOR | 7 | 136 | 1.2% | 54 | 82 |

## BUG, UNCLEAR and UNTRIAGED rules

| Tool | Rule | Class | Conf | only-rewrite | only-reference | Pkgs | Reason |
|---|---|---|---|---:|---:|---:|---|
| ruff | E101 | BUG | med | 0 | 10058 | 13 | Ruff's E101 only flags a line whose own indentation mixes tabs and spaces, while pycodestyle flags every line whose indent character differs from the file's first indented line, so a file that indents |
| ruff | SIM102 | BUG | high | 8 | 136 | 54 | Ruff misses a collapsible `elif X:` whose body is a lone `if` whenever the first `if` branch holds more than one statement, because nested_if_body applies the "only child" check to the first branch's  |
| ruff | PLR1704 | BUG | high | 17 | 101 | 27 | Verified CONFIRMED (medium): a second loop over the same argument, or the else-copy of a loop, is not reported; ruff gives 3 of the 7 reports pylint's own functional test expects. |
| ruff | N801 | BUG | high | 27 | 0 | 10 | Verified CONFIRMED: `class Fine_:` is flagged; pep8-naming's tests mark it Okay; ruff#15939 called the deviation a bug but fixed only leading underscores. |
| ruff | B012 | BUG | high | 0 | 9 | 2 | ruff's B012 walks only the bodies of `if`/`try`/`with`/loops inside a `finally` block, so a `return` in an `elif`/`else` branch or in an `except` handler is never reported, while bugbear walks every c |
| ruff | F402 | BUG | high | 0 | 6 | 5 | ruff reports a loop variable that shadows an import only when both bindings are in the same branch, so a loop inside an `if` or `try` body that the import is not in is never reported, whereas pyflakes |
| ruff | F823 | BUG | high | 0 | 2 | 2 | ruff's F823 only looks at the latest binding of each name in a function and the binding that one directly shadows, so a global read before assignment is missed whenever the function assigns the name m |
| ruff | E711 | BUG | high | 0 | 1 | 1 | Verified CONFIRMED (minor): a None (or True, E712) that is the left side of a later comparison in a chain is never checked (`a is None == b`). |
| ruff | PLW0177 | UNCLEAR | high | 28 | 2 | 4 | Verified DEBATABLE: ruff also reports `in`/ordering comparisons with NaN; maintainers may keep it (NaN membership is unreliable anyway). |
| ruff | F602 | UNCLEAR | high | 0 | 1 | 1 | After the re-run: one flake8-only in an executing fuzz sample (repeated variable key `TargetVersion`); not examined. |
| oxlint | id-length | BUG | high | 0 | 152 | 15 | filed |
| oxlint | no-magic-numbers | BUG | high | 0 | 100 | 15 | filed |
| oxlint | unicorn/consistent-function-scoping | BUG | high | 51 | 5 | 15 | filed |
| oxlint | unicorn/prefer-string-replace-all | BUG | med | 6 | 36 | 16 | 33 of the 36 ESLint-only reports are .replace(REGEX_CONST, ...) where unicorn resolves a constant /…/g variable statically (it has done so since at least v63) and oxlint checks only inline regex liter |
| oxlint | sort-vars | BUG | med | 0 | 42 | 12 | oxlint compares each declarator with the one just before it, while ESLint compares with the last declarator that was in order, so ESLint reports every declarator below the running maximum and oxlint o |
| oxlint | no-shadow | BUG | high | 0 | 27 | 2 | not filed, conflicts #19461 |
| oxlint | unicorn/prefer-regexp-test | BUG | high | 4 | 22 | 4 | oxlint's boolean-context check has no LogicalExpression case, so a .match()/.exec() that is an operand of && or || in a condition is never reported (all 22 ESLint-only, yargs-parser, brace-expansion,  |
| oxlint | prefer-template | BUG | high | 0 | 11 | 6 | oxlint skips every + expression that has any + ancestor, even across a conditional, call or function body, whereas ESLint merges only directly chained concatenations, so nested concatenations such as  |
| oxlint | no-useless-assignment | BUG | med | 2 | 9 | 5 | oxlint treats a class field initializer as code that runs once, so it flags id = ++ID on a module counter (2 oxlint-only, minimatch), and it misses dead stores that ESLint finds (a chained o.p = x = f |
| oxlint | no-param-reassign | BUG | high | 0 | 5 | 3 | oxlint walks only FormalParameter items, so reassigning a rest parameter (...args, ...children, ...plugins) is never reported; all 5 ESLint-only reports are rest parameters. |
| oxlint | max-depth | BUG | high | 0 | 4 | 1 | oxlint treats any if whose parent is an if as an else-if continuation, so if (a) if (b) {} (b is the consequent) adds no depth; ESLint skips only real else-ifs, so js-yaml's if (ch === 33) if (!isName |
| oxlint | unicorn/prefer-at | BUG | high | 2 | 1 | 3 | Two oxlint defects explain 2 of the 3 reports: x.slice(-1)[0] in an initializer is reported twice (once from the member-expression path and once from the call-expression path, commander), and it is ne |
| oxlint | no-div-regex | BUG | high | 0 | 3 | 1 | filed |
| oxlint | sort-imports | BUG | high | 0 | 3 | 1 | oxlint collects only the leading run of import declarations and stops at the first other statement, so imports after a statement such as TypeScript's hoisted var _a, _b, _c; are never checked (yargs-p |
| oxlint | no-loop-func | BUG | high | 0 | 3 | 1 | For var bindings declared outside the loop oxlint counts only writes inside the loop, while ESLint treats any write after the loop start as unsafe, so a closure created in a loop that reads a var assi |
| oxlint | no-lonely-if | BUG | high | 0 | 2 | 2 | oxlint returns early when the outer if is itself an else-if, so the final else { if (...) {} } of an if / else if / else chain is never reported (ajv parseJson, ws extension); ESLint reports it. |
| oxlint | unicorn/catch-error-name | BUG | high | 0 | 2 | 1 | oxlint skips any unused catch parameter whose name starts with an underscore, while unicorn (and oxlint's own docs) exempt only an unused _, so catch (_err) {} is reported by ESLint only (yargs). |
| oxlint | class-methods-use-this | BUG | high | 1 | 0 | 1 | oxlint ignores this used in a parameter default, so ajv's errorsText(errors = this.errors, ...) is reported as a method that does not use this; ESLint counts the default value as part of the method. |
| oxlint | no-self-compare | BUG | high | 1 | 0 | 1 | not filed, debatable |
| oxlint | no-setter-return | BUG | high | 0 | 1 | 1 | filed |
| oxlint | unicorn/prefer-native-coercion-functions | BUG | med | 0 | 1 | 1 | oxlint skips every function whose parent is an object property, so qs's RFC3986: function (value) { return String(value) } (and shorthand methods) are never reported, while unicorn has reported both f |
| oxlint | max-params | BUG | high | 0 | 1 | 1 | oxlint counts only params.items, which excludes the rest parameter, so (str1, str2, count, ...args) => {} has 4 parameters for ESLint and 3 for oxlint (yargs browser shim). |
| oxlint | unicorn/custom-error-definition | UNCLEAR | high | 5 | 3 | 5 | Verified DEBATABLE: oxlint also checks named class expressions; unicorn's narrower scope looks accidental. |
| biome | style/useSingleVarDeclarator | BUG | high | 75 | 6578 | 82 | filed |
| biome | complexity/useMaxParams | BUG | med | 0 | 267 | 40 | biome migrate eslint turns max-params (ESLint default max 3) into "useMaxParams": "error" without a max, and Biome's default is 4, so all 267 four-parameter functions stop being reported; even an expl |
| biome | suspicious/noDoubleEquals | BUG | high | 0 | 193 | 24 | filed |
| biome | suspicious/noReturnAssign | BUG | high | 98 | 0 | 10 | filed |
| biome | correctness/noUndeclaredVariables | BUG | high | 78 | 0 | 6 | 67 of the 78 Biome-only reports are 'The arguments variable is undeclared' for arguments used inside class constructors and methods (argparse, whatwg-url), which is always defined there; plain functio |
| biome | complexity/noArguments | BUG | high | 52 | 0 | 10 | Biome reports every use of arguments, including the non-computed member access arguments.length (48 of 52), which ESLint's prefer-rest-params deliberately allows, although Biome lists the rule as the  |
| biome | style/noParameterAssign | BUG | med | 0 | 12 | 6 | Biome does not check parameters bound by destructuring, so cwd = toPath(cwd) in function ({ cwd = ... } = {}), v = ... in ([k, v]) => and minimatch's ([$0, ext = '']) are ESLint-only (11 of 12); the l |
| biome | suspicious/noEmptyBlockStatements | BUG | med | 0 | 8 | 1 | Biome skips an empty block that is followed by a comment on the same line, as in eslint-scope's attach() {} // eslint-disable-line ..., although its doc exempts only blocks that contain a comment; ESL |
| biome | performance/noAwaitInLoops | BUG | high | 3 | 4 | 4 | Biome reports only the first await inside each loop and repeats it once per enclosing loop, so a second await in the same loop body is missed (postcss 336, readable-stream, find-up) and an await insid |
| biome | suspicious/noGlobalAssign | BUG | med | 7 | 0 | 3 | Biome treats exports as a read-only global and reports the common CommonJS idiom module.exports = exports = X (ajv, semver, whatwg-url), even in a .cjs file, where exports is the module wrapper's para |
| biome | suspicious/noMisleadingCharacterClass | BUG | med | 5 | 1 | 3 | Biome reports the standard identifier-part class [$_\u200C\u200D\p{ID_Continue}] (js-tokens, path-to-regexp) as a joined character sequence although the ZWJ is followed by a property escape, not a cha |
| biome | suspicious/useAwait | BUG | med | 0 | 1 | 1 | Biome skips async arrow functions with an expression body (p-limit's (async () => function_(...arguments_))()), because the rule returns early when the body has no statement list; ESLint's require-awa |
| biome | correctness/noSetterReturn | BUG | high | 0 | 1 | 1 | filed |
| biome | style/noNegationElse | BUG | med | 0 | 1 | 1 | Biome misses a negated test when it is parenthesized, as in json5's (propertyString !== undefined) ? propertyString : 'null'; the same ternary without parentheses is reported by both. |

No longer disagree (21): ruff::B004 [CFG], ruff::B011 [CFG], ruff::B026 [CFG], ruff::C400 [CFG], ruff::C402 [CFG], ruff::C408 [CFG], ruff::C409 [CFG], ruff::C414 [CFG], ruff::C416 [CFG], ruff::E702 [CFG], ruff::E703 [CFG], ruff::F403 [CFG], ruff::F632 [CFG], ruff::F901 [CFG], ruff::PLE0001 [CFG], ruff::PLE0011 [CFG], ruff::PLR0022 [CFG], ruff::PLW0012 [CFG], ruff::SIM208 [CFG], ruff::SIM211 [CFG], ruff::W292 [CFG]
