# US-005 · Set up EAS builds, internal distribution and over-the-air updates

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | M | To do |

- **Depends on:** [US-001](US-001-apple-developer-account-and-devices.md) · [US-003](US-003-expo-app-skeleton.md)
- **Decisions:** [ADR-0002](../adr/0002-mobile-stack-expo.md) · [ADR-0003](../adr/0003-ios-distribution-ad-hoc.md) · [ADR-0016](../adr/0016-repository-environments-ci.md) · [ADR-0018](../adr/0018-development-and-test-devices.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want reproducible cloud builds that staff install from a link, and over-the-air updates for JavaScript fixes, so that I can ship without a Mac or the App Store.

## Acceptance criteria

- [ ] `eas.json` has three profiles: `development` (development client, staging backend), `preview` (staging backend, internal distribution) and `production` (production backend, internal distribution).
- [ ] EAS manages the iOS credentials: the distribution certificate, and an Ad Hoc provisioning profile that includes the registered devices.
- [ ] A development build runs the US-003 skeleton on the test iPhone (the developer's partner's, F-05) and reloads live from the Windows machine. The phone reaches the Metro bundler in WSL2 through WSL mirrored networking (Windows 11) or `expo start --tunnel`.
- [ ] An Android development build, made with EAS Build, runs the same skeleton on an Android emulator on Windows, for day-to-day UI work (`RECOMMENDED`, [ADR-0018](../adr/0018-development-and-test-devices.md)). It is never distributed.
- [ ] A `preview` build installs on the three registered iPhones from the EAS link, with Developer Mode turned on.
- [ ] EAS Update channels `preview` and `production` exist. A JavaScript-only change published to `preview` reaches the installed preview app the next time it launches.
- [ ] A runtime-version policy prevents an update from reaching a build with incompatible native code.
- [ ] Settings shows the app version, build number and update ID, for support.
- [ ] Builds are triggered deliberately, not on every commit (the free plan includes 15 iOS builds a month).

## Notes

- Adding a phone later means registering it, rebuilding and reinstalling (runbook, US-093).
- The test iPhone belongs to the developer's partner. Development and preview builds use staging, which holds synthetic data only, so no client data reaches it ([ADR-0018](../adr/0018-development-and-test-devices.md)).
