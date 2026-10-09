# US-091 · Pilot with the two staff members

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E9 · Go-live | Must | P6 | M | To do |

- **Depends on:** [US-008](US-008-nightly-encrypted-backups.md) · [US-092](US-092-legal-and-privacy-checklist.md) · [US-093](US-093-operations-runbook.md) · [US-094](US-094-retention-and-erasure.md)
- **Decisions:** [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md)
- **Open points:** F-07 (see [open questions](../discovery/open-questions.md))

## Story

As the company, we want to run real handovers on the staff phones, with paper as a fallback, so that we find problems before dropping the paper form.

## Acceptance criteria

- [ ] Every Must story of phases P0 to P5 is done, and so are US-008, US-092, US-093 and US-094.
- [ ] The hosting budget for after the Free plan is agreed (F-07).
- [ ] Both staff phones have the production build installed (Developer Mode on) and their own accounts.
- [ ] A written test script covers:
  - adding a vehicle;
  - creating a client with documents;
  - a Départ with French and English PDFs;
  - an extension;
  - a Retour with RAS;
  - a Retour with new damage;
  - maintenance, repair and a new reference set;
  - revoking a lost phone.
- [ ] During the pilot (2 weeks, `RECOMMENDED`), each handover is also done on paper, and every difference is logged as an issue.
- [ ] The go/no-go decision is recorded with the client.
