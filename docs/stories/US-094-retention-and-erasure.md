# US-094 · Apply retention and erasure rules

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E9 · Go-live | Must | P6 | M | To do |

- **Depends on:** [US-092](US-092-legal-and-privacy-checklist.md) · [US-007](US-007-audit-trail-and-immutability.md) · [US-008](US-008-nightly-encrypted-backups.md)
- **Decisions:** [ADR-0014](../adr/0014-file-storage.md) · [ADR-0015](../adr/0015-backups.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** L-03, L-07 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want a tested way to delete or anonymise a client's data when the law requires it, so that we can honour retention periods and data-protection requests.

## Acceptance criteria

- [ ] Until L-03 and L-07 are answered, nothing is deleted or anonymised (default for L-03 and L-07). This procedure implements their answers.
- [ ] A server-side procedure, run by the developer and never from the app, can:
  - delete a client's document files;
  - anonymise the client record;
  - anonymise the personal values kept in contract snapshots and audit rows, for contracts whose retention period has ended.

  It writes an audit event that doesn't contain the erased values.
- [ ] Files it deletes are also deleted from the backup's `files/` area, using the developer's admin key (the CI key can't delete). Database dumps that still contain the data expire through rotation ([ADR-0015](../adr/0015-backups.md)).
- [ ] An erasure log records what was erased and when, without the erased values, so that a restore from an older backup can re-apply the erasures.
- [ ] It is tested on staging with synthetic data, including a contract that is still within its retention period and must be kept.

## Notes

- When contracts must be kept for a period and the client asks for erasure, L-03 and L-07 decide which wins.
