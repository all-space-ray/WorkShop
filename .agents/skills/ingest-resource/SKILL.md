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
