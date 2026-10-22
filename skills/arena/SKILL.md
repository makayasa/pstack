---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

Read [Pi + herdr runtime](../poteto-mode/references/pi-herdr.md) before acting, including when invoked directly. Only the coordinator creates visible Pi workers. No hidden or sequential substitute for required delegation.

Open a todolist with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Pick runners from `arena runners` in `~/.agents/pstack-models.md`. Keep one seat per entry. Resolve aliases and budget through the runtime rules. Missing settings or unavailable models block the affected seat until the user confirms a mapping. More design directions may require more runners. Repeated models are allowed for generation-bound work, but do not claim model diversity from them.
4. Give every candidate that writes artifacts its own branch and worktree, per the **separate-before-serializing-shared-state** principle skill. Read-only candidates may report in their terminal.

## Phase B: Fan out

The coordinator starts all N independent Pi workers through herdr and submits their briefs before waiting. Each gets the task, shared grounding path, its own worktree when writing, and instructions to report the artifact and a short rationale naming alternatives considered and rejected.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all Phase B candidates complete, choose one model from `arena cross-judge pool` in the settings file. Prefer a family different from the coordinator's. Start one read-only Pi judge through herdr. It sees the rubric and candidate paths, scores each criterion, and recommends a base with rationale. It runs alongside your Phase D reading, never while candidates are still writing. An unavailable judge leaves verification incomplete.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
