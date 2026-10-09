# US-063 · Re-open, re-share or regenerate a contract PDF

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E6 · Active rentals | Should | P4 | S | To do |

- **Depends on:** [US-042](US-042-archive-and-share-pdfs.md) · [US-055](US-055-departure-pdf.md)
- **Decisions:** [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0011](../adr/0011-localisation.md)
- **Open points:** R-17 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to send a contract again, or in the other language, so that I can answer a client's request later.

## Acceptance criteria

- [ ] A contract screen lists its archived PDFs (stage, language, date). Any of them can be opened and shared.
- [ ] « Générer en English / Français » renders the same revision in the other language. It uses the same template version and the terms version of that language in force at signature (default for R-17).
- [ ] If no terms version existed in that language at signature, the regeneration is refused with an explanation.
- [ ] The new file has the same content but its own bytes and hash. It is archived as a new document, and the original stays the reference.
