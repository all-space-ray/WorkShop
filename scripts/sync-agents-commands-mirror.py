#!/usr/bin/env python3
"""Mirror .cursor/commands/*.md into .agents/commands/ for Cloud discovery."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / ".cursor" / "commands"
AGENTS_COMMANDS_DIR = ROOT / ".agents" / "commands"
TEAM_COMMANDS_PATH = ROOT / ".cursor" / "team-commands.txt"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_team_commands() -> set[str]:
    commands: set[str] = set()
    if not TEAM_COMMANDS_PATH.exists():
        return commands

    for line in read_text(TEAM_COMMANDS_PATH).splitlines():
        command = line.strip()
        if command and not command.startswith("#"):
            commands.add(command)
    return commands


def render_mirror(source_text: str) -> str:
    rendered = source_text.replace(".cursor/skills/", ".agents/skills/")
    if not rendered.endswith("\n"):
        rendered += "\n"
    return rendered


def sync_mirror(only: set[str] | None, check: bool) -> int:
    team_commands = load_team_commands()
    updated = 0

    for command_name in sorted(team_commands):
        if only and command_name not in only:
            continue

        source = COMMANDS_DIR / f"{command_name}.md"
        if not source.exists():
            raise SystemExit(f"Missing source command: {source}")

        target = AGENTS_COMMANDS_DIR / f"{command_name}.md"
        rendered = render_mirror(read_text(source))

        if target.exists() and target.read_text(encoding="utf-8") == rendered:
            continue

        if check:
            print(f"Command mirror out of sync: {target}")
        else:
            AGENTS_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
            target.write_text(rendered, encoding="utf-8")
            print(f"Mirrored {target}")

        updated += 1

    expected = {AGENTS_COMMANDS_DIR / f"{name}.md" for name in team_commands}
    for existing in AGENTS_COMMANDS_DIR.glob("*.md"):
        command_name = existing.stem
        if command_name not in team_commands:
            if check:
                print(f"Unexpected mirror command: {existing}")
            else:
                existing.unlink()
                print(f"Removed stale mirror: {existing}")
            updated += 1

    if updated == 0:
        print("Agent command mirrors already in sync.")
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("commands", nargs="*", help="Optional command names to mirror.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    only = set(args.commands) if args.commands else None
    updated = sync_mirror(only, args.check or args.dry_run)

    if args.check and updated:
        print(
            "Agent command mirrors are out of sync. "
            "Run python3 scripts/sync-agents-commands-mirror.py."
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
