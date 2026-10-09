# ADR-0017: Report crashes to an EU-hosted service with personal data removed

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 | Developer, with the client's answers | RECOMMENDED (no question) · F-02 · L-03 |

## Context

- There is no Mac, so native crash logs from the phones can't be read with Xcode ([ADR-0002](0002-mobile-stack-expo.md)).
- EAS build logs only show build failures, not crashes on the phones.
- The app handles personal data, so crash reports must not carry any ([ADR-0013](0013-personal-device-data-protection.md)).

## Decision

- **Service:** use **Sentry** (`@sentry/react-native` with its Expo config plugin), with the EU (Germany) data storage location chosen when the organisation is created. Start on the free developer plan. This is `RECOMMENDED`.
- **No personal data in reports:**
  - `sendDefaultPii` is off;
  - no screenshots and no session replay;
  - events and breadcrumbs are cleaned of request bodies, URLs with query strings, and text typed by staff;
  - the user is identified by the staff profile ID only.
- **Readable stack traces:** each event carries the app version, build number and update ID. Source maps are uploaded during EAS builds and updates.
- **Ownership:** the Sentry organisation belongs to the company, and the developer is a member (default for F-02). A data processing agreement is accepted (L-03, [US-092](../stories/US-092-legal-and-privacy-checklist.md)).

## Consequences

**Positive**

- Crashes and errors on the staff phones become visible and debuggable without a Mac.

**Negative / risks**

- One more processor of (scrubbed) data, so the data processing agreement and the record of processing must include it.
- The scrubbing rules must be kept up to date as screens are added.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| No crash reporting | Crashes on staff phones would go unnoticed and couldn't be investigated without a Mac |
| Firebase Crashlytics | Adds Google services, and data residency is harder to control |
| Self-hosted GlitchTip (Sentry-compatible) | One more server to run and patch |

## Revisit when

The client refuses another processor (fall back to self-hosting), or the free plan's limits are reached.

## Implemented by

- [US-014](../stories/US-014-crash-reporting.md): Report crashes without personal data
- [US-092](../stories/US-092-legal-and-privacy-checklist.md): Send the legal and privacy questions, and close them before go-live
