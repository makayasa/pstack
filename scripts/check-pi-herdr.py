#!/usr/bin/env python3
"""Check source contracts. This does not execute agents or prove live delegation."""

import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "skills/poteto-mode/references/pi-herdr.md"
errors = []
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
playbooks = sorted((ROOT / "skills/poteto-mode/playbooks").glob("*.md"))

for path in skills:
    text = path.read_text()
    header = re.match(r"\A---\n(.*?)\n---\n(.+)", text, re.S)
    if not header:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter or body")
        continue
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*\S", header[1], re.M):
            errors.append(f"{path.relative_to(ROOT)}: missing {field}")
    if not re.search(rf"^name: {re.escape(path.parent.name)}$", header[1], re.M):
        errors.append(f"{path.relative_to(ROOT)}: name differs from directory")

for path in [*skills, *playbooks]:
    if "pi-herdr.md" not in path.read_text():
        errors.append(f"{path.relative_to(ROOT)}: missing runtime contract")

runtime = RUNTIME.read_text()
for required in (
    'test "${HERDR_ENV:-}" = 1',
    "Only the coordinator creates workers",
    "DELEGATION NEEDED",
    "Never blindly resubmit",
    "user-controlled",
    "A finished worker remains open",
    "its own branch and worktree",
    "Do not cap concurrency",
    "task-specific permission",
    "not merge, deploy, force-push",
    "coordinator's exact current provider and model",
    "confirmed reasoning exceptions",
    "--kind pi",
    "--no-focus",
    "herdr agent read",
):
    if required not in runtime:
        errors.append(f"runtime: missing contract {required!r}")

for path in skills:
    text = path.read_text()
    for stale in (
        "If your harness has no subagent tool",
        "subagent_type:",
        "pstack-models.mdc",
        "closest valid slug",
        "omit `model`",
        "default `grok-4.7",
        "default `claude-opus",
    ):
        if stale in text:
            errors.append(f"{path.relative_to(ROOT)}: stale transport or model rule {stale!r}")

manifest = json.loads((ROOT / "package.json").read_text())
if manifest.get("pi", {}).get("skills") != ["./skills"]:
    errors.append("package.json: Pi skills directory is not declared")
if manifest.get("dependencies") or manifest.get("pi", {}).get("extensions"):
    errors.append("package.json: unexpected runtime dependency or extension")

files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
).splitlines()
checked_links = 0
for name in sorted(set(files)):
    path = ROOT / name
    if path.suffix != ".md" or not path.is_file():
        continue
    text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
        target = unquote(target.split("#", 1)[0])
        if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        if any(token in target for token in ("<", ">", "*", "{", "}")):
            continue
        checked_links += 1
        if not (path.parent / target).exists():
            errors.append(f"{name}: broken local link {target}")

if errors:
    print("FAIL: source contracts", file=sys.stderr)
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(skills)} skill contracts, {len(playbooks)} playbooks, {checked_links} local links")
print("NOT RUN: live Pi + herdr delegation. Follow docs/harness/pi-herdr.md.")
