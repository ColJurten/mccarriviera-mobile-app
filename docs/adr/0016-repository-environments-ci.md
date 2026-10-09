# ADR-0016: One repository, three environments and an automated delivery pipeline

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | F-02 (answered) · defaults for T-04, N-06 |

## Context

- One developer builds and maintains the app with coding agents (B-11).
- The app (Expo), the database (Supabase) and the docs change together.
- Builds happen in the cloud ([ADR-0002](0002-mobile-stack-expo.md), [ADR-0003](0003-ios-distribution-ad-hoc.md)).
- Development happens on Windows with WSL2. A phone on the network can't reach services inside WSL2 by default.

## Decision

- **One repository:**
  - `app/`: the Expo app;
  - `supabase/`: migrations, seed with synthetic data, database tests, functions;
  - `docs/`: this documentation;
  - `scripts/`: backup, admin, import, erasure.
- **Agent guidance:** a root `AGENTS.md`, with `CLAUDE.md` pointing to it, tells coding agents to start from `docs/README.md` (default for N-06).
- **Git host:** a private GitHub repository on the developer's account (F-02; default for T-04). It also runs CI and the backup workflow.
- **Environments:**
  - **local:** Supabase CLI in Docker on WSL2, for migrations and database tests. The Metro bundler also runs in WSL2. The phone reaches it through WSL mirrored networking (Windows 11) or `expo start --tunnel`.
  - **development builds on the phone:** use the **staging** backend, because the phone can't reach the local stack inside WSL2.
  - **Android emulator on Windows:** runs an Android development build of the same app for day-to-day UI work, also against staging ([ADR-0018](0018-development-and-test-devices.md)).
  - **staging:** a Supabase Free project with synthetic data only, plus the EAS `preview` profile and channel.
  - **production:** a Supabase Free project, plus the EAS `production` profile and channel.
- **CI on every pull request:**
  - typecheck, lint, unit tests and the translation-key check;
  - HTML snapshot tests of the contract;
  - database tests (`supabase start`, then `supabase test db`);
  - a check that the generated types are up to date.
- **Database releases:** migrations are applied to staging when merged to `main`, and to production on a release tag, after manual approval.
- **App releases:**
  - EAS builds are triggered on purpose (the free plan includes 15 iOS builds a month);
  - JavaScript-only fixes go through EAS Update;
  - a runtime-version policy keeps an update from reaching an incompatible build.
- **Secrets:**
  - the app only gets the public URL and the anon key for each environment, through EAS environment variables;
  - the service-role key, the storage S3 keys and the backup credentials live only in protected CI environments.
- **Working style:** short-lived branches, pull requests that cite story and ADR IDs, and a protected main branch.
- **Docs written alongside the stories:** `testing.md` (US-002), `screens.md` (US-003) and `runbook.md` (US-093). The UML diagrams in `architecture/` (first version 2026-10-09) are kept up to date by US-004, US-006, US-050 and US-070.

## Consequences

**Positive**

- Changes to the app, the database and the docs are reviewed together.
- Database changes reach staging before production.
- No real data is used in development.

**Negative / risks**

- The free EAS build quota means builds must be planned.
- Development against staging needs a connection.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Separate repositories for app and backend | Overhead for one developer |
| Committing generated native folders | Harder upgrades; Expo's continuous native generation is preferred |
| Pointing development builds at the local stack | Needs network bridging into WSL2 for both the API and storage; staging is simpler |

## Revisit when

A second developer joins, or the free build quota becomes a bottleneck.

## Changes

- 2026-10-09: Android emulator added for day-to-day work (ADR-0018).
- 2026-10-09 (later): F-02 answered: the repository is on the developer's account. The UML diagrams in `architecture/` replace the planned `architecture.md`, `data-model.md` and `user-flows.md`.

## Implemented by

- [US-002](../stories/US-002-repository-and-agent-guidance.md): Set up the repository, checks and agent guidance
- [US-004](../stories/US-004-supabase-environments.md): Create the Supabase environments
- [US-005](../stories/US-005-eas-builds-and-internal-distribution.md): Set up EAS builds, internal distribution and over-the-air updates
- [US-093](../stories/US-093-operations-runbook.md): Write the operations runbook
