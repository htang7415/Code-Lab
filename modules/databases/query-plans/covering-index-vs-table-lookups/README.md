# Covering Index Vs Table Lookups

> Track: `databases` | Topic: `query-plans`

## Concept

A covering index can satisfy a query from index entries alone. A non-covering index still helps locate rows, but the engine may need extra table or heap lookups for every result row.

## Key Points

- Index probes are often mostly fixed work based on tree height.
- Heap or table lookups add extra per-row cost after the probe.
- The more rows a query returns, the more expensive a non-covering path becomes.
- This is why projected columns matter, not just filter columns.

## Minimal Code Mental Model

```python
summary = lookup_summary(index_height=4, result_rows=25)
```

## Function

```python
def index_probe_work(index_height: int) -> int:
def table_lookup_work(result_rows: int, covering: bool) -> int:
def total_lookup_work(index_height: int, result_rows: int, covering: bool) -> int:
def lookup_summary(index_height: int, result_rows: int) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/query-plans/covering-index-vs-table-lookups/python -q
```
