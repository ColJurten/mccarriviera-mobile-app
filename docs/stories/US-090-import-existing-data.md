# US-090 · Import existing vehicles and clients

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E9 · Go-live | Could | P6 | S | To do |

- **Depends on:** [US-006](US-006-core-database-schema-and-rls.md) · [US-008](US-008-nightly-encrypted-backups.md) · [US-092](US-092-legal-and-privacy-checklist.md)
- **Decisions:** —
- **Open points:** T-02 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want our existing fleet, and client list if there is one, imported, so that staff don't retype them.

## Acceptance criteria

- [ ] This applies only if a source file exists (T-02). A one-off script imports vehicles, and clients if any, from CSV.
- [ ] The script is tested on staging with a synthetic file in the same format. Real data is imported only into production, once backups (US-008) and the legal checklist (US-092) are in place.
- [ ] Each imported vehicle still needs a reference photo set before its first Départ.
- [ ] The source file is deleted from the developer's machine after the import, since it contains personal data.
