---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [rules, writing, style, language]
sources: []
description: Universal writing style rules for any generated prose, comments, commit messages, or documents (no em dashes, verified quantified claims, no invented facts).
---

# Writing style rules (universal)

Language rules that apply to every piece of text an agent produces for the owner: documents, wiki pages, emails, code comments, commit messages, and chat deliverables. These are enforced rules, not suggestions. The rules below are seeded defaults from the original system; the owner edits, removes, or extends them.

## Rules

1. **No em dashes.** Use commas, colons, semicolons, parentheses, pipes, or separate sentences instead. En dashes are acceptable only inside numeric and date ranges (2019-2022). Delivery gate for documents: extract the text and verify zero em dash characters before shipping.
2. **Quantified claims must survive arithmetic.** Recompute every growth percentage, rate, and total before it ships. Prefer verifiable forms: "X to Y (Z% total, W% annualized)".
3. **Verify before you generate.** Technical claims reused in deliverables get checked against records first, and marked verified vs owner-attested. Never upgrade a list into a classification without verifying each element's category.
4. **No invented facts, no filler superlatives.** If a claim cannot be sourced to the wiki, the owner, or a verified record, it does not ship.

## Exports

- This repository: enforced via `.cursor/rules/writing-style.mdc`, generated from this page by `scripts/sync-rules.py` (Agent-Requested; the body loads on demand when producing text). Do not edit the `.mdc` by hand.
- Root `AGENTS.md` carries a pointer to this section.
- Export to other repos on request per the [section conventions](README.md).
