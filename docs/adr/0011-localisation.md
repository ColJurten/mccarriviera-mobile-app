# ADR-0011: Localisation: language-neutral data, FR/EN catalogues, versioned general terms

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 | Developer, with the client's answers | Brief · B-07 · defaults for R-17, N-01 |

## Context

- The brief requires the contract in French or English, with the same underlying data whatever the language.
- Business data must not be duplicated per language.

## Decision

- **Language-neutral data:**
  - enumerations are stored as codes, for example `fuel_type = 'unleaded_95'` or `payment_method = 'cash' | 'card'`;
  - fuel is stored in eighths, from 0 to 8;
  - amounts are `numeric(10,2)` in euros;
  - times are UTC timestamps, displayed in Europe/Paris time.
- **Free text** typed by staff (addresses, comments, damage notes) is printed as typed in both languages. It isn't translated.
- **Labels and fixed sentences** of the contract come from two catalogues with identical keys (`fr`, `en`). A test fails if a key is missing in either.
- **Date and number formats** follow the language: « 27 août 2026 » and « 1 234,56 € » in French, "27 Aug 2026" and "€1,234.56" in English.
- **General terms** are versioned texts per language (`terms_versions`):
  - French v1 is the current text, to be updated after the legal review (L-02);
  - English v1 is the client's approved translation (R-17);
  - each contract revision records which versions were in force at signature.
- **English PDFs** are refused, with an explanation, until an approved English text exists (default for R-17).
- **Regenerating in the other language** ([US-063](../stories/US-063-reopen-or-regenerate-a-pdf.md)) prints that language's terms version in force at signature. If none existed then, the regeneration is refused.
- **The staff app itself** is in French, built with translation keys so English can be added cheaply (default for N-01).

## Consequences

**Positive**

- One data set and one template serve both languages.
- A signed contract can be rendered again in either language, when that language's terms were in force.

**Negative / risks**

- English PDFs depend on the client delivering an approved translation of the general terms.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| One template per language | The layouts drift apart over time |
| Translated copies of business data | Duplication that the brief rules out |

## Revisit when

A third language is needed (R-17).

## Implemented by

- [US-003](../stories/US-003-expo-app-skeleton.md): Create the Expo app skeleton
- [US-006](../stories/US-006-core-database-schema-and-rls.md): Create the core database schema, access rules and storage
- [US-031](../stories/US-031-create-a-client.md): Create a client
- [US-040](../stories/US-040-contract-pdf-template.md): Contract PDF template in French and English, with the signature block at the bottom right
- [US-041](../stories/US-041-general-terms-per-language.md): Manage the general terms (CGV) per language
- [US-052](../stories/US-052-fill-in-rental-details.md): Fill in the rental details
- [US-055](../stories/US-055-departure-pdf.md): Generate the departure PDF in French or English
- [US-063](../stories/US-063-reopen-or-regenerate-a-pdf.md): Re-open, re-share or regenerate a contract PDF
- [US-071](../stories/US-071-return-km-and-fuel.md): Record the return km and fuel
- [US-075](../stories/US-075-final-pdf.md): Generate the final PDF in French or English
