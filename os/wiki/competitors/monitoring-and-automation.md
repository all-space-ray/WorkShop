---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [competitors, monitoring, automation, news-feeds, contracts, market-intelligence]
sources: [../../raw/competitors/2026-07-10-competitive-landscape-research.md, ../../raw/competitors/2026-07-10-york-competitive-landscape-research.md]
---

# Competitor monitoring and weekly automation

> Purpose: keep the competitor wiki current with minimal effort by defining exactly what to watch, where, and how to automate a weekly refresh that an agent runs and files per the ingest schema. Covers **both competitor sets**: the [All.Space terminal-market set](threat-ranking.md) and the [York constellation-market set](york-threat-ranking.md).

## What to monitor (per competitor)

1. **Press releases / newsroom** (product launches, contracts, partnerships, leadership).
2. **Federal contract awards** (who is winning what, and against whom).
3. **Industry trade press** (analysis, program shifts, show announcements).
4. **Capital events** (funding, M&A) that change a competitor's staying power.
5. **Program signals** in the accounts All.Space/York target (Navy, Army, Space Force, SDA/SDN, MDA, Golden Dome, allied).

## Sources by type

### Federal contracts (authoritative, free, structured)

- **SAM.gov** - contract opportunities and awards. Search by company name; save searches.
- **USAspending.gov** - award data filterable by recipient (competitor legal names), agency, NAICS (334220 Radio/TV Broadcasting & Wireless Comms Equipment; 517410 Satellite Telecom). Has a public API for automation.
- **defense.gov/News/Contracts** - daily DoD contract announcements (>$7.5M).
- **Highergov / GovTribe / GovWin** (paid) - richer pipeline/forecast data if a subscription is justified.

### Company newsrooms (RSS or scrape weekly)

**All.Space competitor set** ([ranking](threat-ranking.md)):

| Competitor | Newsroom |
|------------|----------|
| Kymeta | kymetacorp.com/about/news-insights |
| ThinKom | thinkom.com/news |
| CesiumAstro | cesiumastro.com/press-release |
| Hanwha Phasor | hanwhaphasor.com (+ Hanwha group news) |
| Ball / BAE Systems | baesystems.com/space newsroom |
| Get SAT | getsat.com/news |
| Intellian | intelliantech.com/en/news |
| Viasat | news.viasat.com (+ investor relations) |
| L3Harris | l3harris.com/newsroom (+ investor relations) |
| SpaceX Starshield / Amazon Leo | spacex.com/starshield; aboutamazon.com/news/amazon-leo |

**York competitor set** ([ranking](york-threat-ranking.md)):

| Competitor | Newsroom |
|------------|----------|
| SpaceX (Starshield) | spacex.com/updates; spacex.com/starshield |
| Lockheed Martin / Terran Orbital | lockheedmartin.com/en-us/news; terranorbital.com/news |
| Northrop Grumman | news.northropgrumman.com |
| Rocket Lab | rocketlabcorp.com/updates; investors.rocketlabcorp.com |
| L3Harris | l3harris.com/newsroom |
| Boeing / Millennium Space | millennium-space.com/media; boeing.mediaroom.com |
| Sierra Space | sierraspace.com/press-releases |
| Apex Space | apexspace.com (news) |
| K2 Space | k2space.com (news) |
| Muon Space | muonspace.com (news) |

Also monitor **SDA award announcements directly at sda.mil (news page)** and York's own investor feed (ir.yorkspacesystems.com/news) for context. Public companies (YSS, RKLB, LMT, NOC, LHX, BA, RTX, MDA, Viasat) file 8-Ks and earnings with material contract news; SEC EDGAR full-text search covers them all.

### Industry trade press (feeds available)

- **SpaceNews** (spacenews.com) - RSS; the primary source for satellite/defense contract news.
- **SatNews** (satnews.com) - RSS; high-volume industry announcements.
- **Via Satellite** (satellitetoday.com) - analysis and executive interviews.
- **Runway Girl Network** (runwaygirlnetwork.com) - aero ESA/IFC depth.
- **Breaking Defense**, **DefenseScoop**, **Air & Space Forces Magazine**, **Defense Daily**, **Orbital Today**, **EDR Magazine**, **GovConWire**, **SpaceandDefense.io**, **KeepTrack** space briefs.

### Pre-built contract pull (presetup, tested)

`scripts/competitor-weekly-pull.py` (repo root) queries the USAspending API for the trailing week of contract awards across **all 20 tracked companies in both sets** and prints a markdown digest (or `--json`). Stdlib-only, no keys. Validated live 2026-07-10. The weekly agent runs this first, then merges results with newsroom/trade-press findings. Note: very large recipients (Lockheed, Northrop) occasionally 502/time out on the free API; the script retries once and reports remaining gaps explicitly.

### Search alerts (zero-cost baseline)

- Google Alerts / news alerts for each company name plus terms: "electronically steered antenna", "flat panel antenna", "multi-orbit terminal", "Ka-band terminal", "SATCOM contract".

## Weekly automation design

A cloud agent (or scheduled task) runs this loop once a week and files results via `/ingest-resource`:

1. **Pull sources:** fetch each competitor newsroom (RSS where available, otherwise fetch and diff against last week's snapshot stored in `os/raw/competitors/<slug>/snapshots/`), pull SpaceNews/SatNews feeds filtered by the competitor list, and query the USAspending API for new awards to each competitor legal name in the trailing 8 days.
2. **Filter:** keep only items dated in the last week and relevant to ESA/terminals/Ka/contracts/leadership/capital.
3. **File:** for each material item, append a dated, sourced bullet to the relevant competitor page under a `## Updates` section (newest first), and drop the raw item into `os/raw/competitors/<slug>/sources/`.
4. **Re-score:** if an item is a product ship, a target-account program win, or a major raise, update that competitor's score inputs and re-derive [threat-ranking.md](threat-ranking.md).
5. **Report + commit:** produce a one-page "week in review" (biggest moves, ranking changes, recommended actions) and commit as `Ingest: competitor weekly <date>`.

> **Step-by-step setup instructions:** see [weekly-automation-setup.md](weekly-automation-setup.md) for the exact Cursor Automation configuration and a ready-to-paste prompt.

### Implementation options (in order of robustness)

- **Cursor cloud scheduled agent / cron** pointed at this repo, running the loop above; simplest given the existing Personal OS and git workflow. Full runbook: [weekly-automation-setup.md](weekly-automation-setup.md).
- **USAspending API** (documented, free) for structured contract pulls; SAM.gov has APIs (registration required) for opportunities/awards.
- **RSS aggregation** (a small script or a service like an RSS-to-webhook) feeding the agent the week's items.
- Escalate to a paid GovWin/Highergov feed only if pipeline/forecast intelligence proves worth the cost.

## Cadence and ownership

- **Weekly:** the automated pull + file + report (above).
- **Monthly:** human review of the ranking and the "findings that matter most" on [threat-ranking.md](threat-ranking.md).
- **Event-driven:** immediate ingest when a major competitor move breaks (a target-account loss, a competitor acquisition, a network access policy change).

## Related
- [Threat ranking](threat-ranking.md) | [All.Space profile](../company/all-space/company-profile.md) | [Competitors index](README.md)
