# US-042 · Archive, download and share contract PDFs

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E4 · Contract document | Must | P2 | M | To do |

- **Depends on:** [US-040](US-040-contract-pdf-template.md) · [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0014](../adr/0014-file-storage.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md) · [ADR-0005](../adr/0005-online-only.md)
- **Open points:** T-05 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want each generated PDF archived and shareable through the iOS share sheet, so that the client receives it through any channel and the company keeps a copy.

## Acceptance criteria

- [ ] After generation, the PDF is uploaded to `contract-pdfs` with a database row: contract, revision, stage (`departure`, `amendment` or `final`), language, template version, terms version, SHA-256, author, time.
- [ ] The iOS share sheet opens with the PDF (Files, Mail, Messages, WhatsApp, AirDrop…). The app sends nothing by itself.
- [ ] The file is named `{contract number}_{depart|avenant-N|final}_{fr|en}.pdf`, for example `MCR-2026-0042_depart_fr.pdf`.
- [ ] If the upload fails, the contract shows « PDF non archivé » and the app retries.
- [ ] The PDF can be regenerated with the same content from the stored data. The new file's bytes and hash can differ, so the archived original stays the reference.
- [ ] From a contract screen, any archived PDF can be opened and shared again (downloaded through a signed URL).
