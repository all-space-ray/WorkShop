#!/usr/bin/env bash
set -euo pipefail

# Validate Cursor skill and command files for Cloud-agent slash-menu discovery.
# Fails on frontmatter patterns that break naive YAML parsers on cursor.com/agents.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

missing=0
declare -A team_commands=()

if [[ -f ".cursor/team-commands.txt" ]]; then
  while IFS= read -r command || [[ -n "$command" ]]; do
    [[ -z "$command" || "$command" == \#* ]] && continue
    team_commands["$command"]=1
  done < ".cursor/team-commands.txt"
fi

extract_frontmatter() {
  awk '/^---$/{p++;next} p==1 && /^---$/{exit} p==1 {print}' "$1"
}

check_skill() {
  local skill_file="$1"
  local skill_dir
  skill_dir="$(basename "$(dirname "$skill_file")")"
  local normalized fm
  normalized="$(mktemp)"
  tr -d '\r' < "$skill_file" > "$normalized"

  if [[ "$(head -n1 "$normalized")" != "---" ]]; then
    echo "Missing YAML frontmatter: $skill_file"
    missing=1
    rm -f "$normalized"
    return
  fi

  fm="$(extract_frontmatter "$normalized")"

  if [[ ! "$skill_dir" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
    echo "Skill directory must be lowercase letters, digits, and hyphens: $skill_file"
    missing=1
  fi

  if ! grep -Eq "^name:[[:space:]]*${skill_dir}[[:space:]]*$" <<< "$fm"; then
    echo "name frontmatter must match folder: $skill_file"
    missing=1
  fi

  if grep -Eq '^allowed-tools:' <<< "$fm"; then
    echo "Move allowed-tools out of frontmatter (Cloud slash menu): $skill_file"
    missing=1
  fi

  if grep -Eq '^argument-hint:' <<< "$fm"; then
    echo "Move argument-hint out of frontmatter (Cloud slash menu): $skill_file"
    missing=1
  fi

  if [[ -n "${team_commands[$skill_dir]:-}" ]]; then
    local key
    for key in $(awk '/:/ && !/^[[:space:]]/ {print $1}' <<< "$fm" | tr -d ':'); do
      case "$key" in
        name|description|disable-model-invocation) ;;
        *)
          echo "Team command skill has non-Cloud frontmatter key ($key): $skill_file"
          missing=1
          ;;
      esac
    done

    if ! grep -Fq "disable-model-invocation: true" <<< "$fm"; then
      echo "Team command skill must set disable-model-invocation: true: $skill_file"
      missing=1
    fi

    if ! grep -Eq '^description:[[:space:]]*>' <<< "$fm"; then
      echo "Team command skill must use folded description (description: >): $skill_file"
      missing=1
    fi

    if grep -F '"' <<< "$fm" >/dev/null; then
      echo "Remove double quotes from skill frontmatter: $skill_file"
      missing=1
    fi

    if grep -F "'" <<< "$fm" >/dev/null; then
      echo "Remove apostrophes from skill frontmatter: $skill_file"
      missing=1
    fi

    if grep -F '`' <<< "$fm" >/dev/null; then
      echo "Remove backticks from skill frontmatter: $skill_file"
      missing=1
    fi

    if grep -E $'[\342\206\222\342\200\224\342\200\223]' <<< "$fm" >/dev/null; then
      echo "Replace unicode arrows or dashes in skill frontmatter: $skill_file"
      missing=1
    fi
  fi

  if grep -Eq '^metadata:' <<< "$fm"; then
    echo "Nested metadata block not supported in Cloud slash menu: $skill_file"
    missing=1
  fi

  if grep -Eq '^description:[[:space:]]*\|' <<< "$fm"; then
    echo "Use folded description (description: >) not literal block (description: |): $skill_file"
    missing=1
  fi

  if grep -Eq '\([^)]+\.com\):' <<< "$fm"; then
    echo "Avoid (url): patterns inside descriptions: $skill_file"
    missing=1
  fi

  rm -f "$normalized"
}

check_command() {
  local command_file="$1"
  local command_name
  command_name="$(basename "$command_file" .md)"
  local normalized fm
  normalized="$(mktemp)"
  tr -d '\r' < "$command_file" > "$normalized"

  if ! grep -Eq "^name:[[:space:]]*${command_name}[[:space:]]*$" "$normalized"; then
    echo "Command must set name frontmatter matching filename: $command_file"
    missing=1
  fi

  if ! grep -Eq '^description:' "$normalized"; then
    echo "Command is missing description frontmatter: $command_file"
    missing=1
  fi

  fm="$(extract_frontmatter "$normalized")"

  if grep -Eq '^description:[[:space:]]*>' <<< "$fm"; then
    echo "Use single-line command description, not folded block (description: >): $command_file"
    missing=1
  fi

  if grep -Eq '^description:[[:space:]]*\|' <<< "$fm"; then
    echo "Use single-line command description, not literal block (description: |): $command_file"
    missing=1
  fi

  fm="$(extract_frontmatter "$normalized")"
  if grep -E $'[\342\206\222\342\200\224\342\200\223]' <<< "$fm" >/dev/null; then
    echo "Replace unicode arrows or dashes in command frontmatter: $command_file"
    missing=1
  fi

  if grep -Eq '\([^)]+\.com\):' "$normalized"; then
    echo "Avoid (url): patterns inside command descriptions: $command_file"
    missing=1
  fi

  rm -f "$normalized"
}

for skill_file in .cursor/skills/*/SKILL.md; do
  check_skill "$skill_file"
done

for command_file in .cursor/commands/*.md; do
  check_command "$command_file"
done

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "Skill and command frontmatter validation passed."
