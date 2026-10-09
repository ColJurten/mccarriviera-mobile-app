# US-007 · Record an audit trail and protect signed data

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | M | To do |

- **Depends on:** [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md) · [ADR-0012](../adr/0012-authentication-and-authorisation.md)
- **Open points:** L-03 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want every change to business data recorded with who and when, and signed data impossible to modify, so that contracts stay trustworthy and disputes can be investigated.

## Acceptance criteria

- [ ] Triggers on business tables add a row to `audit_events` with the server time, the actor (`auth.uid()`), the action, the table, the row ID, and the values before and after (JSON).
- [ ] The tables protected in US-006 reject UPDATE and DELETE from the app, and status columns change only through server functions. Tests prove it.
- [ ] Audit rows hold references to files, never the files themselves.
- [ ] The runbook has SQL snippets to see the audit trail of a contract, a vehicle or a client.
- [ ] All audit and signature timestamps come from the server, not from the phone's clock.
- [ ] Audit rows contain personal values (before and after). Their anonymisation follows the retention procedure ([US-094](US-094-retention-and-erasure.md)).
