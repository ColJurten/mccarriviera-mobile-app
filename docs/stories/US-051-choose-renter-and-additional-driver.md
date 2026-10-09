# US-051 · Choose the renter and the additional driver

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-050](US-050-start-a-depart.md) · [US-030](US-030-find-and-select-a-client.md) · [US-031](US-031-create-a-client.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** R-03, R-04 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to select or create the renter and, if needed, an additional driver, so that both appear on the contract.

## Acceptance criteria

- [ ] Renter: select an existing client or create one inline (US-030, US-031), then come back to the Départ.
- [ ] Additional driver: optional, one in the MVP. Select or create a client.
- [ ] If an additional driver is added, their name, date of birth and licence number are mandatory before signing. These are the fields the current form has (default for R-03).
- [ ] Missing mandatory fields (list in US-031) appear as a checklist that opens the client form.
- [ ] The renter's age is displayed, with no warning or blocking (default for R-04).
