# US-026 · Guided reference photo capture

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Must | P1 | M | To do |

- **Depends on:** [US-005](US-005-eas-builds-and-internal-distribution.md) · [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md) · [ADR-0014](../adr/0014-file-storage.md) · [ADR-0005](../adr/0005-online-only.md)
- **Open points:** B-09 Q1 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want the app to guide me through the standard photo angles, so that every reference set is complete and comparable.

## Acceptance criteria

- [ ] The capture screen walks through the 8 exterior angles, with a hint for each: front, front-left, left, rear-left, rear, rear-right, right, front-right (default for B-09 Q1). The list is configurable in code.
- [ ] An interior photo can be added to the set, but it isn't required (F-10).
- [ ] There is no dashboard photo in the set, because it would show an old odometer reading at every later Départ.
- [ ] Reference photos come from the in-app camera only (`RECOMMENDED`), so each set is consistent and dated.
- [ ] Each photo can be retaken before saving. The set is saved only when every exterior angle has a photo.
- [ ] Photos are resized (1600 px on the long edge, JPEG about 0.7), stripped of location metadata, and uploaded to `condition-photos`.
- [ ] Uploads retry automatically while the app is open ([ADR-0005](../adr/0005-online-only.md)).
- [ ] Once every upload has succeeded, one server function creates the set and its photo rows (angle, size, SHA-256, author, time). They can't be changed afterwards.
- [ ] A new set replaces the previous one as current. The old set stays in the history and is never deleted.

## Notes

- Used when adding a vehicle (US-022), after a damage repair (US-082), and optionally after routine maintenance (US-081).
