# Template rollout runbook

Operational, step-by-step instructions for making this repository work as the team's template source of truth: owner-side GitHub setup, consumer-side first import (blank and populated repos), and the weekly sync automation. Consumer mechanics live in the [import-template skill](../.cursor/skills/import-template/SKILL.md); this runbook is the click-by-click rollout guide.

## Part 1: Owner setup (once, on this repository)

### 1.1 Do NOT rely on GitHub's "Template repository" checkbox

The Settings checkbox only powers GitHub's "Use this template" button, which stamps out a **one-time, full copy** of every file into a brand-new repo: no update mechanism, no amend semantics, and the copy would wrongly include `template-manifest.json` (which marks a repo as the template source and blocks the importer) plus this repo's `os/log.md` history. Our importer replaces that feature for both new and existing repos. Leave the checkbox unchecked (checking it is harmless only if nobody uses the button).

### 1.2 Keep it private; grant the team read access

The repo does **not** need to be public. Consumers only need to be able to `git clone` it:

1. GitHub -> this repo -> **Settings -> Collaborators and teams -> Add teams** (or people).
2. Grant the team the **Read** role (enough to clone and pull; nobody imports by pushing).
3. Alternatively set the organization's base permission to Read (Org Settings -> Member privileges) if every member should see every repo.

### 1.3 Token for cloud agents (once per team)

Members working in desktop Cursor or a terminal clone with their own GitHub auth and need nothing extra. **Cloud agents** run with credentials scoped to the repo they are working in, so the weekly automation needs a read token to clone this template cross-repo:

1. Open the fine-grained token form directly: <https://github.com/settings/personal-access-tokens/new> (click path: profile photo -> Settings -> **Developer settings**, at the very bottom of the left sidebar -> Personal access tokens -> Fine-grained tokens -> Generate new token).
2. **Resource owner: select the organization that owns this repo** (not your personal account), or the template repo will not appear in the repository picker.
3. Repository access: **Only select repositories** -> this template repo. Permissions: Repository permissions -> **Contents: Read-only** (Metadata Read-only is added automatically). Generous expiry.
4. Cursor Dashboard (<https://cursor.com/dashboard>) -> **Cloud Agents -> Secrets** -> add secret named **`TEMPLATE_REPO_TOKEN`** with that value, team-scoped.

Org-policy caveats: if the org does not appear as a resource owner, an org admin must allow fine-grained PATs (Org Settings -> Third-party Access -> Personal access tokens); some orgs hold new tokens as "pending" until an admin approves them there (Pending requests, same page).

**If fine-grained tokens are unavailable and you cannot change org policy:** a classic token (<https://github.com/settings/tokens>) CANNOT be restricted to one repository; its `repo` scope covers every repo its owner can access, so containment must come from the account, not the token. The safe pattern is a dedicated machine account:

1. Create a fresh GitHub account (e.g. `<org>-template-bot`).
2. In the template repo -> Settings -> Collaborators -> invite the bot with the **Read** role (repo-level admin is enough; no org settings needed). Accept from the bot account.
3. As the bot, generate a classic token with the `repo` scope, and use THAT as `TEMPLATE_REPO_TOKEN`. The bot can only reach this one repo, so the token is effectively contained to it.

Never use a classic token from a personal account as a team-scoped secret; it would expose everything that account can access.

The importer picks the env var up automatically and never writes the token to disk.

## Part 2: Consumer first import (per repository)

Works identically for a blank repo and a fully populated one; the only difference is how many files land in the merge queue. The consumer needs: `git`, `bash`, `python3` (all present in Cursor agents), and read access to the template.

### 2.1 Run the bootstrap (agent-driven, recommended)

Open an agent on the consumer repository and paste:

```
Bootstrap this repository from the team template. Run this exactly (it uses TEMPLATE_REPO_TOKEN
when set, so the first clone works for a private template on a cloud agent, and falls back to an
unauthenticated clone otherwise):
  if [ -n "$TEMPLATE_REPO_TOKEN" ]; then
    git clone --depth 1 "https://x-access-token:${TEMPLATE_REPO_TOKEN}@github.com/ALLdotSPACE/All-Space-Setup" /tmp/template-src
  else
    git clone --depth 1 https://github.com/ALLdotSPACE/All-Space-Setup /tmp/template-src
  fi
  python3 /tmp/template-src/scripts/import-template.py --source /tmp/template-src
(If the clone fails with "Repository not found" or an auth error, TEMPLATE_REPO_TOKEN is missing or
unreadable; set it up per docs/template-rollout.md Part 1.3 in the template repo.)
Then, if the importer staged files under .template-incoming/, merge each one additively into
its local counterpart: preserve ALL existing local content, add the template's sections and
entries, and flag genuine conflicts to me rather than dropping either side. Delete each staged
copy after merging and run: python3 scripts/import-template.py --record
Finish with: bash scripts/check-repo.sh and fix anything it flags. Commit everything as
"Import template: <date> (first import)" and push. Then tell me to start a NEW agent thread
and run /initialize.
```

(Manual equivalent: run the two commands yourself, merge staged files by hand, `--record`, `check-repo.sh`, commit, push.)

### 2.2 What to expect

- **Blank repo (just a README):** everything imports as new; the existing `README.md` stages to `.template-incoming/README.md` (the importer never replaces an existing file it did not write). Merge: usually keep the consumer's README title and add anything useful from the template's.
- **Populated repo:** same, plus staged copies for whatever already exists on both sides, typically `.gitignore`, `.editorconfig`, `AGENTS.md`, `.cursor/rules/*`, `docs/README.md`, `scripts/README.md`, `src/README.md`, `tests/README.md`. Each merge is additive; existing project content is never lost. Project code is untouched (the manifest only carries universal paths).
- `.template-state.json` appears at the root: **commit it** (it is how future imports tell your edits from template updates).

### 2.3 Onboard the user

In a **new agent thread** (new so the freshly imported skills are discovered; if the `/` menu looks stale, plain language works: "use the initialize skill"):

1. Run `/initialize`: it explains the Personal OS, the skill workflow, rules, and template sync, then walks personal setup: voice samples, optional PII, issue tracker (`/setup-matt-pocock-skills`), automation.
2. Personal content (voice, career, experiences, log) stays local; it is never exported back to the template.

## Part 3: Weekly sync automation (per consumer repository)

1. Go to **cursor.com/automations** -> New automation.
2. Trigger: **Scheduled**, e.g. cron `0 13 * * 1` (Mondays 13:00 UTC).
3. Repository: **the consumer repository**, default branch. (Scheduled triggers default to NO repository; forgetting this is the most common mistake.)
4. Prompt: paste the "Weekly update automation" prompt from the [import-template skill](../.cursor/skills/import-template/SKILL.md).
5. Confirm `TEMPLATE_REPO_TOKEN` exists as a Cloud Agents secret (Part 1.3), then set the automation **Active**.
6. Verify after the first run: a commit like `Import template: YYYY-MM-DD (...)` on the default branch, or a "template already current" report.

## Part 4: Test plan for the two pilot repositories

### Test A: the blank repo (README only)

1. Run the Part 2.1 bootstrap prompt. Expected importer report: `~288 new, 0 fast-forwarded, 1 staged for merge` (the README).
2. Confirm the agent merged the README additively, `--record` ran, `check-repo.sh` passes, and one commit landed.
3. New thread -> `/initialize` -> confirm the tour runs and first-run detection flags voice + issue tracker as unset.
4. Set up the Part 3 automation; trigger it once manually if you want instant verification: expected result "template already current".
5. Durable-sync check: make a small change in the template repo (e.g. edit a rules page, regenerate manifest via `/improve-system` or `python3 scripts/update-template-manifest.py`, merge to main), re-run the automation, confirm the change fast-forwards in.

### Test B: the populated active project

1. Branch first for a safe review: `git checkout -b template-import-test`.
2. Run the same Part 2.1 bootstrap prompt. Expected: hundreds of new files, several staged (their README, .gitignore, AGENTS.md, etc. as in Part 2.2); **zero project files modified** (verify with `git status` that only additions plus the merged shared files changed).
3. Review the staged-file merges carefully: every pre-existing line of their configs must survive.
4. `check-repo.sh` green, commit, open a PR to their default branch, review, merge.
5. New thread -> `/initialize`; then Part 3 automation.
6. Amend-protection check: edit an imported file locally (add a line to `AGENTS.md`), then run the sync again after any template change: the file must stage for merge, not be overwritten.

## Troubleshooting

- **`Repository not found` when a cloud agent clones the template:** this IS the access failure; GitHub reports private repos you cannot reach as "not found" rather than 403 to avoid revealing they exist. Verified empirically (2026-07-11): cloud-agent git tokens are scoped to the repo the agent runs in and cannot read sibling org repos, so `TEMPLATE_REPO_TOKEN` (Part 1.3) is REQUIRED for the weekly automation and for any cloud-agent-driven import. A temporary classic token with a 7-day expiry (user-scoped secret) is an acceptable stopgap while a fine-grained token awaits org approval; swap and revoke once approved.
- **`Authentication failed` on clone:** set up `TEMPLATE_REPO_TOKEN` (Part 1.3) or run the import from a machine where `git clone` of the template works.
- **"This directory carries template-manifest.json":** the importer is being run inside the template source repo (or a full GitHub "Use this template" copy). Consumers must not carry the manifest; delete it in the copy or import into a normal repo.
- **Staged files pile up unmerged:** each import re-stages unmerged files (idempotent); run the merge step of the weekly prompt, then `--record`.
- **Slash commands missing after import:** commit to the default branch, start a new agent thread, hard-refresh the client; plain-language invocation always works meanwhile.
