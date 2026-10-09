# US-021 · Search, filter and sort vehicles

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E2 · Home and vehicles | Must | P1 | S | To do |

- **Depends on:** [US-020](US-020-home-screen.md)
- **Decisions:** —
- **Open points:** N-03 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to find a vehicle by plate or model and filter it by status, so that I find the right car quickly.

## Acceptance criteria

- [ ] Search matches the plate (ignoring spaces and dashes) and the make/model, regardless of case and accents.
- [ ] Status filters: Tous, Disponible, En cours, Maintenance, Archivé.
- [ ] Sort by plate, model, status or planned return. By default, rented cars come first, soonest return first (default for N-03).
- [ ] A rental is overdue once its planned return time has passed or, when no time was given, once the planned return date has passed (end of day). Overdue rentals are highlighted.
