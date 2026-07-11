# System Guide: how this repository works

This repository is a **template and single source of truth** for skills, company data, enforced rules, and document templates. Employees import it into their own repositories, add their personal information locally, and pull updates on a schedule. This guide explains every moving part. To be walked through it interactively (with first-run setup), run `/initialize`.

## The three systems

### 1. The Personal OS (`os/`)

A persistent, agent-maintained knowledge base:

- **`os/raw/`** - immutable source documents. Agents never modify these after creation.
- **`os/wiki/`** - agent-owned distilled pages: company profiles, competitor dossiers, rules, concepts, experiences.
- **`os/AGENTS.md`** - the schema (read it before any work inside `os/`); **`os/index.md`** - the catalog (read it before answering from the wiki); **`os/log.md`** - append-only history.

Two operating skills drive it: **`/ingest-resource`** (bring knowledge in: save raw, summarize, cross-reference, index, log) and **`/improve-system`** (capture session lessons, lint the wiki, and in the template repo, refresh the export manifest).

Token discipline: outside `os/` work the directory costs zero tokens; inside it, go schema -> index -> only the pages you need. Never bulk-read the wiki.

### 2. Enforced rules (`os/wiki/rules/` -> `.cursor/rules/`)

Rules pages are the master copies. `scripts/sync-rules.py` exports each one to `.cursor/rules/<slug>.mdc`:

- Pages with `globs:` frontmatter auto-attach when matching files are edited (e.g. the FastAPI/React standards).
- Pages without `globs:` are agent-requested by description (e.g. writing style, the program workflow).
- Nothing uses `alwaysApply`, so idle context cost is one description line per rule.

Edit the wiki page, run `python3 scripts/sync-rules.py`, never hand-edit a generated `.mdc`. `scripts/check-repo.sh` fails on drift.

### 3. The skills (`.cursor/skills/`)

31 team skills, each exposed as a `/` slash command. They fall into groups:

- **Engineering flow (Matt Pocock's skills):** the ordered pipeline for building things; see the next section.
- **Personal OS operations:** `/ingest-resource`, `/improve-system`.
- **Repo/system operations:** `/initialize`, `/import-template`, `/handoff`, `/setup-matt-pocock-skills`.
- **Deliverables and writing:** `/docx`, `/executive-briefing`, `/edit-article`, `/humanizer`, `/teach`, `/obsidian-vault`.

`/ask-matt` is the router: ask it which skill fits when unsure.

## The engineering flow: proper order and usage

This is enforced by the [program-workflow rule](../os/wiki/rules/program-workflow.md). Full detail lives there; the shape:

```text
                         one-time per repo: /setup-matt-pocock-skills
                                       |
  /research (background, feeds in) --> /wayfinder   (DEFAULT ENTRY: chart the map, then
                                       |             resolve one decision ticket per session;
                                       |             drives /grilling + /domain-modeling inside;
                                       |             prototype tickets: /handoff -> /prototype)
                                       |
                                       |   small effort, no fog? fall back to /grill-with-docs
                                       |   (or /grill-me without a codebase), same conversation
                                       v
                       multi-session?  /to-spec -> /to-tickets     single-session? skip
                                       |
                                       v
                       /implement per ticket (fresh context each) -- drives /tdd internally
                                       |
                                       v
                       /code-review (Standards + Spec axes) -> commit
                                       |
                                       v
                       /improve-system (capture lessons back into the OS)

  on-ramp: incoming bugs/requests you did not write -> /triage first
  on-ramp: hard bug -> /diagnosing-bugs (feedback loop first, then regression-test fix)
  vocabulary underneath: /domain-modeling (terms), /codebase-design (module shape)
```

**Why this order:** wayfinding (and the grilling it drives) kills assumptions before they become code, one decision-sized session at a time; specs and tickets let each implementation run in a small, fresh context window (the token-burn control); TDD plus two-axis review make quality repeatable. Wayfinder resolves ONE map ticket per session; on the grill fallback, keep grill -> spec -> tickets in ONE unbroken context window; give each `/implement` its own.

**When it applies:** new programs, products, major features, multi-session builds. NOT simple research questions, quick fixes, or informational asks.

## Voice, tone, and style (`os/wiki/my-voice/`)

For agents to write in **your** voice, you must give them samples. During `/initialize` (or any time after):

1. Provide 3-10 writing samples that sound like you: emails you are proud of, docs, posts. Paste them or `/ingest-resource` them; they are filed under `os/wiki/my-voice/<your-slug>/samples/`.
2. The agent distills a voice profile (sentence length, formality, vocabulary, signature moves, things you never say) into `os/wiki/my-voice/<your-slug>/profile.md`.
3. Deliverable-producing skills (docx, executive-briefing, edit-article) consult that profile; the universal [writing-style rules](../os/wiki/rules/writing-style.md) still apply on top.

The more varied the samples (formal + casual, long + short), the better the profile.

## What is universal vs personal

| Universal (ships in the template) | Personal (you add locally, never exported) |
|-----------------------------------|--------------------------------------------|
| All skills, commands, rules, scripts | `os/wiki/my-voice/` samples and profiles |
| Company profiles (York, All.Space) | `os/wiki/career/` content (resumes, applications) |
| Competitor dossiers and rankings | `os/wiki/experiences/` (your session lessons) |
| Document templates and generators | `os/log.md` (your repo's history) |
| The Personal OS schema and scaffolding | Any project-specific domains you create |

The import tool never deletes or overwrites your local changes: modified files are staged for an additive merge instead (see next section).

## The template lifecycle

- **This repo (the source of truth):** `template-manifest.json` lists every universal file with a content hash. `/improve-system` refreshes it after each session; `scripts/check-repo.sh` fails if it goes stale.
- **Employee repos (consumers):** run `/import-template` (or `python3 scripts/import-template.py`) to pull the latest template. First run copies everything and records state; later runs fast-forward unmodified files, stage changed-on-both-sides files into `.template-incoming/` for an agent-mediated additive merge, and never delete local content.
- **Staying current:** set a weekly scheduled automation in the consumer repo with the prompt in [import-template's SKILL.md](../.cursor/skills/import-template/SKILL.md). Personal setup (voice, PII) happens once via `/initialize`, not on weekly syncs.
- **Rollout runbook:** owner-side GitHub setup (visibility, team access, cloud-agent token), first-import steps for blank and populated repos, and the pilot test plan live in [template-rollout.md](template-rollout.md).

## Housekeeping commands

| Task | Command |
|------|---------|
| Validate everything | `bash scripts/check-repo.sh` |
| After editing skills/commands | `python3 scripts/normalize-cloud-skill-frontmatter.py && bash .cursor/scripts/sync-skill-commands.sh && bash scripts/sync-cloud-agent-assets.sh && python3 scripts/reindex-skills.py` |
| After editing rules pages | `python3 scripts/sync-rules.py` |
| Refresh the export manifest (template repo only) | `python3 scripts/update-template-manifest.py` |
| Pull template updates (consumer repos) | `python3 scripts/import-template.py` |
| Weekly competitor intel pull | `python3 scripts/competitor-weekly-pull.py` |
