# Personal OS — Schema

This directory is a Personal OS: a persistent, LLM-maintained knowledge base built on the LLM Wiki pattern. The human curates sources and asks questions; the agent does all writing, filing, cross-referencing, and maintenance.

Read this file before any operation inside `os/`. Do NOT read it (or anything under `os/`) for tasks unrelated to the knowledge base — that is the token-efficiency contract of this system.

## Three layers

1. **`raw/`** — immutable source documents (articles, transcripts, notes, images under `raw/assets/`). Agents read raw files but NEVER modify or delete them.
2. **`wiki/`** — LLM-generated markdown pages. Agents own this layer entirely: create, update, and cross-reference pages to keep the whole wiki consistent.
3. **This schema** — the rules. Co-evolves with the human; propose changes when a convention stops working, never change silently.

## Layout

```text
os/
  AGENTS.md          This schema
  index.md           Content catalog — the navigation entry point
  log.md             Append-only chronological record
  raw/               Immutable sources, grouped by domain: raw/<domain>/YYYY-MM-DD-slug.md
                     (raw/assets/ for images; domainless one-offs directly in raw/)
  wiki/
    <domain>/        One folder per knowledge domain (e.g. career/), holding ALL of that
                     domain's pages — entities, syntheses, and a sources/ subfolder for
                     that domain's source summary pages
    rules/           Enforced best practices: coding standards per language/architecture and
                     universal writing rules; master copy, exported to repos' rule systems
    company/         The owner's companies: one folder per company, holding products,
                     marketing material, templates, manuals, and guidelines
    competitors/     Competitive intelligence: one folder per competitor company with
                     market intelligence, company information, and product information
    my-voice/        Writing samples per user and derived voice profiles, distilled into
                     rules/skills so agents write in that user's tone and style
    career/          The owner's professional history: master reference, per-role job
                     descriptions, targeting rules, fact-check registry, applications
    concepts/        Cross-domain ideas, methods, frameworks: slug.md
    experiences/     Session-captured personal lessons, in the human's voice: YYYY-MM-DD-slug.md
    synthesis/       Cross-domain overviews, comparisons, filed answers: slug.md
    sources/         Summary pages for domainless sources: YYYY-MM-DD-slug.md
```

The rules/, company/, competitors/, my-voice/, and career/ sections were added at the owner's direction; each section's README defines its conventions and is the authority for filing within it.

**Folders are navigation; frontmatter is classification.** A page's `type:` says what kind of page it is; its folder says where a human browsing the tree finds it. The owner wants everything separated very cleanly: when a new topic area arrives, create a new domain section folder rather than scattering pages across the base sections. Start each domain flat; add subfolders once a section grows past roughly ten pages. If the right domain for a source is unclear, ask once.

Create a folder's first file when the first page belongs there; do not pre-create empty folders.

## Page conventions

Every wiki page starts with YAML frontmatter:

```yaml
---
type: source | entity | concept | experience | synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [lowercase, hyphenated]
sources: [relative paths to raw/ files this page draws on]
---
```

- **Links:** relative markdown links (`[title](../concepts/slug.md)`), never bare wikilinks — portable across Obsidian, GitHub, and agents.
- **Names:** lowercase-hyphenated slugs. Dated prefix (`YYYY-MM-DD-`) only for sources, raw files, and experiences.
- **Size:** keep pages focused; if a section outgrows its page, split it into a new page and link.
- **Citations:** claims in wiki pages cite their raw source(s) via the `sources:` frontmatter and inline links.
- **Contradictions:** when a new source contradicts an existing claim, do not overwrite silently. Note both, cite both, and flag it under a `## Open questions` section on the affected page.
- **Voice:** `experiences/` pages preserve the human's own words and voice; everywhere else, write clean neutral prose.
- **Enforced rules pages:** pages under `wiki/rules/` may carry two optional frontmatter fields, `description:` (one-line summary) and `globs:` (comma-separated file patterns). `scripts/sync-rules.py` exports each such page to `.cursor/rules/<slug>.mdc` so agents actually follow it; `scripts/check-repo.sh` fails on missing or stale exports. Pages with `globs:` become Auto-Attached rules (body loads only when a matching file is in context); pages without become Agent-Requested (only the description is surfaced). No export uses `alwaysApply: true`, keeping idle context cost to one line per rule. The wiki page is the source of truth; never hand-edit the generated `.mdc`.

## Operations

### Ingest (`/ingest-resource`)

0. If more than one source is provided, ask first: process one at a time with review between each, or batch-ingest with a single combined report. Never assume.
1. Save the source verbatim to `raw/<domain>/YYYY-MM-DD-slug.md` (with origin URL/metadata at top). Never modify it afterward.
2. Read it fully. Write the source summary page in the domain's `sources/` subfolder (or `wiki/sources/` for domainless one-offs): TL;DR (2-4 sentences), key points, relevance to existing knowledge.
3. Integrate: update or create the entity/concept/synthesis pages the source touches. Add cross-links both directions. Flag contradictions.
4. Update `index.md` (add the new pages, revise one-liners if a page's scope changed).
5. Append to `log.md`.
6. Report what was filed, what was linked, and any suggested follow-ups.

### Query

1. Read `index.md` first to locate relevant pages. Do not bulk-read the wiki.
2. Drill into only the pages you need; follow links outward as required.
3. Synthesize the answer with citations to wiki pages and raw sources.
4. If the answer is durable (a comparison, an analysis, a discovered connection), file it into `wiki/synthesis/` and index it. Append a `query` entry to `log.md` when you file something; skip logging throwaway answers.

### Lint / improve (`/improve-system`)

Periodic health check plus session capture:

- Contradictions between pages; stale claims superseded by newer sources.
- Orphan pages (no inbound links); concepts mentioned often but lacking a page; missing cross-references.
- Index entries that drifted from page content; log format violations.
- Durable lessons from the current session worth saving to `experiences/`.
- Schema rules that the session proved wrong — propose the change, do not silently rewrite.

Flag destructive actions (delete, merge) for human approval; apply additive fixes directly.

## index.md format

Content-oriented catalog, one line per page, grouped by category:

```markdown
## Concepts
- [Page Title](wiki/concepts/slug.md) — one-line summary
```

Updated on every ingest and whenever a filed query adds a page. When answering queries, this is the entry point — read it before opening wiki pages.

## log.md format

Append-only. Every entry starts with a grep-able heading:

```markdown
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query | Question asked
## [YYYY-MM-DD] lint | Scope of pass
```

One to three lines of body per entry: what changed, which pages were touched. Never rewrite or delete past entries. `rg "^## \[" os/log.md | tail -5` shows recent activity.

## Token discipline

- Outside `os/` work: this directory costs zero tokens. The root `AGENTS.md` carries only a pointer here.
- Inside `os/` work: schema → index → only the pages needed. Never glob-read `wiki/`.
- The index is the retrieval mechanism. At the current scale no search tooling is needed; if the wiki outgrows the index (~hundreds of pages), propose adding local search (e.g. qmd) via `/improve-system`.

## Git

Every ingest, filed query, or lint pass is committed with a conventional message: `Ingest: <title>`, `File query: <topic>`, `Improve system: <scope>`. The wiki's git history is its version history.
