---
name: poteto-help
description: Guide pstack setup and skill selection in Pi and herdr.
disable-model-invocation: true
---

# Poteto help

Read [Pi + herdr runtime](../poteto-mode/references/pi-herdr.md) before answering. Answer help questions without starting the work or launching workers. For an actual work request, read poteto-mode and perform the requested task within runtime boundaries.

Read the file you recommend before quoting it. Use this fork's local paths or its actual repository URL, not an upstream URL for changed instructions. Give at most one example prompt. Pi commands use `/skill:name`.

## Setup

Load this checkout with `pi --skill ./skills` from a herdr-managed pane. To register the reviewed local package, use `pi install /absolute/path/to/pstack`. Do not load duplicate pstack copies.

Run `/skill:setup-pstack` for budget and per-role model choices. It writes `~/.agents/pstack-models.md`. Missing settings require setup before delegation. No default model is guessed. `auto` and `inherit-parent` mean the coordinator's exact model, not Pi's startup default. Budget controls reasoning, not money or worker count.

Then give `/skill:poteto-mode` a goal and a check that can pass or fail. The coordinator picks a playbook. Direct skills use the same visible worker mechanism. There is no Cursor Custom Mode, native subagent fallback, or built-in `/loop` in this fork.

## Pick a skill

| Need | Skill |
|---|---|
| Run a non-trivial task | [poteto-mode](../poteto-mode/SKILL.md) |
| Check understanding before work | [in-your-own-words](../in-your-own-words/SKILL.md) |
| Improve the task brief | [sharpen](../sharpen/SKILL.md) |
| Explain current behavior | [how](../how/SKILL.md) |
| Investigate rationale | [why](../why/SKILL.md) |
| Learn a change or subsystem | [teach](../teach/SKILL.md) |
| Reconstruct recent context | [recall](../recall/SKILL.md) |
| Catch up within this chat | [ketchup](../ketchup/SKILL.md) |
| Find breakage outside a diff | [blast-radius](../blast-radius/SKILL.md) |
| Settle types and module shape | [architect](../architect/SKILL.md) |
| Compare implementations of one brief | [arena](../arena/SKILL.md) |
| Cover independent slices or races | [swarm](../swarm/SKILL.md) |
| Challenge a diff with model panels | [interrogate](../interrogate/SKILL.md) |
| Fix a bug with a cheap regression check | [tdd](../tdd/SKILL.md) |
| Apply TypeScript rules | [typescript-best-practices](../typescript-best-practices/SKILL.md) |
| Review comments | [no-comments](../no-comments/SKILL.md) |
| Clean prose | [unslop](../unslop/SKILL.md) |
| Write technical documents | [technical-writing](../technical-writing/SKILL.md) |
| Restate the last reply plainly | [bro](../bro/SKILL.md) |
| Generate app verification | [create-verification-skill](../create-verification-skill/SKILL.md) |
| Maintain app verification | [maintain-verification-skill](../maintain-verification-skill/SKILL.md) |
| Generate property verification | [create-formal-verification-skill](../create-formal-verification-skill/SKILL.md) |
| Maintain property verification | [maintain-formal-verification-skill](../maintain-formal-verification-skill/SKILL.md) |
| Vet a measured performance number | [benchmark-checklist](../benchmark-checklist/SKILL.md) |
| Design a bespoke workflow | [figure-it-out](../figure-it-out/SKILL.md) |
| Keep a decision trail | [show-me-your-work](../show-me-your-work/SKILL.md) |
| Configure models and budget | [setup-pstack](../setup-pstack/SKILL.md) |
| Create a personal mode | [automate-me](../automate-me/SKILL.md) |
| Turn session lessons into approved edits | [reflect](../reflect/SKILL.md) |
| Prevent repeated repository mistakes | [correct](../correct/SKILL.md) |

Playbooks live inside poteto-mode and have no separate slash command. Principles are one-rule skills. Read the relevant principle before recommending it. `make-bot-ui` and Benny are unsupported because they require Cursor Automations. Explain that limitation rather than starting setup.

## Explain monitoring and permissions

Only the coordinator creates required workers. Every worker is an interactive Pi session in herdr. Writers get separate branches and worktrees. Panel entries determine panel size. Do not reduce a panel or add a worker cap to fit the screen.

The coordinator keeps the dominant pane where feasible. Additional workers use readable task-owned panes or tabs without stealing focus. Completed sessions remain open. The user requests cleanup separately.

Monitoring does not transfer control. On declared takeover, the coordinator sends nothing to that worker until the user returns control. It can continue other independent work.

Default work is local. PR or MR creation permission includes its necessary branch push, not merge, deploy, force-push, or destructive cleanup. A request to continue unattended does not expand permissions.

## Diagnose a run

- Missing herdr caller context blocks delegation. Do not invent context or launch hidden workers.
- Missing model settings require setup. Unavailable models require a confirmed replacement.
- A stalled or blocked worker needs status and output inspection before recovery. Never blindly resend a prompt.
- Shared-file collisions require isolated writing worktrees, not more panes.
- A changed settings file affects new worker launches, not already-running Pi sessions.
- A green build does not prove behavior. Ask for actual runtime evidence and uncompleted verification cases.

Offer project verification only when it addresses the user's question. For live fork checks, point to [Pi + herdr verification](../../docs/harness/pi-herdr.md#verify-in-a-test-repository). Keep help short and answer only the user's situation.
