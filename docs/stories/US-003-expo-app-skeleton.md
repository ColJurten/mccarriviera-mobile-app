# US-003 · Create the Expo app skeleton

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | M | To do |

- **Depends on:** [US-002](US-002-repository-and-agent-guidance.md)
- **Decisions:** [ADR-0002](../adr/0002-mobile-stack-expo.md) · [ADR-0011](../adr/0011-localisation.md) · [ADR-0012](../adr/0012-authentication-and-authorisation.md)
- **Open points:** N-01, R-18 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want an Expo app with navigation, theme and translations in place, so that features can be added screen by screen.

## Acceptance criteria

- [ ] An Expo app (latest stable SDK at project start) in `app/`, with TypeScript, Expo Router and continuous native generation (no committed `ios/` folder).
- [ ] These screens exist as stubs: Sign-in, Home, Vehicle detail, Client detail, Départ flow, Retour flow, Settings.
- [ ] Theme tokens for the gold/black palette are used by every component. Placeholder values are used until the brand assets arrive (default for R-18). Text scales with the iPhone's text-size setting.
- [ ] Translations are set up with French as the app language (default for N-01). A test fails if a key is missing from a catalogue.
- [ ] TanStack Query (in memory, no persister) and a Supabase client typed from the generated schema types are wired. The environment (staging or production) comes from the build profile.
- [ ] A global error screen in French never shows raw stack traces or personal data.
- [ ] `docs/screens.md` lists the screens and the navigation between them, as a Mermaid diagram that matches the stubs.

## Notes

- The skeleton is first checked on an iPhone in [US-005](US-005-eas-builds-and-internal-distribution.md), which produces the first development build.
