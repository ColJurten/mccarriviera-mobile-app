# US-061 · Extend a rental or amend allowed fields

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E6 · Active rentals | Must | P4 | M | To do |

- **Depends on:** [US-060](US-060-active-rentals.md) · [US-007](US-007-audit-trail-and-immutability.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md) · [ADR-0009](../adr/0009-signatures.md)
- **Open points:** R-11 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to extend a rental or correct the terms that may change, without touching what was signed, so that the contract stays accurate and traceable.

## Acceptance criteria

- [ ] « Prolonger / modifier » creates a new revision from the current one.
- [ ] Fields that can change (default for R-11): planned return date and time, return place, additional driver, km included, « Conditions & tarifs », pricing lines, intermediary.
- [ ] Fields that stay locked: renter, vehicle, departure date and time, and the departure km, fuel and condition.
- [ ] A reason is required, for example « Prolongation demandée par téléphone le … ».
- [ ] If the client is present, they sign the amendment on the pad. If not, staff confirm « sans signature du client » (default for R-11).
- [ ] Earlier revisions stay readable. The contract screen shows the revision history: who, when, why, and what changed.
- [ ] One server function saves the amendment. It accepts it only for an active contract whose latest revision number matches what the staff member was editing, so two people can't overwrite each other.
- [ ] After saving, the amendment PDF is generated ([US-064](US-064-amendment-pages-in-the-pdf.md)).

## Notes

- The terms say an extension must be requested at least 48 hours ahead (CGV Art. 8). The app only records it; it doesn't enforce the rule (R-11 Q5 is open).
