#!/usr/bin/env python3
"""Import or sync the universal template into this repository. Amends, never replaces.

Pulls the template source of truth (skills, rules, company data, templates,
scripts) listed in the template's template-manifest.json and applies it here:

  - file absent locally               -> copied in
  - file identical to the template    -> skipped (state recorded)
  - local file unmodified since the
    last import, template changed     -> fast-forwarded to the template version
  - local file MODIFIED and template
    also changed                      -> incoming version staged under
                                         .template-incoming/<path>; local file
                                         untouched; an agent merges additively
  - nothing is ever deleted locally

State (what each past import delivered) lives in .template-state.json, which
should be committed. After an agent finishes merging staged files (and empties
.template-incoming/), run with --record to mark the merge complete.

Usage:
  python3 scripts/import-template.py                       # sync from GitHub
  python3 scripts/import-template.py --dry-run             # report only
  python3 scripts/import-template.py --source /path/clone  # local source
  python3 scripts/import-template.py --record              # after manual merges
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_SOURCE = "https://github.com/ALLdotSPACE/All-Space-Setup"
DEFAULT_BRANCH = "main"
TOKEN_ENV = "TEMPLATE_REPO_TOKEN"

ROOT = Path.cwd()
STATE_PATH = ROOT / ".template-state.json"
INCOMING_DIR = ROOT / ".template-incoming"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"source": DEFAULT_SOURCE, "last_import": None, "files": {}}


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sanitize_url(url: str) -> str:
    """Strip any embedded credentials so they never land in the state file."""
    return re.sub(r"^(https?://)[^/@]+@", r"\1", url)


def clone_url(source: str) -> str:
    """Inject TEMPLATE_REPO_TOKEN for private https clones (cloud agents whose
    ambient git auth is scoped to the consumer repo). Used at clone time only;
    the sanitized URL is what gets recorded."""
    token = os.environ.get(TOKEN_ENV)
    if token and source.startswith("https://") and "@" not in source:
        return source.replace("https://", f"https://x-access-token:{token}@", 1)
    return source


def obtain_source(source: str, branch: str, tmp: str) -> Path:
    src = Path(source).expanduser()
    if src.exists():
        return src.resolve()
    dest = Path(tmp) / "template-src"
    print(f"cloning {sanitize_url(source)} (branch {branch}) ...")
    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", branch, clone_url(source), str(dest)],
        check=True,
    )
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=DEFAULT_SOURCE,
                        help="Template repo URL or local path (default: %(default)s).")
    parser.add_argument("--branch", default=DEFAULT_BRANCH,
                        help="Branch to import from when cloning (default: %(default)s).")
    parser.add_argument("--dry-run", action="store_true", help="Report actions, write nothing.")
    parser.add_argument("--record", action="store_true",
                        help="After manual merges: record manifest hashes for all files no "
                             "longer staged, without copying anything.")
    args = parser.parse_args()

    src_as_path = Path(args.source).expanduser()
    if src_as_path.exists() and src_as_path.resolve() == ROOT:
        print("Source and destination are the same directory; nothing to import.",
              file=sys.stderr)
        return 1
    if (ROOT / "template-manifest.json").exists() and not args.record:
        print("This directory carries template-manifest.json (it IS the template source); "
              "run the importer from a consumer repository instead.", file=sys.stderr)
        return 1

    state = load_state()
    new_files: list[str] = []
    updated: list[str] = []
    staged: list[str] = []
    unchanged = 0
    kept_local = 0

    with tempfile.TemporaryDirectory() as tmp:
        src_root = obtain_source(args.source, args.branch, tmp)
        manifest_path = src_root / "template-manifest.json"
        if not manifest_path.exists():
            print(f"No template-manifest.json in source {src_root}", file=sys.stderr)
            return 1
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        files: dict[str, str] = manifest["files"]

        if args.record:
            for rel, mhash in files.items():
                if not (INCOMING_DIR / rel).exists():
                    state["files"][rel] = mhash
            state["last_import"] = dt.date.today().isoformat()
            state["source"] = sanitize_url(args.source)
            if not args.dry_run:
                save_state(state)
                if INCOMING_DIR.exists() and not any(INCOMING_DIR.rglob("*")):
                    shutil.rmtree(INCOMING_DIR)
            print("state recorded for all non-staged files")
            return 0

        for rel, mhash in files.items():
            src_file = src_root / rel
            if not src_file.exists():
                print(f"warning: {rel} listed in manifest but missing in source; skipped",
                      file=sys.stderr)
                continue
            incoming_hash = sha256(src_file)
            local = ROOT / rel
            last = state["files"].get(rel)

            if not local.exists():
                new_files.append(rel)
                if not args.dry_run:
                    local.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_file, local)
                    state["files"][rel] = incoming_hash
                continue

            local_hash = sha256(local)
            if local_hash == incoming_hash:
                unchanged += 1
                state["files"][rel] = incoming_hash
                continue
            if last == local_hash:
                # Local untouched since last import -> safe fast-forward.
                updated.append(rel)
                if not args.dry_run:
                    shutil.copy2(src_file, local)
                    state["files"][rel] = incoming_hash
                continue
            if last == incoming_hash:
                # Template unchanged since last import; the difference is a local
                # amendment. Leave it alone.
                kept_local += 1
                continue
            # Both sides changed (or file predates state tracking): stage for merge.
            staged.append(rel)
            if not args.dry_run:
                dest = INCOMING_DIR / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest)

        state["last_import"] = dt.date.today().isoformat()
        state["source"] = sanitize_url(args.source)
        if not args.dry_run:
            save_state(state)

    prefix = "[dry-run] " if args.dry_run else ""
    print(f"{prefix}import complete: {len(new_files)} new, {len(updated)} fast-forwarded, "
          f"{len(staged)} staged for merge, {kept_local} local amendments kept, "
          f"{unchanged} already current")
    for rel in new_files:
        print(f"  new: {rel}")
    for rel in updated:
        print(f"  updated: {rel}")
    for rel in staged:
        print(f"  STAGED (merge additively, then delete the staged copy): "
              f".template-incoming/{rel}")
    if staged:
        print("\nNext: merge each staged file into its local counterpart additively "
              "(preserve local content), remove the staged copies, then run: "
              "python3 scripts/import-template.py --record")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
