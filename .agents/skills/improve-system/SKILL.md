---
name: improve-system
description: >
  Review the current session and update the Personal OS - capture durable
  lessons into the wiki, update skills and schema, run a lint pass over
  os/, and flag stale or duplicated content for review.
disable-model-invocation: true
---

# Improve System

Review the current session and update the Personal OS — skills, knowledge, and structure — to reflect what actually happened. This skill combines session capture with the **Lint** operation defined in `os/AGENTS.md` — read that schema first.

## When to use

Invoke `/improve-system` at the end of a session (or after a meaningful chunk of work) when:

- You iterated on a skill's output and want those corrections captured
- You shared a lesson, story, or preference worth keeping
- You established new conventions, folder usage, or workflows
- You want a periodic health check of the wiki

## Steps

### 1. Review the session

Look for:

- **Skill iterations** — places where the user corrected, refined, or rejected output from a skill or workflow
- **Lessons and stories** — personal anecdotes, hard-won insights, "here is how I do it" moments
- **New knowledge** — preferences, constraints, or frameworks that came up
- **Structural changes** — new folders, renamed paths, updated conventions

### 2. Update skills when output was iterated

If the user refined a skill's output during the session:

1. Open the skill's `SKILL.md`.
2. Encode the iteration as a durable rule — the underlying preference, not a transcript.
3. Keep edits minimal and specific; do not rewrite unrelated sections.
4. Run any repo sync/validation scripts that apply to skills.

### 3. Save lessons to experiences

If the user shared a lesson or experiential insight, save it to `os/wiki/experiences/YYYY-MM-DD-slug.md`: what happened, what was learned, when it applies again. Preserve the user's voice — this is personal knowledge, not a summary report. Index and log it per the schema.

### 4. Update other Personal OS areas when warranted

| Signal | Where to update |
|--------|-----------------|
| Reusable method or mental model | `os/wiki/concepts/` |
| Durable cross-domain analysis or thesis | `os/wiki/synthesis/` |
| Domain-specific detail (person, org, project, tool) | that domain's folder, `os/wiki/<domain>/` |
| Wiki conventions that changed | `os/AGENTS.md` (propose, do not silently rewrite) |
| Repo-wide agent conventions | root `AGENTS.md` |

Do not invent updates. If nothing durable emerged, say so.

### 5. Lint the wiki

Run the health checks from the schema:

- Contradictions between pages; stale claims superseded by newer sources
- Orphan pages with no inbound links; concepts mentioned often but lacking a page
- Index entries that drifted from page content; log format violations
- Data gaps worth a web search or a new source

Apply additive fixes directly. Flag destructive actions (delete, merge) with file path, issue, and suggested action — let the user decide.

### 6. Refresh the template export (template source repo only)

If `template-manifest.json` exists at the repo root, this repository is the template source of truth for consumer repos. Regenerate the manifest so this session's changes ship on their next sync:

```bash
python3 scripts/update-template-manifest.py
```

Skip this step in consumer repositories (they have no manifest file).

### 7. Report back

```
## Improve System — Session Update

**Skills updated:** (list or "none")
**Experiences saved:** (list or "none")
**Other updates:** (list or "none")
**Flagged for review:** (list or "none")
```

Commit with: `Improve system: [scope]`.

## Quality bar

- **Capture decisions, not chatter** — write what future sessions need to know.
- **Minimal diffs** — touch only files that clearly benefit from the session.
- **Preserve voice** in `os/wiki/experiences/`.
- **Flag, do not purge** — surface stale or duplicated content; the user approves deletions.
