# Contributing

## Repository layout

- `.cursor/` - Cursor rules and repository-specific AI guidance.
- `docs/` - Notes, decisions, references, and design documents.
- `src/` - Implementation code when a concrete project is added.
- `tests/` - Automated tests that match the code in `src/`.
- `scripts/` - Small repository automation scripts.

## Change expectations

1. Keep changes scoped to the idea or task at hand.
2. Document new setup steps, commands, and conventions.
3. Run `bash scripts/check-repo.sh` before opening a pull request.
4. Avoid committing secrets, generated artifacts, dependency caches, or local editor files.
