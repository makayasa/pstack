### Orchestrate

Read [Pi + herdr runtime](../references/pi-herdr.md) first. This playbook coordinates a project that outlives one worker. One task with a done predicate uses Autonomous run instead.

Only the coordinator creates workers. A track lead may plan and summarize its track, but requests workers from the coordinator instead of spawning children. All agents are Pi sessions on this machine, visible in herdr. No cloud agents, hidden watchers, nested spawning, fixed concurrency cap, or orchestration daemon.

#### Frame and record

1. State the done predicate, scope, dependency graph, and permissions. Do not equate local integration with a remote merge.
2. Keep a compact worker table and a Markdown task checklist. For a long program, save them with standing orders, scoped briefs, verification receipts, and the decision trail in a task-owned directory. The coordinator owns shared state. Workers report in their terminals or their own worktrees.
3. Run one representative unit from brief through implementation, verification, and reviewed local integration. Fix the workflow from observed failures before scaling it.
4. Start all ready independent units through herdr. Preserve configured review panels. Start dependent units only when their upstream evidence is available. Relay full relevant results, not only a status word.

#### Brief

Each brief includes goal, role, allowed paths, exclusive worktree for writes, exact base SHA, inputs, acceptance criteria, verification commands, runtime policy path, forbidden actions, and report format. Include standing orders and all user corrections. The worker reports status, exact commit, changed paths, commands actually run, results, and unresolved risks.

If the worker needs another role, it returns `DELEGATION NEEDED`. The coordinator creates that worker and relays the result. Never silently absorb missing verification or claim coverage from an uncompleted worker.

#### Review and integrate

Read every completed reply and inspect its evidence. For risky units, request an independent verifier through the coordinator, preferably using a different model family. Match verdicts to exact commit SHAs. New code invalidates earlier verification for affected behavior. A green build is not proof of the requested behavior.

Review diffs before local integration. Serialize integration into a shared target branch. Leave unrelated changes untouched. Resolve conflicts deliberately instead of resetting worktrees. Only publish branches, PRs, or MRs when the task grants that permission. Merge, deploy, force-push, and destructive cleanup require separate permission.

#### Failure and pickup

Inspect herdr status and output before retrying a stalled worker. Do not automatically restart, replace, approve, or switch models. Hold dependent units when state is uncertain. Other units may continue.

Respect declared user takeover until control is returned. Do not close completed sessions or delete worktrees automatically. On coordinator restart, read the saved table and briefs, then inspect the named live agents and session paths. Reconcile what exists before sending new prompts. Never infer that a restart killed or completed a worker.

#### Close

Account for every worker, verification gap, locally integrated commit, and authorized remote write. Verify the done predicate against the real artifact. Save a handoff if anything remains blocked. Keep worker sessions, worktrees, and evidence for manual inspection.

**Reply:** outcome against the predicate, verified units, blocked units, local branch and commits, authorized PR or MR links, worker locations, and the trail path.
