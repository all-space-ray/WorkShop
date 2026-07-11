# Scripts

Place small repository automation scripts here.

Scripts should be safe to run from the repository root and should document any required dependencies in `README.md`.

## Available scripts

- `check-repo.sh` - Verifies the repository scaffold, skill commands, team command manifest, generated skill index, Cloud-safe frontmatter, and rule exports (`sync-rules.py --check`).
- `sync-rules.py` - Exports enforced rules from `os/wiki/rules/*.md` into `.cursor/rules/*.mdc` (Auto-Attached when a page declares `globs:`, otherwise Agent-Requested; never `alwaysApply`). Run with `--check` to fail on drift. Never hand-edit the generated `.mdc` files.
- `update-template-manifest.py` - Regenerates `template-manifest.json`, the export manifest consumer repos import against (universal files only; personal content excluded). `--check` wired into `check-repo.sh`; `/improve-system` refreshes it each session.
- `import-template.py` - Consumer-side importer: pulls the template source of truth and applies it with amend-not-replace semantics (new files copied, unmodified files fast-forwarded, modified files staged to `.template-incoming/` for additive merge, nothing deleted). `--dry-run`, `--source`, `--record` supported.
- `competitor-weekly-pull.py` - Queries the USAspending API for the trailing week of federal awards across all tracked competitors (see `os/wiki/competitors/monitoring-and-automation.md`).
- `normalize-cloud-skill-frontmatter.py` - Strips Cloud-unsafe keys from team-command `SKILL.md` frontmatter and folds descriptions.
- `sync-agents-skills-mirror.py` - Mirrors team-command `SKILL.md` files into `.agents/skills/` for Cloud agent discovery.
- `sync-agents-commands-mirror.py` - Mirrors `.cursor/commands/*.md` into `.agents/commands/` for Cloud slash-menu discovery.
- `sync-cloud-agent-assets.sh` - Runs both Cloud mirror sync scripts (used by `.cursor/environment.json` install).
- `reindex-skills.py` - Regenerates `.cursor/skills/INDEX.md` and `.cursor/skills/index.json` from installed skills.
- `sync-skill-commands.py` - Regenerates `.cursor/commands/*.md` wrappers from skill `SKILL.md` descriptions. Wrapper: `bash .cursor/scripts/sync-skill-commands.sh`.
- `.cursor/scripts/validate-skills.sh` - Fails on frontmatter patterns that break Cloud slash-menu discovery.
