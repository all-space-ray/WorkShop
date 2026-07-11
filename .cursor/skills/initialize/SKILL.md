---
name: initialize
description: >
  First-run onboarding for this repository. Explains how the whole system
  works (Personal OS, skill flow and order, rules, template sync), then
  walks the user through personal setup - voice samples, optional PII
  sections, issue tracker, and update automation. Use on a fresh import or
  whenever the user asks how the system works.
disable-model-invocation: true
---

# Initialize

Onboard a user into this repository. Two jobs: **explain the system**, then **set up what only they can provide**. Run interactively; ask one question at a time. Safe to re-run at any time; skip anything already configured.

## Step 1: Explain how the system works

Give a concise tour (offer to go deeper on any part). Source of truth: `docs/system-guide.md`; read it first and base the tour on it. Cover, in order:

1. **The Personal OS** (`os/`): raw vs wiki layers, schema/index/log, `/ingest-resource` to add knowledge, `/improve-system` to capture lessons. Token discipline: schema -> index -> only needed pages.
2. **The skill flow**: the mandatory order for major work (grill -> spec -> tickets -> implement -> review) per `os/wiki/rules/program-workflow.md`, on-ramps (`/triage`, `/diagnosing-bugs`, `/wayfinder`, `/research`), and `/ask-matt` as the router. Emphasize: this applies to major programs and tasks, not simple questions.
3. **Enforced rules**: `os/wiki/rules/` is the master copy, exported to `.cursor/rules/` by `scripts/sync-rules.py`; writing style applies to all generated text.
4. **Template sync**: this repo's content comes from the template source of truth; `/import-template` pulls updates; personal content stays local and is never overwritten (modified files stage into `.template-incoming/` for additive merges).

## Step 2: Detect first-run state

Check and report what is or is not configured yet:

- `os/wiki/my-voice/` contains only a README -> voice not set up.
- `docs/agents/issue-tracker.md` missing -> engineering skills not configured.
- `README.md` still has `<REPO-NAME>` placeholders -> repo identity not set.
- `.template-state.json` missing -> template import state absent (fine in the template repo itself; in a consumer repo, suggest `/import-template`).

## Step 3: Personal setup (ask, one at a time; all optional)

1. **Repo identity**: fill the `README.md` placeholders (repo name, one-line description) if the user wants.
2. **Voice and tone**: offer to set up their voice profile now. If yes: request 3-10 writing samples (paste, file, or URL), file them verbatim under `os/wiki/my-voice/<user-slug>/samples/` (immutable), then distill `os/wiki/my-voice/<user-slug>/profile.md` capturing sentence rhythm, formality, vocabulary, signature moves, and anti-patterns (what they never say). Index and log per the OS schema. Explain: deliverable skills consult this profile; more varied samples = better profile.
3. **PII and per-repo domains**: explain which sections are personal (`my-voice/`, `career/`, `experiences/`, new project domains) and offer to ingest anything they want now via `/ingest-resource` (resumes into `career/`, project docs into a new domain folder). Never push PII into the template source repo.
4. **Issue tracker**: if `docs/agents/issue-tracker.md` is missing, offer to run `/setup-matt-pocock-skills` now (it configures tracker, triage labels, and domain docs; required before the first engineering flow).
5. **Update automation**: offer to set up the weekly template-sync automation; the ready-to-paste prompt is in the `import-template` skill. Note: personal setup (this skill) is one-time; weekly syncs never re-prompt for it.

## Step 4: Verify and report

Run `bash scripts/check-repo.sh` and report the result. Then summarize: what was explained, what was configured, what was skipped and how to do it later (`/initialize` again, or the specific skill). Commit any changes with `Initialize: [scope]`.

## Quality bar

- One question at a time; the user may know none of the vocabulary.
- Never invent personal data; only file what the user provides.
- Re-runs must be idempotent: detect existing state, offer to update rather than duplicate.
