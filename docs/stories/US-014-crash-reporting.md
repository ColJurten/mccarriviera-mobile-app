# US-014 · Report crashes without personal data

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E1 · Access, security and monitoring | Should | P0 | S | To do |

- **Depends on:** [US-005](US-005-eas-builds-and-internal-distribution.md)
- **Decisions:** [ADR-0017](../adr/0017-crash-reporting.md) · [ADR-0013](../adr/0013-personal-device-data-protection.md)
- **Open points:** F-02, L-03 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want crashes on the staff phones reported to me without any client data, so that I can fix problems without a Mac.

## Acceptance criteria

- [ ] Sentry is set up with `@sentry/react-native` and its Expo config plugin. The organisation uses the EU (Germany) data storage location, chosen at creation, and belongs to the company (default for F-02).
- [ ] `sendDefaultPii` is off, with no screenshots and no session replay. Events and breadcrumbs are cleaned of request bodies, URLs with query strings, and text typed by staff. The user is identified by the staff profile ID only.
- [ ] Each event carries the app version, build number and update ID. Source maps are uploaded during EAS builds and updates, so stack traces are readable.
- [ ] A test crash in a preview build shows up with a readable stack trace and no personal data.
- [ ] The data processing agreement is tracked in [US-092](US-092-legal-and-privacy-checklist.md).
