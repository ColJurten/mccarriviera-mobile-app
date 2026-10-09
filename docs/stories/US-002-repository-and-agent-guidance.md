# US-002 · Set up the repository, checks and agent guidance

| Epic | Priority | Phase | Size | Status |
|---|---|---|---|---|
| E0 · Foundations | Must | P0 | S | To do |

- **Depends on:** —
- **Decisions:** [ADR-0016](../adr/0016-repository-environments-ci.md) · [ADR-0001](../adr/0001-record-architecture-decisions.md)
- **Open points:** T-04, N-06 (see [open questions](../discovery/open-questions.md))

## Story

As the developer, I want one repository for the app, the database and the docs, with automatic checks, so that every change is reviewed and coding agents work from the same references.

## Acceptance criteria

- [ ] A private GitHub repository on the developer's account (F-02; default for T-04), with folders `app/`, `supabase/`, `docs/`, `scripts/`.
- [ ] `docs/` contains this documentation set. The scanned reference PDFs are not committed (ignored, or kept outside the repo).
- [ ] A root `AGENTS.md`, and a `CLAUDE.md` that points to it, say: start from `docs/README.md`, follow the ADRs, never use real customer data, and how to run the checks (default for N-06).
- [ ] TypeScript strict mode, ESLint and Prettier are configured. `npm run check` runs typecheck, lint and tests.
- [ ] GitHub Actions runs `check` on every pull request. The main branch is protected: a PR and green checks are required.
- [ ] A pull-request template asks for the story ID and any ADR it touches.
- [ ] Secrets are never committed: `.env*` is ignored and `.env.example` lists the variables.
- [ ] `docs/testing.md` describes the test layers: unit tests, database tests, HTML snapshot tests of the contract, and the checklist run on a real iPhone.
