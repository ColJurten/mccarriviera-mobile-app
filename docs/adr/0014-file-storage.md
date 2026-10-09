# ADR-0014: File storage: private buckets, upload-only evidence, short-lived signed URLs

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 | Developer, with the client's answers | Brief · B-04, B-09 · defaults for R-15, L-03, L-07 |

## Context

- Photos, client documents, signatures and PDFs are personal data.
- Signatures, photos and PDFs are also evidence.
- The brief says: "Do not assume documents should be publicly accessible via simple URLs".
- The Free plan has 1 GB of file storage ([ADR-0004](0004-backend-supabase.md)).

## Decision

- **Private buckets only:**
  - `condition-photos`: reference sets, extra departure photos, damage photos;
  - `client-documents`;
  - `signatures`;
  - `contract-pdfs`.
- **Object paths use IDs, never names:**
  - `vehicles/{vehicle_id}/baselines/{baseline_id}/{photo_id}.jpg`
  - `damages/{damage_id}/{photo_id}.jpg`
  - `inspections/{inspection_id}/{photo_id}.jpg`
  - `clients/{client_id}/{document_id}.{ext}`
  - `contracts/{contract_id}/signatures/{signature_id}.png`
  - `contracts/{contract_id}/pdfs/{revision}-{stage}-{lang}-{timestamp}.pdf`, where the stage is `departure`, `amendment` or `final`.

  The file name staff see when sharing is in [US-042](../stories/US-042-archive-and-share-pdfs.md).
- **Access policies on storage objects:**
  - `condition-photos`, `signatures`, `contract-pdfs`: active staff can upload and read. Nobody can overwrite or delete through the API: there is no update or delete policy, and uploads never overwrite an existing file.
  - `client-documents`: upload, read, and delete, for a document uploaded by mistake (default for R-15).
  - Files are read through signed URLs that expire within 5 minutes. Nothing is public.
  - Supabase's S3 access keys bypass these policies. Only the backup job uses them ([ADR-0015](0015-backups.md)), and they are treated like the service-role key.
- **Size:**
  - photos are resized to 1600 px on the long edge, JPEG quality about 0.7 (roughly 200–400 KB each);
  - document files are limited to 10 MB;
  - PDF photo thumbnails are generated on the phone at render time.
- **Metadata:** every file has a database row recording what it belongs to, its kind, size, SHA-256, who uploaded it, when, and whether it came from the photo library (« importée »).
- **Retention:**
  - The app deletes nothing, except client documents uploaded by mistake.
  - Every generated PDF is archived, since the brief lists generated PDFs among the backend data.
  - Deletion and anonymisation follow the retention procedure ([US-094](../stories/US-094-retention-and-erasure.md)). Until L-03 and L-07 are answered, nothing is deleted (default for L-03 and L-07).

## Consequences

**Positive**

- No file is reachable without a valid session.
- Evidence can't be overwritten or deleted from the app.
- Storage use stays small.

**Negative / risks**

- Signed URLs expire, so the viewer must refresh them.
- A file uploaded by mistake to an evidence bucket stays there. Only the developer can remove it, through the retention procedure.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Public buckets with unguessable names | Still public links |
| Separate S3 or R2 storage | Another processor and more code; not needed now |

## Revisit when

The storage limit forces a move to Pro or to a different store ([ADR-0004](0004-backend-supabase.md)).

## Implemented by

- [US-006](../stories/US-006-core-database-schema-and-rls.md): Create the core database schema, access rules and storage
- [US-013](../stories/US-013-minimum-local-data-on-phones.md): Keep client data on staff phones to a minimum
- [US-022](../stories/US-022-add-a-vehicle.md): Add a vehicle with its reference photos
- [US-026](../stories/US-026-guided-reference-photo-capture.md): Guided reference photo capture
- [US-033](../stories/US-033-client-documents.md): Attach and view client documents
- [US-042](../stories/US-042-archive-and-share-pdfs.md): Archive, download and share contract PDFs
- [US-053](../stories/US-053-confirm-departure-condition.md): Confirm the departure condition
- [US-072](../stories/US-072-return-inspection.md): Inspect the vehicle: new damage or RAS
- [US-094](../stories/US-094-retention-and-erasure.md): Apply retention and erasure rules
