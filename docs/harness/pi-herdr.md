# Operate pstack in Pi and herdr

[Pi + herdr runtime](../../skills/poteto-mode/references/pi-herdr.md) is the execution contract. The [ADR](../adr/0001-pi-herdr-primary-environment.md) records the decisions. No extension, daemon, or orchestration engine is added by this fork.

## Start a coordinator

From a herdr-managed terminal in this checkout:

```sh
pi --skill ./skills
```

This loads skills for this invocation without installing the fork. Use `pi install /absolute/path/to/pstack` only when you want Pi to register the local package. Check for duplicate pstack skill names first. Run `/reload` after editing skills in an active Pi session.

Use `/skill:setup-pstack` to confirm a budget and model mapping. Start tasks with `/skill:poteto-mode` or invoke a specific skill directly. Every skill loads the same runtime boundaries. Missing herdr blocks required workers, not non-delegated coordinator work.

## Monitor and take over

Ask the coordinator for its worker table. Each row identifies the task, live agent name, pane ID, cwd, role, model, ownership, and status. Inspect a session in herdr without changing its ownership.

To take control, tell the coordinator which worker you are taking over. The coordinator stops sending prompts and keys to that worker. To return it, tell the coordinator explicitly. It inspects the current state before resuming. Other workers can continue throughout.

Completed sessions remain open. Request cleanup only after inspecting their branches, worktrees, and uncommitted changes. A finished task never implies permission to close a pane or delete files.

## Verify in a test repository

Run the source check first:

```sh
python3 scripts/check-pi-herdr.py
```

A source check is not live verification. Run the following from an actual herdr-managed coordinator pane with working Pi credentials. Do not export fake herdr variables or control the user's focused session from outside herdr. Use a disposable repository in your scratch directory, not the fork or an unrelated project. Leave its sessions and worktrees intact for inspection.

1. Create a small committed fixture with a text file and one runnable assertion. Record its base SHA. Load this checkout's skills in Pi. Confirm which skill paths Pi discovers and that no duplicate upstream copy wins.
2. Invoke `/skill:how` directly for the fixture. Confirm a visible Pi explainer starts through herdr. Read its actual response and inspect the file references. Submission success alone does not pass.
3. Invoke `/skill:poteto-mode` for a small fixture change whose workflow requests a writer and independent review. Confirm the writer has its own branch and worktree at the recorded base. Run its assertion and review the diff before local integration. No remote write is permitted in this test.
4. Exercise a skill with nested delegation, such as architect. Confirm the worker returns `DELEGATION NEEDED`, the coordinator creates the requested workers, and results return to the requesting role. A worker must not create children.
5. Take over one worker by telling the coordinator. Continue the worker manually. Confirm the coordinator sends no prompts or keys until you explicitly return control. Inspect the Pi session history for that interval.
6. Inspect layout and focus after worker creation. Confirm the coordinator remains the larger pane where feasible, overflow uses readable task-owned panes or tabs, unrelated panes are unchanged, and the user focus is preserved.
7. Keep finished workers open. Confirm their Pi processes, panes, branches, and worktrees still exist. Verify that the configured panel length was preserved and independent tasks were submitted before waiting.
8. Test missing herdr in a separate foreground shell with herdr caller variables removed. Required delegation must report blocked without a process launch. This is not permission to use `pi --print` for workers.
9. Test an unavailable model through a task-local fixture mapping, not by overwriting real user settings. The coordinator must report the affected seat and request confirmation. It must not launch a default or silently reduce the panel.
10. Observe a declared test wait timeout while the worker is still running, or use a controlled blocked fixture. Confirm the coordinator reads status and output, sends no duplicate prompt, and holds dependent work. Do not deliberately wedge an unrelated agent or bypass an approval.

Record each case with its command or prompt, real reply, pane ID, session path, commit when relevant, and PASS, FAIL, or BLOCKED. Do not mark absent cases passed. Provider calls can incur charges. Keep the test scope small and never submit fixture code to a remote forge.

## Current verification boundary

Live behavior remains unverified until the cases above have real receipts. Static checks, installed CLI help, and an installed state integration prove prerequisites only. A handoff must name any remaining blocked cases.
