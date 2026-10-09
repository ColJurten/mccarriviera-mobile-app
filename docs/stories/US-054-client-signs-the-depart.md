# US-054 · Client signs the Départ

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-051](US-051-choose-renter-and-additional-driver.md) · [US-052](US-052-fill-in-rental-details.md) · [US-053](US-053-confirm-departure-condition.md) · [US-057](US-057-sign-departure-server-function.md) · [US-009](US-009-spike-signature-and-pdf-on-iphone.md)
- **Decisions:** [ADR-0009](../adr/0009-signatures.md) · [ADR-0005](../adr/0005-online-only.md)
- **Open points:** L-01 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want the client to sign once on my phone, so that the contract is concluded and the vehicle becomes rented in one step.

## Acceptance criteria

- [ ] Before signing, a recap screen shows the key terms: vehicle, renter, dates, km included, deductible, typed amounts, km and fuel out. The client can read the general terms there in French or English (`RECOMMENDED`, [ADR-0009](../adr/0009-signatures.md)).
- [ ] The signature pad (the library chosen in US-009) is full-screen in landscape, with « Effacer » and « Valider ». An empty signature can't be validated.
- [ ] On « Valider », the signature image is uploaded first. Then the app calls the signing function ([US-057](US-057-sign-departure-server-function.md)) with an idempotency key.
- [ ] If another Départ took the vehicle in the meantime, the screen explains it and offers to go back. Nothing is stored as signed.
- [ ] If the network drops, the app retries the upload and the call. The idempotency key prevents a second contract.
- [ ] When signing succeeds, the flow moves on to choosing the language and generating the PDF ([US-055](US-055-departure-pdf.md)).

## Notes

- The signature is a simple electronic signature with an evidence record ([ADR-0009](../adr/0009-signatures.md)). The lawyer confirms whether that is enough (L-01).
