# US-055 · Generate the departure PDF in French or English

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-054](US-054-client-signs-the-depart.md) · [US-040](US-040-contract-pdf-template.md) · [US-042](US-042-archive-and-share-pdfs.md)
- **Decisions:** [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0011](../adr/0011-localisation.md) · [ADR-0009](../adr/0009-signatures.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to choose French or English and get the signed contract as a PDF, so that I can give the client their copy straight away.

## Acceptance criteria

- [ ] After signing, staff choose « Français » or « English » (brief, step 5). The default is the language shown on the recap screen.
- [ ] The PDF shows the departure signature in the « Signature départ » box at the bottom right of every page. The « Signature retour » boxes and the Retour column are empty.
- [ ] The PDF is archived and the share sheet opens ([US-042](US-042-archive-and-share-pdfs.md)).
- [ ] The same contract can be generated again later in the other language ([US-063](US-063-reopen-or-regenerate-a-pdf.md)).
