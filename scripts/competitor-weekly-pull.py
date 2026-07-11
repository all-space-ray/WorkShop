#!/usr/bin/env python3
"""Pull recent federal contract awards for all tracked competitors from USAspending.

Presetup for the weekly competitor-intelligence automation (see
os/wiki/competitors/weekly-automation-setup.md). Uses only the Python standard
library and the free, keyless USAspending API (validated 2026-07-10).

Queries the trailing N days (default 8) of contract awards for every company on
both competitor lists (All.Space set and York set) plus York itself, and prints
a markdown digest to stdout (or JSON with --json). The weekly agent runs this
first, then merges the results with newsroom/trade-press findings.

Usage:
  python3 scripts/competitor-weekly-pull.py            # markdown digest, 8 days
  python3 scripts/competitor-weekly-pull.py --days 30  # wider window
  python3 scripts/competitor-weekly-pull.py --json     # machine-readable
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import urllib.request

API = "https://api.usaspending.gov/api/v2/search/spending_by_award/"

# slug -> recipient search terms (legal-name fragments USAspending matches on)
COMPANIES: dict[str, list[str]] = {
    # Subject companies
    "york-space-systems": ["York Space Systems"],
    "all-space": ["All.Space", "Isotropic Systems"],
    # All.Space competitor set
    "kymeta": ["Kymeta"],
    "thinkom": ["ThinKom"],
    "cesiumastro": ["CesiumAstro", "Cesium Astro"],
    "hanwha-phasor": ["Hanwha Phasor"],
    "ball-bae-systems": ["BAE Systems Space", "Ball Aerospace"],
    "get-sat": ["Get SAT"],
    "intellian": ["Intellian"],
    "viasat": ["Viasat"],
    "l3harris": ["L3Harris"],
    "spacex-starshield": ["Space Exploration Technologies"],
    # York competitor set (new folders)
    "lockheed-martin": ["Lockheed Martin"],
    "northrop-grumman": ["Northrop Grumman"],
    "rocket-lab": ["Rocket Lab"],
    "boeing-millennium-space": ["Millennium Space"],
    "sierra-space": ["Sierra Space"],
    "apex-space": ["Apex Technology", "Apex Space"],
    "k2-space": ["K2 Space"],
    "muon-space": ["Muon Space"],
}

FIELDS = [
    "Award ID", "Recipient Name", "Start Date", "Award Amount",
    "Awarding Agency", "Awarding Sub Agency", "Description",
]


def fetch_awards(terms: list[str], start: str, end: str, limit: int = 25) -> list[dict]:
    body = {
        "filters": {
            "recipient_search_text": terms,
            "time_period": [{"start_date": start, "end_date": end}],
            "award_type_codes": ["A", "B", "C", "D"],
        },
        "fields": FIELDS,
        "limit": limit,
        "page": 1,
        "sort": "Start Date",
        "order": "desc",
    }
    req = urllib.request.Request(
        API, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read()).get("results", [])


def in_window(row: dict, start: str) -> bool:
    d = row.get("Start Date") or ""
    return d >= start


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=8, help="Trailing window in days (default 8).")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown.")
    args = parser.parse_args()

    end = dt.date.today()
    start = end - dt.timedelta(days=args.days)
    start_s, end_s = start.isoformat(), end.isoformat()

    digest: dict[str, list[dict]] = {}
    errors: dict[str, str] = {}
    for slug, terms in COMPANIES.items():
        rows: list[dict] = []
        for attempt in range(2):  # the API 502s/times out on giant recipients; one retry helps
            try:
                rows = [r for r in fetch_awards(terms, start_s, end_s) if in_window(r, start_s)]
                errors.pop(slug, None)
                break
            except Exception as exc:  # noqa: BLE001 - report gaps, never guess
                errors[slug] = str(exc)
                time.sleep(3 * (attempt + 1))
        digest[slug] = rows
        time.sleep(0.4)  # be polite to the free API

    if args.json:
        print(json.dumps({"window": [start_s, end_s], "awards": digest, "errors": errors}, indent=2))
        return 0

    print(f"# Federal award digest {start_s} to {end_s} (USAspending)\n")
    any_hit = False
    for slug, rows in digest.items():
        if not rows:
            continue
        any_hit = True
        print(f"## {slug}")
        for r in rows:
            amt = r.get("Award Amount")
            amt_s = f"${amt:,.0f}" if isinstance(amt, (int, float)) else str(amt)
            desc = (r.get("Description") or "").strip()[:160]
            print(
                f"- {r.get('Start Date')}: {amt_s} | {r.get('Awarding Agency')}"
                f" / {r.get('Awarding Sub Agency')} | {r.get('Recipient Name')}"
                f" | award {r.get('Award ID')} | {desc}"
            )
        print()
    if not any_hit:
        print("No new awards found in the window for any tracked company.\n")
    if errors:
        print("## Query errors (report these as gaps, do not guess)")
        for slug, err in errors.items():
            print(f"- {slug}: {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
