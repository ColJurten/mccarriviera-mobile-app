# ADR-0006: Contract-only scope: billing, payment and price calculation stay outside the app

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-04, B-05, B-10 · F-06 (answered) · F-09 · L-02, L-04, L-05 |

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
  - no card data.
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
- **Removed from the template** (default for F-09): the card imprint area, the expiry date and the CVV.
  - This is an `INTERPRETATION` of B-10 ("payment handled elsewhere") and a `RECOMMENDED` security choice: PCI DSS forbids keeping a CVV after authorisation.
  - The acceptance text still authorises charges to « la carte de crédit désignée sur ce contrat ». With no card recorded, the lawyer must reword it (L-02).
- **Title:** stays « CONTRAT / FACTURE LOCATION », as on the template (B-04). If the accountant says a document titled « facture » must follow invoice rules (L-04), it becomes « CONTRAT DE LOCATION », a one-line change in the label catalogue.

## Consequences

**Positive**

- The app stays out of invoicing compliance (including the e-invoicing reform) and out of PCI DSS scope.
- The data model for amounts stays simple.

**Negative / risks**

- Hand-typed totals can be inconsistent with the lines. An automatic sum can be added later if wanted.
- By design, the amounts stored in the app aren't usable for accounting.
- The card-charge authorisation needs new wording (F-09, L-02).

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Prices computed from rate cards | Ruled out by B-05 |
| The app as the invoicing system | Ruled out by B-10 |
| Keep card details on the contract | Payment is handled elsewhere (B-10), and it would bring PCI DSS obligations |

## Revisit when

The company wants the app to calculate prices, totals or invoices, or F-09 is answered differently.

## Changes

- 2026-10-09: F-06 answered: totals, costs and the number of rental days are typed by staff.

## Implemented by

- [US-040](../stories/US-040-contract-pdf-template.md): Contract PDF template in French and English, with the signature block at the bottom right
- [US-052](../stories/US-052-fill-in-rental-details.md): Fill in the rental details
- [US-071](../stories/US-071-return-km-and-fuel.md): Record the return km and fuel
- [US-073](../stories/US-073-return-pricing-lines.md): Complete the pricing lines at the Retour
- [US-092](../stories/US-092-legal-and-privacy-checklist.md): Send the legal and privacy questions, and close them before go-live
