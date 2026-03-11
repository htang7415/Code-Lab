# Streaming And CDC

Streaming connects operational databases to downstream systems without waiting for batch syncs.

## Purpose

Use this topic to learn events, consumer groups, CDC, and the patterns that keep data pipelines correct under retries and replay.

## First Principles

- An event is a fact that happened. A stream is an ordered log of those facts.
- CDC captures database changes after commit. Application events are explicit signals from business logic. They solve different problems.
- Delivery guarantees do not remove the need for idempotent consumers.
- Streaming systems are often the glue between transactional databases, caches, analytics systems, and AI pipelines.

## Minimal Query Mental Model

```json
{
  "event_id": "evt_001",
  "topic": "document.ingested",
  "document_id": 918,
  "workspace_id": 42,
  "occurred_at": "2026-03-11T10:00:00Z"
}
```

## Canonical Modules

- `event-stream-basics`
- `cdc-vs-application-events`
- `consumer-groups-and-offsets`
- `idempotent-consumers`
- `outbox-and-materialized-view-patterns`
- `connectors-and-pipeline-shapes`

## When To Use What

- Use CDC when downstream systems need committed database changes.
- Use application events when business meaning matters more than raw row-level change capture.
- Use idempotent consumers whenever retries or replay are possible.
- Use streaming when freshness across systems matters enough that batch polling is no longer acceptable.
