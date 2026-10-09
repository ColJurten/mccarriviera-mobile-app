# US-070 · Start a Retour

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E7 · Retour | Must | P4 | S | To do |

- **Depends on:** [US-060](US-060-active-rentals.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-05 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to pick the rented car and see its departure information, so that I can check it in against what was signed.

## Acceptance criteria

- [ ] Start from « Retour » by choosing an active rental (US-060), or from the vehicle's detail screen.
- [ ] The Retour screen shows: contract number, renter, departure date and time, planned return (as last amended), km out, fuel out, reference photos, damages open at departure, and any extra departure photos.
- [ ] The return date and time default to now and can be edited (default for R-05).
- [ ] A Retour in progress is saved on the server as it is entered, so it can be finished later. Until the client signs, the vehicle shows « Retour en attente de signature » and stays « En cours » (F-04; `RECOMMENDED`).
- [ ] `docs/user-flows.md` gets the Retour flow diagram (Mermaid).
