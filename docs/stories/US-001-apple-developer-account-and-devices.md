# US-001 · Open the Apple developer account and register the iPhones

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | S | To do |

- **Depends on:** —
- **Decisions:** [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md) · [ADR-0018](../adr/0018-development-and-test-devices.md)
- **Open points:** F-01 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want the company's Apple Developer Program membership with the staff phones and my test iPhone registered, so that I can install builds on them without the App Store.

## Acceptance criteria

- [ ] The company holds the Apple Developer Program membership as an organisation, and the developer is added as Admin (F-02).
- [ ] Enrolment starts on day one, because these steps can take a week or more. The company requests its free D-U-N-S number if it has none. It already has the website and the e-mail address on its own domain that Apple asks for (F-02), and a person who can sign for the company completes the enrolment.
- [ ] The membership (99 USD/year) is active, and the developer's Apple account can manage certificates and profiles.
- [ ] The two staff iPhones and the developer's test iPhone (his partner's, F-05) are registered with `eas device:create`, each under a recognisable name (for example "Staff 1 – iPhone").
- [ ] For each phone, the model and iOS version are recorded and checked against the minimum iOS version of the Expo SDK in use. A phone that's too old is updated first (default for F-01).
- [ ] Each staff member confirms, when their phone is registered, that they accept the requirements on their personal phone: Developer Mode on (iOS 16 and later), a device passcode, and a reinstall once a year (F-03: likely yes).
- [ ] The membership renewal date and the certificate expiry date are recorded in the runbook ([US-093](US-093-operations-runbook.md)), with a reminder 30 days before.

## Notes

- Ad Hoc allows up to 100 iPhones per membership year. Apple's licence covers devices owned by people affiliated with the account holder, which is why the company should hold the membership ([ADR-0003](../adr/0003-ios-distribution-ad-hoc.md)).
- Apple ID passwords are never shared. Signing credentials are managed by EAS.
- The staff phone models aren't known yet (F-01). SDK 56 already required iOS 16.4 or later; check the current SDK's minimum in Expo's documentation before registering.
