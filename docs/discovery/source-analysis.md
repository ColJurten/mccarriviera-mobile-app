# Source analysis: reference documents

> **Status:** observations from the reference documents are `CONFIRMED`. Readings of ambiguous handwriting or marks are
> tagged `INTERPRETATION` and linked to a question in [`open-questions.md`](open-questions.md).
> **Inputs:** the brief (`attachment.txt`), `current_template.pdf`, `model_template.pdf`, `meeting_client.pdf`.
> **Date:** 2026-10-07.

## 0. Findings that change the design

1. **The current form is a contract *and* an invoice.** It is titled « CONTRAT / FACTURE LOCATION » and has a full pricing block (HT, TVA 20 %, TTC, prepaid, balance). The meeting notes say « Template : tarif complet ». The brief never mentions pricing or invoicing. Whether the app issues invoices decides numbering, VAT, retention and exposure to the French e-invoicing reform. See B-04 and B-05.
2. **The client signs in four places today, all on page 1:** next to the deductible (franchise) block, under the acceptance of the general terms and the card-charge authorisation, in the departure condition box and in the return condition box. The model template has one signature per page instead. See B-06.
3. **In the brief's order, the client signs before the contract exists in a language.** The signature is step 4, the language choice is step 5 and the PDF is step 6. See B-07.
4. **The "completed" sample has no return signature.** The client may not be present at return. The general terms also provide for a car left outside opening hours, with the renter keeping custody and risk until the agency opens. See B-08.
5. **The form asks for a card imprint, the card expiry date and the CVV**, plus an authorisation to charge the card remotely. PCI DSS forbids keeping a CVV after authorisation, so the app should not capture card numbers. See B-10.
6. **The general terms bill time in 12-hour blocks with a 59-minute tolerance,** yet the sample has dates without times. Times are therefore contractually relevant, and the app can record them automatically. See R-05.
7. **The general terms exist only in French** (one article has an English paragraph), and parts are out of date: the privacy clause predates GDPR and one Civil Code article number predates the 2016 reform. An English contract needs an approved English translation. See R-17 and L-02.
8. **Photos replace the damage drawings** (brief: "WE NEED ONLY PHOTOS"). However, the brief also asks for damage records with comments at return. In the meeting notes, both the Départ and the Retour flows end in a box that says « à fournir : photo sortie » (exit photos to provide), while the brief says a departure inherits the vehicle's existing photos. See B-09 and R-10.
9. **The model template is another rental company's document, and both samples contain real customers' personal data.** Use the model for layout only and keep both scans out of the repository.
10. **Fuel is recorded in eighths on the current form and as a percentage on the model.** The terms say the car leaves with a full tank, but the sample's departure gauge is below half. See R-06.
11. **Most of the sample is typed, not handwritten.** Identity, addresses, document numbers, vehicle, dates, rates, deductible and amounts are in a computer font. Only the invoice reference, the two odometer readings, the fuel and damage marks, the highlight and the signatures are by hand. So the form is already filled on a computer before printing. Its source file would give the exact labels and maybe the missing footnote texts, and the tool may hold existing client data. See T-02.

## 1. Inputs and how they were read

| File | What it is | Pages | How it was read | Personal data inside |
|---|---|---|---|---|
| `attachment.txt` | The brief | – | Full text | No |
| `current_template.pdf` | Phone scan of a completed MC Car Riviera rental (vehicle returned) | 3 | Image-only scan with no text layer. Each page was rendered and read visually, with zoomed crops for small print | **Yes**: a real renter's name, address, licence and ID numbers, date of birth, signatures |
| `model_template.pdf` | Phone scan of another rental company's completed agreement (pick-up) | 3 | Same | **Yes**: a real renter's name, email, phone, passport number, date of birth, address, signatures |
| `meeting_client.pdf` | Phone scan of handwritten meeting notes with a flow sketch and wireframes | 1 | Same | No |

All four inputs were available and fully inspected. **None of the personal data in the samples is reproduced in these docs.**

`RECOMMENDED`: keep the scans out of the git repository and never derive test fixtures from them. Use synthetic data.

## 2. `current_template.pdf`: the contract in use today

### 2.1 Page structure

| Page | Title | Content | Signature zones |
|---|---|---|---|
| 1 | CONTRAT / FACTURE LOCATION | Company header, renter, additional driver, payment, vehicle, mileage, dates, rates, deductible, fuel gauges, pricing/invoice block, two condition boxes (départ / retour), acceptance text | 4 (see 2.3) |
| 2 | CONDITIONS GÉNÉRALES DE LOCATION | General terms, Art. 1–12, in French (Art. 10 also has an English paragraph). Printed on the back ("au verso") | None visible |
| 3 | DÉPART · RETOUR | Two columns of drawings of the rented model (top, left, right, front, rear) for marking damage | None |

### 2.2 Field inventory: page 1

*Owner* is the entity a value belongs to. It is input for the domain model, not a final decision.
*When*: **D** = at Départ, **R** = at Retour, **S** = static / settings, **C** = computed.
*Sample*: whether the completed sample has a value.

In the sample, most values are **typed** in a computer font. Only the invoice reference, the two odometer readings,
the fuel and damage marks, the highlight and the signatures are handwritten.

#### Header

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| Logo, company name, address (Juan-les-Pins), SIRET, APE code, two phone numbers | Company settings | S | printed | Static. Goes into the PDF header/footer |
| CONTRAT / FACTURE LOCATION | – | S | printed | Contract **and** invoice: B-04 |
| *(no printed contract number)* | Contract | D | – | « FACT 1336 » is handwritten at the top: looks like an invoice reference added by hand (`INTERPRETATION`, B-04, R-09) |
| Tél : | ? | D | the company's own mobile number | Purpose unclear: R-08 |
| Intermédiaire : | Contract | D | « MC CAR RIVIERA » | Booking intermediary? R-08 |

#### Locataire / Rentier / Conducteur (renter, main driver)

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| *(name line)* | Client | D | filled | One line for the full name |
| Adresse de facturation / Home adress | Client | D | filled | Street + floor/apartment, postcode, city. No country line, although the sample address is abroad (R-03) |
| Tél. (under the billing address) | Client | D | blank | |
| Adresse locale / Contact adress (2 lines) + Tél. | Client or rental? | D | blank | Address during the stay (hotel, villa…). It may belong to the rental rather than the client (R-03) |
| Permis de conduire N° / Licence N° | Client | D | filled | Number only. There is no issue date, although CGV Art. 1 requires a licence held for more than one year (R-04) |
| Date de naissance / Date of birth | Client | D | filled | A country is written after the date: place of birth or nationality? (R-03) |
| Passeport N° / Passport · Carte d'identité | Client | D | filled | The passport label is blacked out and an ID-card number plus a country is written. So the field is: document type + number + country (issuing country or nationality? R-03) |
| Mode de paiement: ESP · CC | Contract | D | a cross over the « ESP » (cash) label | Either cash selected or cash struck out, meaning card (`INTERPRETATION`, no design impact) |
| Empreinte carte de crédit, Type carte / CC type | Contract | D | blank | Large empty area for a physical card imprint (B-10) |
| Date de validité · CVV | Contract | D | blank | Card expiry and security code (B-10) |

#### 2ème conducteur / Additionnal driver

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| *(name line)* | Client (additional driver) | D | blank | Room for one additional driver only (R-03) |
| Date de naissance / Date of birth | Client (additional driver) | D | blank | |
| Permis de conduire N° / Licence N° | Client (additional driver) | D | blank | No ID document or address for the additional driver, although CGV Art. 1 requires every authorised driver to show an ID card or passport (R-03) |

#### Véhicule (vehicle and mileage)

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| Immat | Vehicle | S | filled | Registration plate |
| Color | Vehicle | S | filled | |
| Modèle | Vehicle | S | filled | Make and model on one line |
| ☐ SANS PLOMB 95 / UNLEADED 95 | Vehicle | S | highlighted by hand | Fuel type. A second printed line below it is blacked out |
| Kms Retour / Kms In | Return | R | handwritten | |
| Kms Départ / Kms Out | Departure | D | handwritten | |
| Kms Parcourus / Kms Drive | – | C | blank | Km in − km out |
| Kms Inclus / Kms Allowed | Contract terms | D | filled | Km allowance. Per rental or per day? (R-06) |
| Kms Facturés / Extra Kms | – | C | blank | max(0, driven − allowed) |

#### Dates

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| Date & heure départ / Date & time | Departure | D | date only | No time written |
| Date & heure retour / Date & time | Return | R | blank | Actual return |
| Retour prévu / To be checked in at | Contract | D | date only | Planned return |
| Lieu de retour / Return | Contract | D | blank | Implies returns elsewhere. There is no departure-place field (R-05) |

#### Conditions & tarifs (rates)

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| Tarif/J. 1 à 3 j … 4 à 7 j … / Rate per day | Contract terms (vehicle defaults?) | D | blank | Two daily-rate tiers |
| Jours sup … Km inclus … / Extra day | Contract terms | D | blank | « Km inclus » also appears in the Véhicule block (« Kms Inclus »): a second duplicate, like « Jours sup » (B-05) |
| Forfait … € pour … Jours | Contract terms | D | filled | Package price for N days |
| Jours sup … Km sup … / Extra day · Extra kms | Contract terms | D | Km sup filled (price per km) | « Jours sup » appears on two rows. The difference is unclear (B-05) |

#### Franchise minimum (deductible)

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| ☐ VISA ☐ AMEX ☐ AUTRE | Contract | D | VISA ticked | Card brand held as guarantee? (R-07) |
| Vol / Excess theft | Contract terms | D | filled | |
| Accident responsable / Excess accident | Contract terms | D | filled | |
| Signature (zone **S1**) | Signature | D | signed | See 2.3 |

#### Jauge essence / Fuel gauge

| Printed label | Owner | When | Sample | Notes |
|---|---|---|---|---|
| DÉPART: scale E · 1/8 … 7/8 · F | Departure | D | marked between two ticks | Eighths. Staff mark between ticks |
| RETOUR: same scale | Return | R | marked | |

#### Pricing / invoice block (right column)

Lines, top to bottom: Location / Rental · J / Sup (Nb extra days) · Km Sup (Extra kms) · Total H.T. Location ·
Assurance −25 ans · Conducteur Sup · Livraison / Delivery · Option I · Option II · Option III · Carburant / Gazoline ·
Divers · **TOTAL H.T.** · **TVA 20 %** · **TOTAL TTC** · **TOTAL PRÉPAYÉ / Total Deposit** · **SOLDE**.

In the sample, only the rental line and TOTAL TTC are filled, with the same amount. Every other line, HT and VAT are
blank. The block is filled at D (base amounts) and R (extras, balance). See B-04 and B-05.

#### Acceptance text (bottom right, French only)

> « J'ai lu et accepté les conditions stipulées ci-contre et au verso de ce contrat. Je suis seul responsable des
> infractions à la législation relative à la circulation routière ou stationnement et autres et j'autorise la société
> de location à recouvrir le montant de cette location, franchise, dégâts et contraventions au moyen de la carte de
> crédit désignée sur ce contrat y compris par v.a.d. »

This is followed by signature zone **S2**.

#### Descriptif véhicule ×2 (condition boxes)

Each box has a generic car outline, a legend (// éraflure = scratch, X bosse = dent, □ manque = missing part), two
blank text lines and a signature zone: « Signature départ » (**S3**) in the left box, « Signature retour » (**S4**)
in the right box. Per the brief, the drawings are replaced by photos only.

### 2.3 Signature zones

| Zone | Location | What it approves | Sample |
|---|---|---|---|
| S1 | Its own box, directly under « Franchise minimum » | The label is only « Signature ». From its position, it seems to approve the deductible amounts and the card held as guarantee (`INTERPRETATION`) | signed |
| S2 | Under the acceptance text, bottom right | Stated by the text: the general terms on both sides, responsibility for offences, and the authorisation to charge rental, deductible, damage and fines to the card, including remotely (v.a.d.) | signed |
| S3 | « Signature départ », departure condition box | Vehicle condition at departure | signed |
| S4 | « Signature retour », return condition box | Vehicle condition at return | **blank** |

The zone labels carry footnote numbers: S3 = 3 and S4 = 4, while the other two are only partly legible. The footnote
texts are not on the scanned pages. Nothing is signed on page 2 (terms) or page 3 (drawings). Note that CGV Art. 3
gives signing a meaning of its own: by signing the contract, the renter accepts the vehicle in its current condition.

### 2.4 Rules in the general terms (page 2) that affect the app

| Art. | Rule (summary) | Impact |
|---|---|---|
| 1 | The renter and the drivers authorised by the company and **named on the front** must present a valid ID card or passport and a driving licence **issued more than one year ago**, valid where they drive | The licence issue date is not on the form (R-04). The additional driver has no ID field (R-03) |
| 1 | The lessor may end the rental immediately, without compensation, if an essential obligation is breached (use of the vehicle, payment, return conditions) | Early termination by the company (R-12) |
| 1 | Cites "art. 1384 du Code civil" | This article was renumbered in the 2016 reform, so the terms need a legal review (L-02) |
| 2.8 | No driving outside metropolitan France and Monaco | Terms only |
| 2.9 | Lost keys: flat fee of 350 € | Possible « Divers » charge |
| 3 | The vehicle is delivered in apparent good working order, with tyres, spare wheel and accessories in good condition. **By signing the contract, the renter accepts the vehicle in its current condition** and must return it in the same condition | What signing approves (B-06). Inspection scope: tyres, spare wheel, accessories (B-09) |
| 5-2 | Insurance exclusions include damage to the underbody, tyres, roof and soft top (« bas de caisse, pneumatique, toit et capote »), theft with the key, failure to return the car at the agreed date and place, and an unauthorised driver | These areas matter for the photo angles (B-09) |
| 5-3 | Accidents, damage and theft must be declared to the company within a deadline (about 24 h; the text is cut off) | Incident recording is not in the brief (post-MVP candidate) |
| 5-4 | Liability limited to the deductible "indiqué au départ au contrat" | Deductible amounts must be on the signed departure contract |
| 6 | Fuel is paid by the renter. The car is supplied with a full tank (text partly cut off). If it is not returned full, refuelling is invoiced | Conflicts with the sample, where the departure gauge is below ½ (R-06) |
| 6 | **A rental day runs hour to hour, in non-divisible 12-hour blocks with a 59-minute tolerance. Each further hour is billed** | Departure and return **times** matter (R-05, B-05) |
| 6 | Provisional rent is paid up front and the final rent adjusted. The renter authorises payment or debit by v.a.d. | Prepaid and balance lines, remote card charge (B-10) |
| 7 | The security deposit amount is "fixé au recto" (set on the front). Any excess is refunded within one month at most | No front field is labelled « dépôt de garantie » (R-07) |
| 8 | **An extension must be requested at least 48 h in advance, with the matching payment. The lessor may refuse** | Extension workflow (R-11) |
| 9 | Returning the car, its keys and **all its administrative documents** at the agreed place and date ends the rental. Returns must happen during opening hours. If the car is left outside them, the renter keeps custody and risk until opening | A return inspection without the client present is plausible (B-08). Checking car papers and keys at return (R-02) |
| 10 | Fines are the renter's. The card is charged, plus a 25 € fee per fine (FR + EN paragraph) | Renter identity must stay retrievable after the rental (L-06) |
| 11 | Privacy clause citing the 1978 law. Data may be passed to third parties for marketing, with opt-out by letter | Pre-GDPR wording (L-02, L-03) |
| 12 | Jurisdiction: the court of the company's registered office | Legal review (L-02) |

### 2.5 Page 3: DÉPART / RETOUR drawings

These are drawings of the rented model (top, left side, right side, front, rear), with one column for départ and one
for retour. In the sample, damage is marked in the **départ** column of page 3 only. On page 1, though, marks appear
on the **retour** outline and not on the départ outline. The paper process records condition in two places that
don't agree. `RECOMMENDED`: the app keeps one record (photos per inspection). Per the brief, photos replace both the
page-1 outlines and this page. Confirm in R-01.

### 2.6 What the sample shows about current practice

- Times are not written, only dates.
- Computed values (km driven, extra km, extra days, HT and VAT totals) are left blank.
- The return signature is blank on a completed rental.
- The card fields are blank (no imprint, expiry or CVV).
- An invoice reference is added by hand.
- The fuel type is highlighted by hand.
- The renter was under 25 at departure, yet the « Assurance −25 ans » line is blank (R-04).
- The rental line, the package price and TOTAL TTC are the same amount, with HT and VAT blank, so amounts seem to be entered including VAT (B-05).
- The return fuel mark is below the departure mark, yet no « Carburant » charge is billed (R-06).
- Blank areas are acceptable (brief, and meeting note « Champ vide ✓ »). The PDF must render empty optional fields cleanly.

## 3. `model_template.pdf`: the target presentation

### 3.1 What it is

It is a completed pick-up agreement from another rental company (Drive Luxury, Geneva/Paris). `RECOMMENDED`: use it
**as a layout reference only**. Don't copy its logo, wording or terms: they are another company's text, written under
Swiss law.

### 3.2 Pages and fields

| Page | Title | Fields and blocks |
|---|---|---|
| 1 | Car Rental Agreement (Pick up) | Pick-up location + date/time · Drop-off location + date/time · Reservation no. · Flight/Train · Renter (title, first name, last name) · DOB · Email · Mobile · Street & house no. · ZIP · City · State · Country · Additional info · Passport/ID no. + issue/expiry · Driver's licence no. + issue/expiry · No. of days · Car make · Licence plate · Fuel type · Rules paragraph (return at the same fuel level or a penalty per quarter tank, cleaning penalty, lost keys and lockouts, fines) · Additional driver · Deposit · Services included (insurance + liability per damage) · Liability paragraph · Traffic-violations paragraph · Declaration "I have read… and agree with the Terms and Conditions (URL)" · Pick-up driver · Renter signature (bottom of page, no box) |
| 2 | Vehicle Inspection | Reservation no. · Renter · Driver's licence no. · Renter DOB · Car make · Licence plate · Issue/expiry · Car papers (yes/no) · Tank reading (%) · Kilometres · Clean inside (yes/no) · Clean outside (yes/no) · Navigation/GPS (yes/no) · Generic car outline with damage marks · Declaration "I have inspected the vehicle at pick-up and/or drop-off and accept its condition" · Signature & date (pick-up) |
| 3 | Terms & Conditions | Full terms in English, signed at the bottom |

Every page has the logo at the top right and the company addresses and contacts in the footer.

### 3.3 Presentation traits: what "moving toward the model" can mean (confirm in R-01)

- One topic per page: agreement, then vehicle inspection, then terms.
- Full-width label/value tables with shaded label cells, and no dotted lines to fill in.
- Dates printed with times.
- Logo at the top right and a contact footer on every page.
- One signature per page. On pages 1 and 2 it sits under a one-sentence declaration of what is being signed. On page 3 it follows the terms.
- Terms printed in the contract language and signed.

### 3.4 Current vs model: field comparison

The user's instruction is `CONFIRMED`: keep the model's presentation **with every field of the current form**.
This table shows the overlap and what remains open.

| Information | current_template | model_template | Handling |
|---|---|---|---|
| Renter name | one line | title / first / last | Keep. Structure open (R-02) |
| Home address | street, postcode, city | street, ZIP, city, state, country | Keep. Add a country? (R-03) |
| Local / contact address + phone | yes | – | Keep |
| Email | – | yes | `OPEN` (R-02) |
| Phone | « Tél. » lines | Mobile no. | Keep |
| Date of birth | yes (+ a country) | yes | Keep |
| ID document | passport or ID card + country | Passport/ID no. + issue/expiry | Keep. Expiry `OPEN` (R-02) |
| Licence | number | number + issue/expiry | Keep. Dates `OPEN` (R-02, R-04) |
| Additional driver | name, DOB, licence | name | Keep the current fields |
| Departure / return place | « Lieu de retour » only | pick-up and drop-off locations | `OPEN` (R-05) |
| Dates | départ, retour, planned retour | pick-up and drop-off date-time | Keep. Times `OPEN` (R-05) |
| Contract / reservation number | none (invoice ref. handwritten) | Reservation no. | Needed (R-09) |
| Flight / train | – | yes | `OPEN` (R-02) |
| Vehicle: plate, model, colour, fuel type | yes | make, plate, fuel type | Keep the current fields |
| Km out / in / driven / allowed / billed | yes | one km reading | Keep the current fields |
| Fuel | eighths, départ + retour | % (pick-up) | `OPEN` (R-06) |
| Car papers on board | no field, but CGV Art. 9 requires the documents back at return | yes/no | `OPEN` (R-02) |
| Cleanliness, GPS | – | yes/no | `OPEN` (R-02) |
| Rates (daily tiers, package, extra day/km) | yes | – | Keep |
| Deductible (theft, accident) | yes | liability per damage | Keep the current fields |
| Deposit | CGV Art. 7 / « Total prépayé »? | Deposit | `OPEN` (R-07) |
| Pricing lines, HT / TVA / TTC, prepaid, balance | yes | – | Keep. Invoice status `OPEN` (B-04) |
| Payment method | ESP / CC | – | Keep |
| Card imprint, expiry, CVV | yes | – | Not recommended (B-10) |
| Intermediary + phone | yes | – | Keep. Meaning `OPEN` (R-08) |
| Staff / pick-up driver | – | yes | `OPEN` (R-19) |
| Damage recording | outline + legend + 2 lines, plus the model-drawings page | generic outline | Photos only (`CONFIRMED`, brief). Comments `OPEN` (R-10) |
| Signatures | 4 zones on page 1 | 1 per page | `OPEN` (B-06) |
| Terms | French, on the back | English, page 3 | Contract language chosen per contract (`CONFIRMED`). English text `OPEN` (R-17) |

## 4. `meeting_client.pdf`: notes and wireframe

### 4.1 Transcription

Uncertain readings are marked (?).

**Flow sketch** (headed « U-J » (?), probably "user journey")

- An unlabelled stick figure → **Retour / Départ**
  - **Retour** → (dashed arrow) → box « Contrat rempli — à fournir : photo sortie »
  - **Départ** (choix véhicule) → « Crée client » or « Choisir client » → « Template .pdf » → (arrow) → **the same box**

So both flows end in the box that says « à fournir : photo sortie » (exit photos to provide).

**Notes**

- « Template : », followed by a list of what the contract template must cover:
  - « tarif complet »
  - « champ vide ✓ »
  - « jauge essence »
  - « droit de km »
  - « modification »
- « Palette : gold / black »

**Wireframes**

- **Home:** buttons « Retour » and « Départ ». Below them, a list with a sort/filter control (↑↓ ≡) and a « + » button. Rows « En cours » (?) with a thumbnail, « Dispo » and « Maintenance ». An arrow goes from Maintenance to « Reset status ou pas ».
- **Retour:** « Km retour = km total », « Jauge », « Dégât », « V = avec client » (?), and « Signature client sur tt page » (client signature on every page), written inside this wireframe.
- **Départ:** « Choisi client + 2nd driver ».

### 4.2 What it confirms or adds

- `CONFIRMED`: Départ and Retour are the two entry points. Clients are created or selected. There is an additional driver. The template must cover the full pricing, empty fields, the fuel gauge, the km allowance and modifications. The vehicle list shows the statuses Dispo / En cours / Maintenance. The palette is gold/black.
- « Reset status ou pas » next to Maintenance literally means "reset the status or not". `INTERPRETATION`: it matches the brief's rule of refreshing the reference condition only when appropriate (after a damage repair). See R-14.
- « Signature client sur tt page » is written in the Retour wireframe. The brief says the same thing for the Départ ("every relevant page"). See B-06.
- Added by the notes: « tarif complet », meaning pricing belongs in the template (the brief is silent). See B-04 and B-05.
- « à fournir : photo sortie » sits in the box where both flows end. The most natural reading is "exit (departure) photos to provide", i.e. fresh photos at each departure, which differs from the brief (B-09).
- « V = avec client »: the V is probably a tick, so "done with the client", meaning the inspection is done with the client present (B-08).

## 5. Contradictions between sources

| ID | Topic | One source says | Another source says | Question |
|---|---|---|---|---|
| C-01 | Signing order | Brief: sign (step 4), then choose language (5), then generate the PDF (6) | A signature should approve a document the client has seen, in a language they understand | B-07 |
| C-02 | Signature placement | Current form: 4 zones with distinct meanings, all on page 1 | Model: one per page. Notes (Retour wireframe): "every page". Brief (Départ): "every relevant page" | B-06 |
| C-03 | Return signature | Brief: the client signs again at return | Completed sample: return signature blank. Terms Art. 9 provide for a car left outside opening hours | B-08 |
| C-04 | Damage information | Brief (template section): "only photos" | Brief (Retour step 4): record damage + photos + comments. Current form: free-text lines | R-10 |
| C-05 | Departure photos | Brief: inherit the vehicle's existing photos | Notes: both flows end in « à fournir : photo sortie » (exit photos to provide) | B-09 |
| C-06 | Fuel | Current form: eighths. Terms: full tank at departure | Model: %. Sample: departure below ½ | R-06 |
| C-07 | Pricing and invoice | Brief: no pricing or invoicing requirement. Model: no pricing | Current form: contract + invoice with full pricing. Notes: « tarif complet » | B-04, B-05 |
| C-08 | Times | Labels say « date & heure » | Sample has dates only. Terms bill per 12 h with a 59-min tolerance | R-05 |
| C-09 | Licence age | Terms Art. 1: licence held for more than one year | No licence issue date on the form (the model has one) | R-04 |
| C-10 | Deposit | Terms Art. 7: deposit amount on the front | No such labelled field (closest: « Total prépayé / Total deposit », « Franchise minimum ») | R-07 |
| C-11 | Extensions | Brief: staff amend the active contract | Terms Art. 8: request ≥ 48 h ahead with payment, lessor may refuse. The client is often not on site | R-11 |

## 6. Gaps: not covered by any source

- Contract numbering (no printed number): R-09
- Meaning of « Intermédiaire » and the « Tél. » beside it: R-08
- Departure place, delivery (« Livraison » line), return place: R-05
- Place of birth vs nationality next to the date of birth, and the number of additional drivers: R-03
- Who may do what (roles): R-16
- Vehicle statuses beyond Dispo / En cours / Maintenance, and future bookings: R-13
- Content of a maintenance record, and partial repairs: R-14
- Cancelling a signed contract, swapping the vehicle, early return: R-12
- Which client documents are required, and how long they are kept: R-15, L-03
- The English text of the general terms: R-17
- Devices, connectivity, Mac availability, hosting and ownership: B-01 to B-03, B-11, T-01 to T-07

## 7. Who owns which information (derived from the contract, input to the domain model)

| Entity | Information |
|---|---|
| Company (settings) | Name, logo, address, SIRET, APE code, phone numbers, VAT rate, general terms text per language |
| Vehicle | Plate, make/model, colour, fuel type, current km, current fuel level, status, condition photos, known damage. No default rates: prices are typed by staff (B-05) |
| Client (renter or additional driver) | Name, home/billing address, phone(s), licence number, date of birth (+ place/nationality?), ID document type, number and country, uploaded documents |
| Rental contract | Number, renter, additional driver(s), vehicle, intermediary, planned return date (and time?), return place, rates and package, km allowance, extra-km price, deductible amounts, payment method, language, status, revisions, generated PDFs, signatures S1 and S2 |
| Departure (check-out) | Date-time, km out, fuel out, photos, comments, signature S3 |
| Return (check-in) | Date-time, km in, fuel in, photos, new damage or RAS, comments, signature S4 |
| Charges | Rental, extra days, extra km, young-driver insurance, additional driver, delivery, options I–III, fuel, miscellaneous, HT, VAT, TTC, prepaid, balance |
| Computed by the app | Km driven and extra km billed (default for R-06). Totals, costs and the number of days are typed by staff (F-06). See [ADR-0006](../adr/0006-contract-only-scope.md) |
