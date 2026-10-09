# ADR-0002: Build the app with Expo (React Native, TypeScript), compiled in the cloud

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | B-01, B-02, B-11 · F-05 (answered) · F-01 |

## Context

- The app runs on the personal iOS devices of the company's two employees (B-02). iPhones are assumed. Their models aren't known yet, so they are checked when the phones are registered (F-01, US-001).
- The developer works on Windows + WSL and can't get a Mac (B-01). Native Swift/SwiftUI development needs Xcode, which only runs on macOS.
- The developer builds and maintains the app alone (B-11) and is new to iOS development.
- The app needs these device features: camera, photo library, file picking, handwritten signature, PDF generation, the iOS share sheet, Keychain storage and Face ID.

## Decision

- Build the app with **React Native and Expo**, in **TypeScript** (strict mode).
- Use the latest stable Expo SDK at project start (SDK 57 was released on 30 June 2026). Upgrade deliberately, one SDK at a time.
- Use Expo's continuous native generation. No `ios/` folder is committed: native configuration lives in `app.config.ts` and config plugins.
- Compile iOS builds in the cloud with **EAS Build**. No local Xcode.
- Test on a real iPhone with a development build (`expo-dev-client`), installed through internal distribution ([ADR-0003](0003-ios-distribution-ad-hoc.md)). There is no iOS simulator on Windows. The test iPhone, and the Android emulator used for day-to-day work, are in [ADR-0018](0018-development-and-test-devices.md).
- The Metro bundler runs in WSL2. The phone reaches it through WSL mirrored networking (Windows 11) or `expo start --tunnel`. Development builds use the staging backend ([ADR-0016](0016-repository-environments-ci.md)).
- Native crash logs can't be read without a Mac, so crashes are reported to an EU-hosted service with personal data removed ([ADR-0017](0017-crash-reporting.md)).
- Core libraries. Changing them goes through an ADR, or through the story that needs the change:
  - **Navigation:** Expo Router.
  - **Server data and forms:** TanStack Query, in memory only, over the typed Supabase client; react-hook-form with zod schemas.
  - **Device:**
    - expo-camera and expo-image-picker (photos), expo-image-manipulator (resize, strip metadata);
    - expo-image, with a memory-only cache for personal data ([ADR-0013](0013-personal-device-data-protection.md));
    - expo-document-picker (files), expo-print (HTML to PDF), expo-sharing (share sheet), expo-file-system;
    - expo-secure-store (Keychain), expo-local-authentication (Face ID), expo-localization.
  - **Signature pad:** chosen in the spike [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md). Candidates are react-native-signature-canvas and a Skia-based pad.

## Consequences

**Positive**

- Everything is developed on Windows, in one language (TypeScript) for the app, the database scripts and any server function.
- The result is a normal installed iOS app with native UI components, so it meets the "iOS application" requirement.
- JavaScript-only fixes ship over the air with EAS Update, without a reinstall.

**Negative / risks**

- The project depends on Expo's services. The free plan includes 15 iOS builds a month in a low-priority queue. The Starter plan costs $19/month if more is needed.
- There is no iOS simulator on Windows. Day-to-day UI work runs on an Android emulator, but every iOS-specific check needs the test iPhone ([ADR-0018](0018-development-and-test-devices.md)).
- Native crashes are harder to investigate without Xcode. Crash reports ([ADR-0017](0017-crash-reporting.md)) and EAS build logs replace Xcode's tools.
- Expo Go in the App Store lags behind new SDKs (it wasn't available there for SDK 56 and 57 at release), so development builds are the normal way to run the app.
- SDK upgrades come every few months and need a little planned time.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| Native Swift / SwiftUI | Best platform integration (PencilKit, VisionKit, PDFKit), but it needs a Mac with Xcode (B-01) |
| Swift on a rented cloud Mac | Remote-desktop development is slow and costs money every month, and B-01 rules out a Mac |
| Flutter (Dart) | A good UI toolkit, but iOS builds and on-device debugging still need macOS or a CI service. Nothing it offers outweighs Expo's cloud builds and over-the-air updates |
| Installable web app (PWA) | No Apple distribution needed, but the client asked for an iOS app, and iOS limits web apps' storage, camera and file handling. Kept as a fallback if Apple distribution becomes a blocker |

## Revisit when

A Mac becomes available and a native-only capability becomes necessary, or Expo's cost or limits become a problem.

## Changes

- 2026-10-09: F-05 answered (the test iPhone is the developer's partner's); the development and test setup moved to ADR-0018.

## Implemented by

- [US-003](../stories/US-003-expo-app-skeleton.md): Create the Expo app skeleton
- [US-005](../stories/US-005-eas-builds-and-internal-distribution.md): Set up EAS builds, internal distribution and over-the-air updates
- [US-009](../stories/US-009-spike-signature-and-pdf-on-iphone.md): Spike: prove signature capture and PDF generation on a real iPhone
