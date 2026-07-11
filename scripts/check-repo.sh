#!/usr/bin/env bash
set -euo pipefail

required_paths=(
  ".cursor/rules/project.mdc"
  ".cursor/environment.json"
  ".cursor/skills/INDEX.md"
  ".cursor/skills/index.json"
  ".cursor/team-commands.txt"
  ".cursorignore"
  ".editorconfig"
  ".github/PULL_REQUEST_TEMPLATE.md"
  ".gitignore"
  "AGENTS.md"
  "CONTRIBUTING.md"
  "README.md"
  "docs/README.md"
  "docs/decisions/README.md"
  "scripts/README.md"
  "src/README.md"
  "scripts/reindex-skills.py"
  "scripts/sync-rules.py"
  "scripts/sync-skill-commands.py"
  "scripts/sync-agents-skills-mirror.py"
  "scripts/sync-agents-commands-mirror.py"
  "scripts/sync-cloud-agent-assets.sh"
  "tests/README.md"
)

required_skills=(
  "ask-matt"
  "code-review"
  "codebase-design"
  "diagnosing-bugs"
  "docx"
  "domain-modeling"
  "edit-article"
  "executive-briefing"
  "grill-me"
  "grill-with-docs"
  "grilling"
  "handoff"
  "humanizer"
  "implement"
  "import-template"
  "improve-codebase-architecture"
  "improve-system"
  "ingest-resource"
  "initialize"
  "obsidian-vault"
  "prototype"
  "research"
  "resolving-merge-conflicts"
  "setup-matt-pocock-skills"
  "tdd"
  "teach"
  "to-spec"
  "to-tickets"
  "triage"
  "wayfinder"
  "writing-great-skills"
)

missing=0
shopt -s nullglob

for path in "${required_paths[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "Missing required path: $path"
    missing=1
  fi
done

for skill in "${required_skills[@]}"; do
  skill_path=".cursor/skills/$skill/SKILL.md"
  command_path=".cursor/commands/$skill.md"

  if [[ ! -f "$skill_path" ]]; then
    echo "Missing required skill: $skill_path"
    missing=1
  fi

  if [[ ! -f "$command_path" ]]; then
    echo "Missing required skill command: $command_path"
    missing=1
  elif ! grep -Fq "$skill_path" "$command_path"; then
    echo "Skill command does not reference its skill: $command_path"
    missing=1
  elif ! grep -Fq "disable-model-invocation: true" "$skill_path"; then
    echo "Team command skill must set disable-model-invocation: true: $skill_path"
    missing=1
  elif ! grep -Eq '^description:' "$command_path"; then
    echo "Skill command is missing description frontmatter: $command_path"
    missing=1
  elif ! grep -Eq "^name:[[:space:]]*${skill}[[:space:]]*$" "$command_path"; then
    echo "Skill command must set name frontmatter matching filename: $command_path"
    missing=1
  elif grep -Eq '^description:[[:space:]]*>' "$command_path"; then
    echo "Skill command must use single-line description, not folded block: $command_path"
    missing=1
  fi
done

declare -A team_commands=()

if [[ -f ".cursor/team-commands.txt" ]]; then
  while IFS= read -r command || [[ -n "$command" ]]; do
    [[ -z "$command" || "$command" == \#* ]] && continue

    if [[ ! "$command" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
      echo "Invalid team command name: $command"
      missing=1
      continue
    fi

    if [[ -n "${team_commands[$command]:-}" ]]; then
      echo "Duplicate team command entry: $command"
      missing=1
    fi

    team_commands["$command"]=1
  done < ".cursor/team-commands.txt"
fi

for skill_file in .cursor/skills/*/SKILL.md; do
  skill_dir="${skill_file%/SKILL.md}"
  skill="${skill_dir##*/}"
  command_path=".cursor/commands/$skill.md"

  if [[ ! -f "$command_path" ]]; then
    echo "Missing command for installed skill: $command_path"
    missing=1
  elif ! grep -Fq "$skill_file" "$command_path"; then
    echo "Installed skill command does not reference its skill: $command_path"
    missing=1
  fi
done

for command_path in .cursor/commands/*.md; do
  command_file="${command_path##*/}"
  command="${command_file%.md}"
  skill_path=".cursor/skills/$command/SKILL.md"

  if [[ ! -f "$skill_path" ]]; then
    echo "Command has no matching skill: $command_path"
    missing=1
  fi

  if [[ -z "${team_commands[$command]:-}" ]]; then
    echo "Command is not listed as a team command: $command_path"
    missing=1
  fi
done

for command in "${!team_commands[@]}"; do
  command_path=".cursor/commands/$command.md"
  agents_command_path=".agents/commands/$command.md"
  agents_skill_path=".agents/skills/$command/SKILL.md"

  if [[ ! -f "$command_path" ]]; then
    echo "Team command has no command file: $command"
    missing=1
  fi

  if [[ ! -f "$agents_skill_path" ]]; then
    echo "Team command has no Cloud skill mirror: $agents_skill_path"
    missing=1
  fi

  if [[ ! -f "$agents_command_path" ]]; then
    echo "Team command has no Cloud command mirror: $agents_command_path"
    missing=1
  elif ! grep -Fq "$agents_skill_path" "$agents_command_path"; then
    echo "Cloud command mirror does not reference its skill: $agents_command_path"
    missing=1
  fi
done

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

bash .cursor/scripts/validate-skills.sh

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

python3 scripts/sync-skill-commands.py --check
python3 scripts/sync-agents-skills-mirror.py --check
python3 scripts/sync-agents-commands-mirror.py --check
python3 scripts/reindex-skills.py --self-test --quiet
python3 scripts/reindex-skills.py --output-dir "$tmp_dir" --quiet

if ! cmp -s "$tmp_dir/index.json" ".cursor/skills/index.json"; then
  echo "Skill index is stale: .cursor/skills/index.json"
  missing=1
fi

if ! cmp -s "$tmp_dir/INDEX.md" ".cursor/skills/INDEX.md"; then
  echo "Skill index is stale: .cursor/skills/INDEX.md"
  missing=1
fi

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

python3 scripts/sync-rules.py --check

if [[ -f "template-manifest.json" ]]; then
  python3 scripts/update-template-manifest.py --check
fi

echo "Repository scaffold checks passed."
