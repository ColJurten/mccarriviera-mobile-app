# US-082 · Finish a damage repair and refresh the reference photos

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E8 · Maintenance | Must | P5 | M | To do |

- **Depends on:** [US-080](US-080-put-a-vehicle-into-maintenance.md) · [US-026](US-026-guided-reference-photo-capture.md) · [US-072](US-072-return-inspection.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-14 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to close a repair by marking the repaired damages and taking a new reference set, so that future rentals start from the repaired condition.

## Acceptance criteria

- [ ] Staff confirm which of the selected damages were actually repaired. Partial repairs are allowed (default for R-14).
- [ ] Repaired damages become `repaired`, with the maintenance record and the date. The others stay open.
- [ ] A new complete reference photo set is required before the vehicle can return to `available` (brief).
- [ ] The old reference set, and the damage records with their photos, stay in the history.
- [ ] The change is recorded in the audit trail.
