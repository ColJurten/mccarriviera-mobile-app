# US-006 · Create the core database schema, access rules and storage

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | L | To do |

- **Depends on:** [US-004](US-004-supabase-environments.md)
- **Decisions:** [ADR-0004](../adr/0004-backend-supabase.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md) · [ADR-0008](../adr/0008-vehicle-condition-model.md) · [ADR-0011](../adr/0011-localisation.md) · [ADR-0012](../adr/0012-authentication-and-authorisation.md) · [ADR-0014](../adr/0014-file-storage.md)
- **Open points:** R-03, R-09, R-13, R-14, F-09 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want the tables, constraints, access rules and storage buckets for the whole MVP, so that every feature builds on one consistent, protected data model.

## Acceptance criteria

- [ ] Migrations create the tables listed in the notes. Every table has UUID primary keys, `created_at`/`created_by` and English snake_case names.
- [ ] The fields cover every field of the current contract that the app keeps (see `discovery/source-analysis.md` §2.2). Card imprint, expiry date and CVV are excluded (default for F-09).
- [ ] Storage is language-neutral: enumerations as codes, fuel as an integer from 0 to 8 (eighths), amounts as `numeric(10,2)`, times as `timestamptz` ([ADR-0011](../adr/0011-localisation.md)).
- [ ] Free-text fields have maximum lengths, so the contract pages never overflow ([ADR-0010](../adr/0010-contract-pdf-generation.md)). For example, 80 characters for names and address lines, and 500 for comments.
- [ ] A partial unique index allows at most one `active` contract per vehicle. Check constraints keep km ≥ 0 and fuel between 0 and 8.
- [ ] RLS is on for every table and denies by default. Only active staff can read and write business tables.
- [ ] Status columns (`contracts.status`, `vehicles.status`, `damages.status`) can't be updated by the app's database role (column-level grants). They change only through server functions ([ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)).
- [ ] These tables accept INSERT only: signed revisions, completed inspections, `signatures`, `condition_baselines`, `photos`, `contract_documents`, `audit_events`. Unsigned draft revisions can be updated. Damage descriptions and photos can't be changed; only the repair fields change, through the maintenance function.
- [ ] Four private buckets exist: `condition-photos`, `client-documents`, `signatures`, `contract-pdfs`. In `condition-photos`, `signatures` and `contract-pdfs`, staff can upload and read but not overwrite or delete. In `client-documents`, they can also delete. No bucket is public ([ADR-0014](../adr/0014-file-storage.md)).
- [ ] Generated PDFs record their stage as `departure`, `amendment` or `final`.
- [ ] A seed script loads synthetic vehicles and clients only. No real data.
- [ ] Database tests (`supabase test db`) prove that:
  - anonymous users and inactive staff can't read anything;
  - a second active contract on the same vehicle is rejected;
  - append-only tables reject UPDATE and DELETE;
  - the app's role can't change a status column;
  - staff can't overwrite or delete files in the evidence buckets.
- [ ] `docs/data-model.md` has the entity-relationship diagram (Mermaid) and is kept in step with the migrations.

## Notes

- Tables (working names): `staff_profiles`, `vehicles`, `condition_baselines`, `photos`, `damages`, `maintenance_records`, `clients`, `client_documents`, `contracts`, `contract_revisions`, `contract_drivers`, `inspections` (stage = departure | return), `signatures`, `contract_documents` (generated PDFs), `terms_versions`, `audit_events`, `contract_number_counters`.
- Vehicle statuses: `available`, `rented`, `maintenance`, `archived` (default for R-13). Contract statuses: `draft`, `active`, `closed`, `void` ([ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)).
- Contract numbers: `MCR-YYYY-NNNN` (default for R-09).
- Client fields are listed in US-031 (default for R-03). Maintenance fields are in US-080 (default for R-14).
- This can be delivered as two pull requests: tables and RLS first, then storage.
