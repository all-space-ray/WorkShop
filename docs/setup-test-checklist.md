# Setup and test checklist

Persistent, cross-agent tracker for validating the All-Space-Setup import and walking the full new-user experience. This file is committed to git, so it survives across Cloud Agent sessions. Any agent working setup or testing should read this first and keep it current.

## How to use

- Status keys: `[ ]` not started, `[~]` in progress or partial, `[x]` done, `[-]` skipped/not needed.
- When you finish or advance an item, update its box and add a dated note under [Log](#log).
- Keep this additive. Do not delete history; append.
- This is the owner's validation tracker, not a template-universal convention. It stays local to this repo.

## Personal setup (from `/initialize`)

- [x] **Repo identity** - README description set (PR #2).
- [~] **Voice and tone** - two email extractions ingested (Claude 52 + Fable 5 65), profile built at `os/wiki/my-voice/raymond/voice-profile.md`. Pending: curated Word-document samples once authorship is confirmed.
- [ ] **PII / career** - optional. Ingest a resume into `os/wiki/career/` and/or add project domains via `/ingest-resource`.
- [~] **Issue tracker** - `/setup-matt-pocock-skills` done: GitHub tracker, PRs off, default labels, single-context; config in `docs/agents/` and the `## Agent skills` block in `AGENTS.md`. Remaining: create the five GitHub labels once with write access (commands in `docs/agents/triage-labels.md`); this Cloud agent's `gh` is read-only.
- [ ] **Update automation** - optional weekly `/import-template` scheduled agent to stay current with the template.

## System / feature testing (the UX walkthrough)

### Personal OS
- [x] `/ingest-resource` - exercised by the voice ingests.
- [ ] Query the wiki - ask a question answered from `os/index.md` and a wiki page; confirm token discipline (index first).
- [ ] `/improve-system` - capture a session lesson into `os/wiki/experiences/` and refresh state.

### Engineering flow (requires the issue tracker above)
- [ ] `/triage` - process an incoming issue through the label state machine.
- [ ] `/wayfinder` - create a map issue and resolve one decision ticket.
- [ ] `/grill-with-docs` or `/grill-me` - small-effort fallback grilling.
- [ ] `/to-spec` then `/to-tickets` - multi-session path.
- [ ] `/implement` (drives `/tdd`) - build one ticket in a fresh context.
- [ ] `/code-review` - two-axis review (Standards + Spec).
- [ ] `/diagnosing-bugs` - feedback-loop-first bug hunt.
- [ ] Vocabulary skills: `/domain-modeling`, `/codebase-design`, `/improve-codebase-architecture`.
- [ ] `/prototype` (via `/handoff`).

### Deliverables and writing (should consult the voice profile)
- [ ] `/docx` - generate a Word document.
- [ ] `/executive-briefing`.
- [ ] `/edit-article`.
- [ ] `/humanizer`.
- [ ] `/teach`.
- [ ] `/obsidian-vault`.

### Repo / system operations
- [x] `/initialize` - system tour + personal setup (this walkthrough).
- [ ] `/import-template` - pull template updates additively.
- [ ] `/handoff` - write a `GrabMe/` handoff and confirm a later agent picks it up.
- [ ] `/ask-matt` - router picks the right skill.

### Rules and infrastructure
- [ ] Writing-style enforcement - confirm generated text has no em dashes.
- [ ] Program-workflow enforcement - confirm major-task requests route through the workflow.
- [ ] `python3 scripts/sync-rules.py` - rules export in sync.
- [x] `bash scripts/check-repo.sh` - scaffold gate green.
- [ ] Cloud slash-menu discovery - confirm `/` commands appear from `.agents/` mirrors in a fresh Cloud agent.

## Log

- 2026-07-11: Created this checklist. Repo identity done; voice done for email (2 extractions), Word docs pending; started `/setup-matt-pocock-skills` (GitHub tracker, single-context).
- 2026-07-11: `/setup-matt-pocock-skills` config complete - wrote `docs/agents/{issue-tracker,triage-labels,domain}.md` and the `## Agent skills` block in `AGENTS.md`. GitHub labels not yet created (Cloud `gh` is read-only); commands documented in `docs/agents/triage-labels.md`.
