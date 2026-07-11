#!/usr/bin/env python3
"""Sync .cursor/commands/*.md wrappers from skill SKILL.md frontmatter."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cloud_skill_frontmatter import render_command_frontmatter

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".cursor" / "skills"
COMMANDS_DIR = ROOT / ".cursor" / "commands"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def decode_scalar(value: str) -> str:
    if len(value) < 2 or value[0] != value[-1]:
        return value

    if value[0] == '"':
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
        return decoded if isinstance(decoded, str) else value

    if value[0] == "'":
        return value[1:-1].replace("''", "'")

    return value


def parse_frontmatter_text(text: str) -> dict[str, str]:
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}

    values: dict[str, str] = {}
    frontmatter_lines: list[str] = []

    for line in lines[1:]:
        if line.strip() == "---":
            break
        frontmatter_lines.append(line)

    index = 0

    while index < len(frontmatter_lines):
        line = frontmatter_lines[index]
        index += 1

        if line.startswith((" ", "\t")) or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value in {"|", ">", "|-", ">-", "|+", ">+"}:
            block_lines: list[str] = []

            while index < len(frontmatter_lines):
                next_line = frontmatter_lines[index]

                if next_line and not next_line.startswith((" ", "\t")) and ":" in next_line:
                    break

                block_lines.append(next_line)
                index += 1

            value = " ".join(part.strip() for part in block_lines if part.strip())

        value = decode_scalar(value)
        values[key] = value

    return values


def render_command(skill_name: str, description: str, skill_path: str) -> str:
    return (
        render_command_frontmatter(skill_name, description)
        + "\n\n"
        + f"Read and follow `{skill_path}` completely.\n"
    )


def sync_commands(only: set[str] | None, dry_run: bool) -> int:
    updated = 0

    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill_name = skill_file.parent.name
        if only and skill_name not in only:
            continue

        frontmatter = parse_frontmatter_text(read_text(skill_file))
        description = frontmatter.get("description", "").strip()
        if not description:
            raise SystemExit(f"Missing description in {skill_file}")

        command_path = COMMANDS_DIR / f"{skill_name}.md"
        skill_path = skill_file.relative_to(ROOT).as_posix()
        rendered = render_command(skill_name, description, skill_path)

        if command_path.exists() and command_path.read_text(encoding="utf-8") == rendered:
            continue

        if dry_run:
            print(f"Would update {command_path}")
        else:
            command_path.write_text(rendered, encoding="utf-8")
            print(f"Updated {command_path}")

        updated += 1

    if updated == 0:
        print("Command wrappers already in sync.")
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if any command wrapper is out of sync.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show files that would change.")
    parser.add_argument("skills", nargs="*", help="Optional skill names to sync.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    only = set(args.skills) if args.skills else None
    updated = sync_commands(only, args.dry_run or args.check)

    if args.check and updated:
        print("Command wrappers are out of sync. Run bash .cursor/scripts/sync-skill-commands.sh.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
