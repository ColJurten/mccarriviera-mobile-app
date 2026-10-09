# US-008 · Run nightly encrypted backups and test a restore

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P6 | M | To do |

- **Depends on:** [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0015](../adr/0015-backups.md)
- **Open points:** L-07 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want an encrypted off-site copy of the database and files every night, so that contracts and photos survive an incident even on the free plan.

## Acceptance criteria

- [ ] A nightly GitHub Actions workflow runs in a protected `backup` environment.
- [ ] The database is dumped with the Supabase CLI's documented commands (roles, schema, data) through the session pooler, because GitHub's runners only have IPv4 and the direct database address is IPv6.
- [ ] The dump includes the `auth` schema. Its row counts per table match production, otherwise the job fails. This catches a dump made by a role subject to RLS, which fails or comes out empty. Which role is used (`postgres`, or a read-only role with BYPASSRLS) is recorded in the runbook.
- [ ] Dumps are encrypted with `age` and uploaded to `db/daily/`, and on the 1st of the month also to `db/monthly/`. The provider's lifecycle rules delete them after 30 days and 12 months. These periods are `RECOMMENDED`; L-07 may change them.
- [ ] Files are copied incrementally with `rclone copy` to an rclone `crypt` remote under `files/`. Each file is copied once, and nothing is deleted.
- [ ] The backup bucket is EU-located, held by the developer (F-02), and with a different provider from the one holding the files. The CI key for it can write and list, but not delete.
- [ ] The Supabase S3 keys and the database credential live only in the protected environment, and are documented as full-access credentials.
- [ ] The `age` private key and the crypt password are stored offline by the developer. The company keeps a sealed copy, so it can restore without him by following the runbook (US-093).
- [ ] A failed run sends an alert, and a weekly check confirms the latest dump exists.
- [ ] Before the pilot, the latest backup is restored into the local Supabase stack on the developer's encrypted disk. Counts are compared with production, the time is recorded, and the restored copy is wiped. Staging is never used for this.
- [ ] After a month of nightly runs, Supabase egress is checked against the Free plan's 5 GB.

## Notes

- This must be in place before any real client data enters production (before US-090 and US-091).
