### Autonomous run

Read [Pi + herdr runtime](../references/pi-herdr.md) first. Use bounded foreground waits and visible Pi workers only where requested. This fork provides no `/loop`, scheduler, or cloud workers. Unattended work retains the permission ceiling and failure inspection rules.

**You own the exit condition. Define done, then drive to it without stopping.**

1. State the exit condition as a checkable predicate before the first iteration (tests green, repro fixed, all N PRs merged, pixel-diff zero).
2. Use bounded foreground waits for worker completion or observable events. If the task requests a watcher, the coordinator creates a visible Pi worker through herdr. Do not assume a scheduler can wake a completed chat. If the environment cannot continue safely, save a handoff instead of claiming unattended execution.
3. Each iteration makes the smallest change the evidence justifies, verifies it against the predicate, commits if it advanced, discards changes that didn't help. Belt-and-suspenders that "might help" gets reverted, not left to ride.
   Sequence the work via the **sequence-verifiable-units** principle skill, verifying each unit before the next instead of batching checks at the end.
4. Repair issues that block the scoped predicate. Record unrelated findings separately rather than expanding the task. Keep out-of-band fixes local unless publication is authorized. Ask only for product decisions, permission gates, or recovery decisions that evidence cannot resolve. Preserve the original predicate.
5. Checkpoint every iteration via the **show-me-your-work** skill, a row for what changed and whether the predicate moved.
6. Stop when the predicate is met. A plateau is not a stop, so keep going and pivot your approach to push past it. Surface a genuine dead end rather than spinning, and never relax the predicate to declare victory.

**Reply:** the exit condition, iterations run, what landed, what was discarded, final predicate state.
