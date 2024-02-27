# Record architecture decisions

## Status

Accepted

## Context

We need to record the architectural decisions (including context, motivations and consequences) made on this project: those that affect the
structure, non-functional characteristics, dependencies or construction techniques.

## Decision

We will use Architecture Decision Records,
 [as described by Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions):

* ADRs will be numbered sequentially and monotonically. Numbers will not be reused.
* If a decision is reversed, we will keep the old one around, but mark it as superseded. (It's still relevant to know
  that it was the decision, but is no longer the decision.)

We will keep ADRs in this repository under `docs/decisions/NNNN-{short-title}.md`.

Besides pure architectural decisions, will also record other relevant technical decisions, such as on code style, developer tooling or documentation strategies.

## Consequences
> The motivation behind previous decisions is visible for everyone, present and future. Nobody is left scratching their heads to understand, "What were they thinking?" and the time to change old decisions will be clear from changes in the project's context.

---
See Michael Nygard's article, linked above.
