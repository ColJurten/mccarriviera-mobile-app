# ADR-0010: Generate the contract PDF on the phone from versioned HTML templates

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-04, B-06, B-07 · F-08 (partly answered) · defaults for R-01, R-02, R-18, R-19, F-08 · R-17 |

## Context

- The contract follows the model's presentation and contains every field of the current form (instruction from the client).
- It is produced in French or English, with a signature on every page.
- Staff must be able to save and share it from the phone.
- The app works online only, and there is no Mac.
- Supabase Edge Functions run on Deno and don't include a browser engine to render HTML.

## Decision

- **Rendering:** HTML/CSS templates are rendered **in the app** and converted to an A4 PDF with **expo-print** (iOS's WebKit print engine).
- **Versioning:** templates are versioned code in the repository. Each generated PDF records its template version and terms version. Old template versions stay in the code.
- **Page layout** (default for R-01 and F-08):
  1. **Contract, as signed at the Départ:**
     - header with logo, title, contract number and company identity;
     - renter, additional driver, intermediary and phone;
     - vehicle, km out, km included, fuel out;
     - departure date and time, planned return, return place;
     - « Conditions & tarifs », deductible, payment method;
     - the pricing block as typed at the Départ, and the acceptance text.
  2. **Départ / Retour:**
     - the Départ column: reference photo thumbnails, damage open at departure, extra photos, comments;
     - the Retour column: actual return date and time, km in, km driven, extra km, fuel in, new damage with thumbnails or « RAS », comments;
     - a « Décompte final / Final statement » block with the pricing lines as completed at the Retour.
  3. **General terms** in the chosen language.
  4. **Amendments**, if any: one block per amendment, each change as old → new, the reason, the date, and the amendment signature or « Sans signature du client ».
- **Every field of the current form is kept.** Each value is printed in the section of the stage that produced it ([ADR-0009](0009-signatures.md)).
- **Pagination:**
  - Every page is an explicit A4 block.
  - Sections that can grow (photos, terms, amendments) continue on extra pages. Every page, including continuation pages, repeats the header, the footer with « page x/y » and the signature block at the bottom right, in the same place in French and English.
  - Fixed sections never overflow, because free-text fields have maximum lengths ([US-006](../stories/US-006-core-database-schema-and-rls.md)).
  - The general terms are stored already split into pages ([US-041](../stories/US-041-general-terms-per-language.md)).
- **Signature block:** at the bottom right of every page, with the « Signature départ » and « Signature retour » boxes (F-08). Amendment pages carry the amendment's own signature there instead of the departure signature (default for F-08, [ADR-0009](0009-signatures.md)).
- **Photos:** embedded as compressed thumbnails. Full-size photos stay in storage (default for R-01).
- **Fields:**
  - None of the model-only fields are added (default for R-02). The contract number is added because the system needs it.
  - The staff member's name is not printed (default for R-19).
- **Company details:** name, address, SIRET, APE code, phone numbers and logo come from one configuration file, filled with details the client has confirmed. Fonts and logo are bundled in the app. The brand palette uses placeholders until the assets arrive (default for R-18).
- **Output:** written to the app cache, uploaded to the `contract-pdfs` bucket with its SHA-256 ([ADR-0014](0014-file-storage.md)), then opened in the iOS share sheet.
- **Regeneration:** any PDF can be regenerated with the same content: the same data, template version and terms version. The new file's bytes and hash can differ, so the archived original stays the reference.
- **Tests:**
  - HTML snapshot tests in CI cover synthetic cases: empty optional fields, maximum-length fields, an additional driver, 30 photos, 5 amendments, French and English.
  - Every template change is also checked as a PDF on a real iPhone.

## Consequences

**Positive**

- No PDF server to run or pay for.
- HTML/CSS makes it easy to follow the model's look.
- One template serves both languages.

**Negative / risks**

- WebKit print CSS has quirks, and repeated footers must be built as explicit page blocks. This is proven in the spike [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md) and checked on a real iPhone.
- PDFs with many photos take longer on older phones, so thumbnails are kept small.
- The layout places return values in the Retour section rather than on page 1 as on paper. The client confirms this (F-08).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Server-side rendering with a headless browser | Needs a separate, always-on service |
| Drawing the PDF with pdf-lib on the phone | Tedious layout and text flow |
| Filling a fixed PDF form | Can't follow the model's presentation, or switch language easily |

## Revisit when

Rendering on the phone proves too slow or unreliable (spike US-009), or the PDF must be produced without a phone.

## Changes

- 2026-10-09: the signature block sits at the bottom right of every page (F-08), and the final PDF always carries the return signature (F-04).

## Implemented by

- [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md): Spike: prove signature capture and PDF generation on a real iPhone
- [US-040](../stories/US-040-contract-pdf-template.md): Contract PDF template in French and English, with the signature block at the bottom right
- [US-041](../stories/US-041-general-terms-per-language.md): Manage the general terms (CGV) per language
- [US-042](../stories/US-042-archive-and-share-pdfs.md): Archive, download and share contract PDFs
- [US-055](../stories/US-055-departure-pdf.md): Generate the departure PDF in French or English
- [US-063](../stories/US-063-reopen-or-regenerate-a-pdf.md): Re-open, re-share or regenerate a contract PDF
- [US-064](../stories/US-064-amendment-pages-in-the-pdf.md): Amendment pages in the PDF
- [US-075](../stories/US-075-final-pdf.md): Generate the final PDF in French or English
