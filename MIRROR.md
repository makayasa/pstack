# Review upstream changes selectively

This fork derives from [backnotprop/pstack](https://github.com/backnotprop/pstack) and [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack). It is no longer an automatically synchronized mirror.

Review upstream diffs on a separate branch or checkout. Take changes that improve engineering behavior without undoing the [Pi + herdr runtime](skills/poteto-mode/references/pi-herdr.md). Preserve attribution, license notices, and the source commit for each adopted change.

Before adopting a change, check for native subagent transports, cloud-only workflows, model slug fallbacks, external writes, automatic cleanup, Cursor paths, and nested worker creation. Adapt the meaning to this fork rather than copying the old execution instructions.

Run `python3 scripts/check-pi-herdr.py` and the relevant live verification after changes to delegation. Keep `agents/comment-sicko.md` and `skills/no-comments/references/comment-sicko.md` aligned when their shared prompt changes.

Never copy upstream files over the working tree wholesale, run a destructive sync, or push as part of an automatic update. Publication requires task-specific permission.
