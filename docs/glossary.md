# Glossary: French / English rental vocabulary

Terms as they appear in the brief, the current contract (`current_template.pdf`), its general terms (CGV) and the
meeting notes. Code and the database use English identifiers. The UI and the contract use the French or English
labels below.

## Workflow

| French | English | Meaning in this project |
|---|---|---|
| Départ | Check-out / pick-up | Start of a rental: vehicle handed over, contract signed |
| Retour | Check-in / return / drop-off | End of a rental: return km, fuel and condition recorded |
| Restitution | Return (of the vehicle) | CGV Art. 9: returning car, keys and papers ends the rental |
| Prolongation | Extension | CGV Art. 8: extending the rental period |
| Avenant | Amendment | A change to a signed contract, stored as a new revision and printed on its own page (ADR-0007, F-08) |
| Photos de référence | Reference photo set | The vehicle's current set of condition photos, reused at each Départ. Database table `condition_baselines` (ADR-0008) |
| Décompte final | Final statement | The pricing lines as completed at the Retour, printed in the Retour section (F-08) |
| Importée | Imported | A photo picked from the phone's library rather than taken in the app (ADR-0014) |
| État des lieux | Condition inspection | Inspection at départ or retour |
| Descriptif véhicule | Vehicle condition description | The condition boxes on the current form |
| Dégât | Damage | |
| Éraflure · Bosse · Manque | Scratch · Dent · Missing part | Legend of the current damage diagram (to be replaced by photos) |
| RAS (Rien à signaler) | Nothing to report | Return inspection with no new damage |
| Retour en attente de signature | Check-in awaiting signature | Return data entered, but the client hasn't signed yet. The car stays « En cours » (F-04) |
| Reset (du statut / de l'état) | Status / baseline reset | Brief: new reference condition photos after a damage repair, only when appropriate. Meeting notes: « Reset status ou pas » next to Maintenance |

## Vehicle statuses (meeting notes, plus « Archivé »)

| French | English | Note |
|---|---|---|
| Dispo(nible) | Available | Database code `available` |
| En cours | Rented / in use | `INTERPRETATION` of the handwriting « Encours ». Used as the app's badge label. Database code `rented` |
| Maintenance | Maintenance | Database code `maintenance` |
| Archivé | Archived | Sold or retired, kept for history. Database code `archived` (default for R-13) |

## People and parties

| French | English | Meaning |
|---|---|---|
| Locataire / Rentier / Conducteur | Renter / main driver | The client signing the contract |
| 2ème conducteur · Conducteur sup(plémentaire) | Additional driver | Also a pricing line (« Conducteur sup ») |
| Intermédiaire | Intermediary | Printed on the form. Exact meaning is open (R-08) |
| Loueur · Société de location | Lessor · Rental company | MC Car Riviera |

## Client data

| French | English |
|---|---|
| Adresse de facturation | Billing / home address |
| Adresse locale | Local / contact address during the stay |
| Permis de conduire | Driving licence |
| Carte d'identité · Passeport | ID card · Passport |
| Date de naissance | Date of birth |

## Vehicle, mileage and fuel

| French | English | Meaning |
|---|---|---|
| Immat(riculation) | Registration plate | |
| Modèle | Model | Make + model on one line on the current form |
| Kms départ · Kms retour | Km out · Km in | Odometer at check-out and check-in |
| Kms parcourus | Km driven | Km in − km out (computed) |
| Kms inclus · Droit de km | Km allowance | Km included in the price |
| Kms facturés | Extra km billed | Km driven above the allowance |
| Jauge essence | Fuel gauge | Eighths from E to F on the current form |
| Sans plomb 95 | Unleaded 95 | Fuel type |
| Carburant | Fuel | Also the refuelling charge line |

## Pricing and payment

| French | English | Meaning |
|---|---|---|
| Tarif/J. (1 à 3 j · 4 à 7 j) | Daily rate (1–3 days · 4–7 days) | Two rate tiers |
| Jour(s) sup | Extra day(s) | |
| Km sup | Extra km | Price per extra km |
| Forfait … € pour … jours | Package: … € for … days | |
| Location | Rental | Base rental amount |
| Assurance −25 ans | Young-driver insurance | Surcharge for drivers under 25 |
| Livraison | Delivery | Delivering the car to the client |
| Option I / II / III | Options | Unnamed option lines |
| Divers | Miscellaneous | |
| HT · TVA · TTC | Excl. VAT · VAT · Incl. VAT | VAT printed at 20 % |
| Total prépayé | Prepaid total | Printed sub-label says "Total deposit". Meaning is open (R-07) |
| Solde | Balance due | |
| Franchise (vol · accident responsable) | Deductible / excess (theft · at-fault accident) | Renter's maximum liability (CGV Art. 5-4) |
| Dépôt de garantie | Security deposit | CGV Art. 7 |
| Loyer provisionnel | Provisional rent | CGV Art. 6: paid up front, adjusted at the end |
| Mode de paiement: ESP · CC | Payment method: cash · card | |
| Empreinte carte de crédit | Card imprint | Paper imprint area on the current form (see B-10) |
| v.a.d. (vente à distance) | Remote (card-not-present) charge | |
| Facture | Invoice | The current form is titled « Contrat / Facture location » (B-04) |

## Documents

| French | English |
|---|---|
| Contrat de location | Rental agreement / contract |
| CGV, Conditions générales de location | General terms and conditions of rental |
| Recto · Verso | Front · Back (of the paper contract) |
