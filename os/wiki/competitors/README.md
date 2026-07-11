---
type: concept
created: 2026-07-09
updated: 2026-07-09
tags: [competitors, market-intelligence, meta]
sources: []
---

# Competitors

Competitive intelligence on companies competing with [All Space](../company/all-space/README.md) and [York Space Systems](../company/york/README.md). One folder per competitor, so each company's knowledge stays clean and human-navigable.

## Structure

```text
competitors/
  README.md                This page, plus the competitor index below
  <company-slug>/          One folder per competitor (lowercase-hyphenated)
    README.md              Company landing page: who they are, why they matter, threat level
    sources/               Ingest summary pages for this competitor's sources
    ...content pages...    Market intelligence, company information, product information
```

Expected content per competitor (pages created lazily as material arrives):

| Content type | Examples |
|--------------|----------|
| Company information | overview, leadership, funding/financials, org changes, facilities |
| Product information | product lines, specs, certifications, roadmaps, pricing signals |
| Market intelligence | contract wins/losses, customers, teaming, positioning, conference presence |

Raw originals live in `os/raw/competitors/<company-slug>/` (immutable, created on first ingest).

## Conventions

- **Whose competitor:** tag each competitor page with `all-space`, `york`, or both, since the two companies compete in different markets.
- **Claims are dated and sourced.** Competitive intelligence goes stale fast; every claim carries its date and source, and contradicting updates use the schema's contradiction rule rather than silent overwrites.
- **Fact-check discipline applies:** competitor claims that feed real deliverables (battle cards, briefings) get verified vs owner-attested markings, same as the career domain.

## Competitor index: All.Space set (ranked by threat, 2026-07-10)

Full analysis and scoring: [threat-ranking.md](threat-ranking.md). Weekly refresh model: [monitoring-and-automation.md](monitoring-and-automation.md).

1. [Kymeta](kymeta/README.md) - CRITICAL
2. [ThinKom](thinkom/README.md) - HIGH
3. [CesiumAstro](cesiumastro/README.md) - HIGH
4. [Hanwha Phasor](hanwha-phasor/README.md) - MEDIUM-HIGH
5. [Ball / BAE Systems](ball-bae-systems/README.md) - MEDIUM-HIGH
6. [Get SAT](get-sat/README.md) - MEDIUM
7. [Intellian](intellian/README.md) - MEDIUM
8. [Viasat](viasat/README.md) - MEDIUM (coopetition)
9. [L3Harris](l3harris/README.md) - MEDIUM (frenemy)
10. [SpaceX Starshield / Amazon Leo](spacex-starshield/README.md) - STRATEGIC / vertical

These compete against [All.Space](../company/all-space/company-profile.md) (a York Space Systems company) in the terminal market.

## Competitor index: York set (ranked by threat, 2026-07-10)

Full analysis and scoring: [york-threat-ranking.md](york-threat-ranking.md). These compete against [York Space Systems](../company/york/company-profile.md) in the proliferated-constellation and missile warning/tracking market. SpaceX and L3Harris appear in both sets; their pages carry a section per angle.

1. [SpaceX (Starshield)](spacex-starshield/README.md) - CRITICAL
2. [Lockheed Martin / Terran Orbital](lockheed-martin/README.md) - CRITICAL
3. [Northrop Grumman](northrop-grumman/README.md) - CRITICAL
4. [Rocket Lab](rocket-lab/README.md) - HIGH
5. [L3Harris](l3harris/README.md) - HIGH
6. [Boeing / Millennium Space](boeing-millennium-space/README.md) - MEDIUM-HIGH
7. [Sierra Space](sierra-space/README.md) - MEDIUM-HIGH
8. [Apex Space](apex-space/README.md) - MEDIUM-HIGH (rising)
9. [K2 Space](k2-space/README.md) - MEDIUM (rising)
10. [Muon Space](muon-space/README.md) - MEDIUM (rising)

Watchlist (promote on a program win in York's lanes): Blue Canyon Technologies (RTX, being acquired by MDA Space), True Anomaly, Astranis, Firefly Aerospace, Airbus U.S. Space & Defense, Loft Orbital.

## Delivered documents (2026-07-10)

Twelve docx dossiers were generated from this wiki and delivered to the Google Drive `Cursor Exports` folder: the All.Space company dossier, one dossier per competitor (10), and the holistic competitive landscape report with the threat ranking and weekly monitoring plan. Regenerate with `node src/scripts/generate-competitive-intel-docx.js`.
