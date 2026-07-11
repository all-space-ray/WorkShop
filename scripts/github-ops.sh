#!/usr/bin/env bash
# github-ops.sh - token-free GitHub writes for read-only (Cloud Agent) environments.
#
# Enqueues a batch of write operations for the Actions executor
# (.github/workflows/github-ops.yml), waits for it to run with the built-in
# GITHUB_TOKEN, and prints the results JSON. No user token required.
#
# Usage:
#   scripts/github-ops.sh path/to/ops.json      # ops.json is the JSON array of ops
#   echo '<ops-json-array>' | scripts/github-ops.sh -
#
# Each op is one of (see docs/agents/issue-tracker.md for the full schema):
#   {"op":"create_label","name":"..","description":"..","color":"ededed"}
#   {"op":"create_issue","title":"..","body":"..","label":"..","nonce":".."}
#   {"op":"comment","issue":N,"body":".."}
#   {"op":"add_label"|"remove_label","issue":N,"label":".."}
#   {"op":"assign","issue":N,"assignee":"login"}
#   {"op":"sub_issue","parent":N,"child":N}
#   {"op":"blocked_by","issue":N,"blocker":N}
#   {"op":"close","issue":N,"comment":".."}
#
# Created issue numbers come back keyed by the "nonce" you supplied.
set -euo pipefail

repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root"

src="${1:-/dev/stdin}"; [ "$src" = "-" ] && src=/dev/stdin
ops=$(cat "$src")
echo "$ops" | jq -e 'type=="array"' >/dev/null || { echo "error: ops must be a JSON array" >&2; exit 2; }

id="ops-$(date -u +%Y%m%d%H%M%S)-$RANDOM"
mkdir -p .github/ops
jq -n --arg id "$id" --argjson ops "$ops" '{id:$id, ops:$ops}' > .github/ops/request.json

branch=$(git rev-parse --abbrev-ref HEAD)
git add .github/ops/request.json
git commit -q -m "ops request $id"
git push -q origin "$branch"
sha=$(git rev-parse HEAD)
echo "github-ops: enqueued $id on $branch ($sha)" >&2

deadline=$(( $(date +%s) + 240 ))
status=""; conclusion=""
while [ "$(date +%s)" -lt "$deadline" ]; do
  line=$(gh run list --limit 30 \
    --json headSha,status,conclusion,workflowName \
    --jq ".[] | select(.headSha==\"$sha\" and .workflowName==\"GitHub ops executor\") | \"\(.status) \(.conclusion)\"" 2>/dev/null | head -1 || true)
  status=$(printf '%s' "$line" | awk '{print $1}')
  conclusion=$(printf '%s' "$line" | awk '{print $2}')
  [ "${status:-}" = "completed" ] && break
  sleep 5
done
echo "github-ops: run ${status:-none} ${conclusion:-}" >&2

git pull -q --rebase origin "$branch" 2>/dev/null || git pull -q origin "$branch" || true

res=".github/ops/results/${id}.json"
if [ -f "$res" ]; then
  cat "$res"
else
  echo "{\"id\":\"$id\",\"results\":[],\"warning\":\"no results file; check Actions run for $sha\"}"
fi
[ "${conclusion:-}" = "success" ] || { echo "github-ops: warning, run did not succeed" >&2; }
