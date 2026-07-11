---
type: concept
created: 2026-07-10
updated: 2026-07-10
tags: [rules, coding-standards, fastapi, sqlalchemy, react, vite, typescript, docker-compose, security]
sources: [../../raw/rules/2026-07-10-fastapi-react-vite-monorepo-rules.md]
description: Enforced standards for FastAPI + SQLAlchemy backends with React + Vite + TypeScript frontends deployed via Docker Compose (thin handlers, server-side authz, migration/audit discipline, verification gate).
globs: apps/api/**, apps/web/**, **/*.py, **/*.ts, **/*.tsx, **/*.jsx, docker-compose*.yml, docker-compose*.yaml, **/alembic/**, infra/**
---

# FastAPI React Vite monorepo rules (enforced)

Enforced coding standards for projects that pair a FastAPI + SQLAlchemy backend with a
React + Vite + TypeScript frontend, deployed via Docker Compose. These are rules, not
suggestions. Numbered so they can be cited precisely (e.g. "AR-3", "SEC-2"). Source:
[FastAPI React Vite Monorepo Rules](sources/2026-07-10-fastapi-react-vite-monorepo-rules.md).

## Architecture (AR)

1. Keep backend, frontend, deployment, scripts, and documentation in clear top-level areas such as `apps/api`, `apps/web`, `infra`, `scripts`, and `docs`.
2. Follow the repository's existing route, service, model, component, hook, and utility patterns before introducing new abstractions.
3. Keep business logic out of HTTP route handlers and UI event handlers when it can live in testable services, hooks, or pure utility modules.
4. Use project-specific names, environment-variable prefixes, package names, and paths; do not copy names from another product.
5. Document architecture, security, deployment, and operational decisions under `docs` when they affect future contributors.

## Backend (BE)

1. Use FastAPI dependencies for database sessions, current users, and permissions.
2. Keep route handlers thin; place business logic in service modules and data access behind SQLAlchemy models or repositories.
3. Validate request and response shapes with Pydantic models and explicit field constraints.
4. Use SQLAlchemy 2 style and the repository's session helpers for transactions, rollback, and cleanup.
5. Follow Alembic migration discipline: explicit upgrade, real downgrade, local migration verification, and SQLite-safe batch operations when SQLite is used.
6. Production must never run with development authentication, default session secrets, permissive CORS, or debug-only settings.

## Authorization and audit (AUTH)

1. Every sensitive read and mutation enforces authorization server-side; frontend permission checks are only a user-experience layer.
2. Every mutating API path that persists user-meaningful data emits an audit event unless a documented exception applies.
3. Use OIDC or another approved identity provider in production when the app handles authenticated business data.
4. Keep development-only auth paths isolated and guarded by environment checks.

## Security (SEC)

1. Store secrets only in the deployment platform or gitignored environment files; never commit real secrets.
2. Prevent open redirects by accepting only safe relative return paths.
3. Configure production session cookies for HTTPS-only transport with an appropriate SameSite policy.
4. Add rate limiting, upload size limits, and security headers when endpoints accept auth traffic, file imports, or sensitive data.

## Frontend (FE)

1. Use a centralized API client or fetch wrapper for browser API calls so credentials, headers, errors, and development behavior stay consistent.
2. Use React Query for server state and invalidate query keys after successful mutations.
3. Use permission-aware UI helpers when available, but never treat frontend checks as security enforcement.
4. Keep reusable UI in `components`, route pages in `pages`, hooks in `hooks`, pure helpers in `lib`, and DTOs or shared types in `types`.
5. Update local TypeScript types when API response shapes change, until generated shared types exist; prefer generated OpenAPI TypeScript contracts once the API surface is stable.
6. Preserve accessible dialogs, labels, focus states, and keyboard navigation.

## Data and integration (DATA)

1. Treat the database schema as a contract; update migrations, models, API schemas, tests, and frontend types together.
2. Keep integration boundaries explicit: external services, sidecars, and import pipelines have documented URLs, timeouts, health checks, error handling, and tests.
3. Do not duplicate another service's responsibility inside the main app; call the integration through its documented interface.
4. Produce large generated or imported data with repeatable scripts, not hand edits.
5. Give backups, exports, and imported files documented retention, encryption, and access-control expectations.

## Deployment (DEP)

1. For Docker Compose deployments, keep API, web, worker, and sidecar services internal behind the public reverse proxy unless direct exposure is required.
2. API containers run `alembic upgrade head` before Uvicorn starts.
3. Bind HTTP servers to `0.0.0.0:$PORT` or the port expected by the container/proxy runtime.
4. Required secrets belong in gitignored host `.env` files or platform secret stores, never in git.
5. Preserve liveness and readiness health checks; deploy automation depends on them.
6. Keep reverse-proxy routes, SPA fallback routing, and API prefixes documented and tested.
7. Keep scripts using `set -euo pipefail` and repo-relative paths.

## Verification (VER)

1. Before claiming work is complete, run the relevant focused tests.
2. For broad changes, run the repository's root test command (e.g. `./scripts/test.sh`) when available.
3. Run frontend typecheck and lint commands for TypeScript/React changes.
4. Run backend tests and lint commands for Python/FastAPI changes.
5. Verify generated Word, PDF, OpenAPI, or other exported artifacts open or parse after regeneration.
6. Document schema, permission, audit, deployment, integration, or auth behavior changes in `docs`.

## Notes

- **Port binding (DEP-3)** matches this repository's Render platform rule (bind `0.0.0.0:$PORT`); no contradiction.
- **Universal writing rules** still apply on top of these; see [writing style](writing-style.md).

## Exports

- This repository: enforced via `.cursor/rules/fastapi-react-vite-monorepo.mdc`, generated from this page by `scripts/sync-rules.py`. It is Auto-Attached by the `globs` above, so the rule body enters context only when matching backend/frontend/deploy files are in play (zero cost otherwise), plus Agent-Requested via its `description`. Do not edit the `.mdc` by hand.
- Export into other repos' rule systems (`.cursor/rules/*.mdc`, `AGENTS.md`, `CLAUDE.md`) on request, per the [section conventions](README.md), and record the destination here.
