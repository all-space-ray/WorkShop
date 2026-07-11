---
type: source
created: 2026-07-10
updated: 2026-07-10
tags: [rules, coding-standards, fastapi, react, vite, typescript, docker-compose, security]
sources: [../../../raw/rules/2026-07-10-fastapi-react-vite-monorepo-rules.md]
---

# Source: FastAPI React Vite Monorepo Rules

Owner-supplied coding-standards ruleset, ingested via `/ingest-resource`. Origin:
[raw copy](../../../raw/rules/2026-07-10-fastapi-react-vite-monorepo-rules.md). Delivered as
a Cursor `.mdc`-style rule file (`alwaysApply: true`).

## TL;DR

A universal ruleset for FastAPI + SQLAlchemy backends paired with React + Vite + TypeScript
frontends deployed via Docker Compose. It codifies a thin-handlers / service-layer
architecture, server-side authorization as the only real security boundary, migration and
audit discipline, centralized frontend API access with React Query, and a verification gate
(tests, typecheck, lint) before any work is called done.

## Key points

- **Architecture:** clear top-level areas (`apps/api`, `apps/web`, `infra`, `scripts`, `docs`); business logic lives in services/hooks/utilities, not in route or event handlers; reuse existing patterns and project-specific names.
- **Backend:** FastAPI dependencies for sessions/users/permissions; Pydantic validation; SQLAlchemy 2 style; Alembic discipline (real downgrades, SQLite-safe batch ops); no dev auth, default secrets, permissive CORS, or debug settings in production.
- **Authorization:** every sensitive read/mutation enforced server-side; frontend checks are UX only; mutating paths emit audit events unless a documented exception applies.
- **Frontend:** centralized API client/fetch wrapper; React Query for server state with query-key invalidation after mutations; folder roles (`components`, `pages`, `hooks`, `lib`, `types`); prefer generated OpenAPI TS contracts once the API is stable; preserve accessibility.
- **Security:** OIDC in production; guarded dev-only auth; secrets never in git; no open redirects (safe relative return paths only); HTTPS-only cookies with SameSite; rate limits, upload size limits, and security headers on sensitive endpoints.
- **Data/integration:** treat the DB schema as a contract updated across migrations/models/schemas/tests/types together; explicit integration boundaries with timeouts, health checks, and tests; repeatable scripts over hand-edited data; documented retention/encryption/access for backups and exports.
- **Deployment:** Compose services internal behind a reverse proxy; `alembic upgrade head` before Uvicorn; bind `0.0.0.0:$PORT`; secrets in gitignored `.env`/platform stores; liveness/readiness checks; documented proxy routes and SPA fallback; `set -euo pipefail` scripts.
- **Verification:** run focused tests, then the root test command (e.g. `./scripts/test.sh`) for broad changes; frontend typecheck+lint and backend tests+lint; verify regenerated artifacts open/parse; document behavior changes in `docs`.

## Relevance to existing knowledge

First topic page in the [rules](../README.md) section beyond universal
[writing style](../writing-style.md). Distilled into the enforced rules page
[FastAPI React Vite monorepo](../fastapi-react-vite-monorepo.md). The deployment rule to
bind `0.0.0.0:$PORT` agrees with this repository's Render platform rule, so no
contradiction.
