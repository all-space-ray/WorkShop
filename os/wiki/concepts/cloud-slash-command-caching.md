---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [cursor, cloud-agents, slash-commands, skills, caching, troubleshooting, personal-os]
sources: [../../raw/2026-07-10-personal-os-bootstrap.md]
---

# Cloud slash-command discovery and caching

How Cursor Cloud agents turn committed skills into the `/` slash-command menu, and why
that menu goes stale. This is the operational model behind the skills that drive this
Personal OS (`/ingest-resource`, `/improve-system`), so keeping the menu fresh matters for
running the system.

## The mental model

A skill is exposed as a slash command only when it exists in all four locations, with
Cloud-safe frontmatter, on the repository's default branch:

- `.cursor/skills/<name>/SKILL.md`
- `.cursor/commands/<name>.md`
- `.agents/skills/<name>/SKILL.md`
- `.agents/commands/<name>.md`

The menu you actually see is not read from live `main` at compose time. It is populated
from two cache layers that sit between the files and the menu:

1. The recorded **Cloud environment** for the repository (cached per-repo).
2. The web client's **command list** (cached in the browser session).

So the files on disk can be perfectly correct while the menu is stale. Stale menus are
almost always a discovery/caching problem, not a file problem.

## Diagnosis order

1. Confirm the files are correct: all four locations exist per skill; frontmatter is flat
   and Cloud-safe (`name` matches the folder, `disable-model-invocation: true`, folded
   `description: >`, no quotes/apostrophes/backticks/unicode dashes, no nested `metadata:`).
   In this repo `bash scripts/check-repo.sh` and `bash .cursor/scripts/validate-skills.sh`
   verify all of this automatically.
2. Confirm the skills are on the **default branch** (`main`), not a feature branch or an
   unmerged PR. This is the single most common cause; nothing else helps until they merge.
3. Only then treat it as caching.

## Forcing a refresh

Once the files are correct and merged to `main`:

- Bump `.cursor/environment.json` (a harmless change to the `start` message is enough).
  Cloud then observes a modified environment and re-records it from current `main` on the
  next run. This is the one refresh lever that lives in the repo.
- Start a **brand-new** agent thread (existing sessions keep the environment and command
  list they started with).
- Hard-refresh the web client (Cmd/Ctrl+Shift+R) or log out and back in.
- Optionally re-save/rebuild the environment in the Dashboard; some repos boot
  just-in-time with no snapshot to rebuild, which is expected.

## The guaranteed fallback

The menu is only a convenience listing — skills load from `main` at runtime regardless, so
plain-language invocation always works even when the menu is empty: e.g. "Use the tdd
skill." or "Follow the improve-system skill." If plain-language works but the menu does
not, that definitively confirms a menu-cache issue, which expires on its own (typically
within a short time, up to a day).

## See also

- Source: [Personal OS Bootstrap](../sources/2026-07-10-personal-os-bootstrap.md)
- Concept: [The LLM Wiki pattern](llm-wiki-pattern.md)
