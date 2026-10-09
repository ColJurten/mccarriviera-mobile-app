# Architecture diagrams

UML diagrams of the planned iOS app, back end and database, drawn from the [decisions](../adr/README.md) and [stories](../stories/README.md). First version: 2026-10-09.

- **To read them:** [`architecture.pdf`](architecture.pdf), 15 A4 pages. Each diagram comes with a few key points and the ADRs and stories it is based on. The last two pages compare the hosting options of [F-11](../discovery/open-questions.md) (Supabase, or plain Postgres and S3).
- **To change them:** edit the PlantUML sources (`NN-*.puml`) and regenerate. The SVG files in [`svg/`](svg/) and the PDF are generated; never edit them by hand.

| # | Diagram | UML type | What it shows |
|---|---|---|---|
| 01 | [System overview](svg/01-system-overview.svg) · [source](01-system-overview.puml) | Deployment | What runs where in daily use, how the parts talk, and who holds each account |
| 02 | [Build, release and development](svg/02-build-and-release.svg) · [source](02-build-and-release.puml) | Deployment | From the developer's PC to the staff phones: GitHub, EAS, Apple signing, staging and production |
| 03 | [Front end](svg/03-app-components.svg) · [source](03-app-components.puml) | Component | The Expo app: screens (with their stories), data layer, contract PDF, device services |
| 04 | [Back end](svg/04-backend-components.svg) · [source](04-backend-components.puml) | Component | The Supabase project: Auth, Data API, row-level security, server functions, audit, storage, CI jobs |
| 05 | [Database overview](svg/05-data-overview.svg) · [source](05-data-overview.puml) | Class | The 17 tables and how they relate |
| 06 | [Fleet, photos, damage, maintenance](svg/06-data-fleet.svg) · [source](06-data-fleet.puml) | Class | Fields of `vehicles`, `condition_baselines`, `photos`, `damages`, `maintenance_records` |
| 07 | [Clients, contracts and their terms](svg/07-data-contracts.svg) · [source](07-data-contracts.puml) | Class | Fields of `clients`, `client_documents`, `contracts`, `contract_drivers`, `contract_revisions`, `terms_versions` |
| 08 | [What each handover records](svg/08-data-evidence.svg) · [source](08-data-evidence.puml) | Class | Fields of `inspections`, `signatures`, `contract_documents` |
| 09 | [Contract lifecycle](svg/09-contract-states.svg) · [source](09-contract-states.puml) | State machine | Draft, active (on rental, Retour in progress), closed, void |
| 10 | [Vehicle lifecycle](svg/10-vehicle-states.svg) · [source](10-vehicle-states.puml) | State machine | Available, rented, maintenance, archived |
| 11 | [Départ](svg/11-sequence-depart.svg) · [source](11-sequence-depart.puml) | Sequence | US-050 to US-057, from choosing the car to sharing the signed PDF |
| 12 | [Retour](svg/12-sequence-retour.svg) · [source](12-sequence-retour.puml) | Sequence | US-070 to US-075, with the mandatory signature and « en attente de signature » |
| 13 | [Hosting options](svg/13-hosting-options.svg) · [source](13-hosting-options.puml) | Deployment sketch | The four options of F-11 side by side |

## Conventions

- **Colours** (shared look in [`style.iuml`](style.iuml)): gold for the company's account (Apple), blue-grey for the developer's accounts (F-02), a dashed outline for an option still open (F-11), a bold black outline for a phone or computer. On the hosting sketch, red marks what the developer would build or run himself.
- **Names:** tables and columns are the working names from [US-006](../stories/US-006-core-database-schema-and-rls.md). Once the migrations exist, they are the reference and the class diagrams follow them.
- **IDs in labels** (US-xxx, ADR-xxxx, F-xx, R-xx) tie each element back to the backlog and the open questions.
- **PlantUML pitfalls:** font sizes must be whole numbers (a size like 10.5 is misread and blows the text up), and class attributes that contain brackets start with `{field}`, otherwise PlantUML draws them as methods.

## Regenerate

Needs Java 17 or later, Graphviz, [PlantUML](https://plantuml.com/download) (drawn with 1.2026.8), the Inter font, and Python 3 with Playwright and its Chromium (`pip install playwright`, then `playwright install chromium`). From the repository root:

```bash
PLANTUML_JAR=/path/to/plantuml.jar python3 docs/architecture/build_pdf.py
```

This renders every `NN-*.puml` to `svg/` and prints `architecture.pdf`. The page titles and key points are in [`build_pdf.py`](build_pdf.py). Commit the sources, the SVG files and the PDF together.

## When to update

- [US-004](../stories/US-004-supabase-environments.md) keeps the system, back-end and sequence diagrams up to date as server functions are added.
- [US-006](../stories/US-006-core-database-schema-and-rls.md) keeps the class diagrams in step with the migrations.
- [US-050](../stories/US-050-start-a-depart.md) and [US-070](../stories/US-070-start-a-retour.md) check the Départ and Retour sequences against the flows as built.
- A change to an ADR that alters a diagram updates the diagram in the same pull request.
