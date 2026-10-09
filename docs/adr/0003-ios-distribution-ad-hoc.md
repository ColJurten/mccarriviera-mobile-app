# ADR-0003: Distribute the app as an Ad Hoc build to registered iPhones, under the company's Apple account

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-02, B-11 · F-02, F-03 (answered) · F-01 |

## Context

- Two employees will use their **personal iPhones** (B-02). The app must not be on the public App Store.
- There is no Apple developer account yet (B-11), and the cheapest workable setup is wanted.
- Apple's options as of October 2026:

| Option | What it implies here |
|---|---|
| **Ad Hoc** (registered devices) | Apple Developer Program at 99 USD/year. Up to 100 iPhones per membership year. Apple's licence allows devices "owned or controlled by You, or owned by individuals who are affiliated with You": the company's staff are affiliated with the company. No App Review. Each new phone must be registered and needs a new build. Certificates and profiles expire every year. On iOS 16 and later, the phone must have **Developer Mode** turned on. |
| **Custom app** through Apple Business | Apple's recommended route for business apps. Every version goes through App Review. The client needs an Apple Business account (free since April 2026, verified with a D-U-N-S number). Installed with redemption codes or on managed devices. Updated like App Store apps. No yearly expiry, no Developer Mode. |
| **Unlisted** App Store app | App Review plus an unlisted-distribution request. Anyone with the link can download it, though the login protects the data. Needs a privacy-policy URL and App Store privacy details. No yearly expiry, no Developer Mode. |
| TestFlight | Builds expire after 90 days. Meant for beta testing, not daily use. |
| Apple Developer Enterprise Program | Requires 100 or more employees. Not eligible. |

## Decision

- **The company holds the membership** (F-02, answered 2026-10-09): an organisation membership of the Apple Developer Program (99 USD/year), with the developer added as Admin. The company has the website and the e-mail address on its own domain that Apple asks for.
- **Apple's requirements for an organisation:**
  - a D-U-N-S number;
  - legal entity status;
  - a person with authority to sign for the company;
  - a work e-mail on the company's domain;
  - a public website on that domain.

  Getting a D-U-N-S number and passing Apple's verification can take a week or more, so this starts on day one ([US-001](../stories/US-001-apple-developer-account-and-devices.md)).
- **If Apple refuses the company's enrolment**, the developer's individual membership is a temporary fallback. It is a weaker fit: the licence covers devices of people affiliated with the account holder, and the client's staff are not affiliated with the developer. Moving to the company's account later costs a re-registration and a rebuild, with no data migration.
- **Distribution:** every build (development, staging, production) goes out with **EAS internal distribution (Ad Hoc)**.
  - Register the two staff iPhones and the developer's test iPhone (his partner's, F-05) with `eas device:create`. The owner opens a link or QR code and installs a small profile.
  - The staff phones' models aren't known yet. At registration, each phone's model and iOS version are recorded and checked against the minimum iOS version of the Expo SDK in use (SDK 56 already required iOS 16.4 or later). A phone that's too old is updated first (default for F-01).
  - Staff install the app from the EAS install link.
  - EAS runs under the developer's Expo account (F-02) and holds the distribution certificate of the company's Apple team, through his Admin access. If the collaboration ends, the company revokes that certificate and issues a new one (handover procedure, [US-093](../stories/US-093-operations-runbook.md)).
  - JavaScript-only fixes ship with EAS Update. Native changes need a new build and a reinstall.
- **Requirements on the personal phones** (F-03):
  - Developer Mode turned on;
  - a device passcode, needed for the app lock ([ADR-0012](0012-authentication-and-authorisation.md));
  - a reinstall once a year, when the certificate is renewed.

  Staff are likely to accept them, since this is the only way to install the app without going through the App Store (F-03, answered 2026-10-09). Each staff member confirms when their phone is registered.
- **No App-Store-free alternative:** for a company this size, Ad Hoc is the only method that never goes through the App Store. Unlisted and Custom apps are hidden from the public, but Apple reviews them and they are installed from the App Store app. The Enterprise program, which avoids the App Store, needs 100 or more employees.
- **Renewal:** the yearly renewal (membership, certificate, profile) is in the runbook, with a reminder 30 days before expiry ([US-093](../stories/US-093-operations-runbook.md)).

## Consequences

**Positive**

- No App Review, no demo account for Apple, no Apple Business setup, no device management.
- The cheapest option: 99 USD a year.
- The company owns its signing identity.

**Negative / risks**

- If the yearly renewal is missed, the app stops opening on staff phones. The runbook and the reminder cover this.
- Staff must turn on Developer Mode on their personal phones (F-03).
- A new or replaced phone needs the developer: register it, rebuild, reinstall. That takes a few minutes plus build time.
- Organisation enrolment can take a week or more (D-U-N-S number, Apple's verification). The company has the website and domain e-mail address Apple asks for (F-02).

## Alternatives considered

The options are in the table above. Custom app and Unlisted both avoid Developer Mode and the yearly reinstall, but they need App Review for every native release. Custom app also needs Apple Business and a D-U-N-S number on the client's side.

## Revisit when

- The client refuses Developer Mode or the yearly reinstall: move to an **Unlisted** App Store app.
- More phones are needed, or the company wants managed devices: move to a **Custom app** through Apple Business.

## Changes

- 2026-10-09: F-03 answered (Developer Mode likely acceptable, confirmed at registration); phone models are checked at registration (F-01); the test iPhone is the developer's partner's (F-05).
- 2026-10-09 (later): F-02 answered: the company holds the Apple account; EAS runs under the developer's Expo account.

## Implemented by

- [US-001](../stories/US-001-apple-developer-account-and-devices.md): Open the Apple developer account and register the iPhones
- [US-005](../stories/US-005-eas-builds-and-internal-distribution.md): Set up EAS builds, internal distribution and over-the-air updates
- [US-091](../stories/US-091-pilot-with-the-staff.md): Pilot with the two staff members
- [US-093](../stories/US-093-operations-runbook.md): Write the operations runbook
