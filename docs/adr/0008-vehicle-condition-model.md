# ADR-0008: Vehicle condition: reference photos reused at Départ, damage records, reset only after repair

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-09 · brief (Retour, maintenance) · F-10 (answered) · defaults for B-09 Q1, R-10, R-14 |

## Context

- **B-09:** reuse the vehicle's reference photos at Départ, and only take fresh photos when needed.
- **Brief (Retour, step 4):**
  - photos only, with no diagrams;
  - new damage is recorded with photos ("take/upload") and comments, otherwise « RAS »;
  - damage that existed before the rental is kept apart from new damage.
- **Brief (maintenance):** refresh the reference condition only after a damage repair, and never delete history.

## Decision

- **Reference set:** each vehicle has one **current reference photo set**, recording who took it, when, and why (initial, after repair, or manual). A new set becomes current and the old sets are kept.
- **Angles:** 8 exterior angles, all required (default for B-09 Q1): front, front-left, left, rear-left, rear, rear-right, right, front-right.
  - Interior photos are optional (F-10, answered 2026-10-09).
  - There is no dashboard photo in the reference set: reused at every later Départ, it would show an old odometer reading.
  - Reference photos come from the in-app camera only (`RECOMMENDED`), so each set is consistent and dated.
- **Dashboard photo at a handover** (km and fuel): optional at each Départ and Retour (F-10). The app offers it.
- **Damage records:** photos and a comment, a status (open or repaired), the Retour where the damage was found and the maintenance where it was repaired (default for R-10).
- **Départ:**
  - The departure condition is the current reference set plus the damage open at that moment, stored by reference.
  - Staff can add extra photos with a comment when something looks different (B-09).
- **Retour:**
  - The reference set and the open damage are shown for comparison.
  - Staff record each new damage (at least one photo and a comment) or « RAS ». Photos are needed only for new damage (brief, Retour step 4).
- **Photo sources** for extra departure photos and damage photos:
  - the in-app camera by default;
  - the photo library, since the brief says "take/upload". Library photos are flagged « importée » ([ADR-0014](0014-file-storage.md)).
- **Damage repair:**
  - Finishing a repair maintenance closes the repaired damage.
  - A new complete reference set is then required before the vehicle can be rented again.
  - Partial repairs are allowed (default for R-14).
- **Ordinary maintenance** doesn't require new photos (« Reset status ou pas »).
- Nothing is deleted.

## Consequences

**Positive**

- A fast Départ, with no photo session.
- Damage that existed before the rental and new damage stay clearly apart.

**Negative / risks**

- Reference photos can be weeks old, which is weaker evidence than dated photos of each handover. This is mitigated by:
  - extra photos and the optional dashboard photo;
  - the client's signature (by signing, the renter accepts the vehicle's condition, CGV Art. 3);
  - the damage recorded at the previous Retour.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| A fresh photo set at every Départ | Ruled out by B-09 |
| Drawings with marks | Ruled out: "only photos" |
| A dashboard photo inside the reference set | Shows a stale odometer reading at every later Départ |

## Revisit when

A damage dispute shows the reference photos are not enough evidence.

## Changes

- 2026-10-09: F-10 answered: interior and dashboard photos are optional, and the reference set has 8 required exterior angles. `INTERPRETATION`: « the inside of the car » covers both the interior angle and the dashboard photo.

## Implemented by

- [US-006](../stories/US-006-core-database-schema-and-rls.md): Create the core database schema, access rules and storage
- [US-022](../stories/US-022-add-a-vehicle.md): Add a vehicle with its reference photos
- [US-023](../stories/US-023-vehicle-detail.md): Vehicle detail
- [US-026](../stories/US-026-guided-reference-photo-capture.md): Guided reference photo capture
- [US-050](../stories/US-050-start-a-depart.md): Start a Départ by choosing an available vehicle
- [US-053](../stories/US-053-confirm-departure-condition.md): Confirm the departure condition
- [US-072](../stories/US-072-return-inspection.md): Inspect the vehicle: new damage or RAS
- [US-080](../stories/US-080-put-a-vehicle-into-maintenance.md): Put a vehicle into maintenance
- [US-081](../stories/US-081-finish-routine-maintenance.md): Finish a routine maintenance
- [US-082](../stories/US-082-finish-a-damage-repair.md): Finish a damage repair and refresh the reference photos
