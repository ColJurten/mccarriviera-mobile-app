# US-062 · Void a signed contract

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E6 · Active rentals | Could | P4 | S | To do |

- **Depends on:** [US-054](US-054-client-signs-the-depart.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-12 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to cancel a contract signed by mistake before the car leaves, so that the vehicle becomes available again without deleting anything.

## Acceptance criteria

- [ ] Only an active contract with no Retour can be voided, and a reason is required (default for R-12).
- [ ] The contract becomes `void`. It is kept, never deleted. The vehicle returns to `available`, and the event is audited.
- [ ] Any PDF generated for a voided contract carries an « ANNULÉ / VOID » watermark.
