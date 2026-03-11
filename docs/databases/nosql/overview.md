# NoSQL Trade-Offs

NoSQL is a family of data model choices, not one thing.

## Purpose

Use this topic to understand when document, key-value, and wide-column systems fit better than a relational model, and when they do not.

## First Principles

- The data model should follow the access pattern and consistency needs.
- Flexible schema does not remove the need for design. It just moves the design pressure elsewhere.
- Different NoSQL systems trade joins, transactions, secondary indexes, and consistency guarantees for scale or simplicity on specific workloads.
- Many teams can stay in a relational database longer than they think by using good schema design and selective JSONB-style flexibility.

## Minimal Query Mental Model

```json
{
  "session_id": "abc123",
  "user_id": 42,
  "messages": [
    {"role": "user", "text": "Find last week's failed runs"},
    {"role": "assistant", "text": "I found 3 failed runs"}
  ]
}
```

## Canonical Modules

- `key-value-patterns`
- `document-modeling`
- `consistency-and-quorum-mental-model`
- `secondary-index-tradeoffs`
- `wide-row-and-time-series-patterns`
- `when-postgres-is-enough`

## When To Use What

- Use key-value systems for extremely simple lookup paths with predictable keys.
- Use document stores when nested data is the natural product shape and cross-document joins are limited.
- Use wide-row or time-series models when write shape and retention patterns dominate the design.
- Stay relational when consistency, joins, and flexible querying matter more than a narrow scaling win.
