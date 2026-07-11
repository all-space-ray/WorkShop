#!/usr/bin/env bash
set -euo pipefail

# Sync repo assets Cloud agents read at cold start (.agents/* mirrors).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/sync-agents-skills-mirror.py
python3 scripts/sync-agents-commands-mirror.py
