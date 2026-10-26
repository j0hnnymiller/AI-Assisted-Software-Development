---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "create-microservices-instructions-20261022"
prompt: |
  create an instruction file for building microservices
started: "2026-10-22T16:04:38.234-07:00"
ended: "2026-10-22T16:11:40.283-07:00"
task_durations:
  - task: "repository guidance review"
    duration: "00:01:30"
  - task: "instruction drafting"
    duration: "00:03:30"
  - task: "validation and refinement"
    duration: "00:02:02"
total_duration: "00:07:02"
ai_log: "ai-logs/2026/10/22/create-microservices-instructions-20261022/conversation.md"
source: "user request"
applyTo: "**/*.{cs,ts,js,py,java,go,rb,kt,swift,yml,yaml,json}"
---

# Microservices Instructions

## Overview

Use this guidance to design, build, change, and verify microservices when that architecture has been selected for the system. A microservice is an independently deployable service that owns a coherent business capability and its data.

These instructions do not select microservices as the default architecture. Follow approved architecture decisions and existing repository patterns. If a request could reasonably mean either a modular monolith or independently deployed services, clarify the intended boundary before introducing service infrastructure.

## Table of Contents

- [Decision and Scope](#decision-and-scope)
- [Service Boundaries and Ownership](#service-boundaries-and-ownership)
- [Communication and Contracts](#communication-and-contracts)
- [Data and Consistency](#data-and-consistency)
- [Security and Privacy](#security-and-privacy)
- [Resilience and Operations](#resilience-and-operations)
- [Build, Deployment, and Change](#build-deployment-and-change)
- [Testing and Verification](#testing-and-verification)
- [Anti-Patterns](#anti-patterns)
- [Validation Checklist](#validation-checklist)

## Decision and Scope

- Review the system's approved architecture, requirements, current service boundaries, operational capabilities, and applicable repository instructions before changing a service.
- Implement the smallest change that satisfies the requested capability. Do not create a new service, gateway, broker, database, or orchestration platform without an approved requirement or explicit user direction.
- Prefer a modular monolith when independent deployment, scaling, ownership, or fault isolation does not justify the cost of distributed operation.
- Make service boundaries explicit: capability, owner, API/event contracts, data ownership, dependencies, deployment unit, and operational responsibility.
- Keep each service independently buildable and deployable only where the repository's architecture and delivery process support that goal.

## Service Boundaries and Ownership

- Organize each service around a cohesive business capability or bounded context, not a technical layer or database table.
- Keep service internals private. Expose behavior through documented APIs or message contracts rather than shared database access or shared domain models.
- Give each service authoritative ownership of its data. Other services must not read or write its tables directly; integrate through an explicit, authorized contract.
- Share only stable, cross-cutting technical utilities when they reduce real duplication without coupling service releases. Do not use shared libraries to distribute mutable domain rules or force lockstep deployment.
- Keep changes within the owning service unless a cross-service contract or workflow must change. Identify affected consumers and coordinate compatible rollout where required.

## Communication and Contracts

- Choose synchronous request/response when a caller needs an immediate result; choose asynchronous messaging for independent, deferred work. Document the choice and its failure/consistency consequences.
- Keep network calls purposeful and bounded. Avoid chatty request chains and cyclic service dependencies; introduce an intermediary or asynchronous workflow only when justified by the use case.
- Define API and message contracts with explicit schemas, validation, authorization, error behavior, compatibility expectations, and ownership.
- Evolve public contracts compatibly where possible. Use additive changes, support old and new consumers during migration, and document deprecation and removal. Do not silently change field meaning or event semantics.
- Treat delivery as potentially duplicated, delayed, or out of order unless the transport and contract guarantee otherwise. Consumers must be idempotent where retries or redelivery are possible; establish deduplication and ordering rules when required.
- Set timeouts for remote calls. Retry only transient failures, with bounded attempts and backoff; do not retry unsafe operations without an idempotency mechanism. Use circuit breaking or bulkheads when supported by the existing stack and justified by failure risk.

## Data and Consistency

- Keep transactions local to a service's owned data store. Avoid distributed transactions and cross-service dual writes.
- State the required consistency and freshness for cross-service workflows. Use eventual consistency only when the user-visible behavior can tolerate it, and define how clients observe pending or failed work.
- For reliable publication of events tied to a database change, use a transactional outbox or an established equivalent. Make consumers resilient to duplicate delivery; use an inbox or deduplication record when needed.
- Use a saga or other explicit process manager only for a multi-step business transaction that spans service boundaries. Define step ownership, timeouts, retries, compensations, and manual recovery; do not imply compensation can always undo an external side effect.
- Version and retain data and messages according to actual compatibility, retention, privacy, and recovery requirements. Plan schema changes so old and new service versions can coexist during rollout.

For command/query separation or event sourcing, follow [CQRS Architecture](cqrs-architecture.instructions.md); do not introduce those patterns solely because the system has multiple services.

## Security and Privacy

- Treat every service boundary as a trust boundary. Authenticate callers and authorize each operation using the repository's approved identity and access-control mechanisms.
- Apply least privilege to service identities, data stores, queues, and deployment permissions. Do not rely on network location alone for authorization.
- Validate inputs at public boundaries and enforce resource limits. Protect sensitive data in transit and at rest using approved platform mechanisms.
- Store credentials in the approved secret-management system, never in source, images, logs, or plain configuration.
- Minimize sensitive data in messages and telemetry. Redact or omit credentials, tokens, personal data, and confidential payloads from logs and traces.
- Follow repository and organization security, privacy, regulatory, and dependency policies. Raise conflicts or unknown requirements rather than inventing controls or compliance claims.

## Resilience and Operations

- Handle dependency failures explicitly. Define timeouts, bounded retries, idempotency, cancellation, and user-visible failure behavior appropriate to each operation.
- Provide health and readiness signals using existing platform conventions. A health probe must distinguish inability to serve traffic from optional dependency degradation where the platform supports it.
- Emit structured logs, metrics, and traces with consistent service identity and correlation/trace context. Do not expose sensitive payloads through observability data.
- Make service ownership, dependency maps, operational runbooks, and recovery procedures discoverable for production-critical services.
- Set measurable availability, latency, throughput, and recovery targets only when they are approved or supported by requirements. Monitor dependency errors, queue depth/age, retries, and workflow completion where relevant.

## Build, Deployment, and Change

- Reuse the repository's supported build, configuration, container, orchestration, and CI/CD patterns. Do not add new platforms or tools without approval.
- Keep runtime configuration outside the deployable artifact and validate required configuration at startup. Do not silently substitute unsafe defaults for missing required settings.
- Make each production service independently buildable, testable, and releasable when required by its architecture. Pin and manage its dependencies under [Dependency Management Policy](dependency-management-policy.instructions.md).
- Design database and message-contract migrations for safe rollout and rollback. Prefer expand-migrate-contract steps when versions overlap; do not remove fields or consumers until compatibility is verified.
- Ensure deployments expose health, logs, and rollback or recovery signals expected by the existing operations process.

## Testing and Verification

- Test behavior at service boundaries, including authorization, validation, contract compatibility, and documented error responses.
- Use unit tests for local domain rules, integration tests for owned persistence and messaging behavior, and contract tests for important producer/consumer agreements.
- Verify failure cases that affect correctness: timeouts, transient errors, duplicate delivery, delayed messages, partial workflow completion, and incompatible configuration or schema where relevant.
- Avoid tests that depend on live external services unless the repository explicitly supports and configures them. Use deterministic fakes, emulators, or test containers following existing practices.
- Run the smallest relevant test set first, then required build, type-check, lint, contract, and deployment validation. Report unrun checks and unresolved failures explicitly.
- Follow [Test-Driven Development](test-driven-development.instructions.md) and [Vertical Slice Instructions](vertical-slice.instructions.md) where applicable; do not impose either architecture where the repository does not use it.

## Anti-Patterns

- Splitting a service by technical layer, table, or anticipated scale without evidence.
- Replacing an existing modular design with microservices without an approved decision.
- Sharing databases, mutable domain libraries, or internal schemas across services.
- Building synchronous call chains or cyclic dependencies that amplify outages.
- Assuming exactly-once message delivery or retrying non-idempotent work without safeguards.
- Performing uncoordinated dual writes or using distributed transactions as the default.
- Treating an API gateway, service mesh, broker, saga, CQRS, or event sourcing as mandatory components.
- Logging secrets, credentials, tokens, or unnecessary sensitive payloads.

## Validation Checklist

- [ ] Architecture selection and service boundary are approved and justified by requirements.
- [ ] Service capability, ownership, data, APIs/events, and dependencies are explicit.
- [ ] No service accesses another service's private database or mutable internal model.
- [ ] Contracts, compatibility, authorization, and errors are defined and tested.
- [ ] Remote calls have bounded timeouts and safe retry/idempotency behavior.
- [ ] Cross-service consistency, duplicate handling, recovery, and compensation behavior are documented where needed.
- [ ] Secrets, sensitive data, and least-privilege access follow approved policy.
- [ ] Build, deployment, health, observability, and migration practices match the existing platform.
- [ ] Relevant unit, integration, contract, and failure-path checks pass or are reported as not run.
- [ ] Related architecture and repository instructions have been followed.

## References

- [Vision and Scope Instructions](vision-and-scope.instructions.md)
- [CQRS Architecture Instructions](cqrs-architecture.instructions.md)
- [Dependency Management Policy](dependency-management-policy.instructions.md)
- [Test-Driven Development Instructions](test-driven-development.instructions.md)
- [Vertical Slice Instructions](vertical-slice.instructions.md)
- [AI-Assisted Output Instructions](ai-assisted-output.instructions.md)
