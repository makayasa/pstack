# Run unattended work with visible workers

Unattended work still needs a checkable finish condition, isolated writers, evidence, and a permission ceiling. Pi workers stay visible in herdr. They run on this machine, so do not assume work continues after the machine sleeps or shuts down.

## Give a bounded task

```text
/skill:poteto-mode migrate every caller to the new parser. Done means zero old callers and all parser fixtures pass. Keep a decision log. Make local commits only. If blocked, preserve the work and report why.
```

The coordinator follows the relevant playbook and keeps a decision trail for review. Required workers run through herdr. No hidden worker, cloud service, built-in `/loop`, new daemon, or scheduler is assumed. Use bounded foreground waits for observable events.

An autonomy request means continue within scope. It does not grant push, PR or MR creation, merge, force-push, deploy, or deletion. Ask for those explicitly when needed. A request to create a PR or MR includes its necessary branch push, not merge.

## Check before leaving

- Confirm that the workflow has passed a small live trial.
- Give every writer a separate branch and worktree.
- Define verification that exercises the actual behavior.
- Confirm the model mapping, panel count, and required credentials.
- State when to report a blocker instead of retrying.

A stalled or unknown worker is inspected before recovery. The coordinator never blindly duplicates a prompt, answers an approval, or replaces a worker. Dependent work waits when the state is uncertain. Independent workers may continue.

## Return and inspect

Use `/skill:ketchup` for status or `/skill:show-me-your-work` for the decision trail and independent review. Read the real verification receipts and exact commits. Missing review lanes remain gaps.

Worker sessions, branches, and worktrees remain available. Declare takeover before manually directing a worker, then return control explicitly. Ask for cleanup separately.

For a queue, Autopilot-full and Autopilot-stack retain the same permission ceiling. For a project spanning many tasks, Orchestrate keeps delegation centralized in the coordinator. Workers request additional roles rather than creating children.

## Unsupported automation

Cursor Automations, Benny, and webhook-driven make-bot-ui are unsupported. This fork does not build replacements or schedule future runs automatically.

Next: [Steer with principles](08-principles.md).
