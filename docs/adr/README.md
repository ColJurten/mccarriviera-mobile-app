# Architecture decision records

Decisions taken from the client's answers of 2026-10-07, revised after an independent review the same day, and updated
with the answers of 2026-10-09. The format, the labels and the rule for changing a decision are in
[ADR-0001](0001-record-architecture-decisions.md). In short: when an open question is answered, the ADR is updated in
place and the change is logged in its **Changes** section; any other change gets a new ADR that supersedes the old one.

Labels used inside the ADRs:

- "(default for X-nn)": a choice applied to a question that is still open. Every default is listed in [`../discovery/open-questions.md`](../discovery/open-questions.md) § Defaults.
- `RECOMMENDED`: a technical choice that no question asked about.
- `INTERPRETATION`: a reading of an answer that has to be confirmed.

| ADR | Decision | Status | Based on |
|---|---|---|---|
| [ADR-0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted | — |
| [ADR-0002](0002-mobile-stack-expo.md) | Build the app with Expo (React Native, TypeScript), compiled in the cloud | Accepted | B-01, B-02, B-11 · F-05 (answered) · F-01 |
| [ADR-0003](0003-ios-distribution-ad-hoc.md) | Distribute the app as an Ad Hoc build to registered iPhones, under the company's Apple account | Accepted | B-02, B-11 · F-03 (answered) · F-01, F-02 |
| [ADR-0004](0004-backend-supabase.md) | Use Supabase in the EU as the backend, starting on the Free plan | Accepted | B-03, B-11 · follow-ups F-02, F-07 |
| [ADR-0005](0005-online-only.md) | Online-only operation: no offline mode | Accepted | B-03 |
| [ADR-0006](0006-contract-only-scope.md) | Contract-only scope: billing, payment and price calculation stay outside the app | Accepted | B-04, B-05, B-10 · F-06 (answered) · F-09 · L-02, L-04, L-05 |
| [ADR-0007](0007-contract-lifecycle-and-audit.md) | Contract and vehicle lifecycle: signed data is immutable, changes create revisions, everything is audited | Accepted | Brief · B-06, B-08 · defaults for R-09, R-11, R-12, R-13 |
| [ADR-0008](0008-vehicle-condition-model.md) | Vehicle condition: reference photos reused at Départ, damage records, reset only after repair | Accepted | B-09 · brief (Retour, maintenance) · F-10 (answered) · defaults for B-09 Q1, R-10, R-14 |
| [ADR-0009](0009-signatures.md) | Signatures: one capture per handover, at the bottom right of every page, next to the values it covers | Accepted | B-06, B-07, B-08 · F-04 (answered) · F-08 (partly answered) · L-01 |
| [ADR-0010](0010-contract-pdf-generation.md) | Generate the contract PDF on the phone from versioned HTML templates | Accepted | B-04, B-06, B-07 · F-08 (partly answered) · defaults for R-01, R-02, R-18, R-19, F-08 · R-17 |
| [ADR-0011](0011-localisation.md) | Localisation: language-neutral data, FR/EN catalogues, versioned general terms | Accepted | Brief · B-07 · defaults for R-17, N-01 |
| [ADR-0012](0012-authentication-and-authorisation.md) | Authentication and authorisation: personal accounts, invite-only, row-level security | Accepted | B-02 · defaults for T-03, R-16 · F-03 |
| [ADR-0013](0013-personal-device-data-protection.md) | Protect client data on staff personal phones | Accepted | B-02, B-03 · default for T-05 · F-03 · L-03 |
| [ADR-0014](0014-file-storage.md) | File storage: private buckets, upload-only evidence, short-lived signed URLs | Accepted | Brief · B-04, B-09 · defaults for R-15, L-03, L-07 |
| [ADR-0015](0015-backups.md) | Nightly encrypted off-site backups: database dumps plus incremental file copies | Accepted | B-11 · defaults for F-02, L-03, L-07 |
| [ADR-0016](0016-repository-environments-ci.md) | One repository, three environments and an automated delivery pipeline | Accepted | defaults for T-04, N-06 · F-02 |
| [ADR-0017](0017-crash-reporting.md) | Report crashes to an EU-hosted service with personal data removed | Accepted | RECOMMENDED (no question) · F-02 · L-03 |
| [ADR-0018](0018-development-and-test-devices.md) | Develop with an Android emulator on Windows and check iOS on a registered test iPhone | Accepted | F-05 (answered) · B-01 |
