---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [career, meta]
sources: []
---

# Career

The owner's professional history and application machine. This section starts empty; the structure below is the proven pattern for populating it. Everything in it is personal to the owner and internal by default.

## Structure (create files as material arrives)

```text
career/
  README.md                      This page
  <owner>-resume-information.md  Master reference: identifiers, employment history with dates,
                                 education, clearances/credentials, quantified signature
                                 accomplishments, and an Open Questions list of gaps to fill
  job-descriptions/              One page per past role: Job Summary, Job Overview,
                                 Responsibilities, Competencies, Skills, and the verbatim
                                 Resume Bullet Points from the owner's own resume
  job-search-targeting.md        Target roles and levels, lead-identity table, location and
                                 compensation constraints, document format rules; read before
                                 generating any resume or cover letter
  fact-check-registry.md         Verification status for every program, employer, acronym, and
                                 number used in application materials: VERIFIED / CORRECTED /
                                 OWNER-ATTESTED / FLAGGED, with evidence; mandatory read before
                                 generating deliverables
  applications/                  One page per application or deliverable: fit analysis, content
                                 decisions, revision notes, links to generated documents
  sources/                       Ingest summary pages for career sources
```

Raw originals (resumes, service records, program lists, interview transcripts) live in `os/raw/career/` (immutable).

## Operating rules for this section

1. **Everything quantified gets verified.** Claims that fail arithmetic or contradict public records are corrected in the wiki and flagged to the owner; the registry records every verdict.
2. **Interview the owner to fill gaps.** After ingesting a resume, build the Open Questions list (missing numbers, team sizes, awards, date conflicts) and work through it across sessions.
3. **Generated documents follow the [writing rules](../rules/writing-style.md)** and the targeting page's format rules, and are verified before delivery (page counts by rendering, never by intention).
4. **Sensitivity:** career material contains PII. It never flows into public content, and this section stays out of any public repository.
