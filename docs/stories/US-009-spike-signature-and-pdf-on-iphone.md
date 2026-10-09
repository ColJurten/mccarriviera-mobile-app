# US-009 · Spike: prove signature capture and PDF generation on a real iPhone

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | S | To do |

- **Depends on:** [US-005](US-005-eas-builds-and-internal-distribution.md)
- **Decisions:** [ADR-0009](../adr/0009-signatures.md) · [ADR-0010](../adr/0010-contract-pdf-generation.md) · [ADR-0002](../adr/0002-mobile-stack-expo.md) · [ADR-0018](../adr/0018-development-and-test-devices.md)
- **Open points:** — (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want to try the riskiest technical parts on a real iPhone before building features, so that the signature and PDF choices are proven early.

## Acceptance criteria

- [ ] Two signature pads are tried on an iPhone: react-native-signature-canvas and a Skia-based pad. One is chosen for smooth strokes, a clean PNG export at print resolution, and access to stroke points.
- [ ] A test PDF is produced with expo-print, using explicit A4 page blocks. It has a contract page, a photo section that continues over several pages (30 thumbnails), terms over several pages, and 5 amendment blocks.
- [ ] Every page, including continuation pages, repeats the header, the footer and the signature block at the bottom right, at the same position.
- [ ] The same document in French and in English keeps the slots in the same position (B-07).
- [ ] A typical contract (10 photos) is generated in under 5 seconds on the oldest staff phone. The 30-photo case is measured.
- [ ] The PDF opens correctly in Files, Mail and WhatsApp.
- [ ] PDF rendering is judged on the iPhone only: the Android emulator renders PDFs differently ([ADR-0018](../adr/0018-development-and-test-devices.md)).
- [ ] Findings and the chosen library are recorded. If the approach has to change, a new ADR supersedes ADR-0010.

## Notes

- This is throwaway code. Only what is learned is kept.
