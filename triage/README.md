# Triage with LLM agents

LintTwin's report is a triage queue, not a bug list: most disagreements between a rewrite and its original come from
documented design differences, configuration, version lag, or the same problem reported at different positions. We
triaged it with LLM agents: Claude Opus 5.5 (`claude-opus-5-5`) running in Claude Code, with a shell holding both tools
at the study's pinned versions, read access to their documentation, source code and issue trackers, and no permission
to post anything.

**We found the study's bugs with LintTwin and this protocol.** `linttwin triage` writes a report's rules as cases,
with the protocol's two prompts, and `linttwin triage --collect` checks the agents' verdicts against the protocol and
tallies them. `check` marks the causes the study found, which ship with the tool in `src/linttwin/known_causes.tsv`:
one per disagreeing rule (the classes of `tally.md`) and per failing safe fix, with the issue of every bug we reported.
This directory holds the study's two passes: their inputs, prompts and verdicts.

**Pass 1 (14 Oct 2026).** One agent, in an open-ended session without fixed prompts, applied the same steps to the
largest disagreement groups and every rule with failing safe fixes. It found 49 root causes, 17 of them new bugs
(Table II of the paper; `linttwin findings` re-runs their reproducers).

**Pass 2 (batch, 15 Oct 2026; this directory).**

| Step | What | Files |
|---|---|---|
| Inputs | Every rule with disagreements that pass 1 had not covered: 257 rules (ruff 170, oxlint 46, Biome 41), each with its counts, top messages and up to three examples per side with source context. | `inputs/batch_01.md` … `batch_12.md` |
| Classify | Three agents, four batches each, assign one class per rule: BUG, TRACKED, DOC, LAG, REF, CFG, ANCHOR, PARSE or UNCLEAR. | `prompts/1_classify_*.md`, `verdicts/batch_NN.tsv` |
| Verify | One agent per rewrite tries to refute every BUG or UNCLEAR rule and the secondary candidates the classifiers noted: 55 rules (ruff 19, oxlint 23, Biome 13). It confirmed bugs in 47 (ruff 13, oxlint 21, Biome 13). | `candidates/`, `prompts/2_verify_*.md`, `verified/*.tsv` |
| Check | Before filing, every reproducer was re-run on the released versions and the trackers were searched again. This removed oxlint's `max-depth` (the difference follows a change in ESLint 10) and one `no-useless-assignment` finding that another user had reported a few hours earlier. | |
| File | ruff: 9 rules, plus `UP034` from ruff's records of its own failing fixes, in [astral-sh/ruff#29422](https://github.com/astral-sh/ruff/issues/29422); oxlint: 20 rules in [oxc-project/oxc#27746](https://github.com/oxc-project/oxc/issues/27746). Not reported yet: Biome 13 rules, ruff 4 rules. | |

The prompts are verbatim. The three verifiers were interrupted by a usage limit and resumed with the messages in
`prompts/3_resume_messages.md`. The pass took its six agents about four hours and 614 million tokens, nearly all of
them read from the prompt cache (0.12 million output tokens).

**Runs.** Pass 2's inputs come from the run of 14 Oct. Three harness fixes followed on 15 Oct: flake8 plugin crashes
are detected and the batch is re-run file by file, pylint's pragma messages are filtered out, and the JavaScript matcher
no longer depends on output order. `tally.md` maps the verdicts of both passes onto the final run, in which 271 rules
disagree (Table I of the paper). Two corrections followed the first tally: Biome declined `noReturnAssign` as intended
behaviour, and oxlint's `max-depth` follows a change in ESLint 10, so `tally.md` now counts them as DOC and LAG. Neither
changes a rounded share in Table I.

The maintainers' answers are on the two issues; the top-level README tracks the bugs of pass 1.
