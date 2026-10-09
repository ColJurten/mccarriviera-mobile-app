# US-072 · Inspect the vehicle: new damage or RAS

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E7 · Retour | Must | P4 | M | To do |

- **Depends on:** [US-070](US-070-start-a-retour.md) · [US-026](US-026-guided-reference-photo-capture.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0014](../adr/0014-file-storage.md)
- **Open points:** R-10 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to record any new damage with photos and a comment, or confirm nothing is new, so that new damage stays clearly separate from damage that existed before.

## Acceptance criteria

- [ ] The screen shows the reference photos and the damages open at departure next to the camera, for comparison.
- [ ] « RAS — Rien à signaler » takes one tap. It can't be combined with new damage entries.
- [ ] « Ajouter un dégât » requires at least one photo and a short comment (default for R-10). Photos come from the camera or, as the brief allows ("take/upload"), the photo library. Library photos are flagged « importée ». Several damages can be added.
- [ ] New damages are saved as open damages on the vehicle, linked to this return. Damages that already existed are not duplicated.
- [ ] Either RAS or at least one new damage is required to continue.
- [ ] The app offers one dashboard photo showing km and fuel. It is optional (F-10).
- [ ] A general return comment is optional.
