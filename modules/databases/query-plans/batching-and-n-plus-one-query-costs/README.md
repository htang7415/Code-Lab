# Batching And N-Plus-One Query Costs

> Track: `databases` | Topic: `query-plans`

## Concept

An N+1 query pattern turns one parent query into many child round trips. Batching collapses those child lookups into a small number of set-based queries.

## Key Points

- N+1 cost grows with the number of parent rows.
- Batching keeps the number of round trips closer to constant.
- Round-trip latency often dominates the cost even if each individual query is simple.
- The fix is usually to fetch related rows in sets instead of one parent at a time.

## Minimal Code Mental Model

```python
summary = query_cost_summary(
    parent_count=20,
    batch_size=20,
    round_trip_ms=15,
)
```

## Function

```python
def n_plus_one_query_count(parent_count: int) -> int:
def batched_query_count(parent_count: int, batch_size: int) -> int:
def total_round_trip_ms(query_count: int, round_trip_ms: int) -> int:
def query_cost_summary(
    parent_count: int,
    batch_size: int,
    round_trip_ms: int,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/query-plans/batching-and-n-plus-one-query-costs/python -q
```
