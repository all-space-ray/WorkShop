# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual label strings used in this repo's issue tracker.

| Label in mattpocock/skills | Label in our tracker | Meaning                                  |
| -------------------------- | -------------------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | Requires human implementation            |
| `wontfix`                  | `wontfix`            | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label string from this table.

Edit the right-hand column to match whatever vocabulary you actually use.

## One-time label creation

These labels must exist in GitHub before `/triage` can apply them. Create them once (from a machine or agent with write access to the repo; the Cloud Agent `gh` used during setup is read-only):

```sh
gh label create needs-triage   --description "Maintainer needs to evaluate this issue" --color FBCA04
gh label create needs-info     --description "Waiting on reporter for more information" --color D876E3
gh label create ready-for-agent --description "Fully specified, ready for an AFK agent" --color 0E8A16
gh label create ready-for-human --description "Requires human implementation"          --color 1D76DB
gh label create wontfix        --description "Will not be actioned"                     --color FFFFFF
```

`/wayfinder` also uses `wayfinder:map` and `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`) labels; create those when you first run wayfinding, or let the skill create them if it has write access.

