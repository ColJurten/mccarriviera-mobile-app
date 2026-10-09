# US-052 · Fill in the rental details

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E5 · Départ | Must | P3 | M | To do |

- **Depends on:** [US-050](US-050-start-a-depart.md)
- **Decisions:** [ADR-0006](../adr/0006-contract-only-scope.md) · [ADR-0011](../adr/0011-localisation.md) · [ADR-0005](../adr/0005-online-only.md)
- **Open points:** R-05, R-07, R-08, F-09 (see [open questions](../discovery/open-questions.md))

## Story

As a staff member, I want to complete the rental terms with sensible defaults, so that the contract is complete before the client signs.

## Acceptance criteria

- [ ] Dates (default for R-05):
  - the departure date and time default to now and can be edited;
  - the planned return date is required, and its time is optional;
  - the return place is optional free text.
- [ ] Intermediary: free text, defaulting to « MC CAR RIVIERA », with an optional phone (default for R-08).
- [ ] « Conditions & tarifs », all optional and typed by staff: daily rate for 1–3 days, daily rate for 4–7 days, extra day, km included, package price with its number of days, price per extra km.
- [ ] Deductible: card brand (VISA, AMEX, AUTRE), theft amount and at-fault accident amount. All are optional, with a warning if empty, since CGV Art. 5-4 refers to them (default for R-07).
- [ ] Payment method: ESP or CC, optional. There are no card number, expiry or CVV fields (default for F-09).
- [ ] The pricing block is typed by hand: Location, J/Sup, Km Sup, Total HT location, Assurance −25 ans, Conducteur sup, Livraison, Options I–III, Carburant, Divers, Total HT, TVA 20 %, Total TTC, Total prépayé, Solde. Totals, costs and the number of rental days are typed too; nothing is calculated (F-06).
- [ ] Amounts have 2 decimals. Only « Solde » may be negative, for a refund (`RECOMMENDED`).
- [ ] Before signing, the app checks:
  - vehicle;
  - renter mandatory fields;
  - the additional driver's fields, if there is one;
  - departure date and time;
  - a planned return on or after the departure;
  - km out and fuel out.
- [ ] The draft is saved on the server as fields are filled in (online only, [ADR-0005](../adr/0005-online-only.md)).
