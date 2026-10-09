# US-093 · Write the operations runbook

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E9 · Go-live | Must | P6 | S | To do |

- **Depends on:** [US-005](US-005-eas-builds-and-internal-distribution.md) · [US-008](US-008-nightly-encrypted-backups.md) · [US-012](US-012-revoke-a-staff-members-access.md)
- **Decisions:** [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md) · [ADR-0004](../adr/0004-backend-supabase.md) · [ADR-0015](../adr/0015-backups.md) · [ADR-0016](../adr/0016-repository-environments-ci.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As the developer maintaining the app alone, I want a runbook for recurring tasks, so that nothing expires or breaks unnoticed.

## Acceptance criteria

- [ ] `docs/runbook.md` covers:
  - the yearly Apple membership and certificate/profile renewal (rebuild and reinstall before expiry, with a reminder 30 days ahead);
  - registering a new phone;
  - publishing an over-the-air update;
  - applying a migration;
  - the monthly Supabase usage check and upgrade triggers;
  - backup monitoring and restore;
  - revoking a user;
  - the erasure procedure (US-094);
  - upgrading the Expo SDK.
- [ ] Every procedure that can be rehearsed has been run once on staging. The yearly renewal is rehearsed by checking the expiry dates in the Apple and EAS consoles.
