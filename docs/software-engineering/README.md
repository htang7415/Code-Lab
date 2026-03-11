# Software Engineering

This track is about building software that stays correct when code is cheap, change is constant, and AI can generate implementations faster than humans can reason about consequences.

## Purpose

Use this track to learn the engineering responsibilities that still matter most in 2026:
- define stable contracts and invariants
- verify behavior before and after change
- handle state, latency, concurrency, and failure explicitly
- keep systems observable, secure, and operable
- use AI coding tools without giving up review discipline

## First Principles

- AI speeds up implementation. It does not remove the need for contracts, tests, or rollback paths.
- Most expensive bugs happen at boundaries: API boundaries, data boundaries, trust boundaries, and concurrency boundaries.
- Good engineering turns hidden assumptions into explicit schemas, thresholds, tests, alerts, and operating rules.
- Software quality is not just code quality. It also includes delivery safety, production behavior, and incident recovery.

## How To Use This Track

- Start with `tooling`, `apis`, `testing`, and `security-basics`.
- Add `concurrency`, `observability`, `reliability`, and `performance` before going deep on `system-design`.
- Use `python`, `rust`, and `typescript` as implementation support, not as the main curriculum spine.
- Keep `design-patterns` secondary. Prefer patterns that clarify a real boundary or failure mode.
- Finish with `capstones` to combine contracts, tests, operations, and delivery decisions in one workflow.

## Module Authoring Rule

Each software-engineering module should answer the same six questions:
- What contract or invariant matters here?
- What usually fails?
- How do we test it?
- What do we monitor in production?
- What trust boundary exists?
- What changes when AI helps write the code?

## Main Sections

- Tooling and AI-assisted workflow: `docs/software-engineering/tooling`
- APIs and compatibility: `docs/software-engineering/apis`
- Testing and verification: `docs/software-engineering/testing`
- Security and trust boundaries: `docs/software-engineering/security-basics`
- Concurrency and background work: `docs/software-engineering/concurrency`
- Observability and debug signals: `docs/software-engineering/observability`
- Reliability and safe delivery: `docs/software-engineering/reliability`
- Performance and cost: `docs/software-engineering/performance`
- System design and boundaries: `docs/software-engineering/system-design`
- Platform and delivery systems: `docs/software-engineering/platform-and-delivery`
- Capstones and synthesis: `docs/software-engineering/capstones`
- Python engineering: `docs/software-engineering/python`
- Rust engineering: `docs/software-engineering/rust`
- TypeScript engineering: `docs/software-engineering/typescript`
- Practical design patterns: `docs/software-engineering/design-patterns`

## AI-Time 2026 Priorities

- Contract-first engineering over prompt-first engineering.
- Regression resistance for AI-generated changes.
- Observability and rollback before aggressive automation.
- Reliability rules for retries, queues, overload, and partial failure.
- Platform leverage that improves delivery speed without hiding ownership.

## First 20 Canonical Modules

Build the track in this order:

1. `ai-assisted-dev-loop`
2. `reproducible-dev-environments`
3. `repo-layout-and-codegen-boundaries`
4. `api-contract-basics`
5. `schema-evolution-and-compatibility`
6. `idempotency-keys`
7. `retries-timeouts-and-backoff`
8. `test-portfolio-in-practice`
9. `contract-tests`
10. `regression-tests-for-ai-generated-code`
11. `authn-vs-authz`
12. `least-privilege-and-secrets-management`
13. `race-conditions-and-shared-state`
14. `cancellation-deadlines-and-timeouts`
15. `logs-metrics-and-traces`
16. `slis-slos-and-alerting`
17. `graceful-degradation-and-overload`
18. `canary-rollout-and-rollback`
19. `latency-budgeting`
20. `service-boundaries-and-failure-domains`

## Scope Rule

- Prefer stable engineering principles over framework churn.
- Prefer compact modules with clear failure modes over long catalogs of tips.
- Prefer operationally meaningful topics over interview-style trivia.
- Treat AI as a workflow amplifier layered on top of software fundamentals, not as a replacement for them.

## Capstones

- `contract-to-production-api-service` is the first end-to-end capstone.
- `ai-assisted-feature-delivery` is the second capstone focused on spec, review, verification, and rollout discipline.
- The next capstone should cover incident recovery drills.
