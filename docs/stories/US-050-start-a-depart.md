# US-050 · Start a Départ by choosing an available vehicle

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-020](US-020-home-screen.md) · [US-022](US-022-add-a-vehicle.md) · [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md) · [ADR-0005](../adr/0005-online-only.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to start a Départ from an available vehicle and have its data pre-filled, so that I don't retype what the app already knows.

## Acceptance criteria

- [ ] « Départ » lists only vehicles that are available and have a reference photo set. Search works as in US-021.
- [ ] Choosing a vehicle creates a draft contract on the server and pre-fills (brief, step 1):
  - plate, colour, model, fuel type;
  - km out (= current km) and fuel out (= current fuel level);
  - the current reference photos and the open damages.
- [ ] If someone else already has a draft on the same vehicle, a warning says so. Only one Départ can be signed per vehicle at a time (database rule, [US-057](US-057-sign-departure-server-function.md)).
- [ ] « Départ » on a vehicle's detail screen skips straight to choosing the client, with that vehicle.
- [ ] A draft can be resumed or discarded ([US-056](US-056-resume-or-discard-a-draft.md)).
- [ ] The Départ sequence diagram in `docs/architecture/` matches the flow as built.
