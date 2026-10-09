# US-073 · Complete the pricing lines at the Retour

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E7 · Retour | Must | P4 | S | To do |

- **Depends on:** [US-070](US-070-start-a-retour.md)
- **Decisions:** [ADR-0006](../adr/0006-contract-only-scope.md) · [ADR-0007](../adr/0007-contract-lifecycle-and-audit.md)
- **Open points:** F-08 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to type the final amounts (extra days, extra km, fuel, miscellaneous, totals, balance), so that the final contract shows the complete pricing, as on paper.

## Acceptance criteria

- [ ] The pricing block starts with the values of the current revision. Staff can edit any line, and changed lines are highlighted.
- [ ] Totals, costs and the number of extra days are typed too; nothing is calculated (F-06). Amounts have 2 decimals. Only « Solde » may be negative (`RECOMMENDED`).
- [ ] These final amounts belong to the return record. The PDF prints them in the « Décompte final » of the Retour section, while page 1 keeps the departure values (default for F-08).
