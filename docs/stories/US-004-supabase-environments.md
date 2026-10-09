# US-004 · Create the Supabase environments

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | S | To do |

- **Depends on:** [US-002](US-002-repository-and-agent-guidance.md)
- **Decisions:** [ADR-0004](../adr/0004-backend-supabase.md) · [ADR-0016](../adr/0016-repository-environments-ci.md) · [ADR-0012](../adr/0012-authentication-and-authorisation.md)
- **Open points:** F-02, F-07 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want staging and production Supabase projects in the EU plus a local stack, so that I can develop safely and deploy schema changes predictably.

## Acceptance criteria

- [ ] Two Supabase projects on the Free plan in an EU region (Paris or Frankfurt): `mcr-staging` and `mcr-production`, in the company's Supabase organisation with the developer as member (default for F-02).
- [ ] The local Supabase stack runs with the Supabase CLI and Docker inside WSL2, for migrations and database tests. `supabase start` works from the repository.
- [ ] Auth settings: email and password enabled, public sign-up disabled, passwords of at least 12 characters, access tokens valid for 1 hour, refresh-token rotation on. No e-mail sending is configured (password resets by the developer, [US-010](US-010-sign-in-and-sign-out.md)).
- [ ] The service-role key is only in CI secrets and the developer's password manager, never in the app or the repository.
- [ ] Schema changes reach staging and production only through migrations in `supabase/migrations`, never through dashboard edits.
- [ ] Types generated from the schema are committed, and CI fails if they are out of date.
- [ ] `docs/architecture.md` has the system diagram (app, Supabase, EAS, crash reporting, backups) and the list of server functions. It is kept up to date as functions are added.
- [ ] The runbook lists the monthly usage check and the upgrade triggers from [ADR-0004](../adr/0004-backend-supabase.md).
