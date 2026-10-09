# US-080 · Put a vehicle into maintenance

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E8 · Maintenance | Must | P5 | S | To do |

- **Depends on:** [US-023](US-023-vehicle-detail.md) · [US-074](US-074-client-signs-the-retour.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-14 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to put a car into maintenance with the reason, so that it can't be rented until it's ready.

## Acceptance criteria

- [ ] Only an available vehicle can go into maintenance. A rented vehicle goes through the Retour first.
- [ ] Staff choose a kind (default for R-14): « Entretien courant », « Réparation de dégâts » (selecting the open damages being repaired) or « Autre ».
- [ ] They add a description. The start date defaults to today, and the odometer is optional (default for R-14).
- [ ] A server function sets the status to `maintenance`, and the vehicle disappears from the Départ list.
- [ ] After a Retour that recorded new damage, the Retour summary offers « Mettre en maintenance », with those damages preselected for repair.
- [ ] The change is recorded in the audit trail.
