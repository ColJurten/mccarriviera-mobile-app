# Open questions

> **Status (2026-10-09, evening):** all blocking questions B-01 to B-11 are answered and turned into decisions ([`../adr/`](../adr/README.md)). Of the follow-ups, F-02 to F-07, F-09 and F-10 are answered, F-08 partly, and F-01 is checked when the phones are registered. F-11 (where the files live) was opened on 2026-10-09, and R-10 gained a fifth question the same evening, found while drawing the Retour. The R, T and N questions are still open. Where the backlog needed an answer to move on, it uses a **default**, listed in § Defaults so you can confirm or change it.
> **How to answer:** write under each **Answer** line, or reply with the IDs (for example "B-03: b").
> Some questions show a **Suggested default**. This is a recommendation, not an assumption, and it is used only if you confirm it.
> **Owners:** **You** (developer) · **Client** (MC Car Riviera) · **Lawyer** · **Accountant** · **Bank/PSP**.
> Sources are analysed in [`source-analysis.md`](source-analysis.md) (contradictions `C-xx` are listed there).

## Index

| ID | Topic | Owner | Status |
|---|---|---|---|
| **B-01** | Mac access and app technology | You + client | Answered → [ADR-0002](../adr/0002-mobile-stack-expo.md) |
| **B-02** | Devices: type, ownership, number | Client | Answered → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md), [ADR-0013](../adr/0013-personal-device-data-protection.md); follow-up F-01 |
| **B-03** | Connectivity and offline behaviour | Client | Answered → [ADR-0005](../adr/0005-online-only.md) |
| **B-04** | Contract only, or contract + invoice | Client + accountant | Answered → [ADR-0006](../adr/0006-contract-only-scope.md) |
| **B-05** | How prices are filled in | Client | Answered → [ADR-0006](../adr/0006-contract-only-scope.md); totals answered in F-06 |
| **B-06** | Which signatures, and where they appear | Client (+ lawyer) | Answered → [ADR-0009](../adr/0009-signatures.md); position answered in F-08 |
| **B-07** | Signing order: preview before signature | You + client | Answered → [ADR-0009](../adr/0009-signatures.md) |
| **B-08** | Return without the client present | Client | Answered → [ADR-0009](../adr/0009-signatures.md); return signature made mandatory by F-04 |
| **B-09** | Photos at departure | Client | Answered → [ADR-0008](../adr/0008-vehicle-condition-model.md); F-10 answered |
| **B-10** | Payment-card data and the deposit | Client | Answered → [ADR-0006](../adr/0006-contract-only-scope.md); reading to confirm in F-09 |
| **B-11** | Ownership, hosting, budget, maintenance | You + client | Answered → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md), [ADR-0004](../adr/0004-backend-supabase.md), [ADR-0015](../adr/0015-backups.md); follow-ups F-02, F-07 |
| **F-01** | Staff phones: models and iOS versions | Client | Unknown; checked at registration (US-001), default applied |
| **F-02** | Who holds the accounts (Apple, Expo, GitHub, Supabase, backups, Sentry) | You + client | Answered: Apple → the company; the others → the developer |
| **F-03** | Requirements on personal phones: Developer Mode, passcode, yearly reinstall | Client (staff) | Answered: likely yes; confirmed at registration |
| **F-04** | Return signature | Client | Answered: mandatory → [ADR-0009](../adr/0009-signatures.md) |
| **F-05** | A test iPhone for the developer | You | Answered: the partner's iPhone → [ADR-0018](../adr/0018-development-and-test-devices.md) |
| **F-06** | Totals, costs and number of days | Client | Answered: typed by staff → [ADR-0006](../adr/0006-contract-only-scope.md) |
| **F-07** | Hosting budget after the free plan | Client | Answered: covered by the developer's maintenance fee |
| **F-08** | Where the signatures go | Client (+ lawyer) | Partly answered: bottom right of every page; amendment pages still a default |
| **F-09** | Card fields on the contract | Client (+ lawyer) | Answered: kept (last four digits and expiry only; CVV box empty) |
| **F-10** | Interior and dashboard photos | Client | Answered: optional → [ADR-0008](../adr/0008-vehicle-condition-model.md) |
| **F-11** | Where the files live: Supabase Storage or an S3-compatible bucket | You | Open, default applied (Supabase Storage) |
| R-01 | Layout of the new contract | Client | Open, default applied |
| R-02 | Fields only the model template has | Client | Open, default applied |
| R-03 | Client fields and additional drivers | Client | Open, default applied |
| R-04 | Licence and age checks | Client | Open, default applied |
| R-05 | Dates, times and places | Client | Open, default applied |
| R-06 | Fuel and mileage | Client | Open, default applied |
| R-07 | Deductible, deposit and prepayment | Client | Open, default applied |
| R-08 | Intermediary | Client | Open, default applied |
| R-09 | Contract number | Client (+ accountant) | Open, default applied |
| R-10 | Recording damage | Client | Open, default applied; Q5 added on 2026-10-09 (taking back a photo or damage entry before the client signs) |
| R-11 | Extension and other changes after signature | Client | Open, default applied |
| R-12 | Cancellation, vehicle swap, early return | Client | Open, default applied |
| R-13 | Vehicle statuses and future bookings | Client | Open, default applied |
| R-14 | Maintenance and the condition reset | Client | Open, default applied |
| R-15 | Client documents | Client | Open, default applied |
| R-16 | Roles and permissions | Client | Open, default applied |
| R-17 | Languages and the English general terms | Client (+ lawyer) | Open, default applied |
| R-18 | Branding | Client | Open, default applied (placeholder theme) |
| R-19 | Staff and company on the contract | Client | Open, default applied |
| T-01 | Apple accounts | Client | Superseded by F-02 (Ad Hoc needs no Apple Business account) |
| T-02 | Volumes and existing data | Client | Partly answered (2 staff); import is optional (US-090) |
| T-03 | Staff sign-in | You + client | Open, default applied |
| T-04 | Existing cloud accounts and tooling | You + client | Open, default applied |
| T-05 | PDF archive and copies on devices | Client | Open, default applied |
| T-06 | Minimum iOS version | Client | Moved to F-01 |
| T-07 | Timeline and team | You | Partly answered (solo developer); test device → F-05 |
| N-01 – N-06 | Nice to clarify | Various | Open; defaults applied for N-01, N-02, N-03, N-06 |
| L-01 – L-07 | External confirmation before go-live | Lawyer / accountant / bank | Open; tracked in US-092 |

---

## Blocking: needed before the architecture or the core workflows can be finalised

### B-01 · Mac access and app technology
**Owner:** you + client · **Changes:** the whole app architecture, tooling, signature/PDF libraries, build and release pipeline.

You develop on Windows + WSL. A native Swift/SwiftUI app needs Xcode, and Xcode only runs on macOS.

- **a) Native Swift/SwiftUI:** needs a Mac (a base Mac mini is enough) or a rented cloud Mac.
- **b) React Native + Expo (TypeScript):** develop on Windows, iOS builds run in the cloud, and testing happens on a real iPhone/iPad (no iOS simulator on Windows).
- **c) Flutter (Dart):** iOS builds and on-device debugging still need a Mac or a cloud build service.
- **d) Installable web app (PWA):** no Apple distribution at all, but weaker camera, offline storage and file handling on iOS.

1. Can you (or the client) buy or rent a Mac?
2. Is a *native* iOS app a hard client requirement, or is the real requirement "works well on the staff iPhones/iPads"?
3. Will anyone else maintain the code later, and in which language?

**Suggested default:** without a Mac, b). With a Mac, a) and b) are both reasonable, and I'll compare them in an ADR once you've answered.

> **Answer (2026-10-07):** "I cannot get hands on a mac device to dev."
>
> The same answer was given again in full on 2026-10-07.
>
> **Decision:** b) React Native + Expo, built in the cloud with EAS. No Mac is needed, whether owned or rented, and the result is a normal installed iOS app. → [ADR-0002](../adr/0002-mobile-stack-expo.md)
>
> **B-01a: closed.** Expo makes a Mac unnecessary, so the cross-platform question no longer arises.
>
> **Consequence:** there is no iOS simulator on Windows, so testing needs a real iPhone (F-05).

### B-02 · Devices
**Owner:** client · **Changes:** screen layouts and signing area, distribution method, lost-device security.

1. iPhone, iPad or both? (An iPad gives the client more room to sign.)
2. Company-owned devices or staff's own phones? Company devices can receive the app silently and be locked or wiped remotely. Personal devices can't be managed the same way.
3. How many devices and staff users at launch?
4. Is any device management (MDM) already in place?

> **Answer (2026-10-07):** "There are 2 employees in the company; they both will use their personal device for this."
>
> **Recorded:** 2 staff users on 2 personal devices, with no company-owned devices.
>
> **Decisions:**
> - Builds are installed on the registered personal iPhones as Ad Hoc builds → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md). This needs Developer Mode on each phone (F-03).
> - Client data on personal phones is kept to a minimum, with an app lock, server-side revocation and no stored business data → [ADR-0013](../adr/0013-personal-device-data-protection.md). The company's device-use rule is in L-03.
>
> **B-02a → F-01:** are both devices iPhones (no iPad, no Android), and which models and iOS versions?

### B-03 · Connectivity and offline behaviour
**Owner:** client · **Changes:** data architecture (local database, sync, conflicts), on-device encryption, effort.

Where do Départs and Retours happen: agency car park, underground garages, deliveries to hotels, villas or airports? Is mobile data reliable there? What must still work without a connection?

- **a) Online only:** Départ and Retour need a connection. This is the simplest.
- **b) Online to start and sign:** photos and the PDF upload in the background if the connection drops. Moderate effort.
- **c) Fully offline:** Départ and Retour work offline and sync later. This is the most complex: an encrypted local database, a sync queue and conflict rules (for example, two staff renting the same car while offline).

**Suggested default:** b), unless handovers regularly happen without coverage.

> **Answer (2026-10-07):** "May be no and over since we fetch/update contrat through the DB the handover might be inconvenient for this purpose."
>
> The same answer was given again in full on 2026-10-07.
>
> **Decision:** no offline mode. Départ, Retour and every data change need a connection.
> - Uploads retry automatically while the app is open.
> - The signature is uploaded before the contract is marked signed.
> - A PDF that failed to upload can be regenerated from the stored data.
>
> → [ADR-0005](../adr/0005-online-only.md)
>
> **B-03a: closed.** If there's no signal at a handover place, the fallback (for example a paper contract) is the company's decision.

### B-04 · Contract only, or contract + invoice?
**Owner:** client + accountant · **Changes:** numbering, VAT logic, PDF title and mentions, retention, legal exposure.

Today's document is titled « Contrat / Facture location » and has HT / TVA / TTC / prepaid / balance lines. But « FACT 1336 » is handwritten on it, which suggests invoices are numbered elsewhere.

- **a) Contract only:** the app produces the rental contract. Prices appear for information, and invoices stay in the accounting or invoicing software.
- **b) Contract + legal invoice:** the app's PDF is also the invoice. Then invoice numbers must be sequential with no gaps, the legal invoice mentions and VAT rules apply, retention is longer, and the French e-invoicing reform applies. Receiving e-invoices has been mandatory since 1 Sept 2026. Issuing e-invoices and e-reporting (which covers sales to individuals) apply to SMEs and micro-businesses from 1 Sept 2027.

Who issues invoices today, and with what software?

**Suggested default:** a), which keeps the app out of invoicing compliance. Confirm with the client's accountant (L-04).

> **Answer (2026-10-07):** "the PDF contains the legal info just like the template provided"
>
> **Decision:** the PDF reproduces all of the template's legal information. Billing and payment happen outside the app (B-10), so the app doesn't issue invoices. The title stays « CONTRAT / FACTURE LOCATION », as on the template, unless the accountant says a document titled « facture » must follow invoice rules (L-04). → [ADR-0006](../adr/0006-contract-only-scope.md)

### B-05 · How prices are filled in
**Owner:** client · **Changes:** data model (rates per vehicle), return workflow, PDF pricing block, testing effort.

The meeting notes say « Template : tarif complet ». Which of these?

- **a) Typed by staff:** staff type each amount. The app adds up HT / TVA / TTC and the balance, and computes km driven and extra km.
- **b) Pre-filled:** as a), plus each vehicle's default rates (daily tiers for 1–3 and 4–7 days, package, km allowance, extra-km price, deductible amounts) pre-filled and editable, and extras suggested at return (extra km, extra time under the 12-hour rule in the terms, fuel).
- **c) Pricing engine:** seasons, promotions, categories.

Also:

1. Are prices entered including VAT (TTC) or excluding it (HT)? The sample suggests TTC: the rental, the package and TOTAL TTC are the same amount, and HT and VAT are blank.
2. What do the two « Jours sup » rows mean, and the « Km inclus » that appears both in the rates box and in the vehicle box?

**Suggested default:** a) or b) for the MVP, and c) later.

> **Answer (2026-10-07):** "Staff members type the price manually"
>
> **Decision:** staff type every price line. The app calculates no prices from rates. → [ADR-0006](../adr/0006-contract-only-scope.md)
>
> **Totals (F-06, answered 2026-10-09):** totals, costs and the number of rental days are typed by staff too. Km driven and extra km are computed by default (R-06), because they are measurements, not prices. Question 1 no longer matters. Question 2 only affects labels: both rows are kept as typed fields.

### B-06 · Which signatures, and where they appear
**Owner:** client (+ lawyer, L-01) · **Changes:** signing screens, signature storage, PDF layout.

Today the client signs four times on page 1: S1 next to the deductible block, S2 under the terms acceptance and card authorisation, S3 in the departure condition box, S4 in the return condition box. The model has one signature per page. The brief (Départ) says "every relevant page", and the notes (Retour wireframe) say "every page". Also, terms Art. 3 say that signing the contract means accepting the vehicle's condition.

- **a) One signature per visit:** one signature at Départ, stamped in S1, S2, S3 and on every page. One signature at Retour, stamped in S4 and on the return page(s).
- **b) One signature per statement:** a separate signature for each approval at Départ (deductible, terms, condition). This is closest to the paper form but takes more taps.
- **c) Tick each statement, then sign once:** at Départ the client ticks each statement on screen (deductible, terms, card authorisation, condition) and signs once. The PDF shows the signature in every zone and records which statements were accepted, and when.

Which pages must carry it: the contract page, the condition page, every page of the terms?

**Suggested default:** c). It is fast at the counter and still records consent per statement.

> **Answer (2026-10-07):** "one signature on every page"
>
> **Decision:** the client signs once at the Départ, and that signature is placed on every page. At the Retour, the client signs once more, and that signature is placed on every page of the final PDF. Every signature is stored with an evidence record. → [ADR-0009](../adr/0009-signatures.md)
>
> **Position (F-08, answered 2026-10-09):** the signature sits at the bottom right of every page.
>
> **One exception, still a default (F-08):** amendment pages, created after the Départ, carry their own signature there instead of the departure signature. This way the client's signature never appears next to values they didn't approve.

### B-07 · Signing order
**Owner:** you + client · **Changes:** Départ and Retour flows, PDF pipeline (a preview is needed before signing).

In the brief, the client signs (step 4) before the contract language is chosen (step 5) and before the PDF exists (step 6). So the client would sign without having seen the contract in their language. Can the order become: choose language → contract preview → client reads → client signs → final PDF? The same question applies at Retour.

**Suggested default:** yes.

> **Answer (2026-10-07):** "signing always occupies the same location whether it be FR or EN"
>
> **Decision:** the answer is about **where** the signature sits: the slots are at the same place in both languages. It doesn't ask to change **when** the client signs, so the brief's order is kept: sign first, then choose the language. One signature works for either PDF. → [ADR-0009](../adr/0009-signatures.md)
>
> `RECOMMENDED` mitigation: before signing, a recap screen shows the key terms and lets the client read the general terms in French or English (US-054).

### B-08 · Return without the client present
**Owner:** client · **Changes:** Retour flow, contract statuses, evidence recorded.

The completed sample has no return signature (S4). The terms (Art. 9) provide for a car left outside opening hours, with the renter keeping custody and risk until the agency opens. What happens when the client isn't there (key drop, car left out of hours, collection from a hotel), or is there but refuses to sign (disputed damage)?

- **a) Close without the client:** staff completes the return alone. The contract records "returned without client signature" with a reason, the staff identity and the photos. The final PDF is shared with the client afterwards.
- **b) Client signature required:** the return can't be closed without it.

**Suggested default:** a), with "client refused to sign" as a separate reason.

> **Answer (2026-10-07):** "that is a company problem not application"
>
> **Updated by F-04 (2026-10-09):** the return signature is mandatory. The app doesn't handle an absent client: the Retour stays « en attente de signature » until the client signs, and the company deals with the client outside the app. → [ADR-0009](../adr/0009-signatures.md), US-074

### B-09 · Photos at departure
**Owner:** client · **Changes:** Départ flow and duration, storage volume, strength of evidence.

The brief says a Départ inherits the vehicle's existing photos. In the meeting notes, both flows end in a box that says « à fournir : photo sortie » (exit photos to provide).

- **a) Reuse:** use the vehicle's current reference photos. This is fastest.
- **b) Fresh set:** take a new set at every Départ. This gives the strongest evidence: dated photos of this handover.
- **c) Confirm:** show the reference photos, staff confirms "unchanged", takes at least a dashboard photo (km + fuel) and adds photos of anything different.

Also:

1. Which angles make up a standard set? For example: front, rear, both sides, four corners, wheels and tyres, interior, dashboard. The terms single out tyres, spare wheel and accessories (Art. 3), and underbody, roof and soft top (Art. 5-2).
2. Is the same set required at Retour?

**Suggested default:** b) at both Départ and Retour, guided by a fixed list of angles, with the previous photos shown side by side for comparison. This is the client's call.

> **Answer (2026-10-07):** "reuse the vehicle's reference photos, that avoids a fresh photo session if not needed"
>
> **Decision:** a Départ reuses the vehicle's current reference set, plus any open damage. Staff add photos only when something looks different. New reference sets are taken when a vehicle is added and after a damage repair. → [ADR-0008](../adr/0008-vehicle-condition-model.md)
>
> - **Question 1:** the list of angles uses a default (see § Defaults). It has no dashboard photo, because a reused dashboard photo would show an old odometer reading.
> - **Question 2:** answered by the brief (Retour, step 4): at a Retour, photos are taken only for new damage, otherwise « RAS ».
> - **Follow-up F-10:** an optional dashboard photo at each handover.

### B-10 · Payment-card data and the deposit
**Owner:** client (+ bank/PSP, L-05) · **Changes:** security scope, data model, printed contract fields.

The form has a card-imprint area, the expiry date and the CVV, and the client authorises remote charges (v.a.d.). PCI DSS forbids keeping a CVV after authorisation, and storing card numbers would bring the app into PCI DSS scope.

**Proposal:** the app records the payment method, the card brand and, at most, the last four digits and the reference of the deposit or pre-authorisation taken on the payment terminal. It never records the full number, expiry date or CVV, and those printed fields are removed.

1. How is the deposit or deductible guarantee taken today: terminal pre-authorisation, manual imprinter, online payment link?
2. Is the proposal acceptable?

> **Answer (2026-10-07):** "everything concerning billing and payment will be handled elsewhere than this application, we only need this for the contract"
>
> **Decision:** the app handles no payment or billing, and never holds a full card number or a CVV. → [ADR-0006](../adr/0006-contract-only-scope.md)
>
> **Updated by F-09 (2026-10-09):** the card fields stay on the contract, limited to the card brand, the last four digits and the expiry date, with an empty CVV box. The payment method (ESP/CC) also stays as a simple choice.

### B-11 · Ownership, hosting, budget and maintenance
**Owner:** you + client · **Changes:** backend choice, distribution setup, long-term support.

1. Whose Apple Developer account publishes the app, and whose cloud accounts hold the data: the client's (recommended, so they own their app and data and you are added as a member) or yours?
2. What is the monthly hosting budget ceiling?
3. Must data stay in the EU? (Recommended: yes.)
4. Who maintains it after delivery (bug fixes, iOS updates, backups, support)?
5. Do you prefer a managed service or self-hosting? Self-hosting is possible, but someone has to run, patch, monitor and back it up.

> **Answer (2026-10-07):** "We currently do not have an apple account dedicated to this project, we can host the DB in the cheapest way possible, I am the dev and will maintain the project if needed"
>
> **Decisions:**
> - A new Apple Developer Program membership (99 USD/year), held by the company by default, for Ad Hoc distribution → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md).
> - Supabase in the EU on the Free plan → [ADR-0004](../adr/0004-backend-supabase.md), with nightly encrypted backups → [ADR-0015](../adr/0015-backups.md).
> - The developer maintains the app, with a runbook (US-093) and crash reporting ([ADR-0017](../adr/0017-crash-reporting.md)).
>
> **Follow-ups:** F-02 (who holds the accounts), F-07 (budget once the free plan's storage is full).

---

## Follow-ups from the 2026-10-07 answers

These came out of the answers above and out of the review of the decisions. The answers of 2026-10-09 are recorded under each one.

- **Answered:** F-02, F-03, F-04, F-05, F-06, F-07, F-09, F-10. F-08 is partly answered.
- **Checked during the work:** F-01, when the phones are registered (US-001).
- **Still open, with a default meanwhile:** the rest of F-08, and F-11 (opened on 2026-10-09).

### F-01 · Staff phones (was B-02a)
**Owner:** client · **Needed by:** US-001

1. Are both phones iPhones, with no iPad and no Android?
2. Which models and iOS versions? Recent Expo SDKs need a recent iOS: SDK 56 already required iOS 16.4 or later.

> **Answer (2026-10-09):** "I do not have the staff exact phone model"
>
> **Recorded:** checked when the phones are registered (US-001). Each phone's model and iOS version are recorded and compared with the minimum iOS version of the Expo SDK in use. A phone that's too old is updated first.
>
> **Default for F-01:** both phones are iPhones that can run that iOS version. If one turns out to be an Android phone, Expo could build for Android too, but that is outside the current scope and would be a new decision.

### F-02 · Who holds the accounts
**Owner:** you + client · **Needed by:** US-001, US-002, US-004, US-008, US-014

The app needs a few online accounts. "Holding" one means whose name and payment details it's under, and so who owns it if you stop working on the project.

| Account | What it's for | Cost |
|---|---|---|
| Apple Developer Program | Lets the app be signed and installed on the registered iPhones | 99 USD/year |
| Expo (EAS) | Builds the app in the cloud and keeps the signing certificate | Free plan |
| GitHub | Holds the code; runs the automatic checks and the nightly backup | Free |
| Supabase | Hosts the backend: database, staff logins and file storage | Free plan to start ([ADR-0004](../adr/0004-backend-supabase.md)) |
| Backup storage (for example Backblaze B2) | Keeps the encrypted nightly backups | Free tier |
| Sentry | Receives crash reports from the phones | Free plan |

**Default:** the company holds all of them, and you are added as admin, so MC Car Riviera owns its app, its data and its signing identity.

For an Apple account in the company's name, Apple asks for:

- a D-U-N-S number (free);
- a person who can sign for the company;
- a work e-mail address on the company's own domain;
- a public website on that domain.

An individual membership in your name is faster, but a weaker fit: Apple's licence covers devices of people affiliated with the account holder, and the client's staff aren't affiliated with you. Use it only as a temporary fallback.

Still open:

1. Should the accounts be in the company's name (default) or yours?
2. Does the company have a website on its own domain, and an e-mail address on that domain?

> **Answer (2026-10-09):** "what account are you talking about?" The table above explains them.
>
> **Answer (2026-10-09, later):** "yes the account for apple developer will be owned by them, all the rest you mentioned will be under my management (expo, github, supabase, backup, monitoring ...)"
>
> **Decision:**
> - The **Apple Developer Program** account is the company's, as an organisation. The company has the website and the e-mail address on its own domain that Apple asks for. You are added as Admin. → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md)
> - **Expo, GitHub, Supabase, the backup storage and Sentry** are your accounts. → ADR-0004, ADR-0015, ADR-0016, ADR-0017
>
> **Consequences:**
> - Client personal data is hosted in your accounts, so you act as the company's **data processor**. A written data processing agreement between MC Car Riviera and you is needed, listing your sub-processors (L-03, US-092).
> - The runbook gets a **handover procedure**: how the Supabase project, the repository, the Expo project and the backup keys pass to the company or a new provider if the collaboration ends (US-093).
> - The company keeps a sealed copy of the backup keys (ADR-0015).

### F-03 · Requirements on the staff's personal phones
**Owner:** client (both staff) · **Needed by:** US-001

Ad Hoc distribution puts three requirements on each phone:

1. **Developer Mode** turned on (Settings → Privacy & Security, iOS 16 and later).
2. A **device passcode**, needed for the app's Face ID lock.
3. A **reinstall once a year**, when the signing certificate is renewed.

> **Answer (2026-10-09):** "they would probably be open to use developer mode if that is the only way to get the app on their phone without going through the app store"
>
> **Recorded:** likely yes. It is the only way: for a company this size, Ad Hoc is the only method that never goes through the App Store. Unlisted and Custom apps are hidden from the public, but Apple reviews them and they are installed from the App Store app. Each staff member confirms the three requirements when their phone is registered (US-001). → [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md)

### F-04 · Return signature (reading of B-08)
**Owner:** client · **Needed by:** US-074

> **Answer (2026-10-09):** "the return signature is mandatory just like the departure signature"
>
> **Decision:** the return signature is mandatory. A Retour can't be completed without it. If the client isn't there, the Retour is saved « en attente de signature », and the car stays « En cours » until the client signs (`RECOMMENDED`). How the company reaches the client is outside the app (B-08). → [ADR-0009](../adr/0009-signatures.md), US-070, US-074, US-075

### F-05 · A test iPhone for the developer
**Owner:** you · **Needed by:** US-005, US-009

> **Answer (2026-10-09):** "I have my partner's iPhone — but isn't there a way to emulate locally an iPhone when developing this app?"
>
> **Recorded:** the partner's iPhone is the test device. It only gets development and preview builds, which use staging and its synthetic data.
>
> **Emulating an iPhone:** not on Windows. Apple's iOS Simulator is part of Xcode, which only runs on macOS. The closest options:
>
> - an **Android emulator** on Windows runs the same app code. It's the chosen tool for day-to-day UI work, with iOS-specific checks (Face ID, camera, sharing, PDF) on the iPhone;
> - **Expo's cloud iOS simulator** (EAS Simulator) streams an iOS simulator to the browser, but it's a waitlist-only preview for now;
> - **third-party cloud simulators** (for example Appetize.io) have limited free use and are slower.
>
> → [ADR-0018](../adr/0018-development-and-test-devices.md)

### F-06 · Totals
**Owner:** client · **Needed by:** US-052, US-073

> **Answer (2026-10-09):** "yes totals, costs, total days for the rental contract"
>
> **Decision:** totals, costs and the number of rental days are typed by staff. The app calculates none of them. Km driven and extra km are still computed (default for R-06). → [ADR-0006](../adr/0006-contract-only-scope.md)
>
> `INTERPRETATION`: the number of days goes in the current form's fields (« Forfait … pour … jours » and « J / Sup »). No separate « Nombre de jours » line is added, unlike the model template's "No of Day(s)". Say if you want one.

### F-07 · Hosting budget after the free plan
**Owner:** client · **Needed by:** before the pilot (US-091)

The app on the phone is only the front end. The backend runs at a cloud provider, Supabase ([ADR-0004](../adr/0004-backend-supabase.md)), which hosts two things:

- the **database**: text such as clients, contracts and their history. It stays small.
- the **file storage**: vehicle photos, scanned licences and IDs, signatures and the contract PDFs. This is what grows.

The free plan includes 1 GB of files. At roughly 5 MB per rental (photos, PDFs, documents), that's about 200 rentals. When it's full, there are two options:

1. **Supabase Pro**, $25/month (recommended): 100 GB of files, 8 GB of database, daily backups, and no pausing after a quiet week.
2. **Cheaper storage for the files**, for example Cloudflare R2 (10 GB free). It needs extra development for access control and signed links, so it costs more work and adds risk.

Which does the client prefer? A rough number of rentals per month would also show when this happens (T-02).

> **Answer (2026-10-09):** "what storage are you talking about? I thought that the application was just the 'frontend', all the backend DB are hosted on a cloud provider". The explanation is above.
>
> **Answer (2026-10-09, later):** "this will be part of my 'maintenance' fee so I will be the one handling this"
>
> **Decision:** the hosting costs are covered by your maintenance fee, and you decide when and how to scale the storage. Whether the files should move to cheaper S3-compatible storage is F-11. → [ADR-0004](../adr/0004-backend-supabase.md)

### F-08 · Where the signatures go
**Owner:** client (+ lawyer, L-01) · **Needed by:** US-040, US-064, US-073, US-075

> **Answer (2026-10-09):** "always bottom right of the paperwork"
>
> **Decision:** a signature block sits at the bottom right of every page, in the same place in French and English. It holds the departure and the return signatures. → [ADR-0009](../adr/0009-signatures.md), [ADR-0010](../adr/0010-contract-pdf-generation.md)
>
> **Still a default:**
>
> - an amendment page (for example an extension) carries the amendment's own signature in that block, or « Sans signature du client », instead of the departure signature;
> - page 1 keeps the values signed at the Départ;
> - return values and final amounts go in the Retour section.
>
> This way the client's signature is never next to values they didn't approve. Say if page 1 should show the latest values instead.

### F-09 · Card fields on the contract (reading of B-10)
**Owner:** client (+ lawyer, L-02) · **Needed by:** US-006, US-040, US-052

The current paper contract has three fields for the client's credit card, in its « Mode de paiement » box:

- the card imprint area (« Empreinte carte de crédit — Type carte »);
- the card's expiry date (« Date de validité »);
- its security code (« CVV »).

Payment is handled outside the app (B-10), and card-industry rules (PCI DSS) forbid keeping a CVV once a payment has been authorised. The proposal is therefore to **remove these three fields** from the digital contract.

What stays: the ESP / CC boxes (cash or card) and the VISA / AMEX / AUTRE boxes of the deductible block.

One knock-on: the acceptance text says the client authorises charges to « la carte de crédit désignée sur ce contrat ». With no card recorded, the lawyer should reword it (L-02).

**Default:** remove the three fields; the wording goes to the lawyer.

> **Answer (2026-10-09):** "what card fields are removed?" The explanation is above.
>
> **Answer (2026-10-09, later):** "keep those fields just in case"
>
> **Decision:** the three fields stay on the contract, with these limits (`RECOMMENDED`):
> - the imprint area shows the card brand and the **last four digits** only;
> - the **expiry date** (MM/YY) can be typed;
> - the **CVV** box is printed but always left empty.
>
> The app has no field for a full card number or a CVV. Card-industry rules forbid keeping a CVV once a payment is authorised, and these PDFs travel by e-mail and messaging. With the last four digits recorded, the acceptance text's « carte désignée sur ce contrat » has something to refer to; the lawyer still reviews it (L-02). → [ADR-0006](../adr/0006-contract-only-scope.md)

### F-10 · Interior and dashboard photos
**Owner:** client · **Needed by:** US-026, US-053, US-072

> **Answer (2026-10-09):** "yes the inside of the car is optional"
>
> **Decision:** interior photos are optional, both in the reference set and at handovers, and so is the dashboard photo (km + fuel). The reference set has 8 required exterior angles. → [ADR-0008](../adr/0008-vehicle-condition-model.md)
>
> `INTERPRETATION`: « the inside of the car » covers both the interior angle and the dashboard photo.

### F-11 · Where the files live: Supabase Storage or an S3-compatible bucket
**Owner:** you (you pay the hosting, F-07) · **Needed by:** US-006

You asked whether a regular Postgres at a cloud provider, or S3 storage, would be cheaper than Supabase, given two staff and very little traffic.

Traffic isn't what costs money at this size. Two things do: the **storage volume** (mostly files) and **what you'd have to build and run yourself**.

A phone app can't talk to Postgres directly: the database credentials would sit on the phones. Something has to stand in between, to:

- handle the staff logins;
- check every request against the access rules;
- hand out temporary links to the private files.

Supabase provides that layer: Auth, an API with row-level security, and Storage with signed links. With plain Postgres, you'd write and host it yourself.

| Option | What runs where | Approx. cost per month, before VAT (checked 2026-10-09) | Extra work |
|---|---|---|---|
| **A. Supabase for everything** (current plan) | Logins, database, API and files on Supabase | €0 until about 1 GB of files (≈ 200 rentals), then $25 (Pro) | None |
| **B. Supabase + S3 for the files** (recommended) | Logins, database and API on Supabase Free; files in an EU S3-compatible bucket (e.g. Scaleway Object Storage, Paris) | About €0.016 per GB of files, so cents for years. The text data stays within the free 500 MB for years | 1–2 days: a small server function that checks the staff session and hands out temporary upload and download links |
| **C. Managed Postgres + S3 + your own API** | Managed Postgres (e.g. Scaleway, smallest instance), an S3 bucket, a small server for your API | About €11.40 (database) + €5.50 (server) + cents (files): about €17 | Weeks: logins, sessions, permissions, the API itself, TLS, updates, monitoring |
| **D. Self-host everything on one server** | Postgres and the API on a small server (e.g. Hetzner CX23, €5.49 since June 2026), files in S3. It can be self-hosted Supabase, which is open source | About €6–8 | You run it: updates, security, backups and monitoring, for a system holding ID documents |

**Recommendation: B.** It keeps everything Supabase does well, and the $25/month step disappears for years. If costs ever matter more, D with self-hosted Supabase runs the same app code, with no rewrite.

Caveats with B: it's still the Supabase Free plan, so there's no service guarantee, and a project pauses after a week without activity. Daily use and the nightly backup should prevent that. The file storage provider also becomes one of your sub-processors (L-03).

The same comparison, with a sketch of each option, is on the last two pages of [`../architecture/architecture.pdf`](../architecture/architecture.pdf).

**Default:** until you choose, the files stay in Supabase Storage (option A), as decided in ADR-0004 and ADR-0014.

> **Answer:**

---

## Defaults

While the F, R, T, N and L questions are open, the ADRs and stories use these defaults so work can start.

- Each default is marked as "default for X-nn" in the stories and ADRs.
- If an answer differs, update the listed stories **before** building them.
- Defaults stay in force until the matching question is answered.

| Question | Default used | Where |
|---|---|---|
| B-09 Q1 | Reference set of 8 exterior photos from the in-app camera: front, front-left, left, rear-left, rear, rear-right, right, front-right. Interior photos optional (F-10) | ADR-0008, US-026 |
| F-01 | Both staff phones are iPhones that can run the Expo SDK's minimum iOS version; checked when they are registered | ADR-0003, US-001 |
| F-11 | The files stay in Supabase Storage, as decided in ADR-0004 and ADR-0014, until the developer chooses between the options in F-11 | ADR-0004, ADR-0014, US-006 |
| F-08 | Signatures at the bottom right of every page (answered). Default part: page 1 shows the contract as signed at the Départ; amendment pages carry the amendment's own signature there; return values and final amounts are in the Retour section | ADR-0009, ADR-0010, US-040, US-064, US-073, US-075 |
| R-01 | PDF pages: contract as signed at the Départ; Départ / Retour (condition, return values, « Décompte final »); general terms; amendments. Photos as thumbnails. Title as on the template | ADR-0010, US-040 |
| R-02 | No model-only field added, apart from the contract number (the field set stays the current template's) | ADR-0010, US-040 |
| R-03 | Mandatory before signing: name, home address, licence number, date of birth, ID number (the fields filled on the completed sample). A country field is added to the address. One additional driver, stored as a client record, with name, date of birth and licence number mandatory | US-031, US-051 |
| R-04 | The app records only: it shows the age, with no warning and no blocking | US-031, US-051 |
| R-05 | Departure and return date and time default to "now" and can be edited. Planned return: date required, time optional. Return place: free text | US-052, US-070 |
| R-06 | Fuel in eighths. No electric-car support. No fuel charge calculated. One km allowance per contract. Km driven and extra km computed by the app | ADR-0006, US-053, US-071 |
| R-07 | Fields kept as printed; « Total prépayé » is typed like any other amount. Empty deductible amounts trigger a warning | US-052 |
| R-08 | Intermediary is free text, defaulting to « MC CAR RIVIERA », with an optional phone | US-052 |
| R-09 | Contract number `MCR-YYYY-NNNN`, assigned at signature from a yearly counter. Gaps allowed | ADR-0007, US-006, US-057 |
| R-10 | A damage entry is at least one photo plus a comment. « RAS » is one tap. No damage costs | ADR-0008, US-072 |
| R-11 | Amendable fields as listed in US-061. A reason is required. The client's signature is optional. The 48-hour rule is recorded, not enforced | ADR-0007, ADR-0009, US-061 |
| R-12 | Drafts can be discarded. A signed contract can be voided with a reason before its Retour. No vehicle swap: close the contract and open a new one | ADR-0007, US-056, US-062 |
| R-13 | Statuses: available, rented, maintenance, archived. No future bookings | ADR-0007, US-006, US-025 |
| R-14 | Maintenance kinds: routine, damage repair, other. Partial repairs allowed. Odometer optional. No costs | ADR-0008, US-006, US-080, US-082 |
| R-15 | No document is required before a Départ. A document uploaded by mistake can be deleted | ADR-0014, US-033 |
| R-16 | One staff role with full access. The developer does the admin tasks | ADR-0012 |
| R-17 | English PDF blocked until an approved English text of the terms exists. A signed contract can be regenerated in the other language only if that language's terms existed at signature | ADR-0011, US-041, US-063 |
| R-18 | Placeholder gold/black theme until the brand assets arrive | ADR-0010, US-003, US-040 |
| R-19 | Staff name not printed (it isn't on the current template), but recorded in the audit trail | ADR-0010, US-040 |
| T-03 | Email and password. Face ID app lock when the app opens and after 5 minutes in the background. Password resets done by the developer | ADR-0012, US-010, US-011 |
| T-04 | Private GitHub repository on the developer's account (F-02) | ADR-0016, US-002 |
| T-05 | Every PDF archived in the cloud. PDFs cached on the phone are deleted after 7 days and at sign-out | ADR-0013, US-013 |
| N-01 | Staff app in French, with translation keys ready for English | ADR-0011, US-003 |
| N-02 | The vehicle record holds only the fields the contract needs (plate, model, colour, fuel type, km, fuel, notes). More can be added later | US-022 |
| N-03 | Vehicle list sort and filters as in US-021 | US-021 |
| N-06 | Root `AGENTS.md`, plus a `CLAUDE.md` that points to it | ADR-0016, US-002 |
| L-03 | Nothing is deleted or anonymised until the GDPR answers arrive. US-094 then applies them | ADR-0014, US-094 |
| L-07 | Nothing is deleted until retention periods are known. Backup rotation (30 daily, 12 monthly dumps) is a `RECOMMENDED` setting, not a legal retention period | ADR-0014, US-094 |

---

## Business rules: for the client to decide

### R-01 · Layout of the new contract
Proposed structure (model layout + every current field):

1. **Contract:** header, contract number, renter, additional driver, vehicle, dates and places, km, fuel, rates, deductible, pricing lines and totals, payment method, acceptance text, signatures.
2. **Vehicle condition:** a DÉPART column (time, km, fuel, photos, comments, signature) next to a RETOUR column (time, km, fuel, photos, new damage or RAS, comments, signature).
3. **General terms** in the chosen language, signed.

Confirm the following:

1. The car outline, its legend and the model-drawings page are dropped.
2. How photos appear: thumbnails on the condition page plus a full-size photo annex, thumbnails only, or no photos in the PDF?
3. The title: « Contrat de location » or « Contrat / Facture »? This depends on B-04.

> **Answer:**

### R-02 · Fields only the model template has
Add any of these?

- Email
- First and last name as separate fields
- Title (Mr/Ms)
- Pick-up location
- Flight/train
- ID-document expiry
- Licence issue and expiry dates
- Deposit
- Services/insurance included
- Pick-up driver (staff name)
- Car papers on board (the current terms, Art. 9, already require the documents back at return)
- Clean inside / clean outside
- GPS / equipment

Fuel as a percentage is covered in R-06, and the contract number in R-09.

> **Answer:**

### R-03 · Client fields and additional drivers
On the current form, a renter has: full name, home/billing address (street, postcode, city), phone, local address + phone, licence number, date of birth, and an ID document (passport or ID card) with number and issuing country.

1. Which are mandatory before signing, and which are optional?
2. Should the home address get a country field?
3. Is the country written after the date of birth the place of birth or the nationality? And the country after the ID number: issuing country or nationality?
4. Is the local address part of the client record, or of this rental (it changes with each stay)?
5. Additional drivers: only one, as on the form, or several? Should they be full client records with their own documents?
6. The terms (Art. 1) require every authorised driver to show an ID card or passport, but the form only asks the additional driver for name, date of birth and licence. Should the app add ID fields for the additional driver?

> **Answer:**

### R-04 · Licence and age checks
The terms require a licence held for more than one year, and the pricing block has a « −25 ans » insurance line. In the sample, the renter was under 25 and the line is blank. When a licence is under one year old or a driver is under 25, should the app:

- **a)** only record it,
- **b)** warn, or
- **c)** block the Départ?

Options b) and c) need a licence issue date field.

> **Answer:**

### R-05 · Dates, times and places
1. Should departure and return times be recorded automatically? If so, editable by any staff member or by a manager only?
2. Planned return: date only, or date and time?
3. Departure place (not on the form) and return place: free text, a list (agency, airport, hotels…), or a delivery address?
4. One agency or several?
5. Does the app need opening hours (terms Art. 9)?

> **Answer:**

### R-06 · Fuel and mileage
1. Fuel in eighths (current form) or as a percentage (model)?
2. Any electric or hybrid cars (battery level instead of fuel)?
3. Which return rule applies: the same level as at departure (as in the model), or a full tank (as in your terms, Art. 6)? How is refuelling charged: a price per eighth, or entered by hand? In the sample, the car came back with less fuel and no fuel charge was billed.
4. Is the km allowance a fixed number per contract, or per day × number of days?
5. Is the extra-km price set per vehicle or per contract?
6. Should the app compute km driven and extra km automatically? (**Suggested default:** yes.)

> **Answer:**

### R-07 · Deductible, deposit and prepayment
1. Is « Total prépayé / Total deposit » an advance on the rental or the security deposit?
2. Where should the security deposit amount from terms Art. 7 appear?
3. What does the VISA / AMEX / AUTRE choice record? The card held as guarantee?
4. Are the deductible amounts set per vehicle (defaults) or negotiated per contract?

> **Answer:**

### R-08 · Intermediary
1. What is « Intermédiaire »: a hotel, concierge, agency, website…?
2. Is the « Tél. » beside it the intermediary's phone number?
3. Should it be free text or a managed list? (Tracking commissions would come after the MVP.)

> **Answer:**

### R-09 · Contract number
1. What format (for example MCR-2026-0001)?
2. Does the counter restart each year?
3. Must there be no gaps? This is mandatory if the number is also the invoice number (B-04).
4. Does it replace the invoice number written by hand today, or sit next to it?

> **Answer:**

### R-10 · Recording damage
The brief says "only photos" for the template, and also says "record damage, take photos, add comments" at return.

1. Is a damage entry photos plus a short comment, or should it also have a location (for example "front bumper") and a type (scratch / dent / missing part, as in today's legend)?
2. When there's nothing new, is one tap on « RAS — Rien à signaler » enough?
3. Does the client confirm new damage by signing the return?
4. Are damage costs or charges recorded in the app? (Suggested for the MVP: no.)
5. *(added 2026-10-09)* Before the client signs a Départ or a Retour, can staff take back a photo or a damage entry they added by mistake? Today every photo and damage entry is insert-only from the moment it is saved, so a mistake would be printed on the PDF the client signs. (Suggested: yes. Until the client signs, staff can withdraw it: it stays stored and in the audit trail, marked « retiré », and is left off the PDF. After the signature nothing can change. This changes the database rules in US-006 and US-007 and the screens in US-053 and US-072.)

> **Answer:**

### R-11 · Extension and other changes after signature
1. How do extensions usually happen: in person, by phone, by email or by message?
2. Which fields may change after signature: planned return date/time, return place, additional driver, km allowance, price/options? Anything else?
3. Does a change need a new client signature? If the client isn't on site, how is agreement recorded: an email confirmation attached, a signature at return, or a remote-signing link (which would add an e-signature service)?
4. Should each change produce a dated amendment page (« avenant ») in the PDF?
5. Is the 48-hour rule (terms Art. 8) enforced by the app, or for information only?
6. Who may approve an extension: any staff member or a manager?

**Suggested default:** signed data is never overwritten. Each change creates a new numbered revision recording who, when and why, and earlier signed revisions stay readable.

> **Answer:**

### R-12 · Cancellation, vehicle swap, early return
1. Can a signed contract be cancelled (for example, the client changes their mind before leaving)? By whom? It would be marked void, never deleted.
2. Can unsigned drafts be deleted?
3. After a breakdown or accident, can the vehicle be swapped mid-rental in the MVP, or is the contract closed and a new one opened?
4. Early return: is there any rule (refund, charge)?
5. The terms (Art. 1) let the company end a rental immediately after a serious breach. Should the app record a termination by the company?

> **Answer:**

### R-13 · Vehicle statuses and future bookings
Today the statuses are Dispo (available), En cours (rented) and Maintenance. Proposed additions; tell me which you need:

- **Réservé:** reserved for a future rental. Only needed if future bookings are in scope. Are they?
- **À contrôler / nettoyage:** returned, awaiting inspection or cleaning.
- **Immobilisé:** damaged and not rentable, waiting for repair. Is that different from routine maintenance?
- **Archivé:** sold or retired, kept for history.

> **Answer:**

### R-14 · Maintenance and the condition reset
1. Which kinds of maintenance do you need: servicing, damage repair, tyres, cleaning, roadworthiness test (contrôle technique)…?
2. What should be recorded: dates, garage, description, odometer, cost?
3. Who declares a repair finished?
4. After a partial repair (some damage fixed, some not), should individual damages be marked as repaired?
5. The brief says a full new set of reference photos is required after a damage repair. Confirm this, and confirm it is not required after ordinary maintenance (« Reset status ou pas »).

> **Answer:**

### R-15 · Client documents
1. Which documents are required before a Départ can be signed (licence and ID, both sides?), and which are optional?
2. Are documents also required for the additional driver?
3. Which file types: photos, PDFs?
4. How long should documents be kept? (See L-03.)

> **Answer:**

### R-16 · Roles and permissions
Are all staff equal, or is there a manager/admin role? Who can do each of the following:

- edit vehicles and rates
- delete or anonymise clients
- view ID documents
- void contracts
- approve extensions
- change a vehicle's status
- manage staff accounts
- export data

> **Answer:**

### R-17 · Languages and the English general terms
1. Who writes and approves the English general terms (today only Art. 10 exists in English)?
2. Which version prevails if the two differ?
3. Can a contract signed in one language later be regenerated in the other, as a courtesy copy?
4. Are other languages expected later (for example Italian or German)?

> **Answer:**

### R-18 · Branding
1. « Palette gold/black »: for the app, the PDF, or both?
2. Are brand assets available: a vector or high-resolution logo, exact colours, fonts?

> **Answer:**

### R-19 · Staff and company on the contract
1. Should the PDF show the staff member who handled the Départ and the Retour, like the model's « Pick-up driver »?
2. Does the company need to sign or stamp the contract? Neither form has a company signature today.

> **Answer:**

---

## Technical: infrastructure, devices, deployment

### T-01 · Apple accounts
Private distribution through Apple (a "custom app") needs two accounts. The client needs an **Apple Business** account: it is free, it replaced Apple Business Manager in April 2026, and it includes basic device management. The publisher needs an **Apple Developer Program** membership. Organisation accounts are verified with a **D-U-N-S number**. Custom apps still go through App Review, which needs a demo login and sample data.

1. Does the client have a D-U-N-S number?
2. Does the client have an Apple Developer account?
3. Does the client have an Apple Business account?

> **Superseded (2026-10-07):** Ad Hoc distribution ([ADR-0003](../adr/0003-ios-distribution-ad-hoc.md)) needs no Apple Business account. The remaining question, who holds the developer account, is F-02.

### T-02 · Volumes and existing data
1. Fleet size, rentals per month, number of clients and number of staff?
2. Is there an existing vehicle or client list (Excel, other software) to import?
3. The sample contract is mostly typed, so it is filled on a computer before printing. Which tool is used (Word, a PDF form, other software)? Please share that source file. It has the exact labels, may contain the footnote texts for the signatures, and may hold existing client data.

> **Answer:**

### T-03 · Staff sign-in
1. Individual accounts per staff member (suggested), or shared devices?
2. Does the client use Google Workspace or Microsoft 365, which would allow single sign-on? Or should staff use email with a password or one-time code?
3. Should Face ID unlock the app?

> **Answer:**

### T-04 · Existing cloud accounts and tooling
1. Any existing cloud accounts (Google Cloud, AWS, Azure, OVHcloud, Scaleway…)?
2. Is there a domain name for the backend?
3. Where will the code live (GitHub, GitLab)?

> **Answer:**

### T-05 · PDF archive and copies on devices
1. Should every generated PDF also be archived in the cloud? (Suggested: yes, for audit.)
2. Should PDFs saved on a device be removed after a while (lost-device risk), or stay in the Files app?

> **Answer:**

### T-06 · Minimum iOS version
Which device models and iOS versions do staff use? Supporting only recent iOS versions simplifies development.

> **Moved to F-01.**

### T-07 · Timeline and team
1. What is the target date for a first usable version?
2. Are you working on this alone?
3. How many test devices do you have?

> **Partly answered (2026-10-07):** you are the only developer and maintainer (B-11). The test-device question moved to F-05. The target date is still open; the backlog's rough size is in [`../stories/README.md`](../stories/README.md).

---

## Nice to clarify: useful, but not needed to start

- **N-01** Is the app's own language for staff French only, or French and English?
- **N-02** Which vehicle fields beyond the contract are needed (VIN, year, category, seats, gearbox, insurance, contrôle technique date, next service)?
- **N-03** For the vehicle list: what is the default sort, which filters are needed, and what does each row show (photo, plate, model, status, current renter, expected return)?
- **N-04** Are reports or exports (rentals, revenue, utilisation) needed, or can they wait until after the MVP?
- **N-05** Are reminders for overdue or upcoming returns needed, or can they wait until after the MVP?
- **N-06** Besides `/docs`, do you want a root `CLAUDE.md` / `AGENTS.md` that points coding agents to these docs?

> **Answers:**

---

## External confirmation: not needed to start, needed before go-live

### L-01 · Electronic signature (lawyer)
Is a signature drawn on the staff device, with an audit trail (who, when, which document version, which device), sufficient for these contracts? In EU eIDAS terms, that is a *simple* electronic signature. Or is an *advanced* or *qualified* signature through a trust service provider, or a company certificate seal on the PDF, required?

The brief asked for three things to be kept apart (detailed in [ADR-0009](../adr/0009-signatures.md)):

1. **Signature image on several pages.** A drawn signature stamped onto pages is only a picture. On its own, it doesn't tie the client to the document's content.
2. **Digitally signed PDF (PAdES).** The file is cryptographically locked, so any later change is detectable, and the certificate holder is identified. Here the holder would be the company, unless a trust provider issues a certificate to the client.
3. **Electronic signature.** This is the legal notion: eIDAS levels (simple, advanced, qualified) and French Civil Code art. 1366–1367. A drawn signature with an audit trail is generally a simple one. It is admissible as evidence, but if contested the company must prove it is reliable. Only a qualified signature is presumed reliable.

Also ask:

- Is it acceptable to show the departure signature on every page except amendment pages, with later values printed in their own signed sections (F-08)?
- Is an amendment or a return without the client's signature acceptable (R-11, F-04)?

### L-02 · General terms (lawyer)
Update the terms before they are digitised and translated:

- Art. 11: pre-GDPR wording.
- Art. 1: outdated Civil Code reference.
- Art. 12: jurisdiction clause towards consumers.
- The card-charge authorisation in the acceptance text. It refers to « la carte de crédit désignée sur ce contrat », but the app no longer records a card (F-09).
- Approval of the English version.

### L-03 · GDPR (lawyer or DPO)
- The legal basis for each type of data.
- The information notice for clients.
- Whether keeping copies of ID cards and licences is necessary and proportionate.
- Retention periods for contracts, document copies, signatures and photos.
- Erasure requests versus the obligation to keep contracts: which wins, and when (applied by US-094).
- A data processing agreement between MC Car Riviera (controller) and the developer (processor), since client data is hosted in his accounts (F-02). His sub-processors: Supabase, the backup storage provider, Expo, Sentry, and the file storage provider if F-11 changes it.
- The record of processing activities.
- Staff using their personal phones (B-02): a short written rule for client data on those phones. It should cover what may be shared and where, deleting PDFs, and reporting a lost phone.

### L-04 · Invoicing (accountant)
- The outcome of B-04.
- Numbering rules.
- E-invoicing and e-reporting obligations, and their dates, for this company.
- The link with the accounting software.

### L-05 · Card payments (bank or payment provider)
How to handle remote charges (v.a.d.) and deposit pre-authorisations without the app storing card data.

### L-06 · Traffic fines (lawyer)
Which renter data must be kept, and for how long, to name the driver when a fine arrives after the rental.

### L-07 · Retention (lawyer and accountant)
How long signed contracts, photos, client documents and audit logs must, or may, be kept, and how long backups may keep data that has since been erased.
