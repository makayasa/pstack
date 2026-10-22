---
name: setup-pstack
description: Configure pstack models per role and reasoning budget in Pi.
---

# Setup pstack

Read [Pi + herdr runtime](../poteto-mode/references/pi-herdr.md) first. This skill configures models. It does not create workers or require herdr control access.

Keep pstack's budget-first setup and per-role mapping. Write `~/.agents/pstack-models.md`. Do not modify Pi's global model defaults, credentials, installed extensions, or settings. Pi does not automatically load this Markdown file. Each pstack skill reads it before delegation.

## Detect and read

1. Inspect `pi --help` and run `pi --list-models`.
2. Treat each provider and exact model ID as a pair. Preserve slashes, colons, and brackets in IDs. Catalog presence does not prove authentication. Do not print secrets or launch a paid model probe without a reason.
3. Read existing pstack settings if present. Preserve configured model families, panel lists, and aliases on reruns. Show obsolete role lines before removing them. Legacy Cursor slugs need a confirmed Pi mapping, not a string rewrite.

## Choose budget and models

Ask for a budget with numbered chat options:

- `unlimited` uses `max` reasoning.
- `large` uses `xhigh` reasoning.
- `medium` uses `high` reasoning.
- `small` uses `medium` reasoning.

`large` matches the upstream starting effort. Budget is not a dollar cap and does not set concurrency. Keep the model identity separate from its thinking level. Before saving, inspect installed Pi model documentation or metadata for supported reasoning levels. If a model cannot honor the requested level, offer the supported level for confirmation. Do not silently downgrade or strip an ID suffix.

Show every role with its model selection and effective reasoning level. Offer models actually detected in Pi, plus `auto` and `inherit-parent`. Both aliases mean the coordinator's exact current provider and model, not whatever Pi chooses at startup. Resolve that identity before using an alias. If it cannot be established, ask for an explicit model.

Use upstream model families as suggestions, not runnable defaults. Code-oriented roles can use an available code model. Judgment and prose roles can use an available judgment model. The user confirms the mapping. Do not hardcode a provider specific to this machine. For panels, suggest two distinct model families when available. Warn if all entries resolve to one family without silently adding or removing seats.

Panel roles accept a list. Each entry creates one worker, including repeated aliases. `arena cross-judge pool` is a pool from which one judge is selected, preferably from a different family than the coordinator. Preserve all role labels below, including labels containing commas. Separate a role from its value at the first `: `, not every colon.

## Validate and save

Validate all explicit provider and model pairs against the detected catalog. Unknown models, unresolved aliases, and unsupported reasoning choices require confirmation before saving. Do not invent replacements. Show the complete mapping and ask the user to confirm once.

Write the file only after confirmation. Use one `# budget` line, one line per role, and optional `# thinking <role>: <level>` lines for confirmed reasoning exceptions. With no exception, a role uses the budget level. An exception covers all seats in that role. If seats cannot share a supported level, ask the user to change the panel or approve a common level.

This shape uses aliases as placeholders until the user chooses models:

```text
# pstack model configuration for Pi.
# Explicit values are provider/model-id. auto and inherit-parent use the coordinator's exact model.
# budget: large (xhigh)
feature, refactoring: inherit-parent
bug-fix: inherit-parent
perf-issue: inherit-parent
hillclimb: inherit-parent
judgment and prose: inherit-parent
hardest tasks: inherit-parent
how explorer: inherit-parent
how explainer: inherit-parent
why investigators: inherit-parent
why synthesizer: inherit-parent
reflect tooling: inherit-parent
reflect judgment, divergent, synthesizer: inherit-parent
arena runners: inherit-parent, inherit-parent
arena cross-judge pool: inherit-parent, inherit-parent
swarm workers: inherit-parent
architect runners: inherit-parent, inherit-parent
interrogate reviewers: inherit-parent, inherit-parent
```

Do not save this placeholder mapping without confirmation. Preserve panel lengths on reruns. Write atomically so an interrupted setup cannot leave a partial mapping. Report the path and any confirmed exceptions. New tasks read the updated file. Already-running workers keep their launch model.

## Optional project verification

If the project lacks an app verification skill, offer `/skill:create-verification-skill` once. If it lacks a formal verification skill, offer `/skill:create-formal-verification-skill` once. Neither is required to save model settings. Do not generate either without approval.
