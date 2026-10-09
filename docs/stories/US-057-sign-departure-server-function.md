# US-057 · Server function: sign a Départ

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-007](US-007-audit-trail-and-immutability.md) · [US-041](US-041-general-terms-per-language.md)
- **Decisions:** [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md) · [ADR-0009](../adr/0009-signatures.md) · [ADR-0004](../adr/0004-backend-supabase.md)
- **Open points:** R-09 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want signing a Départ to happen in one server-side transaction, so that a contract is either fully signed with its evidence or not signed at all.

## Acceptance criteria

- [ ] One Postgres function, called over RPC, does everything in a single transaction:
  - checks the draft is complete and the vehicle is available;
  - assigns the contract number `MCR-YYYY-NNNN` from the yearly counter (default for R-09);
  - freezes revision 1, with the full snapshot of client and vehicle values, the IDs of the terms versions in force, and the SHA-256 of the snapshot;
  - stores the departure inspection;
  - stores the signature evidence record (image path and SHA-256, server time, staff user, device model, iOS and app versions);
  - sets the contract to `active` and the vehicle to `rented`;
  - writes the audit events.
- [ ] If the vehicle is no longer available, or the signature image isn't in storage, the function fails and nothing changes.
- [ ] Calling it again with the same idempotency key returns the first result, instead of signing twice.
- [ ] Database tests cover: success; two signings at once on the same vehicle (one wins); a retry with the same key; a missing signature file.
