# Issue tracker: GitHub

Issues and PRDs for this repo live as GitHub issues on `all-space-ray/WorkShop`.

**Reads use the `gh` CLI directly. Writes go through a token-free proxy**, because a
Cursor Cloud Agent's `gh` is read-only (it can view GitHub but cannot create or modify
resources). The proxy needs no personal token: a committed GitHub Actions workflow does
the write with the built-in `GITHUB_TOKEN`. See "GitHub writes" below.

`gh` infers the repo from `git remote -v` automatically inside a clone.

## Reads (direct `gh`, allowed everywhere)

- **Read an issue**: `gh issue view <number> --comments`.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with `--label` / `--state` filters.
- **Resolve an issue's numeric database id** (needed for sub-issues/dependencies): `gh api repos/<owner>/<repo>/issues/<n> --jq .id`.

## GitHub writes (token-free proxy)

Do NOT run `gh` write commands (create/edit/close/label/assign) or `gh api --method POST`
directly, and never ask the user to run them: they fail under a read-only Cloud Agent.
Instead enqueue operations for the executor with the helper:

```sh
echo '[ {"op":"create_issue","title":"...","body":"...","label":"needs-triage","nonce":"abc123"} ]' \
  | scripts/github-ops.sh -
# or: scripts/github-ops.sh path/to/ops.json
```

The helper writes `.github/ops/request.json`, commits and pushes it, waits for the
`GitHub ops executor` workflow (`.github/workflows/github-ops.yml`) to run, then prints
the results JSON. Created issue numbers come back keyed by the `nonce` you set.

Operation schema (batch as many as needed in one array; they run in order):

| Canonical skill action | Proxy op |
|---|---|
| create a label | `{"op":"create_label","name":"..","description":"..","color":"ededed"}` |
| publish to the issue tracker (create issue) | `{"op":"create_issue","title":"..","body":"..","label":"..","nonce":".."}` |
| comment on an issue | `{"op":"comment","issue":N,"body":".."}` |
| apply / remove a label | `{"op":"add_label"\|"remove_label","issue":N,"label":".."}` |
| assign (claim) | `{"op":"assign","issue":N,"assignee":"<github-login>"}` |
| link a sub-issue | `{"op":"sub_issue","parent":N,"child":N}` |
| add a blocking dependency | `{"op":"blocked_by","issue":N,"blocker":N}` |
| close | `{"op":"close","issue":N,"comment":".."}` |

Nuances (verified):

- Proxy-created issues are authored by `github-actions[bot]`. Record the real
  author/agent in the issue body when it matters.
- "Claim @me" does not work through the proxy (the actor is the bot). Pass the driving
  dev's GitHub login explicitly in an `assign` op.
- Read results from the returned JSON (or the committed `.github/ops/results/<id>.json`).
  GitHub search indexing lags, so do not rely on `gh issue list --search` to find a
  just-created issue; use the results file or `gh issue view <number>`.
- The five triage labels must exist first; they are created by
  `.github/workflows/setup-triage-labels.yml`.

Direct mode (optional): in an environment that genuinely has GitHub write access (for
example a human running locally with authenticated `gh`), you may run the equivalent
`gh` commands directly instead of the proxy. The proxy also works there, just slower.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as
feature requests; `/triage` reads this flag.)_ When yes, use the read side with
`gh pr view` / `gh pr list` / `gh pr diff`, and route PR label/comment/close writes
through the proxy the same way (extend the executor if a PR-specific op is needed).

## When a skill says "publish to the issue tracker"

Enqueue a `create_issue` op (see above).

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments` (read, direct).

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue with **child** issues as tickets.

- **Map**: `create_issue` with `"label":"wayfinder:map"`, body holding Notes /
  Decisions-so-far / Fog.
- **Child ticket**: `create_issue` with `"label":"wayfinder:<type>"`
  (`research`/`prototype`/`grilling`/`task`) and `Part of #<map>` at the top of the
  body, then a `sub_issue` op to link it under the map.
- **Blocking**: a `blocked_by` op (child blocked_by blocker). Read the live gate with
  `gh api repos/<owner>/<repo>/issues/<n> --jq .issue_dependencies_summary.blocked_by`
  (0 open blockers means unblocked).
- **Frontier query** (read, direct): list the map's open children with `gh issue list`,
  drop any with an open blocker or an assignee; first in map order wins.
- **Claim**: an `assign` op with the driving dev's explicit GitHub login (the session's
  first write).
- **Resolve**: a `comment` op with the answer, then a `close` op; then append a context
  pointer to the map's Decisions-so-far (via a `comment` op on the map).

Note on wayfinder labels: create `wayfinder:map` and `wayfinder:<type>` labels on first
use by enqueuing `create_label` ops (idempotent), then use them on `create_issue`.
