# US-010 · Sign in and sign out

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E1 · Access, security and monitoring | Must | P1 | M | To do |

- **Depends on:** [US-004](US-004-supabase-environments.md) · [US-005](US-005-eas-builds-and-internal-distribution.md) · [US-006](US-006-core-database-schema-and-rls.md)
- **Decisions:** [ADR-0012](../adr/0012-authentication-and-authorisation.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md)
- **Open points:** T-03 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to sign in with my own account, so that the app knows who does each action and nobody else can open client data.

## Acceptance criteria

- [ ] Sign-in with email and password (default for T-03). There is no self-registration screen.
- [ ] Wrong credentials show a generic error, with no hint about whether the email exists. Repeated failures are rate-limited.
- [ ] The session is stored encrypted, with the key in the iOS Keychain. This is the pattern Supabase documents for Expo, because expo-secure-store values are limited to 2048 bytes. The session is refreshed silently and survives restarts until sign-out or revocation.
- [ ] Sign-out (in Settings) ends the session, clears in-memory data and the app's cached files (photos, PDFs), and returns to Sign-in.
- [ ] A deactivated staff profile can't read any data, even with a valid token (RLS), and sees « Compte désactivé ».
- [ ] Password resets and new accounts are handled by the developer, through the dashboard or a script. The app sends no e-mail in the MVP, because Supabase's built-in e-mail only reaches the project's team members (`RECOMMENDED`).
