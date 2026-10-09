# ADR-0005: Online-only operation: no offline mode

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 | Developer, with the client's answers | B-03 |

## Context

- B-03 rules out an offline mode: contracts are read and written in the shared database.
- The two phones must never rent the same car at the same time.
- Offline support would need a local database, a sync queue and conflict rules, and would keep client data on personal phones ([ADR-0013](0013-personal-device-data-protection.md)).

## Decision

- **Every read and write goes to the backend.**
  - These actions need a connection: starting, signing and closing a Départ or a Retour, amendments, and status changes. The database enforces the rules ([ADR-0007](0007-contract-lifecycle-and-audit.md)).
  - Without a connection, the app shows a banner and disables the actions that change data.
- **Uploads:**
  - During a handover, uploads (photos, signature, PDF) retry automatically while the app is open.
  - The signature is uploaded **before** the signing function runs, so a contract is never marked signed without its signature.
  - Photos wait in the app's temporary folder until they are uploaded. If the app is closed before that, the step isn't complete and the photos have to be retaken. Leftover files are deleted at the next launch ([ADR-0013](0013-personal-device-data-protection.md)).
- **PDFs:** if a PDF upload fails, the PDF can be regenerated with the same content from the stored data ([ADR-0010](0010-contract-pdf-generation.md)). The contract shows « PDF non archivé » until the upload succeeds.
- **No local data:** there is no local database and no persisted cache of business data. TanStack Query keeps data in memory only.

## Consequences

**Positive**

- The simplest architecture: no conflicts, and little client data on personal phones.

**Negative / risks**

- No signal means no handover in the app. The fallback (for example a paper contract) is the company's decision.
- Uploads on weak mobile data can be slow, so photos are compressed before upload ([ADR-0014](0014-file-storage.md)).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Background upload queue that survives an app restart | Keeps client data and photos on the phone between sessions. Not needed given B-03 |
| Full offline mode with sync | Much more work, plus conflict handling. Ruled out by B-03 |

## Revisit when

Handovers regularly fail for lack of signal.

## Implemented by

- [US-020](../stories/US-020-home-screen.md): Home screen: Départ, Retour and the fleet
- [US-026](../stories/US-026-guided-reference-photo-capture.md): Guided reference photo capture
- [US-042](../stories/US-042-archive-and-share-pdfs.md): Archive, download and share contract PDFs
- [US-050](../stories/US-050-start-a-depart.md): Start a Départ by choosing an available vehicle
- [US-052](../stories/US-052-fill-in-rental-details.md): Fill in the rental details
- [US-054](../stories/US-054-client-signs-the-depart.md): Client signs the Départ
- [US-074](../stories/US-074-client-signs-the-retour.md): Client signs the Retour and the rental is closed
