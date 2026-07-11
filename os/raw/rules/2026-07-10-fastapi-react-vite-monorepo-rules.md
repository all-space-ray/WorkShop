<!--
Origin: pasted by owner via /ingest-resource
Type: coding-standards ruleset (Cursor .mdc-style rule file)
Ingested: 2026-07-10
Verbatim source preserved below; do not modify.
-->

---
description: Universal rules for FastAPI, SQLAlchemy, React, Vite, TypeScript, and Docker Compose projects
alwaysApply: true
---

# FastAPI React Vite Monorepo Rules

## Architecture

- Keep backend, frontend, deployment, scripts, and documentation in clear top-level areas such as `apps/api`, `apps/web`, `infra`, `scripts`, and `docs`.
- Follow the repository's existing route, service, model, component, hook, and utility patterns before introducing new abstractions.
- Keep business logic out of HTTP route handlers and UI event handlers when it can live in testable services, hooks, or pure utility modules.
- Use project-specific names, environment variable prefixes, package names, and paths; do not copy names from another product.
- Document architecture, security, deployment, and operational decisions under `docs` when they affect future contributors.

## Backend Rules

- Use FastAPI dependencies for database sessions, current users, and permissions.
- Keep route handlers thin; place business logic in service modules and data access logic behind SQLAlchemy models or repositories.
- Validate request and response shapes with Pydantic models and explicit field constraints.
- Every sensitive read and mutation must enforce authorization server-side; frontend permission checks are only a user-experience layer.
- Every mutating API path that persists user-meaningful data should emit an audit event unless a documented exception applies.
- Use SQLAlchemy 2 style and the repository's session helpers for transactions, rollback, and cleanup.
- Follow Alembic migration discipline: explicit upgrade, real downgrade, local migration verification, and SQLite-safe batch operations when SQLite is used.
- Production must never run with development authentication, default session secrets, permissive CORS, or debug-only settings.

## Frontend Rules

- Use a centralized API client or fetch wrapper for browser API calls so credentials, headers, errors, and development behavior stay consistent.
- Use React Query for server state and invalidate query keys after successful mutations.
- Use permission-aware UI helpers when available, but never treat frontend checks as security enforcement.
- Keep reusable UI in `components`, route pages in `pages`, hooks in `hooks`, pure helpers in `lib`, and DTOs or shared types in `types`.
- Update local TypeScript types when API response shapes change until generated shared types exist.
- Prefer generated OpenAPI TypeScript contracts once the API surface is stable.
- Preserve accessible dialogs, labels, focus states, and keyboard navigation.

## Authentication and Security Rules

- Use OIDC or another approved identity provider in production when the application handles authenticated business data.
- Keep development-only auth paths isolated and guarded by environment checks.
- Store secrets only in the deployment platform or gitignored environment files; never commit real secrets.
- Prevent open redirects by accepting only safe relative return paths.
- Configure session cookies for production with HTTPS-only transport and an appropriate SameSite policy.
- Add rate limiting, upload size limits, and security headers when endpoints accept auth traffic, file imports, or sensitive data.

## Data and Integration Rules

- Treat the database schema as a contract; update migrations, models, API schemas, tests, and frontend types together.
- Keep integration boundaries explicit. External services, sidecars, and import pipelines should have documented URLs, timeouts, health checks, error handling, and tests.
- Do not duplicate another service's responsibility inside the main app; call the integration through its documented interface.
- Large generated or imported data should be produced by repeatable scripts, not hand-edited.
- Backups, exports, and imported files must have documented retention, encryption, and access-control expectations.

## Deployment Rules

- For Docker Compose deployments, keep API, web, worker, and sidecar services internal behind the public reverse proxy unless direct exposure is required.
- API containers must continue to run `alembic upgrade head` before Uvicorn starts.
- Bind HTTP servers to `0.0.0.0:$PORT` or the port expected by the container/proxy runtime.
- Required secrets belong in gitignored host `.env` files or platform secret stores, never in git.
- Preserve liveness and readiness health checks; deploy automation should depend on them.
- Keep reverse proxy routes, SPA fallback routing, and API prefixes documented and tested.
- Keep scripts using `set -euo pipefail` and repo-relative paths.

## Verification Rules

- Before claiming work is complete, run the relevant focused tests.
- For broad changes, run the repository's root test command, such as `./scripts/test.sh`, when available.
- Run frontend typecheck and lint commands for TypeScript/React changes.
- Run backend tests and lint commands for Python/FastAPI changes.
- Verify generated Word, PDF, OpenAPI, or other exported artifacts can be opened or parsed after regeneration.
- Document schema, permission, audit, deployment, integration, or auth behavior changes in `docs`.
