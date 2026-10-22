### Autopilot-full

Read [Pi + herdr runtime](../references/pi-herdr.md) first. This playbook owns a queue of independent changes through verification and, only when explicitly authorized, remote merge. An instruction to continue unattended does not grant publication or merge permission.

1. Declare the queue, done predicate, and task-specific permission ceiling. Stop each item at local-ready, PR-ready, or merge-ready according to the grant. Never broaden it to other items.
2. The coordinator starts one visible Pi owner per independent item through herdr. Each writer gets its own branch and worktree from an exact base SHA. Preserve configured models and panel sizes. Owners never create workers. They request reviewers and verifiers from the coordinator.
3. Each owner implements, removes unnecessary changes, runs checks, and reports the committed head with evidence. Publication uses Opening a PR only when authorized. No automatic early push, force-push, or cleanup. Keep a decision trail for long runs.
4. The coordinator requests independent swarm verification at the code-ready SHA. Verify requested behavior on the real artifact and inspect the diff. Aggregate all proven findings into one scoped fix request. A missing lane is a gap. Do not trust an owner's self-proof as the independent verdict.
5. Match verification and CI to the current head. After a substantive change, rerun affected checks and independent verification. Before an authorized merge, inspect the current base and merge result. Conflicts or untested dependency changes require repair and fresh evidence.
6. Merge only with explicit merge permission and a current independent verdict. Follow Shipping. PR or MR creation permission does not authorize merge. Do not bypass forge approvals or arm automatic merge for an unverified head.
7. Inspect stalled, blocked, or unknown workers before deciding recovery. Do not automatically replace them or send duplicate prompts. Preserve user takeover. Reconcile all workers at checkpoints. Use bounded foreground waits, not an assumed `/loop` command or a new scheduler.
8. On stop, cease task writes and report each worker's state. Retain all sessions and worktrees. Close only after the predicate is verified or a real blocker is recorded.

**Reply:** queue state, verified heads, local results, authorized PR or MR links, what actually merged, remaining permission gates, worker locations, and trail paths.
