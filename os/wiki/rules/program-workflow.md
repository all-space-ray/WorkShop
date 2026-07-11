---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [rules, workflow, skills, matt-pocock, planning, token-discipline]
sources: []
description: Mandatory skill workflow when the user starts a discussion about creating a new program, product, feature build, or other major task. Routes work through wayfinder (default entry), spec, tickets, and implementation to reduce assumptions and token burn. Not for simple research or informational questions.
---

# Program and major-task workflow (enforced)

When the user opens a discussion about **creating a new program, product, service, major feature, or any multi-session build**, do not start designing or coding ad hoc. Route the work through the engineering-skill flow below. These are rules, not suggestions. The flow exists to reduce assumptions, produce consistent quality, and keep every phase inside the model's sharp reasoning window instead of burning tokens on rework.

**This rule does NOT apply to:** simple research questions, informational lookups, one-file fixes, quick edits, or conversational questions. For those, just answer or make the change. When in doubt, ask one question: "Is this a quick task, or should we run the full workflow?"

## Trigger examples

- "Let's build a new tool that..." / "I want to create a program for..." -> full workflow, starting at `/wayfinder`.
- "Start a discussion on a new customer portal" -> full workflow, starting at `/wayfinder`.
- "What time is it in London?" / "Research X and file it" / "Fix this typo" -> NOT this rule.

## The mandatory order (the main flow: idea -> ship)

> **Owner preference (2026-07-10):** `/wayfinder` replaces `/grill-with-docs` as the default entry for new programs and major tasks, per Matt Pocock's own updated workflow (he found wayfinding more comprehensive). Grilling does not disappear: wayfinder drives `/grilling` and `/domain-modeling` internally, both when naming the destination and inside its grilling-type tickets.

0. **`/setup-matt-pocock-skills`** - once per repository, before the first engineering flow ever runs. Configures the issue tracker (GitHub / GitLab / local markdown), the five triage labels, and the domain-doc layout (`CONTEXT.md` + `docs/adr/`). If `docs/agents/issue-tracker.md` does not exist in the repo, this step has not been done; do it first. Wayfinder requires the tracker: its map and tickets live there.
1. **`/wayfinder`** - the default entry. Chart the map first: name the destination (via grilling and domain-modeling, one question at a time), map the frontier breadth-first, create the map issue and the tickets you can specify now, and sketch the rest as fog (Not yet specified). Then work the map: **one ticket per session**, producing decisions, not deliverables, until the way to the destination is clear.
   - **Small-effort fallback:** if charting surfaces no fog (the whole journey fits one session), wayfinder itself says stop; run **`/grill-with-docs`** (in a codebase) or **`/grill-me`** (no codebase) in the same conversation instead - the relentless interview, one question at a time, decisions put to the user - then continue at step 3.
2. **Prototype detour (only if needed):** if a question needs a runnable answer (a state model, business logic, a UI you must see), that is a wayfinder prototype-type ticket; standalone, `/handoff` out, run `/prototype` in a fresh session, `/handoff` the learning back. Keep the answer, delete the code.
3. **Scale branch:**
   - Multi-session build -> **`/to-spec`** (turn the resolved map or grilled thread into a spec on the tracker), then **`/to-tickets`** (split into tracer-bullet tickets with explicit blocking edges).
   - Single-session build -> **`/implement`** directly.
4. **`/implement`** per ticket, **clearing context between tickets**. Internally it drives **`/tdd`** (red-green-refactor at pre-agreed seams), typechecks regularly, runs the full suite once at the end.
5. **`/code-review`** - two-axis review (Standards + Spec) before committing. `/implement` closes out with this automatically; run it standalone for branches/PRs.
6. **`/improve-system`** at session end - capture corrections, lessons, and conventions back into the Personal OS.

## Context hygiene (why the order matters)

- Wayfinder is built for context discipline: charting the map is one session; **never resolve more than one map ticket per session**; each session loads the low-res map and zooms only the tickets it needs.
- On the small-effort fallback, keep grill -> spec -> tickets in **one unbroken context window**; do not compact or clear until after `/to-tickets`.
- Each `/implement` starts **fresh** from its ticket. This is the token-burn control: planning happens in small decision-sized windows; execution happens in small, clean windows.
- Respect the smart zone (~120k tokens). If a session approaches it mid-phase, do not push on degraded: `/handoff` and continue in a fresh thread.

## On-ramps (route these into the main flow)

- **Incoming bugs/requests you did not create** -> `/triage` first (it produces agent-ready issues for `/implement`). Never triage tickets `/to-tickets` created; they are already agent-ready.
- **Something is broken and resists a first glance** -> `/diagnosing-bugs` (tight feedback loop first, then fix with a regression test).
- **Research needed** -> `/research` runs in the background and produces a cited file that feeds the map (usually as a research-type wayfinder ticket); research feeds the thinking, it does not replace the flow.

## Vocabulary layers (pull in, do not skip to)

- `/domain-modeling` - when the project's terms are fuzzy or overloaded; keeps `CONTEXT.md` a clean glossary and records ADRs.
- `/codebase-design` - the deep-module vocabulary (seams, depth, interfaces) used by `/tdd` and `/improve-codebase-architecture`.

## Exports

- This repository: enforced via `.cursor/rules/program-workflow.mdc`, generated from this page by `scripts/sync-rules.py` (Agent-Requested; the body loads when a major program or task discussion begins). Do not edit the `.mdc` by hand.
- Ships to consumer repos through the template manifest, so every employee repo inherits the same workflow.
