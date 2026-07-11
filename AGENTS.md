# Agent Instructions

This repository is a workshop for ideas. Preserve that flexibility while keeping the tree easy to navigate.

## Working conventions

- Read `README.md` and the relevant folder README before editing.
- Keep repository-wide conventions in `.cursor/rules/` and contributor-facing guidance in this file.
- Use `.cursor/commands/<name>.md` as callable wrappers for repository skills in `.cursor/skills/<name>/SKILL.md`. Command wrappers set `name` (matching the filename) and a single-line `description` synced from the skill; Cloud agents rely on this format at cold start.
- Team-command skills set `disable-model-invocation: true` in `SKILL.md` so they appear in the `/` menu on desktop and web. Use flat frontmatter (`name`, folded `description: >`, optional flags). Keep skill frontmatter free of double quotes, unicode arrows, nested `metadata:` blocks, and literal `description: |` blocks, which break Cloud slash-menu parsing.
- Keep `.cursor/team-commands.txt` aligned with all repo-shared command files; it is a verification manifest, not a Cursor config file.
- Run `python3 scripts/reindex-skills.py` after changing skills, skill commands, or the team command manifest.
- Run `bash .cursor/scripts/sync-skill-commands.sh` to regenerate command wrappers from skill descriptions.
- Run `bash scripts/sync-cloud-agent-assets.sh` to mirror team skills and commands into `.agents/` for Cloud discovery.
- Run `bash .cursor/scripts/validate-skills.sh` to catch Cloud-unsafe frontmatter before merge.
- Add code under `src/`, tests under `tests/`, scripts under `scripts/`, and documentation under `docs/`.
- The Personal OS (LLM-maintained knowledge base) lives in `os/`. Read `os/AGENTS.md` before any work inside `os/`; ignore the directory entirely for unrelated tasks. Portable setup guide: `docs/personal-os-bootstrap.md`.
- **This repository is the template source of truth** for employee repos: `template-manifest.json` lists every universal file (regenerate with `python3 scripts/update-template-manifest.py`; `/improve-system` does this automatically; `check-repo.sh` fails if stale). Consumer repos pull with `/import-template` (`scripts/import-template.py`), which amends rather than replaces: modified files are staged to `.template-incoming/` for additive merge, and personal content (`os/log.md`, experiences, voice samples, career) is never exported. New users run `/initialize` for the system tour and personal setup; the full explainer is `docs/system-guide.md`.
- When the user starts a discussion about creating a new program, product, or major task, follow the enforced workflow in `os/wiki/rules/program-workflow.md` (wayfinder -> spec -> tickets -> implement -> review; `/ask-matt` routes; grill-with-docs is the small-effort fallback). Not for simple research questions or quick fixes.
- Session handoffs live in `GrabMe/` at the repo root (committed, so they survive across cloud agents). If `GrabMe/` contains a handoff addressed to your task, read it first, then delete it and commit the deletion.
- Setup and testing progress is tracked in `docs/setup-test-checklist.md` (committed, persists across agents). When working on setup or validation, read it first and keep its checkboxes and Log current.
- Enforced rules live in `os/wiki/rules/` (source of truth) and are exported to `.cursor/rules/*.mdc` by `scripts/sync-rules.py`. Cursor auto-attaches or agent-requests them so they apply only when relevant (no `alwaysApply` bloat). Edit the wiki page, then run `python3 scripts/sync-rules.py`; never hand-edit the generated `.mdc`. Writing rules in `os/wiki/rules/writing-style.md` apply to all generated text and documents.
- Do not add a framework, package manager, or generated lockfile until a specific project requires it.
- Keep secrets and local machine state out of git.
- Update documentation when a change introduces a new convention, command, or folder.

## Verification

- Run `bash scripts/check-repo.sh` after changing the scaffold.
- The scaffold check verifies that each required skill has a matching command wrapper, team command entry, `.agents/skills/<name>/SKILL.md` mirror, and `.agents/commands/<name>.md` mirror for Cloud discovery.
- If a language stack is added later, document its install and test commands in `README.md`.

## Cursor Cloud agents

Cloud agents discover slash-menu skills and commands from `.agents/skills/<name>/SKILL.md`, `.agents/commands/<name>.md`, and (fallback) `.cursor/skills/<name>/SKILL.md`. This repo keeps `.agents/` mirrors in sync with `.cursor/`:

- Source of truth: `.cursor/skills/<name>/SKILL.md` and `.cursor/commands/<name>.md`
- Cloud mirrors: `.agents/skills/<name>/SKILL.md` and `.agents/commands/<name>.md` (synced on agent boot via `.cursor/environment.json`)

After changing skills or commands, run:

```sh
python3 scripts/normalize-cloud-skill-frontmatter.py
bash .cursor/scripts/sync-skill-commands.sh
bash scripts/sync-cloud-agent-assets.sh
python3 scripts/reindex-skills.py
bash scripts/check-repo.sh
```

If a brand-new Cloud agent shows stale or missing repo slash commands:

1. Confirm the agent starts from latest `main` (not an old snapshot branch).
2. Hard-refresh cursor.com (the compose-box command list caches) and start a new agent thread, not a follow-up in an existing session.
3. The menu is cosmetic: skills on `main` load at runtime regardless, so describing the skill in plain text (for example, "use the tdd skill") always works.

## Cursor Cloud specific instructions

This repository has no traditional runtime service. The "application" is the agentic-workshop scaffold generated from `universal-repo-bootstrap.md`, plus the Personal OS knowledge base in `os/`. Setup targets are `python3`, `bash`, and `git` only (no package manager or lockfile).

- Lint/test/build gate: `bash scripts/check-repo.sh` (validates required paths, 31 skills, command wrappers, `.agents/` mirrors, manifest parity, rule exports, the template export manifest, and the generated skill index). Treat a green run of this script as the build passing.
- Run the pipeline in this exact order after touching skills/commands: `python3 scripts/normalize-cloud-skill-frontmatter.py` → `bash .cursor/scripts/sync-skill-commands.sh` → `bash scripts/sync-cloud-agent-assets.sh` → `python3 scripts/reindex-skills.py` → `bash .cursor/scripts/validate-skills.sh` → `bash scripts/check-repo.sh`.
- Non-obvious gotcha: `scripts/sync-skill-commands.py` does not create output directories. Before running it against an empty tree, ensure `.cursor/commands/`, `.agents/skills/`, and `.agents/commands/` exist (`mkdir -p`). This only bites when regenerating from scratch; on a populated repo the dirs already exist.
- Rebuilding the scaffold from the bootstrap doc re-fetches external skills from GitHub (`mattpocock/skills`, `anthropics/skills`); this needs network. Once committed the skills live in-repo, so normal runs need no network.
- The `docx` skill's helper scripts import `defusedxml` and `lxml` (installed by the startup update script). `pandoc` and LibreOffice are optional and only needed to verify generated Word documents.
- Personal OS core loop: add knowledge with `/ingest-resource` (saves an immutable copy under `os/raw/`, writes a summary page, updates `os/index.md` and `os/log.md`); capture lessons with `/improve-system`. Never glob-read `os/wiki/`; go schema → `os/index.md` → only the needed pages.
- `os/raw/` files are immutable and are verbatim sources, so link-checkers and `[[wikilink]]` scans will legitimately flag example/`slug.md` links inside them; only enforce link/frontmatter rules on `os/wiki/` pages.
- `README.md` intentionally keeps the `<REPO-NAME>` and one-line-description placeholders until the owner personalizes them (Stage 7); do not invent values.

## Cloud Agent VM desktop preview

- **Cloud Agent VM desktop is viewable: run dev servers on it.** The Cloud Agent VM has a desktop the operator can see through the Cursor interface (Desktop tab), including a browser. So `localhost` on the VM **is** reachable by the user. To let Lindsay preview the site, start the dev server on the VM yourself in a persistent `tmux` session (`npm run dev` from the site's project directory), confirm it serves (`curl -s -o /dev/null -w '%{http_code}' http://localhost:3000`), and tell her to open/refresh `http://localhost:3000` in the Desktop tab. Do **not** claim the VM's localhost is unreachable. Dev mode hot-reloads, so after edits just tell her to refresh.
- **User's preference: start the dev server automatically, don't wait to be asked.** Whenever you make changes to the site project, start (or confirm) the `npm run dev` server on the VM as part of the work, and tell her the URL to refresh. She controls the remote Desktop tab easily and prefers **not** to run bash commands themself, so never leave previewing as a manual step for them. (Reminder: don't run `npm run build` while dev is running, since it clobbers `.next`; stop dev, build, then restart it.)
