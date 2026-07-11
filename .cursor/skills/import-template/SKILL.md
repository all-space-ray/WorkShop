---
name: import-template
description: >
  Pull the latest universal content (skills, rules, company data,
  templates, scripts) from the template source-of-truth repository into
  this repository. Amends rather than replaces: locally modified files are
  staged for an additive merge, never overwritten or deleted. Use to
  import the template into a new or existing repo, or to sync updates.
disable-model-invocation: true
---

# Import Template

Sync this repository with the template source of truth (default: `https://github.com/ALLdotSPACE/All-Space-Setup`, branch `main`). The importer is `scripts/import-template.py`; this skill is the operational wrapper that runs it and finishes the merge like an agent should.

## Behavior contract (amend, never replace)

- **New file in template, absent locally** -> copied in.
- **File identical on both sides** -> skipped, state recorded.
- **Local file unmodified since last import, template changed** -> fast-forwarded to the template version.
- **Local file modified (or never imported) AND template version differs** -> the incoming version is staged at `.template-incoming/<path>`; the local file is untouched. You merge additively.
- **Nothing is ever deleted locally.** Per-repo personal content (`os/log.md`, `os/wiki/experiences/`, voice samples, career content) is not in the manifest at all.

State lives in `.template-state.json` (hashes of what each import delivered); it is how the importer tells "unmodified" from "user-amended".

## Steps

### 1. Run the importer

```bash
python3 scripts/import-template.py            # normal sync (clones template via git)
python3 scripts/import-template.py --dry-run  # show what would happen, write nothing
python3 scripts/import-template.py --source /path/to/local/clone   # offline/testing
```

First-time bootstrap into a repo that does not have the script yet. The bootstrap clone must use `TEMPLATE_REPO_TOKEN` when set (a cloud agent cannot read a private template cross-repo without it); it falls back to an unauthenticated clone when the var is empty:

```bash
if [ -n "$TEMPLATE_REPO_TOKEN" ]; then
  git clone --depth 1 "https://x-access-token:${TEMPLATE_REPO_TOKEN}@github.com/ALLdotSPACE/All-Space-Setup" /tmp/template-src
else
  git clone --depth 1 https://github.com/ALLdotSPACE/All-Space-Setup /tmp/template-src
fi
python3 /tmp/template-src/scripts/import-template.py --source /tmp/template-src
```

### 2. Merge staged files (the amend step)

If the importer reports staged files under `.template-incoming/`:

1. For each staged file, diff it against the local counterpart.
2. Merge **additively**: bring in the template's new sections, entries, and fixes while preserving every local addition. Do not drop local content; if template and local edits genuinely conflict, keep both and flag the conflict to the user with your recommendation.
3. After merging a file, delete its staged copy. When `.template-incoming/` is empty, remove it and re-run `python3 scripts/import-template.py --record` so the state file records the merge.

### 3. Post-import wiring

- Run `bash scripts/check-repo.sh`; fix anything it flags (usually a skills pipeline rerun: normalize frontmatter -> sync commands -> sync mirrors -> reindex).
- If this was the FIRST import into this repo, tell the user to run `/initialize` for the interactive tour and personal setup (voice, PII, issue tracker).
- Commit with `Import template: <date> (<n> new, <n> updated, <n> merged)` and push per the repo's workflow.

## Weekly update automation (ready to paste)

Create a Scheduled automation (e.g. cron `0 13 * * 1`, Mondays 13:00 UTC) pointed at **this consumer repository** and its default branch, with this prompt:

```
Run the import-template skill: execute `python3 scripts/import-template.py` from the repository
root to pull the latest template updates from the source-of-truth repo. If files are staged in
.template-incoming/, merge each one additively into its local counterpart (preserve all local
content; bring in template additions; flag genuine conflicts rather than dropping either side),
delete the staged copies, and re-run `python3 scripts/import-template.py --record`. Then run
`bash scripts/check-repo.sh` and fix what it flags. Do NOT prompt for or modify personal content
(voice, career, experiences, log); personal setup happens only via /initialize. Commit as
"Import template: YYYY-MM-DD (<n> new, <n> updated, <n> merged)" and push. If there were no
changes, report "template already current" and stop without committing.
```

## Private template repo access (cloud agents)

A cloud agent's ambient git credentials are usually scoped to the repo it runs in, so cloning the private template cross-repo can fail with authentication errors. Fix once per user (or team):

1. Create a **fine-grained GitHub personal access token**: repository access = the template repo only; permissions = Contents: Read-only.
2. Add it as a Cursor Cloud Agents secret named **`TEMPLATE_REPO_TOKEN`** (Dashboard -> Cloud Agents -> Secrets; team-scoped works for everyone).
3. Done. The importer detects the env var automatically and injects it at clone time only; it never stores the token (URLs recorded in `.template-state.json` are credential-stripped).

Running locally (desktop Cursor or a terminal where `git clone` of the template already works) needs no token.

## Notes

- The manifest (`template-manifest.json`) lives only in the template source repo and is regenerated there by `/improve-system`; consumers read it from the clone, they do not carry it.
- First-import collisions are normal: any file the consumer repo already has (README, .gitignore, AGENTS.md, existing Cursor rules) stages to `.template-incoming/` for the additive merge instead of being replaced.
