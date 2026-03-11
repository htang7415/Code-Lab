# Indexing And Access Paths

Indexes are physical shortcuts for specific query shapes.

## Purpose

Use this topic to learn how access paths speed up reads, what they cost on writes, and how to choose indexes from actual predicates and sort order.

## First Principles

- An index is not free. It adds storage, write amplification, and maintenance cost.
- Good indexing starts from the query shape: filters, joins, ordering, and limits.
- Composite index order matters because databases use left-prefix access patterns.
- The fastest query is often a combination of better schema, smaller scans, and the right index, not "add indexes everywhere".

## Minimal Query Mental Model

```sql
EXPLAIN
SELECT id, created_at
FROM eval_runs
WHERE workspace_id = 42
  AND status = 'completed'
ORDER BY created_at DESC
LIMIT 20;
```

## Canonical Modules

- `btree-basics`
- `composite-index-order`
- `covering-index-concepts`
- `partial-indexes`
- `jsonb-and-gin-indexing`
- `partition-pruning-basics`

## When To Use What

- Use B-tree indexes first for equality, range, and ordered lookups.
- Use composite indexes when filters and sort order repeat on a hot path.
- Use partial indexes when only a subset of rows matters often enough to justify a targeted structure.
- Use JSONB and GIN only when flexible metadata queries are truly part of the product path.
