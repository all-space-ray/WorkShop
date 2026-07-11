<!--
origin: docs/personal-os-bootstrap.md (Personal OS single-file installer, embedded in universal-repo-bootstrap.md)
type: notes
ingested: 2026-07-10
-->

# Personal OS Bootstrap (single-file installer)

**Purpose:** this one file lets any LLM agent, on any repository, with any quality of model, install the owner's Personal OS: a persistent, LLM-maintained knowledge base built on the LLM Wiki pattern. Everything needed is inlined below verbatim: the schema, the seed files, the two operating skills, the root pointers, a first-ingest walkthrough, a verification checklist, and troubleshooting. No other file or repository access is required.

**If you are an agent reading this in a fresh repo:** work through Parts 2–5 top to bottom, copying the file contents EXACTLY as given (do not paraphrase, summarize, or "improve" them), then run the Part 6 verification and report the results to the owner.

**If you are the human owner:** give this file to an agent with the instruction "Set up my Personal OS by following this document," then do the Part 8 Obsidian setup yourself.

The Personal OS is the owner's most important project; treat setup with care. This document is the complete specification: no other repository, URL, or file access is required to install it.

---

## Part 1: The pattern and the non-negotiable principles

### The pattern in one paragraph

Instead of RAG (re-deriving answers from raw documents on every query), the agent incrementally builds and maintains a persistent wiki: interlinked markdown pages sitting between the human and the raw sources. New sources are read once, summarized, and integrated into existing pages: cross-references added, contradictions flagged, syntheses revised. Knowledge compounds. The human curates sources and asks questions; the agent does all writing, filing, and maintenance. (Lineage: Vannevar Bush's Memex, with the LLM supplying the maintenance labor.)

### Design principles (do not violate any of these)

1. **Token efficiency through isolation.** The OS lives in one directory (`os/`) with its own nested `os/AGENTS.md` schema. Root-level agent config carries only a 2–3 line pointer. Agents pay zero token cost for the knowledge base unless the task needs it; when it is needed, they load schema, then index, then only the relevant pages. Never glob-read the wiki.
2. **Raw sources are immutable.** The agent reads them, never edits them. (Exception: the owner may explicitly direct corrections; even then, add an annotation block and preserve the original text beneath.)
3. **The agent owns the wiki layer entirely.** The human reads; the agent writes.
4. **Index-first retrieval.** `os/index.md` is the navigation entry point; no embedding infrastructure until the wiki outgrows it (~hundreds of pages).
5. **Contradictions are flagged, never silently overwritten.**
6. **Schema changes are proposed, not made silently.** The schema co-evolves with the owner.
7. **Git is the version history.** Every ingest, filed query, and lint pass is a commit.
8. **Verify before you generate** (learned the hard way): technical claims that will be reused in deliverables should be verified against public records where possible and marked *verified* vs *owner-attested*. Agent extrapolation beyond sources is the leading cause of misinformation.

---

## Part 2: Files to create (copy each EXACTLY)

Create these five files with precisely the contents shown. Where a block below is fenced with four backticks, everything inside (including three-backtick fences) is file content.

### 2.1: `os/AGENTS.md` (the schema)

````markdown
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
    concepts/        Cross-domain ideas, methods, frameworks: slug.md
    experiences/     Session-captured personal lessons, in the human's voice: YYYY-MM-DD-slug.md
    synthesis/       Cross-domain overviews, comparisons, filed answers: slug.md
    sources/         Summary pages for domainless sources: YYYY-MM-DD-slug.md
```

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
````

### 2.2: `os/index.md` (seed)

````markdown
# Personal OS — Index

Catalog of every wiki page, grouped by section (folder). Read this first when answering queries; drill into pages from here. Updated on every ingest and filed query. Conventions: [AGENTS.md](AGENTS.md).

## Synthesis

*(no pages yet)*

## Concepts

*(no pages yet)*

## Experiences

*(no pages yet)*

## Sources

*(no pages yet)*
````

Replace each `*(no pages yet)*` with real entries as pages are created; add new domain headings (e.g. `## Career`) when their first page exists.

### 2.3: `os/log.md` (seed)

Replace `YYYY-MM-DD` with today's date:

````markdown
# Personal OS — Log

Append-only chronology of ingests, filed queries, and lint passes. Entry format is defined in [AGENTS.md](AGENTS.md). Recent activity: `rg "^## \[" os/log.md | tail -5`.

## [YYYY-MM-DD] init | Personal OS created

Scaffolded `os/` (schema, index, log, raw/, wiki/) from the portable bootstrap document. Wired `/ingest-resource` and `/improve-system` skills.
````

### 2.4: Skill: `ingest-resource`

Install at the path your tooling reads skills from: `.cursor/skills/ingest-resource/SKILL.md` (Cursor), `.claude/skills/ingest-resource/SKILL.md` (Claude Code), `.agents/skills/ingest-resource/SKILL.md` (generic/Cloud), or `skills/ingest-resource/SKILL.md`. If unsure, install to BOTH `.cursor/skills/...` and `.agents/skills/...`. File content:

````markdown
---
name: ingest-resource
description: >
  Ingest an external resource (URL, video, transcript, notes, attachment)
  into the Personal OS at os/ - save the raw source, summarize it,
  integrate it into wiki pages, and update the index and log.
disable-model-invocation: true
---

# Ingest Resource

Bring an external resource into the Personal OS: fetch, save raw, summarize, integrate, cross-reference. This skill is the operational wrapper for the **Ingest** operation defined in `os/AGENTS.md` — read that schema first; it is the source of truth for layout, page conventions, and index/log formats.

## When to use

Invoke `/ingest-resource` when the goal is **capture and filing**, not immediate action:

- Article or blog post URL
- YouTube video (link or transcript)
- Pasted notes or meeting transcript
- Attachment or local repo file (PDF, doc, markdown)

## Steps

### 1. Choose the processing mode

If more than one source is provided (or the user signals a batch is coming), ask before starting: **one at a time with review between each, or batch-ingest with a single combined report?** Neither is the default — the owner decides per session.

### 2. Detect the source type

| Type | Signals |
|------|---------|
| Article URL | `http(s)://` link to a blog, news site, or documentation page |
| YouTube | `youtube.com`, `youtu.be`, or user mentions a video |
| Transcript | Pasted dialogue, captions, or meeting notes |
| Notes | Freeform text without a URL |
| Local repo file | Path under the workspace |

If the type is ambiguous, ask once before proceeding.

**Cloud Agent limitation:** paths on the user's PC (`C:\...`, OneDrive links) are not reachable from Cloud Agents. Ask the user to paste the text, push the file into the repo, or supply a fetchable URL.

### 3. Fetch or read the content

- **URLs** — fetch and read the page. If fetch fails, ask the user to paste the content.
- **YouTube** — fetch title/description/metadata; use a transcript if available. Note when only metadata was available.
- **Transcript / notes** — use the text provided in the conversation.
- **Local files** — read from the workspace.

### 4. Save the raw source

Pick the domain section (check `os/index.md` for existing domains; create a new appropriately named folder for a new topic area; ask once if unclear). Save verbatim to `os/raw/<domain>/YYYY-MM-DD-slug.md` with origin metadata (URL or origin, type, date) at the top. Domainless one-offs go directly in `os/raw/`. Raw files are immutable after this point.

### 5. Write the source page

Create the summary page in the domain's `sources/` subfolder (e.g. `os/wiki/career/sources/YYYY-MM-DD-slug.md`; domainless: `os/wiki/sources/`) per the schema's page conventions: frontmatter, TL;DR (2-4 sentences), key points, relevance to existing knowledge. Summarize — do not paste the whole source.

### 6. Integrate and cross-reference

1. Read `os/index.md` and grep the wiki for overlapping topics, names, and frameworks.
2. Update or create the entity/concept/synthesis pages the source touches — domain pages live in the domain folder. Link both directions.
3. Flag contradictions with existing claims under `## Open questions` — never overwrite silently.
4. Do not invent connections; if nothing relates yet, say so in the report.

### 7. Update index and log

Add new pages to `os/index.md` and append an `ingest` entry to `os/log.md` in the schema's format. Batch mode: one log entry and one report for the batch.

### 8. Report back

```
## Ingest Resource — Complete

**Source type:** [type]
**Raw:** [os/raw/ path]
**Saved to:** [wiki page paths]
**Summary:** [one-line TL;DR]
**Cross-references:** [linked pages, or "none yet"]
**Suggested follow-up:** [or "none"]
```

Commit with: `Ingest: [short title]`.

## Quality bar

- **Always preserve the source** — origin metadata at the top of the raw file.
- **File once, link widely** — one primary page; cross-reference instead of duplicating.
- **Summaries over dumps** — the raw file holds the verbatim text; wiki pages distill.
- **Search before saving** — check the index to avoid duplicate captures of the same source.
- **Ask once** — if source type or destination is unclear, clarify before writing files.
````

### 2.5: Skill: `improve-system`

Same install locations as 2.4, under `improve-system/SKILL.md`. File content:

````markdown
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

### 6. Report back

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
````

### 2.6: Root pointer (2–3 lines only)

Append to the repo's root agent config (`AGENTS.md`, `CLAUDE.md`, or the rules file your tooling reads). Keep it to these lines; the token-efficiency contract depends on it:

```markdown
- The Personal OS (LLM-maintained knowledge base) lives in `os/`. Read `os/AGENTS.md` before any work inside `os/`; ignore the directory entirely for unrelated tasks.
- Portable setup guide: `docs/personal-os-bootstrap.md`.
```

If the repo has no root agent config at all, create `AGENTS.md` containing just a title line and those two bullets.

### 2.7: Optional: slash-command wrappers

Some tools (e.g. Cursor) surface skills in the `/` menu via command wrappers. If the target repo uses `.cursor/commands/`, create `.cursor/commands/ingest-resource.md`:

```markdown
---
name: ingest-resource
description: Ingest an external resource (URL, video, transcript, notes, attachment) into the Personal OS at os/ - save the raw source, summarize it, integrate it into wiki pages, and update the index and log.
---

Follow the skill instructions in `.cursor/skills/ingest-resource/SKILL.md`.
```

...and the equivalent `improve-system.md` (description from 2.5's frontmatter). Frontmatter safety rules for cloud slash-menu parsing: flat keys only, no double quotes, no unicode arrows, no nested `metadata:` blocks, no literal `description: |`.

### 2.8: Tool compatibility notes

The skill files in 2.4 and 2.5 are valid as written for both major agent harnesses; only the install path differs.

- **Cursor:** skills at `.cursor/skills/<name>/SKILL.md`; add the 2.7 command wrappers if you want `/` menu entries; root pointer in `AGENTS.md` (or the repo's rules file). For Cursor Cloud agents, also mirror skills to `.agents/skills/<name>/SKILL.md`.
- **Claude Code:** skills at `.claude/skills/<name>/SKILL.md` (project scope). They automatically become the `/ingest-resource` and `/improve-system` slash commands; no wrappers needed. The frontmatter used here (`name`, folded `description: >`, `disable-model-invocation: true`) consists entirely of officially supported Claude Code skill fields, and `disable-model-invocation: true` gives the intended behavior: manual invocation only. Root pointer goes in `CLAUDE.md`.
- **Other harnesses (Codex, generic agents):** install to `.agents/skills/<name>/SKILL.md` or a plain `skills/` folder and reference the skills from the root agent config. Even with no skill system at all, the OS still works: the operations are fully specified in `os/AGENTS.md`, so the owner can simply say "ingest this" or "improve the system."
- **Chat-only tools without repo write access** (e.g. a web chat without a file/git harness) cannot install or maintain the OS; use a coding agent for setup and maintenance, and any tool you like for reading.

---

## Part 3: First ingest (do not skip)

An empty system rots; seed it immediately so the loop is proven end to end.

1. Ask the owner for their first source (a document, an article URL, pasted notes). If they have none ready, ingest THIS bootstrap file as the founding source (domainless): raw copy at `os/raw/YYYY-MM-DD-personal-os-bootstrap.md`, source page at `os/wiki/sources/`, and a concept page `os/wiki/concepts/llm-wiki-pattern.md` distilling Part 1.
2. Follow the ingest skill's steps 4–8 exactly, including index, log, and the report.
3. Commit: `Ingest: <title>`.

## Part 4: Copy this file forward

Copy this bootstrap document into the new repo at `docs/personal-os-bootstrap.md` so the chain continues from every installation.

## Part 5: Commit and PR

Commit the scaffold in logical steps (`Add Personal OS: LLM Wiki scaffold with schema, index, log, and first ingest` is a good message) and open a PR per the repo's workflow.

---

## Part 6: Verification checklist (agent: run and report)

- [ ] `os/AGENTS.md`, `os/index.md`, `os/log.md` exist; log has an `init` entry with today's date
- [ ] `os/raw/` and `os/wiki/` exist with at least the first ingest filed (raw + source page)
- [ ] Every wiki page has valid frontmatter (`type`, `created`, `updated`, `tags`, `sources`)
- [ ] All links are relative markdown links (`rg -n "\[\[" os/` returns nothing, meaning no wikilinks)
- [ ] Every relative link resolves (walk `](...)` targets; fix any that 404)
- [ ] Both skills installed and readable at the tool's skill path; frontmatter has `name`, folded `description: >`, `disable-model-invocation: true`
- [ ] Root agent config contains the 2–3 line pointer and nothing more about the OS
- [ ] `rg "^## \[" os/log.md` shows the init and first-ingest entries
- [ ] Everything committed; working tree clean

Report the checklist results to the owner with any deviations.

---

## Part 7: Operating guide (for the owner) and hard-won lessons

### Day-to-day loop

- **Add knowledge:** give the agent a source and say `/ingest-resource` (or just "ingest this"). Multiple sources: the agent will ask one-at-a-time vs batch.
- **Ask questions:** just ask; the agent reads index → pages and answers with citations. Durable answers get filed into `synthesis/`.
- **End of session:** say `/improve-system` to capture lessons and lint the wiki.

### Lessons already paid for (encode-by-default in any new install)

These were learned in earlier installations through real failures; a new installation inherits them free:

1. **Verify before you generate.** When wiki content feeds real-world deliverables (reports, published documents), verify technical claims against public records and keep a *fact-check registry* page per high-stakes domain: every claim marked VERIFIED / CORRECTED / OWNER-ATTESTED / FLAGGED with evidence. The owner's own source documents can contain errors; agent extrapolation creates more.
2. **Owner preferences live in `experiences/`** (e.g. formatting rules, tone bans, workflow choices) so future agents honor them without re-asking. Examples: a punctuation rule ("no em dashes ever"), an ingest-mode preference ("ask one-at-a-time vs batch"), and document formatting requirements.
3. **Cross-agent handoffs:** temporary directories do not survive between cloud sessions. If you use a handoff workflow, persist handoff notes in a committed folder and confirm the commit actually reaches the default branch.
4. **Document deliverables need renderer-independent verification.** If the OS produces documents (Word, PDF), pagination differs across Word/LibreOffice/Google Docs; verify in the renderer the owner actually uses, or two independent ones, before claiming page counts.
5. **Domain sections keep the tree human-navigable.** New topic area = new folder under both `os/raw/` and `os/wiki/`, named plainly (`career/`, `photography/`), with the domain's source summaries in `<domain>/sources/`.

---

## Part 8: Obsidian setup (for any user installing the Personal OS)

The wiki is plain markdown, so Obsidian is the recommended reading UI: the agent writes, you browse. This guide assumes you have installed Obsidian but never used it.

### 1. Open the repo as a vault

1. Clone the repository to your computer (if it only lives on GitHub so far).
2. Launch Obsidian → **Open folder as vault** → select the repository's root folder.
3. If prompted about trusting the vault, accept; it is your own repo.

Opening the repo root (not `os/`) keeps links between the wiki and `docs/` working.

### 2. Focus the vault on the knowledge base

Settings (gear icon, bottom left) → **Files and links**:

- **Excluded files** → add: `.cursor`, `.agents`, `.github`, `scripts`, `src`, `tests`. This hides repo plumbing from search, graph view, and link suggestions.
- Turn **off** "Use [[Wikilinks]]" and set **New link format** to "Relative path to file" so any links you drag in Obsidian match the OS convention (relative markdown links).
- **Default location for new attachments** → "In the folder specified below" → `os/raw/assets`. Images land inside the immutable raw layer where the agent can find them.

### 3. Reading and navigating

- Start at `os/index.md`, the catalog of every page. Click through; use Ctrl/Cmd+Click to open in a new pane.
- **Graph view** (Ctrl/Cmd+G) shows the wiki's shape: hub pages are your syntheses; isolated dots are orphans worth mentioning in the next `/improve-system`.
- Backlinks pane (right sidebar) shows what links to the current page.

### 4. Obsidian Web Clipper (capturing articles)

1. Install the "Obsidian Web Clipper" extension for your browser (official, by Obsidian).
2. Open the extension's settings (cog icon) → add your vault under **Vaults**.
3. Edit the default template: set **Note location** to `os/raw` (or a domain folder like `os/raw/career`), and **Note name** to `{{date|date:"YYYY-MM-DD"}}-{{title}}` to match the raw naming convention. The template stores the source URL in the note automatically.
4. After clipping, in Obsidian run the command "Download attachments for current file" (Ctrl/Cmd+P for the command palette; bind a hotkey in Settings → Hotkeys if you clip often) so images are saved locally under `os/raw/assets`.
5. Commit the clipped file, then tell the agent to `/ingest-resource` it.

### 5. Optional plugins (Settings → Community plugins)

- **Dataview**: dynamic tables over page frontmatter (every wiki page carries `type`, `created`, `tags`).
- **Marp**: render markdown slide decks if you ask the agent for presentations.

### 6. The one rule

You browse in Obsidian; the agent maintains `os/wiki/`, `os/index.md`, and `os/log.md`. Notes you author yourself belong in `os/raw/` (they are sources). If you hand-edit a wiki page, tell the agent so it can keep cross-references and the index consistent.

---

## Part 9: Troubleshooting (common failure modes, especially for weaker models)

| Symptom | Cause | Fix |
|---------|-------|-----|
| Agent reads the whole wiki for a small question | Ignoring index-first retrieval | Point it to the Token discipline section of `os/AGENTS.md`: schema → index → only needed pages |
| Wiki pages use `[[wikilinks]]` | Obsidian habit | Convert to relative markdown links; they must work on GitHub and for agents |
| Raw file edited or "cleaned up" | Immutability violated | Restore from git; corrections go in the wiki layer, or (owner-directed only) as an annotation block above the preserved original |
| New pages missing from `os/index.md` or `os/log.md` | Skipped ingest steps 7 | Re-run steps 7–8 of the ingest skill; every page must be indexed and every operation logged |
| Skills don't appear in the `/` menu | Frontmatter parsing | Flat frontmatter only: `name`, folded `description: >`, `disable-model-invocation: true`; no double quotes, no unicode punctuation; add command wrappers (2.7) if your tool uses them |
| Log entries rewritten or reordered | Append-only violated | Restore from git; the log is history, not documentation |
| Agent invents connections between unrelated pages | Over-eager integration | The ingest skill says: do not invent connections; say "nothing relates yet" |
| Contradictory facts silently replaced | Overwrite instead of flag | Restore both claims, cite both sources, add `## Open questions` |
