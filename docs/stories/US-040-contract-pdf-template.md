# US-040 · Contract PDF template in French and English, with the signature block at the bottom right

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E4 · Contract document | Must | P2 | L | To do |

- **Depends on:** [US-009](US-009-spike-signature-and-pdf-on-iphone.md) · [US-041](US-041-general-terms-per-language.md)
- **Decisions:** [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0009](../adr/0009-signatures.md) · [ADR-0011](../adr/0011-localisation.md) · [ADR-0006](../adr/0006-contract-only-scope.md)
- **Open points:** R-01, R-02, R-18, R-19, F-08, F-09 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want a contract that looks like the model template but holds every field of our current contract, in French or English, so that the PDF replaces the paper form.

## Acceptance criteria

- [ ] HTML/CSS templates are rendered to an A4 PDF with expo-print. Each generated PDF records its template version.
- [ ] The page structure follows [ADR-0010](../adr/0010-contract-pdf-generation.md) (default for R-01 and F-08):
  1. the contract as signed at the Départ;
  2. Départ / Retour: condition, return values and the « Décompte final »;
  3. general terms;
  4. amendments, if any.
- [ ] Pages are explicit A4 blocks. Sections that can grow (photos, terms, amendments) continue on extra pages. Every page repeats the header, the footer and the signature block, at the same position in French and English (B-06, B-07).
- [ ] The signature block sits at the bottom right of every page, with the « Signature départ » and « Signature retour » boxes (F-08). Amendment pages carry the amendment's own signature there instead of the departure signature (default for F-08).
- [ ] These are not printed:
  - card imprint, expiry date and CVV (default for F-09);
  - fields that exist only on the model template, apart from the contract number (default for R-02);
  - the staff member's name (default for R-19).
- [ ] The company's details (name, address, SIRET, APE code, phone numbers, logo) come from one configuration file, filled with details the client has confirmed are current.
- [ ] Empty optional fields show as blank cells, never as « null » or « undefined » (« Champ vide ✓ »).
- [ ] Every label comes from the `fr` and `en` catalogues. Switching language changes labels, fixed sentences, date and number formats and the terms, never the data.
- [ ] Photos are embedded as compressed thumbnails. A contract with 9 reference photos and 4 damage photos stays under 3 MB.
- [ ] HTML snapshot tests in CI cover synthetic cases: empty optional fields, maximum-length fields, an additional driver, 30 photos, 5 amendments, French and English. Each template change is also checked as a PDF on a real iPhone.
- [ ] The style follows the model: full-width label/value tables, shaded label cells, logo at the top right, gold/black palette (placeholders until the brand assets arrive: default for R-18).

## Notes

- The title stays « CONTRAT / FACTURE LOCATION » unless the accountant says otherwise (L-04, ADR-0006).
