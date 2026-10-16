<!-- Verbatim prompt. Agent: Claude Opus 5.5 (claude-opus-5-5) in Claude Code; sent 2026-10-15T02:07:39 UTC. -->

You are triaging disagreements between Rust-rewritten linters and the tools they claim to re-implement (ruff vs flake8/pylint; oxlint and Biome vs ESLint + eslint-plugin-unicorn), found by running both on the 300 most-downloaded PyPI and 100 most-downloaded npm packages with default options (ruff and flake8 aligned at line length 88, Python 3.12). Your batches: /root/lt-tail/summaries/batch_01.md, batch_02.md, batch_03.md, batch_04.md. Each "## tool :: rule" section gives counts (only the rewrite reports / only the reference reports), the number of packages, the top messages and up to 3 real examples per side with source context.

For EVERY rule in your batches, assign exactly one class (the one explaining most of that rule's disagreements; mention a secondary class in the reason if mixed):
- BUG: likely a bug in the rewrite: it behaves differently from the rule it declares equivalent, on the same code, and this is not documented, not tracked, and not explained by options/defaults. Give a minimal reproducer idea.
- TRACKED: an open or closed issue in the rewrite's tracker already covers it (cite #number).
- DOC: a documented or clearly deliberate design difference (cite the doc text you found).
- LAG: the rewrite lags (or is ahead of) a newer release of the original (default or behaviour changed upstream).
- REF: the original tool is wrong (its own bug or false positive/negative) and the rewrite is right.
- CFG: explained by options, defaults or plugin configuration differences (including our setup).
- ANCHOR: the same finding is reported by both tools but at positions our matcher could not pair (e.g. different line of a multi-line statement beyond 2 lines, or a file-level vs line-level report). This is an artefact of the comparison, not a tool difference.
- PARSE: parsing/syntax-version/encoding differences (e.g. Python 2 test data, files one tool reads differently).
- UNCLEAR: cannot decide with reasonable effort (say what is missing).

Evidence you can use (read-only; do not post, comment or file anything anywhere):
- Docs offline: `/root/lt-setup-test/prefix/py/bin/ruff rule <CODE>` (ruff's own rule docs, often stating deviations from the original), `/root/lt-setup-test/prefix/js/node_modules/.bin/biome explain <ruleName>`, `/root/lt-setup-test/prefix/py/bin/pylint --help-msg=<msgid>`. Online: https://eslint.org/docs/latest/rules/<rule>, https://oxc.rs/docs/guide/usage/linter/rules/eslint/<rule>.html (or /unicorn/<rule>.html), flake8 plugin READMEs. Use curl -s -A "Mozilla/5.0" if a fetch tool fails.
- Trackers: `gh api -X GET search/issues -f q='repo:astral-sh/ruff <terms>'` (also oxc-project/oxc, biomejs/biome).
- Small local reproducers ARE allowed and encouraged for BUG candidates: write a tiny file under /root/lt-tail/scratch/ and run one tool at a time: `/root/lt-setup-test/prefix/py/bin/ruff check --isolated --select <CODE> f.py`, `/root/lt-setup-test/prefix/py/bin/flake8 --isolated --select <CODE> f.py`, ESLint/oxlint/biome binaries in `/root/lt-setup-test/prefix/js/node_modules/.bin/` (ESLint needs a flat config file with the rule; oxlint: `oxlint -A all -D <rule> f.js`; biome: a biome.json enabling the rule). The machine has little RAM: run one small process at a time, never lint whole packages, no loops over many files, no parallel runs.

Write your verdicts to /root/lt-tail/verdicts/batch_NN.tsv (one file per batch, NN as in the input), tab-separated with this header:
tool	rule	class	confidence(high/med/low)	only_rewrite	only_reference	packages	reason	evidence
Copy the counts from the section headers. Keep "reason" to one sentence and "evidence" to a doc quote, issue number or reproducer result.

When done, return a short summary: per batch, the count of rules per class, and the list of BUG and UNCLEAR rules with one line each. Be careful and literal: a wrong BUG costs us credibility with maintainers; a DOC needs a real doc statement or an unmistakably deliberate behaviour.
