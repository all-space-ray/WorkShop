#!/usr/bin/env python3
"""Normalize team-command SKILL.md frontmatter for Cloud slash-menu discovery."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from cloud_skill_frontmatter import render_skill_frontmatter, sanitize_for_cloud

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".cursor" / "skills"
TEAM_COMMANDS_PATH = ROOT / ".cursor" / "team-commands.txt"

ALLOWED_KEYS = {"name", "description", "disable-model-invocation"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_frontmatter(text: str) -> tuple[dict[str, str | list[str]], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing frontmatter")

    frontmatter_lines: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            body = "\n".join(lines[len(frontmatter_lines) + 2 :])
            break
        frontmatter_lines.append(line)
    else:
        raise ValueError("unclosed frontmatter")

    values: dict[str, str | list[str]] = {}
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
                if (
                    next_line
                    and not next_line.startswith((" ", "\t"))
                    and ":" in next_line
                    and not next_line.lstrip().startswith("- ")
                ):
                    break
                block_lines.append(next_line)
                index += 1
            values[key] = " ".join(part.strip() for part in block_lines if part.strip())
            continue

        if value == "" and index < len(frontmatter_lines) and frontmatter_lines[index].lstrip().startswith("- "):
            items: list[str] = []
            while index < len(frontmatter_lines):
                next_line = frontmatter_lines[index]
                if not next_line.lstrip().startswith("- "):
                    break
                items.append(next_line.lstrip()[2:].strip().strip('"').strip("'"))
                index += 1
            values[key] = items
            continue

        values[key] = value.strip('"').strip("'")

    return values, body


def metadata_preamble(values: dict[str, str | list[str]]) -> str:
    removed: list[str] = []

    if "argument-hint" in values:
        removed.append(f"**Argument hint:** {values['argument-hint']}")
    if "allowed-tools" in values:
        tools = values["allowed-tools"]
        if isinstance(tools, list):
            removed.append("**Allowed tools:** " + ", ".join(tools))
    if "license" in values:
        removed.append(f"**License:** {values['license']}")
    if "version" in values:
        removed.append(f"**Version:** {values['version']}")
    if "compatibility" in values:
        removed.append(f"**Compatibility:** {values['compatibility']}")

    if not removed:
        return ""

    return "\n".join(removed) + "\n\n"


def load_team_commands() -> set[str]:
    commands: set[str] = set()
    if not TEAM_COMMANDS_PATH.exists():
        return commands

    for line in read_text(TEAM_COMMANDS_PATH).splitlines():
        command = line.strip()
        if command and not command.startswith("#"):
            commands.add(command)
    return commands


def extract_frontmatter_block(text: str) -> str:
    end = text.find("\n---\n", 3)
    if end < 0:
        return ""
    return text[3:end]


def frontmatter_is_cloud_safe(text: str, description: str) -> bool:
    fm = extract_frontmatter_block(text)
    if not fm:
        return False
    if re.search(r"^metadata:", fm, re.M):
        return False
    if re.search(r"^description:\s*\|", fm, re.M):
        return False
    if not re.search(r"^description:\s*>", fm, re.M):
        return False
    if sanitize_for_cloud(description) != description:
        return False
    if '"' in fm:
        return False
    if "'" in fm:
        return False
    if "`" in fm:
        return False
    if re.search(r"[\u2192\u2014\u2013]", fm):
        return False
    return True


def normalize_skill(skill_file: Path, dry_run: bool) -> bool:
    directory = skill_file.parent.name
    text = read_text(skill_file)
    values, body = split_frontmatter(text)

    name = str(values.get("name", directory))
    description = str(values.get("description", "")).strip()
    if not description:
        raise SystemExit(f"Missing description: {skill_file}")

    extra_keys = [key for key in values if key not in ALLOWED_KEYS]
    sanitized = sanitize_for_cloud(description)
    needs_update = bool(extra_keys) or not frontmatter_is_cloud_safe(text, description)

    if not needs_update:
        return False

    preamble = metadata_preamble(values)
    body = body.lstrip("\n")
    if preamble and not body.startswith(preamble.splitlines()[0]):
        body = preamble + body

    rendered = render_skill_frontmatter(name, sanitized) + "\n\n" + body
    if not rendered.endswith("\n"):
        rendered += "\n"

    if dry_run:
        print(f"Would normalize {skill_file}")
    else:
        skill_file.write_text(rendered, encoding="utf-8")
        print(f"Normalized {skill_file}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    team_commands = load_team_commands()
    updated = 0

    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        if skill_file.parent.name not in team_commands:
            continue
        if normalize_skill(skill_file, args.dry_run):
            updated += 1

    if updated == 0:
        print("All team-command skills already Cloud-normalized.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
