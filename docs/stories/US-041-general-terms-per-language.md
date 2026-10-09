# US-041 · Manage the general terms (CGV) per language

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E4 · Contract document | Must | P2 | S | To do |

- **Depends on:** [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0011](../adr/0011-localisation.md) · [ADR-0010](../adr/0010-contract-pdf-generation.md)
- **Open points:** R-17, L-02 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want the general terms stored as versioned texts in French and English, so that each contract prints the version that applied when it was signed.

## Acceptance criteria

- [ ] The `terms_versions` table holds the language, a version label, the effective date, and the HTML body split into pages with explicit page breaks, so pagination is predictable. The active version for each language is the latest effective one.
- [ ] The French text of the current contract is loaded as FR v1, typed from the scan and proof-read against it.
- [ ] EN v1 is loaded once the client provides an approved translation (R-17). Until then, an English PDF can't be generated, and the app says why (default for R-17).
- [ ] Each contract revision stores the IDs of the terms versions in force at signature, per language. There is no English ID if no approved text existed then.
- [ ] The developer updates the terms through a migration or seed script. There is no in-app editor in the MVP.

## Notes

- The lawyer's update of the terms (L-02) produces FR v2. Contracts signed earlier keep v1.
