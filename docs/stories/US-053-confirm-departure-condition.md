# US-053 · Confirm the departure condition

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-050](US-050-start-a-depart.md) · [US-026](US-026-guided-reference-photo-capture.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0014](../adr/0014-file-storage.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to confirm km, fuel and condition against the reference photos, and add photos only if something changed, so that the Départ is fast but accurate.

## Acceptance criteria

- [ ] Km out and fuel out are pre-filled and can be adjusted. Fuel uses an eighths gauge from E to F. If km out is lower than the vehicle's last recorded km, a reason is required.
- [ ] The current reference photos and open damages are shown, read-only, with their dates.
- [ ] Staff can add extra photos with a comment when something looks different (B-09), from the camera or the photo library. Library photos are flagged « importée ».
- [ ] The app offers one dashboard photo showing km and fuel. It is optional (F-10).
- [ ] An optional free-text comment can be added.
- [ ] The departure condition is saved as references to the reference set and open damages at that moment, so later changes don't alter it.
