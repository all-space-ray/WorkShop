#!/usr/bin/env python3
"""Mirror team-command SKILL.md files into .agents/skills for Cloud discovery."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".cursor" / "skills"
AGENTS_SKILLS_DIR = ROOT / ".agents" / "skills"
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


def sync_mirror(only: set[str] | None, check: bool) -> int:
    team_commands = load_team_commands()
    updated = 0

    for skill_name in sorted(team_commands):
        if only and skill_name not in only:
            continue

        source = SKILLS_DIR / skill_name / "SKILL.md"
        if not source.exists():
            raise SystemExit(f"Missing source skill: {source}")

        target_dir = AGENTS_SKILLS_DIR / skill_name
        target = target_dir / "SKILL.md"
        rendered = read_text(source)
        if not rendered.endswith("\n"):
            rendered += "\n"

        if target.exists() and target.read_text(encoding="utf-8") == rendered:
            continue

        if check:
            print(f"Mirror out of sync: {target}")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(rendered, encoding="utf-8")
            print(f"Mirrored {target}")

        updated += 1

    expected = {AGENTS_SKILLS_DIR / name for name in team_commands}
    for existing in AGENTS_SKILLS_DIR.glob("*/SKILL.md"):
        skill_name = existing.parent.name
        if skill_name not in team_commands:
            if check:
                print(f"Unexpected mirror skill: {existing}")
            else:
                existing.unlink()
                if existing.parent.exists() and not any(existing.parent.iterdir()):
                    existing.parent.rmdir()
                print(f"Removed stale mirror: {existing}")
            updated += 1

    if updated == 0:
        print("Agent skill mirrors already in sync.")
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("skills", nargs="*", help="Optional skill names to mirror.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    only = set(args.skills) if args.skills else None
    updated = sync_mirror(only, args.check or args.dry_run)

    if args.check and updated:
        print("Agent skill mirrors are out of sync. Run python3 scripts/sync-agents-skills-mirror.py.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
