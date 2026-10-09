# US-023 · Vehicle detail

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Must | P1 | M | To do |

- **Depends on:** [US-022](US-022-add-a-vehicle.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to see a vehicle's current condition, status and history, so that I know what state it is in before a handover.

## Acceptance criteria

- [ ] The screen shows the vehicle's identity (plate, model, colour, fuel type), current km and fuel level, and status.
- [ ] It shows the current reference photo set (date and author) in a full-screen, swipeable viewer.
- [ ] It shows open damages (photos, comment, date found, contract) and, collapsed, repaired ones.
- [ ] If the vehicle is rented, the active contract appears: renter, departure, planned return.
- [ ] History lists past contracts (number, renter, dates) and maintenance records, newest first.
- [ ] Actions depend on the status:
  - available: « Départ », « Mettre en maintenance », « Modifier », « Archiver »;
  - rented: « Retour », « Prolonger / modifier », « Modifier »;
  - in maintenance: « Terminer la maintenance », « Modifier », « Archiver »;
  - archived: « Restaurer ».

  What « Modifier » allows is in [US-024](US-024-edit-a-vehicle.md).
