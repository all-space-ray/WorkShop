---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [company, meta]
sources: []
---

# Company

Knowledge about the owner's company or companies. This is the home for company-specific material the owner works with daily: products, marketing material, templates, user manuals, and company guidelines.

## Structure

```text
company/
  README.md            This page
  <company-slug>/      One folder per company (e.g. the owner's employer, a parent company,
                       subsidiaries, or the owner's own business)
```

Each company folder holds that company's pages, organized by content type as pages arrive. Expected content types (create pages and subfolders lazily, on first ingest):

| Content type | Examples |
|--------------|----------|
| Products | product pages, spec summaries, roadmaps, part-number references |
| Marketing material | positioning, messaging, collateral summaries, event material |
| Templates | document templates, proposal boilerplate, briefing formats |
| User manuals | manual summaries and key procedures (raw PDFs in `os/raw/company/...`) |
| Company guidelines | policies, brand rules, processes |
| Sources | each company folder gets a `sources/` subfolder for ingest summary pages |

Raw originals live in `os/raw/company/<company-slug>/` (immutable, created on first ingest).

## Sensitivity

Company material is internal by default. Anything marked proprietary, export-controlled, or non-public must carry a sensitivity note on its page, and never flows into public deliverables. When in doubt, ask the owner before reusing company content outside this wiki.

## Companies

- [All.Space](all-space/README.md) - the subject company; builds the Hydra multi-orbit ESA terminals. Full profile: [company-profile.md](all-space/company-profile.md).
- [York Space Systems](york/README.md) - All.Space's parent company (acquisition closed 2026-07-08); tactical spacecraft, C2, and propulsion.
