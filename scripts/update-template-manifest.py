#!/usr/bin/env python3
"""Regenerate template-manifest.json, the export manifest for this template repo.

This repository is the single source of truth for skills, rules, company data,
templates, and automation scripts. The manifest lists every UNIVERSAL file with
a sha256 content hash; consumer repositories import against it with
scripts/import-template.py. Personal/per-repo content (voice samples, career,
experiences, os/log.md, root README identity) is deliberately excluded.

Run with no arguments to (re)write the manifest. Run with --check to verify it
matches the working tree (wired into scripts/check-repo.sh; exits non-zero on
drift). /improve-system regenerates it at the end of every session.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "template-manifest.json"

TEMPLATE_REPO = "https://github.com/ALLdotSPACE/All-Space-Setup"

# Universal content. Directories are walked recursively; files listed as-is.
INCLUDE = [
    ".agents",
    ".cursor",
    ".cursorignore",
    ".editorconfig",
    ".github",
    ".gitignore",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs",
    "os/AGENTS.md",
    "os/index.md",
    "os/raw",
    "os/wiki",
    "README.md",
    "scripts",
    "src",
    "tests",
]

# Per-repo / personal content, never exported. fnmatch patterns on repo-relative paths.
EXCLUDE = [
    "os/log.md",
    "os/wiki/experiences/*",
    "os/wiki/my-voice/*/*",       # keep my-voice/README.md scaffold only
    "os/wiki/career/*/*",         # keep career/README.md scaffold only
    "os/wiki/career/[!R]*",       # any non-README file directly in career/
    "os/wiki/my-voice/[!R]*",
    "GrabMe/*",
    "template-manifest.json",
    ".template-state.json",
    ".template-incoming/*",
    "universal-repo-bootstrap.md",
    "*.pyc",
    "*/__pycache__/*",
]


def excluded(rel: str) -> bool:
    return any(fnmatch.fnmatch(rel, pat) for pat in EXCLUDE)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect() -> dict[str, str]:
    files: dict[str, str] = {}
    for entry in INCLUDE:
        p = ROOT / entry
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            if not excluded(rel):
                files[rel] = sha256(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if not f.is_file():
                    continue
                rel = f.relative_to(ROOT).as_posix()
                if excluded(rel):
                    continue
                files[rel] = sha256(f)
    return dict(sorted(files.items()))


def render(files: dict[str, str]) -> str:
    doc = {
        "template": TEMPLATE_REPO,
        "generated": dt.date.today().isoformat(),
        "file_count": len(files),
        "files": files,
    }
    return json.dumps(doc, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Verify the committed manifest matches the tree (no writes).")
    args = parser.parse_args()

    files = collect()

    if args.check:
        if not MANIFEST.exists():
            print("Missing template-manifest.json (run scripts/update-template-manifest.py)",
                  file=sys.stderr)
            return 1
        current = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if current.get("files") != files:
            old = current.get("files") or {}
            added = sorted(set(files) - set(old))
            removed = sorted(set(old) - set(files))
            changed = sorted(k for k in set(files) & set(old) if files[k] != old[k])
            for k in added:
                print(f"Manifest stale, new file: {k}", file=sys.stderr)
            for k in removed:
                print(f"Manifest stale, removed file: {k}", file=sys.stderr)
            for k in changed:
                print(f"Manifest stale, changed file: {k}", file=sys.stderr)
            print("Run: python3 scripts/update-template-manifest.py", file=sys.stderr)
            return 1
        print("Template manifest is in sync.")
        return 0

    MANIFEST.write_text(render(files), encoding="utf-8")
    print(f"wrote template-manifest.json ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
