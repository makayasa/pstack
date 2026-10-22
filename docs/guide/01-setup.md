# Set up pstack in Pi

## Load the fork

Open a herdr-managed terminal in this checkout and run:

```sh
pi --skill ./skills
```

To register it for later Pi sessions, review the package and run `pi install /absolute/path/to/pstack`. Do not load another pstack copy at the same time. Duplicate skill names can keep the older copy active.

Run `/reload` after changing skills during an active Pi session. Loading this checkout does not change your model settings or install an orchestration service.

## Pick budget and models

```text
/skill:setup-pstack
```

Setup detects models through `pi --list-models`, asks for a reasoning budget, and shows every role for confirmation. It writes `~/.agents/pstack-models.md`. Skills read that file before delegation. Already-running workers retain their launch settings.

The budgets are `unlimited` for `max`, `large` for `xhigh`, `medium` for `high`, and `small` for `medium`. Unsupported reasoning levels require a confirmed alternative. Budget does not cap money or concurrency.

Explicit models use `provider/model-id`. `auto` and `inherit-parent` mean the coordinator's exact model. Panels create one worker per list entry. Setup preserves custom mappings and panel lengths on reruns. Missing or unavailable entries block delegation rather than selecting a hidden fallback.

Setup offers project verification and formal verification skills once when they are absent. You may decline either offer. They are not required for saving the mapping.

## Start a task

```text
/skill:poteto-mode add a --json flag. Preserve existing text output and verify both modes. Keep the result local.
```

The coordinator chooses a playbook and keeps its checklist visible. Workers appear only where a skill asks for them. Watch their labeled herdr sessions. Every writer gets its own branch and worktree.

To publish, explicitly ask for a PR or MR. That grants the necessary branch push, not merge or deploy. To take over a worker, tell the coordinator. Return control explicitly before it sends more tasks.

Pi uses `/skill:name`. This fork does not provide Cursor Custom Modes or a background scheduler. Start each new task explicitly.

Next: [Route work](02-poteto-mode.md). See [live verification](../harness/pi-herdr.md#verify-in-a-test-repository) before treating delegation as proven.
