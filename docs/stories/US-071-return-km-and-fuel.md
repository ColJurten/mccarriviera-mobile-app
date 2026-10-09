# US-071 · Record the return km and fuel

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E7 · Retour | Must | P4 | S | To do |

- **Depends on:** [US-070](US-070-start-a-retour.md)
- **Decisions:** [ADR-0006](../adr/0006-contract-only-scope.md) · [ADR-0011](../adr/0011-localisation.md)
- **Open points:** R-06 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to enter the return km and fuel and see the km driven, so that the contract shows both the departure and the return values.

## Acceptance criteria

- [ ] Km in is required and must be at least km out. A distance above 5,000 km asks for confirmation, to catch typos (`RECOMMENDED`).
- [ ] The app computes km driven (km in − km out) and extra km (max(0, driven − km included)), by default for R-06. They print in the Retour column as « Kms parcourus » and « Kms facturés » (meeting notes: « Km retour = km total »).
- [ ] Fuel in uses the same eighths gauge. If it's below fuel out, a hint is shown, but no charge is calculated (default for R-06).
