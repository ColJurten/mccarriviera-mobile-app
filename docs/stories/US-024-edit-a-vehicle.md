# US-024 · Edit vehicle information

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Must | P1 | S | To do |

- **Depends on:** [US-023](US-023-vehicle-detail.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to correct a vehicle's details, so that the next contracts are right, without changing contracts already signed.

## Acceptance criteria

- [ ] Plate, model, colour, fuel type and notes can be edited in any status.
- [ ] Current km and fuel level can be edited only when the vehicle isn't rented, since the Retour normally updates them.
- [ ] Signed contracts keep the vehicle values printed at signature (snapshot). Editing the vehicle never changes them.
- [ ] Every edit is recorded in the audit trail.
