# ADR-0009: Signatures: one capture per handover, at the bottom right of every page, next to the values it covers

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-06, B-07, B-08 · F-04 (answered) · F-08 (partly answered) · L-01 |

## Context

- **B-06:** one signature on every page.
- **B-07:** the signature sits in the same place whether the contract is in French or English.
- **B-08:** a client absent at the Retour is the company's matter, not the app's.
- **F-04** (2026-10-09): the return signature is mandatory, like the departure signature.
- **F-08** (2026-10-09): the signature always sits at the bottom right of the page.
- **Brief:** the client signs again at the Retour (step 5). Signed data must never be overwritten.
- The brief asks to keep three different things apart:

| | What it is | What it proves |
|---|---|---|
| **Signature image on several pages** | The drawn signature, placed as a picture on each page | On its own, nothing ties it to the content: a picture can be copied elsewhere. Its value comes from the evidence recorded around it |
| **Digitally signed PDF (PAdES)** | A certificate-based cryptographic signature embedded in the file | Any later change to the file is detectable, and the certificate holder is identified. Here that would be the company, unless a trust service issues a certificate to the client |
| **Electronic signature (legal notion)** | eIDAS levels (simple, advanced, qualified); French Civil Code art. 1366–1367 | A drawn signature with an audit trail is generally a **simple** electronic signature. It is admissible, but if contested the company must prove it is reliable. Only a **qualified** signature is presumed reliable |

## Decision

- **Position:** every page has a signature block at the **bottom right**, in the same place in French and English (F-08, B-07). It holds two boxes: « Signature départ » and « Signature retour ».
- **Départ:** after the recap screen, the client signs once on a full-screen pad.
  - The image goes into the « Signature départ » box on every page of the Départ PDF (B-06).
  - It also appears on every page of later PDFs, except amendment pages (see below).
- **Retour:** the client signs once. The signature is **mandatory** (F-04): a Retour can't be completed without it. The image goes into the « Signature retour » box on every page of the final PDF.
  - If the client isn't there, the Retour stays « en attente de signature »: what staff entered is saved, and the Retour is finished when the client signs. The vehicle stays « En cours » until then (`RECOMMENDED`). How the company reaches the client is outside the app (B-08).
- **Amendments:** an amendment page carries the amendment's own signature in its bottom-right block: the client's amendment signature, or « Sans signature du client » (default for R-11).
- **A signature only appears next to values that existed when it was given** (`RECOMMENDED`, default for F-08):
  - page 1 always shows the contract as signed at the Départ;
  - changes appear on amendment pages;
  - return values and final amounts appear in the Retour section.

  The departure signature is therefore not placed on amendment pages. This slightly narrows "every page" (B-06), so the client confirms it (F-08) and the lawyer reviews it (L-01).
- **Language and order:**
  - B-07's answer is about where the signature sits: the signature block is in the same position in French and English.
  - The brief's order is kept: sign first, then choose the language. The same signature works for either PDF.
  - Before signing, a recap screen shows the key terms and lets the client read the general terms in French or English (`RECOMMENDED`, [US-054](../stories/US-054-client-signs-the-depart.md)).
- **Evidence record:** each signature has an append-only record with:
  - the PNG image and, if the pad provides them, the stroke points;
  - the SHA-256 of the image;
  - the server timestamp;
  - the staff user;
  - the device model, iOS version and app version;
  - the contract and revision;
  - the SHA-256 of the data snapshot that was signed;
  - the IDs of the terms versions.
- **PDF integrity:** each archived PDF's SHA-256 is stored, so any later change to the file can be detected.
- **Not in the MVP:** no PAdES signature and no trust-service signature. If the lawyer asks (L-01), the upgrade paths are a company certificate seal on the PDF, or an advanced or qualified signature through a trust service provider.

## Consequences

**Positive**

- Matches the client's expectation of a signature on every page.
- Quick at the counter.
- A signature is never shown next to values the client didn't approve.

**Negative / risks**

- The image alone proves little. The evidence record and the hashes are what make it defensible.
- The client signs before choosing the PDF's language. The recap screen in their language mitigates this.
- A car returned without its client can't be closed in the app, so it can't be rented again, until the client signs (F-04, B-08).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| A separate signature per statement (B-06 b) | Ruled out by B-06 |
| Tick each statement, then sign once (B-06 c) | Not chosen; can be added later |
| Departure signature also on amendment pages | Would show the client's signature next to changes they may not have approved |
| Optional return signature | Ruled out by F-04 |
| Advanced or qualified signature through a trust service | Cost, identity checks and friction aren't justified before legal advice (L-01) |

## Revisit when

The lawyer's answer to L-01 requires a stronger signature, or the client answers the rest of F-08 differently.

## Changes

- 2026-10-09: F-04 answered: the return signature is mandatory (it was optional by default). F-08 partly answered: the signature block sits at the bottom right of every page; the rule for amendment pages stays a default.

## Implemented by

- [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md): Spike: prove signature capture and PDF generation on a real iPhone
- [US-040](../stories/US-040-contract-pdf-template.md): Contract PDF template in French and English, with the signature block at the bottom right
- [US-054](../stories/US-054-client-signs-the-depart.md): Client signs the Départ
- [US-055](../stories/US-055-departure-pdf.md): Generate the departure PDF in French or English
- [US-057](../stories/US-057-sign-departure-server-function.md): Server function: sign a Départ
- [US-061](../stories/US-061-extend-or-amend-a-rental.md): Extend a rental or amend allowed fields
- [US-064](../stories/US-064-amendment-pages-in-the-pdf.md): Amendment pages in the PDF
- [US-074](../stories/US-074-client-signs-the-retour.md): Client signs the Retour and the rental is closed
- [US-075](../stories/US-075-final-pdf.md): Generate the final PDF in French or English
- [US-092](../stories/US-092-legal-and-privacy-checklist.md): Send the legal and privacy questions, and close them before go-live
