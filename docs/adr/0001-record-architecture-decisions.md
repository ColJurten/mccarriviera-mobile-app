# ADR-0001: Record architecture decisions

| Status | Date | Decided by | Based on |
|---|---|---|---|
| **Accepted** | 2026-10-07 (updated 2026-10-09) | Developer, with the client's answers | — |

## Context

One developer, helped by coding agents, builds and maintains this app. Decisions have to be written down once, be
easy to find, and never change silently. The brief also asks that every major technology choice explains why it fits
this project, what its downsides are and which alternatives were considered.

## Decision

- Each significant decision is an ADR in `docs/adr/`, named `NNNN-short-title.md` and numbered in order.
- Every ADR has the same sections: status table, Context, Decision, Consequences, Alternatives considered, Revisit when, Implemented by.
- Status values:
  - **Proposed**: waiting for an answer. Build against it only where a story says so.
  - **Accepted**: in force.
  - **Superseded by ADR-NNNN**: replaced by a later ADR.
  - **Deprecated**: no longer applies.
- An accepted ADR is not rewritten. To change a decision, write a new ADR that supersedes it, and only update the old one's status line.
- ADRs cite the question IDs they come from (`B-xx`, `F-xx`, `R-xx`…) and the stories that implement them. [`README.md`](README.md) in this folder is the index.
- Labels inside an ADR:
  - "(default for X-nn)": the choice applied to a question that is still open. Every default is listed in [`../discovery/open-questions.md`](../discovery/open-questions.md) § Defaults, so it can be confirmed or changed.
  - `RECOMMENDED`: a technical choice that no question asked about.
  - `INTERPRETATION`: a reading of an answer that has to be confirmed.
- When the question behind a default or an interpretation is answered, the ADR is updated in place: the answer replaces the default, and a dated line in the ADR's **Changes** section records it, with the question ID. Any other change to a decision gets a new ADR that supersedes the old one.

## Consequences

- Agents and future maintainers can see why the code is the way it is.
- Each decision costs a little writing time.

## Alternatives considered

| Option | Why not chosen |
|---|---|
| One running decisions log | Hard to link to, and it grows unreadable |
| Decisions kept in tickets or chat | Get lost, and coding agents can't read them |

## Revisit when

The project gets a second team, or the format stops being useful.

## Changes

- 2026-10-09: added the rule for applying answered defaults in place.

## Implemented by

- [US-002](../stories/US-002-repository-and-agent-guidance.md): Set up the repository, checks and agent guidance
