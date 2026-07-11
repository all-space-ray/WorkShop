"""Shared Cloud-safe frontmatter helpers for repo skills and commands."""

from __future__ import annotations

import json
import re


def sanitize_for_cloud(description: str) -> str:
    text = description
    text = text.replace("\u2192", "->").replace("\u2014", "-").replace("\u2013", "-")
    text = text.replace('"', "").replace("`", "").replace("'", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fold_description(description: str) -> str:
    words = re.split(r"\s+", description.strip())
    lines: list[str] = []
    current: list[str] = []

    for word in words:
        candidate = " ".join(current + [word])
        if current and len(candidate) > 72:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)

    if current:
        lines.append(" ".join(current))

    return "\n".join(f"  {line}" for line in lines)


def render_skill_frontmatter(name: str, description: str) -> str:
    clean = sanitize_for_cloud(description)
    folded = fold_description(clean)
    return (
        "---\n"
        f"name: {name}\n"
        "description: >\n"
        f"{folded}\n"
        "disable-model-invocation: true\n"
        "---"
    )


def render_command_frontmatter(name: str, description: str) -> str:
    clean = sanitize_for_cloud(description)
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {json.dumps(clean)}\n"
        "---"
    )
