# ADR-0012: Authentication and authorisation: personal accounts, invite-only, row-level security

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 | Developer, with the client's answers | B-02 · defaults for T-03, R-16 · F-03 |

## Context

- Two employees, each using a personal phone (B-02).
- Every action must be traceable to a person.
- Nobody else may read client data.

## Decision

- **Supabase Auth** with email and password (default for T-03). Public sign-up is disabled; the developer creates the accounts.
- **One account per person.** No shared login.
- **Sessions:**
  - a short-lived access token (1 hour), with refresh-token rotation;
  - the session is stored encrypted: the key is in the iOS Keychain (expo-secure-store), and the encrypted session is in app storage. This is the pattern Supabase documents for Expo, because expo-secure-store values are limited to 2048 bytes.
- **App lock:** Face ID or Touch ID, with the device passcode as fallback, when the app opens and after 5 minutes in the background (default for T-03). It needs a device passcode (F-03).
- **No e-mail in the MVP:** password resets are done by the developer ([ADR-0004](0004-backend-supabase.md)). A custom e-mail provider can be added later.
- **Roles:** one `staff` role with full access to business functions in the MVP, since there are two employees (default for R-16). Administrative tasks (creating or disabling accounts, fixing data, erasure) are done by the developer, through the Supabase dashboard or scripts.
- **Authorisation in the database:**
  - RLS on every table, denied by default;
  - only users with an active staff profile can read or write;
  - append-only tables accept inserts only, and status columns change only through server functions ([ADR-0007](0007-contract-lifecycle-and-audit.md));
  - storage is private, and the evidence buckets accept uploads and reads only ([ADR-0014](0014-file-storage.md));
  - the service-role key and the storage S3 keys never ship in the app.
- **Revocation:** the developer marks the profile inactive, which blocks access immediately through RLS, and revokes all sessions ([US-012](../stories/US-012-revoke-a-staff-members-access.md)).
- **Multi-factor authentication:** not in the MVP. Supabase supports TOTP if it's wanted later.

## Consequences

**Positive**

- Every action is traceable to one person.
- Access can be cut immediately from the server, without touching the phone.

**Negative / risks**

- With a single role, both employees can do everything the app allows, including deleting client documents uploaded by mistake. Signed evidence stays protected by the database rules.
- The developer handles all account administration, including password resets.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| A shared company login | No accountability |
| Google or Microsoft single sign-on | Unknown whether the client uses either (T-03) |
| Magic link or one-time code by email | Needs an e-mail provider; a possible later alternative to passwords (T-03) |

## Revisit when

The company hires more staff, or different access levels are needed (R-16).

## Implemented by

- [US-003](../stories/US-003-expo-app-skeleton.md): Create the Expo app skeleton
- [US-004](../stories/US-004-supabase-environments.md): Create the Supabase environments
- [US-006](../stories/US-006-core-database-schema-and-rls.md): Create the core database schema, access rules and storage
- [US-007](../stories/US-007-audit-trail-and-immutability.md): Record an audit trail and protect signed data
- [US-010](../stories/US-010-sign-in-and-sign-out.md): Sign in and sign out
- [US-011](../stories/US-011-app-lock-with-face-id.md): Lock the app with Face ID
- [US-012](../stories/US-012-revoke-a-staff-members-access.md): Revoke a staff member's access (lost phone or departure)
