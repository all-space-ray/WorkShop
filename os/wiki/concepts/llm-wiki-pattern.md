---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [llm-wiki, knowledge-management, retrieval, personal-os]
sources: [../../raw/2026-07-10-personal-os-bootstrap.md]
---

# The LLM Wiki pattern

An approach to machine-maintained knowledge where an agent incrementally builds and
maintains a persistent wiki of interlinked markdown pages that sit between the human and
the raw sources. New sources are read once, summarized, and integrated into existing
pages — cross-references added, contradictions flagged, syntheses revised — so knowledge
compounds over time.

## How it differs from RAG

RAG re-derives answers from raw documents on every query. The LLM Wiki pattern instead
persists distilled, interlinked knowledge, so retrieval becomes cheap navigation through
an index rather than repeated re-reading of source material. (Lineage: Vannevar Bush's
Memex, with the LLM supplying the maintenance labor.)

## Core principles

1. Token efficiency through isolation — the knowledge base loads only when a task needs it.
2. Raw sources are immutable; the agent owns the wiki layer entirely.
3. Index-first retrieval; no embedding infrastructure until the wiki outgrows it.
4. Contradictions are flagged, never silently overwritten.
5. Schema changes are proposed, not made silently.
6. Git is the version history — every ingest, filed query, and lint pass is a commit.

## See also

- Source: [Personal OS Bootstrap](../sources/2026-07-10-personal-os-bootstrap.md)
