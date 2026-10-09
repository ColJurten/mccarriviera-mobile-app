# ADR-0006: Contract-only scope: billing, payment and price calculation stay outside the app

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-04, B-05, B-10 · F-06, F-09 (answered) · L-02, L-04, L-05 |

## Context

- The current form is titled « CONTRAT / FACTURE LOCATION ». It has a full pricing block and fields for a card imprint, the expiry date and the CVV.
- **B-04:** the PDF contains the legal information, just like the template.
- **B-05:** staff type prices by hand.
- **B-10:** billing and payment are handled outside the app. The app is only for the contract.

## Decision

- **Scope:** the app produces the **rental contract**. It is not an invoicing, pricing or payment system:
  - no invoice numbering;
  - no price calculation from rates;
  - no payment processing;
  - no full card number and no CVV.
- **What the PDF keeps:** all of the template's information, including:
  - the « Conditions & tarifs » box;
  - the deductible block, with the card brand (VISA / AMEX / AUTRE) as a simple choice;
  - the payment method (ESP / CC) as a simple choice;
  - the whole pricing block, from « Location » to « Solde ».
- **Amounts:**
  - Staff type every price line (B-05).
  - Totals (Total HT, TVA, Total TTC, Total prépayé, Solde), costs and the number of rental days are typed by hand too. The app calculates none of them (F-06, answered 2026-10-09).
  - Amounts are in euros with 2 decimals. Only « Solde » may be negative, for a refund (`RECOMMENDED`).
- **Kilometres** are computed (default for R-06), because they are measurements, not prices (meeting notes: « Km retour = km total »):
  - km driven = km in − km out;
  - extra km = max(0, km driven − km included).
- **Card fields** (F-09, answered 2026-10-09: keep them): the card imprint area, the expiry date and the CVV stay on the contract, with these limits (`RECOMMENDED`):
  - the imprint area shows the card brand and the last four digits only;
  - the expiry date (MM/YY) can be typed;
  - the CVV box is printed but always left empty.

  The app has no field for a full card number or a CVV. Card-industry rules (PCI DSS) forbid keeping a CVV once a payment is authorised, and a full card number would bring PCI DSS obligations, for PDFs that are shared by e-mail and messaging. With the last four digits recorded, « la carte de crédit désignée sur ce contrat » in the acceptance text has something to refer to; the lawyer still reviews the wording (L-02).
- **Title:** stays « CONTRAT / FACTURE LOCATION », as on the template (B-04). If the accountant says a document titled « facture » must follow invoice rules (L-04), it becomes « CONTRAT DE LOCATION », a one-line change in the label catalogue.

## Consequences

**Positive**

- The app stays out of invoicing compliance (including the e-invoicing reform). It never holds a full card number or a CVV, so it stays out of PCI DSS scope.
- The data model for amounts stays simple.

**Negative / risks**

- Hand-typed totals can be inconsistent with the lines. An automatic sum can be added later if wanted.
- By design, the amounts stored in the app aren't usable for accounting.
- The lawyer reviews the card-charge wording of the acceptance text (L-02).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Prices computed from rate cards | Ruled out by B-05 |
| The app as the invoicing system | Ruled out by B-10 |
| Full card number and CVV on the contract | Card-industry rules forbid keeping a CVV after authorisation, and a full number would bring PCI DSS obligations |

## Revisit when

The company wants the app to calculate prices, totals or invoices.

## Changes

- 2026-10-09: F-06 answered: totals, costs and the number of rental days are typed by staff.
- 2026-10-09 (later): F-09 answered: the card fields stay, limited to the last four digits and the expiry date, with an empty CVV box (they were removed by default).

## Implemented by

- [US-040](../stories/US-040-contract-pdf-template.md): Contract PDF template in French and English, with the signature block at the bottom right
- [US-052](../stories/US-052-fill-in-rental-details.md): Fill in the rental details
- [US-071](../stories/US-071-return-km-and-fuel.md): Record the return km and fuel
- [US-073](../stories/US-073-return-pricing-lines.md): Complete the pricing lines at the Retour
- [US-092](../stories/US-092-legal-and-privacy-checklist.md): Send the legal and privacy questions, and close them before go-live
