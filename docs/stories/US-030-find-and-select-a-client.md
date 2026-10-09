# US-030 · Find and select a client

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E3 · Clients | Must | P1 | S | To do |

- **Depends on:** [US-006](US-006-core-database-schema-and-rls.md) · [US-010](US-010-sign-in-and-sign-out.md)
- **Decisions:** —
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to search clients by name, phone, licence or ID number, so that I reuse an existing record instead of typing it again.

## Acceptance criteria

- [ ] Search works on name (ignoring accents), phone, licence number and ID document number.
- [ ] Each result shows name, date of birth and city, enough to tell two clients with the same name apart.
- [ ] Inside a Départ, selecting a client returns to the flow with the client filled in. When nothing matches, « Nouveau client » is offered.
