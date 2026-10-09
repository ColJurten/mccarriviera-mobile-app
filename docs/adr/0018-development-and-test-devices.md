# ADR-0018: Develop with an Android emulator on Windows and check iOS on a registered test iPhone

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-09 | Developer, with the client's answers | F-05 (answered) · B-01 |

## Context

- There is no Mac (B-01). Apple's iOS Simulator is part of Xcode, which only runs on macOS, so an iPhone can't be emulated on Windows.
- **F-05** (2026-10-09): the developer can test on his partner's iPhone. It isn't always at hand, and each check on it needs a build installed.
- Most of the app (screens, navigation, forms, data) is the same React Native code on iOS and Android.
- Some parts only behave correctly on iOS: Face ID, the Keychain, the camera, the share sheet, and the PDF, which is rendered by iOS's print engine.

## Decision

- **Test iPhone:** the partner's iPhone is registered as the developer's test device ([US-001](../stories/US-001-apple-developer-account-and-devices.md)), with Developer Mode on.
  - It receives development and preview builds only. They use the **staging** backend, which holds synthetic data only, so no client data reaches it.
  - Production builds go only to the staff phones.
- **Day-to-day UI work:** an Android emulator on Windows (Android Studio), running an Android development build of the same app (`RECOMMENDED`).
  - The Android development build is made with EAS Build. It only needs rebuilding when native modules change.
  - The Metro bundler in WSL2 serves the code to the emulator, through WSL mirrored networking or `expo start --tunnel`.
  - The Android build is a development tool only. The product stays iOS only ([ADR-0003](0003-ios-distribution-ad-hoc.md)).
- **Checked on the iPhone:** every story with a user-facing part is demonstrated on the test iPhone before it is done (Definition of Done). PDF layout, Face ID, the camera and sharing are judged on the iPhone only.
- **Not used for now:**
  - **Expo's cloud iOS simulator (EAS Simulator):** it streams an iOS simulator to the browser from Windows, but in October 2026 it is a limited-access preview, open by waitlist only and not included in any plan. Join the waitlist and revisit when it opens.
  - **Third-party cloud simulators** (for example Appetize.io): they run an iOS simulator build in the browser, with limited free use. Slower than the emulator, and less faithful than the iPhone.
  - **Web preview** (`expo start --web`): most of the native features this app needs don't work in a browser.

## Consequences

**Positive**

- Fast, free day-to-day work without waiting for the iPhone.
- iOS-specific behaviour is still checked on a real iPhone.

**Negative / risks**

- Setting up Android Studio and its emulator on Windows takes some time.
- Android and iOS differ in places, so a screen that works on the emulator can still need fixes on the iPhone. iOS checks shouldn't be left to the end of a story.
- The test iPhone isn't the developer's own, so on-device checks depend on its availability.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| iPhone only | Every check would depend on borrowing the phone and on a new build |
| Rented cloud Mac with Xcode's simulator | Monthly cost and remote-desktop friction (B-01) |
| EAS Simulator | Limited-access preview, waitlist only (October 2026) |
| A dedicated test iPhone | Costs money; possible later if borrowing becomes a bottleneck |

## Revisit when

EAS Simulator becomes generally available, or a dedicated test iPhone is bought.

## Implemented by

- [US-001](../stories/US-001-apple-developer-account-and-devices.md): Open the Apple developer account and register the iPhones
- [US-005](../stories/US-005-eas-builds-and-internal-distribution.md): Set up EAS builds, internal distribution and over-the-air updates
- [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md): Spike: prove signature capture and PDF generation on a real iPhone
