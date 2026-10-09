# US-092 · Send the legal and privacy questions, and close them before go-live

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E9 · Go-live | Must | P0 | S | To do |

- **Depends on:** —
- **Decisions:** [ADR-0009](../adr/0009-signatures.md) · [ADR-0006](../adr/0006-contract-only-scope.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md) · [ADR-0015](../adr/0015-backups.md) · [ADR-0017](../adr/0017-crash-reporting.md)
- **Open points:** L-01, L-02, L-03, L-04, L-05, L-06, L-07 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want the legal points checked before the app replaces paper, so that the digital contract holds up and client data is handled lawfully.

## Acceptance criteria

- [ ] The questions go to the lawyer and the accountant in P0. Their answers can change ADR-0006, ADR-0009 and ADR-0010, and stories US-040, US-041 and US-054. Everything below must be closed before the pilot (US-091).
- [ ] The lawyer's feedback is recorded on:
  - the signature level, including showing a signature only next to the values it covers (L-01, F-08);
  - the updated French terms, an approved English version, and the card-charge wording, now that the card is designated by its brand and last four digits only (L-02, F-09);
  - the GDPR notice, copies of ID documents and retention (L-03);
  - the data needed for traffic fines (L-06);
  - retention periods (L-07).
- [ ] The accountant's feedback on the contract title and invoicing is recorded (L-04).
- [ ] A data processing agreement between the company (controller) and the developer (processor) is signed, since client data is hosted in his accounts (F-02). It lists his sub-processors: Supabase, the backup storage provider, Expo and Sentry, plus the file storage provider if F-11 changes it. The company's record of processing is updated (L-03).
- [ ] The staff device-use rule (L-03) is written and given to both staff members.
- [ ] Every resulting change becomes a story before go-live. The retention answers feed US-094.

## Notes

- Most of this is done by the client and their advisers, outside the app. It is tracked here because go-live depends on it.
