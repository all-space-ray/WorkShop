---
type: source
created: 2026-07-10
updated: 2026-07-10
tags: [personal-os, llm-wiki, knowledge-management, bootstrap]
sources: [../../raw/2026-07-10-personal-os-bootstrap.md]
---

# Source: Personal OS Bootstrap (single-file installer)

Founding source for this Personal OS, ingested during setup because no owner-supplied
source was ready yet. Origin: [raw copy](../../raw/2026-07-10-personal-os-bootstrap.md).

## TL;DR

A single-file installer that lets any LLM agent stand up a persistent, agent-maintained
knowledge base on the LLM Wiki pattern: immutable raw sources, an agent-owned wiki layer,
a schema, an index, and an append-only log. Knowledge compounds because sources are read
once, summarized, and cross-referenced instead of re-derived on every query (unlike RAG).

## Key points

- Three layers: `raw/` (immutable sources), `wiki/` (agent-owned pages), and the schema in `os/AGENTS.md`.
- Token efficiency through isolation: root config carries only a 2-3 line pointer; agents load schema, then index, then only the pages they need.
- Retrieval is index-first — never glob-read the wiki.
- Contradictions are flagged under `## Open questions`, never silently overwritten.
- Every ingest, filed query, and lint pass is a git commit; the log is append-only history.
- Two operating skills drive the loop: `/ingest-resource` (add knowledge) and `/improve-system` (capture lessons and lint).

## Relevance to existing knowledge

Establishes the pattern this whole knowledge base runs on. Distilled into the concept page
[LLM Wiki pattern](../concepts/llm-wiki-pattern.md).
