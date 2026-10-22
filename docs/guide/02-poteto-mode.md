# Route work through poteto-mode

Give the coordinator a goal and a check that can pass or fail:

```text
/skill:poteto-mode users get two notifications after a retry. Reproduce the failure, fix its cause, and verify the result. Keep it local.
```

The coordinator reads the principles, chooses the playbook, and keeps a Markdown checklist. Skipped steps remain visible with a reason. Non-delegated work stays in this session. A skill that requests workers uses interactive Pi sessions through herdr.

## State the outcome

Include the observed problem, expected result, useful evidence, and constraints that affect the work. Do not prescribe a list of skills unless you need a particular workflow override. The playbook already orders them.

For investigation without edits:

```text
/skill:poteto-mode new task. Find why the cache survives logout. Do not change code.
```

For a plain explanation, use `/skill:how`, `/skill:why`, or `/skill:teach` directly. Their worker transport and safety rules are the same outside poteto-mode.

## Keep parallel work visible

Only the coordinator creates workers. A worker that needs another role asks the coordinator for delegation. Independent work runs concurrently. Dependencies wait for actual upstream results. Configured review panels keep every seat.

Each writer uses a separate branch and worktree. Readers may share a checkout. Separate terminal panes do not isolate file writes, ports, databases, or build outputs. The coordinator checks those boundaries before starting work.

The coordinator keeps the larger pane where feasible. Workers use smaller task-owned panes and overflow tabs without stealing focus or rearranging unrelated panes. The worker table identifies their tasks and locations.

## Intervene without losing work

Inspecting a worker does not transfer control. Tell the coordinator when you take over a worker. It sends no prompts or keys until you explicitly return control. Other workers may continue.

Finished sessions stay open. Worktrees and branches are not removed automatically. Request cleanup separately after reviewing their state.

## Continue within the permission ceiling

Follow-ups can be short when the task is unchanged. Start a new task with `/skill:poteto-mode new task ...` so the coordinator chooses a fresh playbook. Pi has no Cursor Custom Mode in this fork.

Local edits, tests, commits, and reviewed integration are allowed within scope. Ask explicitly for PR or MR creation when you want publication. That request does not grant merge, force-push, deploy, or destructive cleanup. Unattended work follows the same limits.

Next: [Understand the code](03-understand.md). The [runtime contract](../../skills/poteto-mode/references/pi-herdr.md) owns execution details.
