### Feature

Read [Pi + herdr runtime](../references/pi-herdr.md) first. The coordinator creates required Pi workers through herdr using `feature, refactoring`. Writers get isolated worktrees. Nested delegation returns to the coordinator. No hardcoded fallback model.

**You own the design. Plan, review, verify.** Delegate implementation. Stay in the lead.

1. `how` over the affected subsystem.
2. `architect` for parallel design exploration.
3. Write the throughput checkpoint as four todo items. A dimension that genuinely does not apply (single file, no fan-out) keeps its item with `n/a: <reason>` rather than being dropped:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target (the **separate-before-serializing-shared-state** principle skill). Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
4. The coordinator delegates implementation to visible Pi workers using `feature, refactoring`. Give each writer an exclusive worktree, named data shape, allowed paths, and success criteria. For competing implementation shapes, run **arena** through the coordinator. A worker that needs another role requests delegation and waits for the relayed result. Do not bypass independent review by doing a second role yourself. Keep edits surgical, inspect upstream-derived source before porting, and verify every affected consumer.
5. Verify on the matching surface. "Inconclusive" or wrong-surface is not a pass. Flag it.
6. Rebase into small, ordered commits. Stack follow-ups.
   Use the **sequence-verifiable-units** principle skill, building, verifying, and committing each small unit before the next.
7. If the design is contested, `interrogate` before shipping.
8. Run **Opening a PR**.

Code-coupled work goes to a single owner with the checkpoint inline. That owner requests any further workers from the coordinator after the blocking phase. Independent artifact slices can run concurrently. Rewrite the checkpoint at phase boundaries. Fresh work gets a fresh owner unless live state must be retained.

**Reply:** what you built, what you chose and why, the throughput checkpoint, open decisions. Tables for design alternatives.
