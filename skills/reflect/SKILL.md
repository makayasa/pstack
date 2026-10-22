---
name: reflect
description: Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

# Reflect

Read [Pi + herdr runtime](../poteto-mode/references/pi-herdr.md) before acting, including when invoked directly. Only the coordinator creates visible Pi workers. No hidden or sequential substitute for required delegation.

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Before fanning out, find this conversation's transcript in the active workspace's session directory. Do not glob across every project's directory. That crosses workspace boundaries and reads private chats from unrelated projects.

Where the transcript lives depends on your harness:

- **Cursor:** the `agent-transcripts/` directory the system prompt names.

  ```bash
  ls -t <agent-transcripts>/*.jsonl <agent-transcripts>/*/*.jsonl <agent-transcripts>/*/subagents/*.jsonl 2>/dev/null | head -10
  ```

  That covers the legacy flat (`<id>.jsonl`), current nested (`<id>/<id>.jsonl`), and subagent (`<parent>/subagents/<child>.jsonl`) layouts. For each candidate, read the first JSONL line. Take the file whose `message.content[0].text` contains the conversation's opening user prompt.
- **Claude Code:** `~/.claude/projects/<slug>/<session-id>.jsonl`, where `<slug>` is the workspace path with every character that isn't a letter or digit turned into "-".
- **Pi:** `~/.pi/agent/sessions/--<slug>--/*.jsonl`, where `<slug>` is the workspace path with the leading slash dropped and each "/" turned into "-".
- **Codex:** `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`. Keep only files whose first line has `payload.cwd` equal to the workspace path.
- **Other harnesses:** check the harness's session directory for this workspace.

Outside Cursor, take the newest candidates first and confirm one by finding the conversation's opening user prompt in its first user message. If none matches, pass a tight digest of the session instead.

## 2. Spawn three reviewers in parallel

The coordinator starts three visible Pi reviewers through herdr and submits all briefs before waiting. Grant scoped read access to the transcript and required MCP sources. Reviewers must not write repository files or external records.

Use the runtime's environment gate and failure handling. Missing herdr leaves the review blocked. No hidden or sequential substitute.

Read each role from `~/.agents/pstack-models.md`. Resolve aliases and reasoning through the runtime rules. Missing settings or unavailable models require confirmation, not fallback.

| Lens | Role line | Prompt template |
|---|---|---|
| Judgment | `reflect judgment, divergent, synthesizer` | `references/judgment-reviewer.md` |
| Tooling | `reflect tooling` | `references/tooling-reviewer.md` |
| Divergent | `reflect judgment, divergent, synthesizer` | `references/divergent-reviewer.md` |

Pass each template verbatim, substituting the transcript path or digest where marked. Read findings from each worker's terminal response.

## 3. Synthesize

After all reviewers finish, the coordinator starts one Pi synthesizer using `reflect judgment, divergent, synthesizer`. It spot-checks citations through scoped read-only MCP access. Pass `references/synthesizer.md` verbatim with each reviewer's full output where marked. Read its Accepted / Rejected / Backlog list from the terminal.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Keep Backlog items local unless the user authorizes tracker writes. Accepted edits still require explicit approval.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): hand to your harness's skill-authoring skill and run its draft / test / iterate loop. That is `create-skill` in Cursor (built in) or Anthropic's `skill-creator`. If you have neither, follow the Agent Skills format at agentskills.io. "`create-skill`" below means whichever of these you use.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): hand to `create-skill` and run its description-optimization loop.
- `new skill via create-skill: <kebab-name>`: hand creation to `create-skill`. Do not invent the shape ad hoc.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
