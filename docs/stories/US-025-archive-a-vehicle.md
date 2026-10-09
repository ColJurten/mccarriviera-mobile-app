# US-025 · Archive and restore a vehicle

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Should | P1 | S | To do |

- **Depends on:** [US-023](US-023-vehicle-detail.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-13 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to archive a sold or retired vehicle, so that it leaves the daily lists while its history stays.

## Acceptance criteria

- [ ] Only an available vehicle, or one in maintenance, can be archived. A rented vehicle can't.
- [ ] Archived vehicles are hidden by default, visible with the « Archivé » filter, and can't be chosen for a Départ.
- [ ] Nothing is deleted. « Restaurer » makes an archived vehicle available again.
