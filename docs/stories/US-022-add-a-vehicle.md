# US-022 · Add a vehicle with its reference photos

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Must | P1 | M | To do |

- **Depends on:** [US-020](US-020-home-screen.md) · [US-026](US-026-guided-reference-photo-capture.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0014](../adr/0014-file-storage.md)
- **Open points:** N-02 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to add a vehicle with the information the contract needs and its reference photos, so that future Départs are pre-filled.

## Acceptance criteria

- [ ] Fields from the current contract:
  - plate (required, unique);
  - make and model (required);
  - colour;
  - fuel type (unleaded 95 by default; other values can be added);
  - current km (required, a whole number ≥ 0);
  - current fuel level (required, in eighths from 0 to 8);
  - notes.

  No other vehicle fields are added for now (default for N-02).
- [ ] The plate is stored in capitals, as typed. No format is enforced, because French plates in current and older formats, Monaco plates and foreign plates all exist. Uniqueness ignores spaces and dashes.
- [ ] A vehicle without a reference photo set can't be chosen for a Départ, and shows « Photos de référence manquantes ».
- [ ] The reference set is captured with the guided capture ([US-026](US-026-guided-reference-photo-capture.md)), right after creation or later.
- [ ] A duplicate plate is rejected with a clear message.
- [ ] The creation is recorded in the audit trail.
