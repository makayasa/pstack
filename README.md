# pstack for Pi + herdr

A fork of [backnotprop/pstack](https://github.com/backnotprop/pstack), originally from [poteto's pstack in cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack).

pstack is a collection of Agent Skills for understanding, changing, reviewing, and verifying software. This fork runs its coordinator and workers in Pi. Required workers are interactive sessions in herdr so you can inspect and interrupt their work.

## Run the fork

Install Pi and herdr first. From this checkout, load the skills without changing installed packages:

```sh
pi --skill ./skills
```

Run that command in a herdr-managed pane. To register the local package for later sessions, review it and run:

```sh
pi install /absolute/path/to/pstack
```

Pi supports local packages without copying them. Avoid installing this alongside another copy of pstack. Duplicate skill names can load the wrong copy. Editing this repository does not install it or change model settings.

In Pi, configure budget and models:

```text
/skill:setup-pstack
```

Then start a task with a checkable goal:

```text
/skill:poteto-mode fix the duplicate notification. Reproduce it, fix the cause, and verify the result. Keep the result local.
```

Pi uses `/skill:name`, not Cursor's `/name`. Start each new task explicitly. This fork does not provide Cursor Custom Modes or `/loop`.

## What changes

- Only skills or playbooks that request subagents create workers. Ordinary work stays in the coordinator.
- Only the coordinator creates workers. Workers request nested delegation rather than spawning children.
- Every worker is a visible Pi session in herdr. No hidden processes, cloud agents, or sequential substitute for required delegation.
- Each writing worker gets its own branch and worktree. Readers may share a checkout.
- Ready independent workers run concurrently. The skill and configured panel determine the count, not a screen-size cap.
- The coordinator keeps the larger pane where feasible. Extra workers use readable task-owned panes or new tabs without stealing focus.
- Declaring takeover stops coordinator input to that worker until you return control.
- Completed sessions, branches, and worktrees stay available until you request cleanup.
- Local work is allowed by default. Remote writes need task-specific permission. A PR or MR request includes its necessary branch push, not merge, deploy, force-push, or destructive cleanup.

[Pi + herdr runtime](skills/poteto-mode/references/pi-herdr.md) is the shared execution contract, including direct skill invocations. These instructions guide agents. They are not an OS permission sandbox.

## Keep pstack's model setup

`setup-pstack` detects models with `pi --list-models`, offers a reasoning budget, and asks you to confirm the mapping for each role. Settings live in `~/.agents/pstack-models.md`.

| Budget | Starting reasoning |
|---|---|
| unlimited | max |
| large | xhigh |
| medium | high |
| small | medium |

Budget does not limit money or worker count. Model IDs and thinking levels are separate. Unsupported models or reasoning levels require a confirmed choice. `auto` and `inherit-parent` resolve to the coordinator's exact model. They do not launch Pi with an unspecified default.

Panels keep one worker per configured entry. Setup warns when a panel lacks model-family diversity. It never silently changes a model or removes a seat.

## Choose a skill

Start with [poteto-mode](skills/poteto-mode/SKILL.md) for a task that needs a workflow. Use a specific skill for narrower work:

| Goal | Pi command |
|---|---|
| Understand behavior | `/skill:how` |
| Investigate rationale | `/skill:why` |
| Learn a subsystem | `/skill:teach` |
| Compare candidate implementations | `/skill:arena` |
| Cover independent slices | `/skill:swarm` |
| Design before implementation | `/skill:architect` |
| Review with configured model panels | `/skill:interrogate` |
| Keep a decision trail | `/skill:show-me-your-work` |
| Configure models and reasoning | `/skill:setup-pstack` |
| Find the right workflow | `/skill:poteto-help` |

Engineering principles and workflow goals remain in [skills](skills/). Existing helper scripts are optional tools, not a worker launcher or required orchestration engine.

## Verify the fork

```sh
python3 scripts/check-pi-herdr.py
```

This checks source structure and policy consistency. It does not prove live delegation. [Live verification](docs/harness/pi-herdr.md#verify-in-a-test-repository) lists the required real Pi and herdr checks. Do not report the migration fully verified until those pass.

## Unsupported and upstream

Cursor cloud agents, Custom Modes, Bugbot installation, and Cursor Automations have no replacement here. [make-bot-ui](skills/make-bot-ui/SKILL.md) and [Benny](automations/benny/README.md) are retained as unsupported upstream material. They stop before setup.

Full compatibility with Cursor or Claude Code is not a goal. [MIRROR.md](MIRROR.md) describes selective upstream review instead of automatic mirroring. Attribution and the MIT license remain intact.

See the [guide](docs/guide/README.md), [glossary](GLOSSARY.md), and [accepted decisions](docs/adr/0001-pi-herdr-primary-environment.md).
