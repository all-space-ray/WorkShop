#!/usr/bin/env bash
set -euo pipefail

# Regenerate .cursor/commands/*.md wrappers from installed skill frontmatter.
# Keeps description-only command frontmatter in sync with SKILL.md.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
exec python3 "$ROOT/scripts/sync-skill-commands.py" "$@"
