# ADR-0015: Nightly encrypted off-site backups: database dumps plus incremental file copies

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-11 · F-02 (answered) · defaults for L-03, L-07 |

## Context

- The Free plan has no backups ([ADR-0004](0004-backend-supabase.md)).
- Contracts, signatures and photos are evidence the company may need years later (retention: L-07).
- Hosting must be as cheap as possible (B-11).
- The Free plan allows 5 GB of egress a month, so copying every file every night would exceed it.
- Every table has RLS: `pg_dump` run by a role subject to RLS fails, or dumps empty tables.
- GitHub's runners only have IPv4, and Supabase's direct database address is IPv6.
- Supabase's S3 access keys give full access to every bucket and bypass storage policies.

## Decision

- **A nightly GitHub Actions workflow**, in a protected `backup` environment:
  1. **Dump the database** with the Supabase CLI's documented commands (`supabase db dump`: roles, schema, data), through the **session pooler**.
     - The dump includes the `auth` schema, because business rows reference staff accounts.
     - It connects as the `postgres` role, which bypasses RLS. A dedicated read-only role with BYPASSRLS is used instead if it can read every schema needed. [US-008](../stories/US-008-nightly-encrypted-backups.md) records which.
  2. **Check the dump:** row counts per table are compared with production, and the job fails if they don't match. This catches an empty dump.
  3. **Encrypt and store the dump:** encrypted with `age` (only the public key is in CI) and uploaded to `db/daily/`. On the 1st of the month it also goes to `db/monthly/`.
  4. **Copy files incrementally:** `rclone copy` to an rclone `crypt` remote (contents and names encrypted), under `files/`.
     - Files are never modified after upload ([ADR-0007](0007-contract-lifecycle-and-audit.md)), so each file is copied once.
     - The job never deletes anything.
- **Where:** an EU-located, S3-compatible bucket, held by the developer (F-02), with a different provider from the one holding the files. Examples: Backblaze B2 in an EU region, or Cloudflare R2 with EU jurisdiction.
  - Their free tiers (about 10 GB) last a long time, since each file is stored once.
  - Beyond that, it costs a few euros a month.
- **Retention** (`RECOMMENDED`; L-07 may change it):
  - The provider's lifecycle rules delete daily dumps after 30 days and monthly dumps after 12 months.
  - File copies are kept until the retention procedure removes them ([US-094](../stories/US-094-retention-and-erasure.md)).
- **Credentials:**
  - The Supabase S3 keys and the database credential give full access. They live only in the protected CI environment, are treated like the service-role key, and are rotated if exposed.
  - The CI key for the backup bucket can write and list, but **not delete**. A leaked CI secret therefore can't destroy backups, and retention is left to the lifecycle rules.
  - The `age` private key and the rclone crypt password are kept offline by the developer (password manager), with a sealed copy for the company. Losing them means losing the backups. With that copy and the runbook's restore procedure, the company can restore without the developer.
- **Egress:** a few MB of dump per night, plus each new file once. This stays well within 5 GB a month.
- **Monitoring:** the workflow alerts on failure, and a weekly check confirms the latest dump exists.
- **Restore test:** before the pilot, then every quarter.
  - Restore the latest backup into a throwaway environment: the local Supabase stack, on the developer's encrypted disk.
  - Compare row and file counts with production, record how long it took, then wipe it.
  - Never restore into staging, which holds synthetic data only.
- **After a move to Pro:** keep this off-site copy alongside Supabase's own backups.

## Consequences

**Positive**

- Costs €0 at this size.
- An off-site copy that doesn't depend on Supabase.
- Backups can't be deleted with the CI's credentials.

**Negative / risks**

- The developer is responsible for the job and the keys.
- CI holds full-access credentials for production data. This is mitigated by the protected environment, and by a backup bucket the CI can't delete from.
- Erasure must also remove files from the backup ([US-094](../stories/US-094-retention-and-erasure.md)).
- The nightly connection probably also counts as activity for Supabase's pause rule, but that isn't guaranteed.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Supabase Pro managed backups (from $25/month) | The planned upgrade; not needed on day one |
| A full copy of every file each night | Exceeds the Free plan's egress and the backup storage's free tier |
| `pg_dump` with a plain read-only role | Fails, or dumps empty tables, because of RLS |
| No backups | Unacceptable for signed contracts |

## Revisit when

The project moves to Pro, or retention rules (L-07) change.

## Changes

- 2026-10-09: F-02 answered: the backup bucket is held by the developer; it must be with a different provider from the files.

## Implemented by

- [US-008](../stories/US-008-nightly-encrypted-backups.md): Run nightly encrypted backups and test a restore
- [US-092](../stories/US-092-legal-and-privacy-checklist.md): Send the legal and privacy questions, and close them before go-live
- [US-093](../stories/US-093-operations-runbook.md): Write the operations runbook
- [US-094](../stories/US-094-retention-and-erasure.md): Apply retention and erasure rules
