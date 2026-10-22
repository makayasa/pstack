# Pi + herdr runtime

This fork uses Pi for the coordinator and workers on one machine. Read this file before executing any pstack skill or playbook, including direct skill invocations. These runtime rules override upstream transport, model fallback, cloud, retry, cleanup, and permission instructions. Keep each skill's purpose, prompts, role names, panel entries, and dependency ordering.

## Permissions

Local reads, edits, tests, commits, and reviewed integration are allowed within the requested scope. Preserve unrelated changes. Remote writes and destructive actions require task-specific permission. Asking to create a PR or MR permits the branch push needed for that submission, not merge, deploy, force-push, or destructive cleanup. An autonomy request does not remove these boundaries.

Do not automatically publish because a playbook ends with Opening a PR. Without publication permission, finish locally and report the branch and verification result. Use `gh` for GitHub and `glab` for GitLab after inspecting the installed CLI help. Read back the exact remote target after an authorized write. Existing Origin support is optional, not a requirement.

These are agent instructions, not an OS sandbox. A read-only brief does not make a shell, MCP tool, extension, or network call read-only.

## Delegate only when required

Create workers only where the invoked skill or playbook asks for subagents. Every worker is an interactive, inspectable Pi session in herdr. Never use hidden CLI processes, native subagent tools, cloud workers, `pi --print`, or RPC as a substitute for visible delegation. The coordinator may do non-delegated work itself.

Only the coordinator creates workers and sends their tasks. A worker whose skill needs another worker reports `DELEGATION NEEDED` with the role, goal, inputs, access needs, and dependencies. The coordinator starts that worker and relays the result. The requesting worker does not run herdr control commands. Resume it only after checking that it is idle and under coordinator control.

Run all independent required workers concurrently. Panel length sets the number of panel workers, including duplicate or alias entries. Do not cap concurrency or shrink a panel to fit the screen. Wait for upstream results before starting dependent work. Missing coverage or a worker dropout is a gap, never a pass.

## Check prerequisites

Before any herdr control command:

```sh
test "${HERDR_ENV:-}" = 1
```

If this fails, report `BLOCKED: visible delegation requires a herdr-managed coordinator pane`. Do not invent caller IDs, export `HERDR_ENV=1`, attach to the user's focused session from outside, or start another mechanism. Continue only work that does not require workers.

Inside herdr, inspect:

```sh
herdr --help
herdr status
herdr agent
herdr pane
herdr tab
herdr worktree
herdr integration status
pi --help
```

The installed help is the authority for syntax. Require a compatible running server, Pi support in `agent start`, and a current Pi state integration. Missing integration is a blocker until the user authorizes its installation. Do not update or restart the server automatically. Never stop the user's server.

## Resolve models

Read `~/.agents/pstack-models.md` at task start and before starting workers after a settings change. `/setup-pstack` retains the upstream role names and budget choices. Use Pi's `--provider`, exact `--model`, and separate `--thinking` arguments, not Cursor model slugs or `-fast` suffixes. Validate each provider and model pair against `pi --list-models`. A catalog entry is not proof of credentials or provider availability.

The budget mapping is `unlimited` to `max`, `large` to `xhigh`, `medium` to `high`, and `small` to `medium`. Read any `# thinking <role>: <level>` lines as confirmed reasoning exceptions for that role. Budget controls reasoning, not dollars or worker count. Use a level supported by the chosen model. If Pi or the provider cannot honor it, present alternatives for confirmation instead of silently downgrading. Do not invent speed flags.

`auto` and `inherit-parent` mean the coordinator's exact current provider and model, not Pi's startup default. Resolve these from the active coordinator session. Pi session JSONL records have `type: "model_change"`, `provider`, and `modelId`. Honor the latest change for this session, not the newest session from another task. If identity cannot be established, ask or run setup. Never launch an alias worker with an omitted model.

An explicit role entry has the form `provider/model-id`. Split at the first slash only. Preserve any later slash, colon, or bracket in the model ID. Panel entries are separated by a comma followed by a space. A missing role or settings file requires setup before delegation, not a guessed model. Unknown model, missing credentials, and unsupported reasoning leave that seat blocked until a replacement is approved. Do not substitute a family's default or claim a diverse review when all seats use one model family.

## Isolate writes

Read-only workers may share a checkout. A worker that writes any repository files, reports, or artifacts needs its own branch and worktree, even for a design candidate. Start from the exact agreed base commit:

```sh
git worktree add -b "$WORKER_BRANCH" "$WORKTREE_PATH" "$BASE_SHA"
```

Choose unused branch names and paths. Do not reset or stash unrelated changes. Worktrees do not inherit uncommitted coordinator edits. Commit only relevant changes locally or provide an explicit patch before delegating work that depends on them. Shared writable services and databases need separate fixtures too. A pane alone does not isolate writes.

The coordinator reviews the diff, verification evidence, and exact commit before local integration. Use an inspected local merge or cherry-pick. Do not integrate conflicting or unrelated edits automatically.

## Create readable locations

Discover live IDs and geometry:

```sh
herdr pane current --current
herdr pane layout --current
herdr pane list --workspace "$HERDR_WORKSPACE_ID"
herdr tab list --workspace "$HERDR_WORKSPACE_ID"
herdr agent list
```

Keep the coordinator's pane dominant. Inspect the installed split ratio semantics before choosing a ratio. Split only the coordinator's pane or panes created for this task. Keep a larger coordinator area and a smaller worker area if both remain readable. Never repeatedly shrink the coordinator or rearrange unrelated panes. If geometry or ratio semantics are unclear, create a worker tab instead. Additional workers use task-owned space or new tabs. Never move focus automatically.

```sh
herdr pane split --current --direction right --cwd "$WORKER_CWD" --no-focus
herdr tab create --workspace "$HERDR_WORKSPACE_ID" --cwd "$WORKER_CWD" --label "$TASK_LABEL" --no-focus
```

These are alternatives, not commands to run both. Parse the new pane ID from `.result.pane.pane_id` for a split or `.result.root_pane.pane_id` for a tab. Do not infer IDs from sidebar order. For a writing worker, `WORKER_CWD` is its worktree. Verify cwd and shell readiness before starting Pi. Label every task-owned pane and tab clearly. Do not reuse user-owned panes.

## Start, submit, and read

Choose a unique agent name matching `[a-z][a-z0-9_-]{0,31}`. Parse IDs and states from CLI JSON. Start an interactive Pi in the available shell pane:

```sh
herdr agent start "$WORKER_NAME" --kind pi --pane "$PANE_ID" -- --provider "$PROVIDER" --model "$MODEL_ID" --thinking "$THINKING" --name "$TASK_LABEL"
```

For readers, Pi supports `--tools read,grep,find,ls`. MCP tools may remain enabled. Keep only the read access the task needs, inspect extensions and MCP tools, and state the no-write boundary explicitly. A reviewer that needs shell tests or external lookups needs a scoped brief and write isolation if those commands can write files. Do not pretend `--tools` is a security sandbox. Do not blanket-pass `--approve` to bypass project trust.

Each brief includes goal, role, allowed paths, base SHA, verification criteria, forbidden remote and destructive actions, and the required report. Include absolute paths to the invoked skill, this runtime file, and relevant prompt templates. Playbook coding workers also read `../SKILL.md` relative to this runtime's parent directory. Tell the worker that it must not create workers and must request any nested delegation from the coordinator. Grant no permissions the coordinator does not have.

Record a compact in-chat worker table with task, live name, pane ID, cwd, role, model, ownership, and status. Do not create a separate orchestration database or daemon. Save this table with the handoff when pausing.

Start and submit all ready independent workers before waiting for results. Use a non-waiting prompt for fan-out, then wait on each started worker:

```sh
herdr agent prompt "$WORKER_NAME" "$BRIEF"
herdr agent wait "$WORKER_NAME" --timeout 120000
herdr agent get "$WORKER_NAME"
herdr agent read "$WORKER_NAME" --source recent-unwrapped --lines 120
```

For one worker, `agent prompt ... --wait --timeout 120000` is sufficient. Never prompt a worker already working. A successful submission is not a completed task. `idle` and `done` mean ready for input, not that the task passed. Read the actual reply and verify its evidence. Prefer terminal output. Only if the response cannot be recovered, ask for a report file in that worker's own writable location and read it there.

## Failures, takeover, and retention

On timeout, stalled submission, `blocked`, or `unknown`, inspect `agent get` and `agent read`. A timeout does not prove non-delivery. Never blindly resubmit, answer an approval, change models, or replace a worker. If the condition remains uncertain, report it and hold dependent tasks. Unrelated workers may continue. A confirmed recoverable failure needs a scoped recovery decision with evidence, not a hidden retry loop.

When the user declares takeover, mark the worker user-controlled. Send no prompts, keys, resume commands, or replacement tasks to it until the user explicitly returns control. Monitoring is not takeover. No automatic typing detector is assumed. On return, read its current state and output before continuing. Do not overwrite changes the user made.

A finished worker remains open. Do not close panes, tabs, or workspaces, terminate Pi, or delete branches and worktrees automatically. New work normally gets a fresh worker with consolidated instructions. Reuse a prior session only when its live state is needed and the user has not taken it over.

## Pi conventions and unsupported features

Pi invokes skills as `/skill:name`. Old `/name` examples in upstream prose mean `/skill:name`, not a registered Pi command. Invoke each task explicitly. Cursor Custom Modes, `/loop`, `Task`, `AskQuestion`, cloud agents, Bugbot installation, and Cursor Automations are not provided by this fork. Use numbered chat questions and bounded foreground waits. Do not install a substitute daemon or scheduler.

Existing automated review comments can still be assessed as evidence. Do not claim Bugbot ran if it did not. `make-bot-ui` and the Benny automation pack require Cursor Automations and are unsupported here. State that and stop those workflows rather than setting them up.

For session pickup and recall, use only this task's Pi session paths, including worker worktrees and any explicit `--session-dir`. Confirm the session's `cwd` and opening prompt. Do not glob every project's private chats. Pi skills may live in `.pi/skills/`, `~/.pi/agent/skills/`, `.agents/skills/`, or `~/.agents/skills/`. Resolve sibling paths from the loaded skill directory. No Hermes dependency is required.
