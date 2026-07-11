---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [competitors, monitoring, automation, cursor-automations, runbook, how-to]
sources: []
---

# Weekly competitor monitoring: setup runbook

> Step-by-step instructions to stand up the automated weekly competitor refresh covering **both competitor sets** (the [All.Space set](threat-ranking.md) and the [York set](york-threat-ranking.md)) plus the subject companies themselves. This is the "how to actually do it" companion to [monitoring-and-automation.md](monitoring-and-automation.md) (which defines what to watch and why). No coding required for the recommended path; the contract-pull step is pre-built and tested (`scripts/competitor-weekly-pull.py`).

## What this automation does, in one sentence

Once a week, a Cursor Cloud Agent wakes up on a schedule, runs the pre-built federal-contract pull, fetches the latest competitor news across both competitor sets, files dated and sourced updates into each competitor's wiki page, re-scores both threat rankings if anything material changed, writes a one-page "week in review," and commits it all to the repository.

## Recommended path: a Cursor scheduled Automation

This is the simplest robust option. Cursor Automations run cloud agents in the background on a schedule you set. Because the automation runs against this repository directly, it can read and write the wiki and commit with no extra credentials. (The `ALL_SPACE_SETUP_TOKEN` secret is only needed if you run the job from a different repository and want it to push here; see the alternative at the bottom.)

### Step 1: Open the Automations screen

- Go to **cursor.com/automations** (or open the Agents Window in the Cursor IDE and choose Automations), then **New automation**.
- Easiest of all: in any Cursor agent chat, type **`/automate`** and describe the job in plain language ("run every Monday, monitor my competitors, file updates to the wiki, commit a report"). Cursor will configure the trigger, prompt, and tools for you. You can still fine-tune afterward.

### Step 2: Choose the trigger

- Trigger type: **Scheduled**.
- Preset: **Weekly**, for example every **Monday 08:00**. For precise control use a **cron expression**; Cursor cron runs in **UTC**. Example for Mondays at 13:00 UTC (roughly start of the US business week): `0 13 * * 1`.

### Step 3: Point it at the repository

- Scheduled triggers default to **no repository**, and with no repository the agent cannot read or write files. You must **select this repository** (the one holding `os/`) and the **`main` branch**. This is the single most common setup mistake.

### Step 4: Paste the instructions (the prompt)

Copy the prompt in the "Ready-to-paste automation prompt" section below into the automation's prompt field.

### Step 5: Choose tools (optional)

- If you want the weekly summary delivered to Slack, connect Slack and enable the **Send to Slack** tool, then tell the prompt which channel.
- The agent already has web fetch and git; no MCP tools are required for the core loop. (Composio/Google Drive tools are only needed if you also want the weekly report pushed to Drive as a docx; leave off unless you want that.)

### Step 6: Save and activate

- Set status to **Active**. The first run happens at the next scheduled time (scheduled runs may start a little late but never early).
- Each run is a Cloud Agent run billed at API model pricing, so roughly one agent session per week.

### Step 7: Verify after the first run

- Check that a commit like `Ingest: competitor weekly 2026-07-14` landed on `main`, that competitor pages gained an `## Updates` entry, and that a week-in-review file or Slack message appeared. If nothing changed that week, the agent should still post "no material changes."

## Ready-to-paste automation prompt

```
You are the weekly competitor-intelligence monitor for York Space Systems and its subsidiary
All.Space. Work on the main branch of this repository. Read
os/wiki/competitors/monitoring-and-automation.md, os/wiki/competitors/threat-ranking.md, and
os/wiki/competitors/york-threat-ranking.md first for context and the two competitor lists.

Step 0 (contracts, presetup): run `python3 scripts/competitor-weekly-pull.py` from the repository
root. It queries the USAspending award API for the trailing 8 days across all tracked companies
in both sets and prints a markdown digest. Treat any "Query errors" section it prints as gaps to
report, not to guess. If you need a wider window use --days N, and --json for machine-readable
output.

Then, for each competitor page in BOTH sets:
- All.Space set: kymeta, thinkom, cesiumastro, hanwha-phasor, ball-bae-systems, get-sat,
  intellian, viasat, l3harris, spacex-starshield
- York set: spacex-starshield, lockheed-martin, northrop-grumman, rocket-lab, l3harris,
  boeing-millennium-space, sierra-space, apex-space, k2-space, muon-space
(spacex-starshield and l3harris appear in both sets; process each page once, covering both angles.)

1. Fetch that competitor's newsroom URL(s) (listed on its page) and scan the industry feeds
   (spacenews.com, satnews.com, satellitetoday.com, breakingdefense.com, defensescoop.com,
   airandspaceforces.com, runwaygirlnetwork.com) for items about the competitor published in the
   last 8 days. Also check sda.mil (news page) for new award announcements, and SEC EDGAR 8-K
   filings for the public companies (YSS, RKLB, LMT, NOC, LHX, BA, RTX, MDA, Viasat).
2. Merge in the Step 0 contract digest for that company.
3. Keep only items that are new this week and relevant to: ESA/flat-panel terminals, Ka-band,
   multi-orbit SATCOM (All.Space angle); proliferated constellations, SDA/PWSA tranches, Space
   Data Network, Golden Dome/SBI, MDA SHIELD, missile warning/tracking, satellite production
   rates (York angle); plus contracts, leadership changes, and capital events (funding/M&A) for
   either angle.
4. For each material item: append a dated, sourced one-line bullet under a "## Updates" section
   at the TOP of that competitor's README.md (newest first, format:
   "- YYYY-MM-DD: <fact>. (source: <url>)"), and save the raw item text to
   os/raw/competitors/<slug>/sources/YYYY-MM-DD-<slug>-<short>.md with origin metadata. Never
   edit raw files after creating them.
5. Re-score when warranted:
   - If an item is a product ship, a win in an All.Space target account (US Navy, Army, Space
     Force, MDA, allied), or a major raise, update that competitor's scoring inputs and re-derive
     the table in os/wiki/competitors/threat-ranking.md, noting the change and date.
   - If an item is a program win in York's lanes (SDN, SDA tranches, Golden Dome/SBI, MDA SHIELD,
     PTS-G), a satellite delivery at rate, or a major raise, do the same for
     os/wiki/competitors/york-threat-ranking.md.
   - Promote watchlist companies (Blue Canyon/MDA Space, True Anomaly, Astranis, Firefly, Airbus
     US, Loft Orbital) into the York ranking if they win a program in York's lanes; create their
     folder per the competitors README structure.
6. Also scan York's own feeds (ir.yorkspacesystems.com/news and SEC EDGAR filings for YSS) and
   all.space news; file material subject-company items as dated Updates bullets on
   os/wiki/company/york/company-profile.md or os/wiki/company/all-space/company-profile.md.
7. Append one entry to os/log.md in the schema format:
   "## [YYYY-MM-DD] ingest | competitor weekly" with a one-line summary.
8. Write a one-page "week in review" to os/wiki/competitors/weekly-briefs/YYYY-MM-DD.md: biggest
   moves across both sets, any ranking changes, and 2-3 recommended actions for York/All.Space.
   Add the brief to os/index.md only if the index has a Weekly briefs entry pattern; otherwise
   leave the index unchanged.
9. Commit everything to main with message "Ingest: competitor weekly YYYY-MM-DD" and push.
   If Slack is connected, also post the week-in-review summary to the chosen channel.

Rules: obey os/wiki/rules/writing-style.md (NO em dashes, ever; verify before asserting; date and
source every claim; mark verified vs inferred). If a source is unreachable, note the gap rather
than guessing. If nothing material happened, still post "no material changes this week" and commit
the log entry.
```

## The data sources, explained plainly

- **USAspending.gov API** (free, no key): the authoritative record of federal contract awards. The endpoint above returns awards filtered by recipient name and date. This is how the agent knows who won what, and against whom.
- **SAM.gov** (free, account/API key for full API): contract opportunities and awards; useful for pipeline, but USAspending is easier to automate for awards.
- **Company newsrooms** (each competitor page lists the URL): product launches, partnerships, leadership. The agent fetches and compares against last week.
- **Trade press** (SpaceNews, SatNews, Via Satellite, Runway Girl): analysis and program shifts. Most have RSS feeds if you prefer feed-based pulls.
- **Google/news alerts:** a zero-effort backstop; set alerts for each company plus "electronically steered antenna," "multi-orbit terminal," "Ka-band terminal," "SATCOM contract," and forward them into the loop if you like.

## Cadence

- **Weekly:** this automation (pull, file, re-score, report, commit).
- **Monthly:** you personally review [threat-ranking.md](threat-ranking.md) and the running weekly briefs.
- **Event-driven:** when something big breaks (a target-account loss, a competitor acquisition, a network access-policy change), start a one-off cloud agent with the same prompt instead of waiting for Monday.

## Alternative: run from a different repository (needs the token)

If you would rather host this automation in another repository (for example All-Space-Setup) but still write competitor data into this repo, the automation's agent needs write access here. Create a fine-grained GitHub token (repository: this repo; permission: Contents read/write), add it as a Cursor Cloud secret named `ALL_SPACE_SETUP_TOKEN`, and have the prompt clone and push using it. This is only necessary for cross-repository writes; the recommended path above avoids it entirely by running the automation against this repository directly.

## Troubleshooting

- **Nothing committed after a run:** the automation probably has no repository selected (Step 3) or is on the wrong branch. Scheduled triggers default to no repo.
- **Agent invents news:** reinforce the rule to date and source every item and to report gaps rather than guess; the prompt already says this.
- **Too noisy or too quiet:** tune the 8-day window and the relevance filter in the prompt.
- **Costs:** each weekly run is one Cloud Agent run at API model pricing; a weekly cadence is a small, predictable cost.

## Related
- [Monitoring and automation](monitoring-and-automation.md) - what to watch and why
- [Threat ranking](threat-ranking.md) | [Competitors index](README.md) | [All.Space profile](../company/all-space/company-profile.md)
