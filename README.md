# WorkShop

Test repository for validating the import of the All-Space-Setup template and the associated post-install setup, walking through the full user experience.

## Repository structure

```text
.agents/     Cloud-agent mirrors of skills and commands (generated; do not edit by hand)
.cursor/     Cursor rules, slash commands, and skills for repository-aware AI assistance
.github/     Pull request templates and GitHub metadata
docs/        Notes, decisions, references, and design documents
GrabMe/      Session handoff documents written by /handoff; deleted after pickup
os/          Personal OS: LLM-maintained knowledge base (schema in os/AGENTS.md)
scripts/     Small repository automation scripts
src/         Implementation code for concrete ideas
tests/       Automated tests that mirror `src/`
```

## Cursor setup

This repository includes a lightweight Cursor environment:

- `.cursor/rules/project.mdc` provides always-on project guidance.
- `.cursor/commands/*.md` exposes callable Cursor slash commands for installed skills.
- `.agents/skills/*/SKILL.md` and `.agents/commands/*.md` mirror team commands for Cloud agent cold-start discovery.
- `.cursor/team-commands.txt` is an auditable checklist of every repo-shared command; Cursor discovers the commands from `.cursor/commands/*.md` (desktop) and `.agents/commands/*.md` (Cloud).
- `.cursor/skills/*/SKILL.md` stores the skill instructions and supporting assets in-repo.
- `.cursor/skills/INDEX.md` and `.cursor/skills/index.json` are generated indexes of the installed skills.
- `.cursorignore` keeps local state, secrets, dependencies, and generated output out of Cursor indexing.
- `AGENTS.md` captures working conventions for coding agents.

Skill sources: engineering/productivity skills from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT); the docx document skill from [anthropics/skills](https://github.com/anthropics/skills); the remaining skills are defined in this repository's bootstrap document.

To call a team command, type `/` in Cursor Agent chat or on cursor.com/agents, then pick a command such as `/tdd`, `/triage`, or `/ingest-resource`. Team skills set `disable-model-invocation: true` so they appear in the slash menu.

Reindex skills and sync Cloud mirrors after changing `.cursor/skills/`, `.cursor/commands/`, or `.cursor/team-commands.txt`:

```sh
bash .cursor/scripts/sync-skill-commands.sh
bash scripts/sync-cloud-agent-assets.sh
python3 scripts/reindex-skills.py
```

## Verification

Run the scaffold check from the repository root:

```sh
bash scripts/check-repo.sh
```
