# US-064 · Amendment pages in the PDF

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E6 · Active rentals | Must | P4 | M | To do |

- **Depends on:** [US-061](US-061-extend-or-amend-a-rental.md) · [US-040](US-040-contract-pdf-template.md) · [US-042](US-042-archive-and-share-pdfs.md)
- **Decisions:** [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0009](../adr/0009-signatures.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** F-08 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want each amendment printed on its own page with its own signature status, so that the contract shows what changed without putting the client's departure signature next to values they didn't sign.

## Acceptance criteria

- [ ] Each amendment gets its own block on the amendment pages: every change as old → new, the reason, the date and time, and the amendment signature or « Sans signature du client ».
- [ ] Page 1 keeps the contract as signed at the Départ. The amendment pages are where the current values are read (default for F-08).
- [ ] At the bottom right, amendment pages carry the amendment's own signature (or « Sans signature du client »), not the departure signature (default for F-08).
- [ ] An amendment PDF (stage `amendment`) is generated, archived and shared like the others ([US-042](US-042-archive-and-share-pdfs.md)). The final PDF includes every amendment.
