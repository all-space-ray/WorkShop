---
type: concept
created: 2026-07-09
updated: 2026-07-09
tags: [rules, coding-standards, style, meta]
sources: []
---

# Rules

The owner's repository of enforced best practices: coding standards per language and architecture, plus language/writing rules that apply to everything an agent produces. The goal is consistency; no matter which agent or AI model does the work, the output follows the same rules, which makes troubleshooting and review dramatically easier.

## How this section works

- **One page per language, framework, or architecture topic:** `rules/typescript.md`, `rules/python.md`, `rules/api-design.md`, and so on. Created when the first rules for that topic arrive.
- **One page for universal language/writing rules:** [writing-style.md](writing-style.md), which applies to prose, comments, commit messages, documents, and any generated text.
- Pages state each rule, the reason for it when known, and any exceptions. Rules are numbered or bolded so they can be referenced precisely.
- Rules come from the owner (stated preferences), from corrections during sessions (captured via `/improve-system`), and from vetted external sources the owner approves.

## How agents must use this section

1. **Authoring rules:** file them here, in the right topic page. Owner corrections during a session are rules in waiting; capture them.
2. **Enforcing rules in a coding session:** when working inside this repository on a topic that has a rules page, read that page first and follow it.
3. **Enforcing rules in this repository (automatic):** every topic page here is exported to `.cursor/rules/<slug>.mdc` by `scripts/sync-rules.py`, and `scripts/check-repo.sh` fails if any export is missing or stale. Exports are token-efficient by design: a page with `globs:` frontmatter becomes an Auto-Attached rule (its body loads only when a matching file is in context), and a page without `globs:` becomes an Agent-Requested rule (only its one-line `description:` is surfaced; the body loads on demand). No export uses `alwaysApply: true`, so idle context cost is at most one description line per rule. Never hand-edit the generated `.mdc` files; edit the wiki page and re-run the generator.
4. **Enforcing rules in other repositories:** this wiki is the master copy, not the enforcement mechanism. On request, export the relevant pages into the target repo's native rule system (`.cursor/rules/*.mdc`, `AGENTS.md`, `CLAUDE.md`) so every agent there inherits them. Record which repos received which rule exports on the relevant rules page.
5. Conflicts between a rules page and an older wiki page: the rules page wins; flag the discrepancy per the schema's contradiction rule.

## Enforcement frontmatter

Rules pages carry two optional fields beyond the standard wiki frontmatter, consumed by `scripts/sync-rules.py`:

- `description:` (required for export) — the one-line summary Cursor surfaces for the Agent-Requested rule; write it so an agent can tell when the rule applies.
- `globs:` (optional) — comma-separated file patterns. When present, the export is Auto-Attached to matching files; when absent, the export is Agent-Requested only.

## Pages

- [Writing style](writing-style.md): universal language rules for all generated text
- [FastAPI React Vite monorepo](fastapi-react-vite-monorepo.md): enforced standards for FastAPI + SQLAlchemy + React + Vite + TypeScript projects on Docker Compose
- [Program and major-task workflow](program-workflow.md): mandatory skill order (wayfinder -> spec -> tickets -> implement -> review) for new programs and major tasks
