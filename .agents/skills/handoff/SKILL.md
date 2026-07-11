---
name: handoff
description: >
  Compact the current conversation into a handoff document for another
  agent to pick up.
disable-model-invocation: true
---

**Argument hint:** What will the next session be used for?

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to a `GrabMe/` folder at the repository root (create the folder if it does not exist), then commit and push it — this is what lets `/handoff` work across cloud agents, whose temporary directories do not survive between sessions.

Make sure the commit actually reaches the default branch: if the current branch's PR has already merged, a commit pushed to that branch strands the handoff (this happened on 2026-07-06 and the next agent had to recover it via cherry-pick). In that case, put the handoff on a fresh branch and open a PR, or confirm with the user how it will land on main.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

End the document with a cleanup note: after the new agent has ingested this file, it should delete the file (and commit the deletion) to keep `GrabMe/` empty between handoffs.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
