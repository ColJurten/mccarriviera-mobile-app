# US-012 · Revoke a staff member's access (lost phone or departure)

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E1 · Access, security and monitoring | Must | P1 | S | To do |

- **Depends on:** [US-010](US-010-sign-in-and-sign-out.md)
- **Decisions:** [ADR-0012](../adr/0012-authentication-and-authorisation.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md)
- **Open points:** L-03 (see [open questions](../discovery/open-questions.md))

## Story

As the company, I want to cut access from a lost phone or a departing employee within minutes, so that client data can't be read from that device.

## Acceptance criteria

- [ ] A runbook procedure and a script, run by the developer, set the staff profile to inactive, sign out all of that user's sessions, and can ban the account.
- [ ] After revocation, every request from that phone is refused immediately (RLS). The app shows « Compte désactivé » and deletes its cached files.
- [ ] The developer can re-enable the account, or create a new one for a new phone.
- [ ] The revocation is recorded in the audit trail.
- [ ] The staff device-use rule (L-03) tells staff to report a lost phone immediately.
