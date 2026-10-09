# ADR-0004: Use Supabase in the EU as the backend, starting on the Free plan

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-03, B-11 · follow-ups F-02, F-07 |

## Context

- Both phones share one set of data: vehicles, clients, contracts and their revisions, inspections, photos, damage and maintenance (brief).
- The data is relational and needs integrity rules. For example, a vehicle has at most one active contract, and signed revisions never change.
- The files are sensitive (ID documents, licences, signatures, contracts) and must never be public.
- Hosting must be as cheap as possible, and the developer maintains it alone (B-11).
- There is no offline mode ([ADR-0005](0005-online-only.md)).
- Client data should stay in the EU (GDPR).

## Decision

- Use **Supabase** in an **EU region** (Paris or Frankfurt). The organisation belongs to the company, and the developer is a member (default for F-02). It provides:
  - **Postgres** for all business data, with row-level security (RLS) on every table;
  - **Supabase Auth** for staff accounts ([ADR-0012](0012-authentication-and-authorisation.md));
  - **Supabase Storage** with private buckets only ([ADR-0014](0014-file-storage.md)).
- **State changes** are Postgres functions called over RPC, each running in one transaction: sign a Départ, close a Retour, amend, void, start or finish a maintenance. The app can't write status columns directly ([ADR-0007](0007-contract-lifecycle-and-audit.md)).
- Edge Functions are used only when something can't run in the database.
- **No e-mail is sent in the MVP.** Supabase's built-in e-mail only reaches the project's team members, with a low hourly limit. The developer handles password resets and invitations ([US-010](../stories/US-010-sign-in-and-sign-out.md)).
- **Projects:** start on the **Free plan** with two projects, `staging` and `production`. The local Supabase stack (CLI, in Docker on WSL2) is used for migrations and database tests.
- **Schema changes** are SQL migrations in the repository, applied by CI ([ADR-0016](0016-repository-environments-ci.md)). The app uses types generated from the schema.
- **Backups:** the Free plan has none, so a nightly encrypted off-site backup runs instead ([ADR-0015](0015-backups.md)).
- **Upgrade to Pro** (from $25/month: daily backups, 8 GB database, more storage and egress, no pausing) when any of these happens:
  - file storage passes 70 % of 1 GB;
  - the database passes 70 % of 500 MB;
  - egress passes 70 % of 5 GB in a month;
  - the project is paused;
  - the client wants managed backups.

  File storage (photos, documents, PDFs) will hit its limit first, after roughly 200 rentals (estimate below), so the client should plan for this cost (F-07).

**Free plan limits (2026):** 500 MB database, 1 GB file storage, 5 GB egress a month, 50,000 monthly active users, 2 free projects, paused after a week of inactivity, no backups.

**What fills the storage** (`ASSUMPTION`: typical sizes, to be measured during the pilot):

- The database holds text (clients, contracts, revisions, audit trail). It stays small for years.
- The files grow:
  - about 0.3 MB per photo, so about 2.5 MB per vehicle reference set;
  - 1–3 MB per contract PDF;
  - about 0.5 MB per scanned client document.
- That's roughly 5 MB per rental, so the free 1 GB holds about 200 rentals.

**When the files outgrow the Free plan** (F-07):

- **Supabase Pro** (recommended): $25/month per project, with 100 GB of files, 8 GB of database, 250 GB of egress, daily backups kept 7 days, and no pausing. Only the production project needs it.
- **Cheaper storage for the files**, for example Cloudflare R2 (10 GB free): the app would need its own code for access control and signed links. That's more work and more risk, so it isn't the default.

## Consequences

**Positive**

- €0 to start.
- Managed Postgres, auth and storage, with TLS and encryption at rest.
- Access rules are enforced in the database, not only in the app.
- SQL fits the relational model, and Postgres is familiar ground.

**Negative / risks**

- A Free project pauses after a week without activity (for example in a quiet season). The nightly backup connection probably counts as activity, but that isn't guaranteed. Watch for Supabase's pause e-mails, and restore the project from the dashboard if it happens.
- Both Free projects are taken by staging and production, so there is no spare project for experiments or restore tests ([ADR-0015](0015-backups.md) restores locally).
- The 1 GB storage limit will be reached. Agree the upgrade cost with the client in advance (F-07).
- Vendor dependency, limited because Postgres (pg_dump) and S3-compatible storage are portable.
- Supabase processes client personal data on the company's behalf, so a data processing agreement is needed (L-03).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Firebase (Firestore, Auth, Storage) | A document database fits integrity rules and revisions poorly, and Storage requires the pay-as-you-go plan |
| Self-hosted on a small VPS (Postgres + API or PocketBase + object storage), about €5/month | Lowest fixed cost, but patching, TLS, backups and monitoring for ID documents all fall on one part-time maintainer. Possible later |
| Custom API (Node or Go) + managed Postgres | More code to write and run, with no benefit at this size |
| Cloudflare Workers + D1 + R2 | Very cheap storage, but authentication and authorisation would have to be built by hand |
| Database-only serverless Postgres (e.g. Neon) | Provides the database only; auth and file storage would still be needed |

## Revisit when

An upgrade trigger fires (move to Pro), or the client wants the data on infrastructure it controls.

## Changes

- 2026-10-09: storage estimate and the cheaper alternative added, to help answer F-07.

## Implemented by

- [US-004](../stories/US-004-supabase-environments.md): Create the Supabase environments
- [US-006](../stories/US-006-core-database-schema-and-rls.md): Create the core database schema, access rules and storage
- [US-057](../stories/US-057-sign-departure-server-function.md): Server function: sign a Départ
- [US-093](../stories/US-093-operations-runbook.md): Write the operations runbook
