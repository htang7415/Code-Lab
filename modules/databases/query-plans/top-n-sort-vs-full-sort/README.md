# Top-N Sort Vs Full Sort

> Track: `databases` | Topic: `query-plans`

## Concept

A small `LIMIT` can change the physical plan. Instead of sorting every row, the database may keep only the best `N` rows in a smaller heap.

## Key Points

- Full sort work grows with all rows that reach the sort.
- A top-N strategy grows with all input rows but only maintains a heap of size `N`.
- When `N` is close to the full result size, the top-N advantage mostly disappears.
- If an index already matches the order, neither explicit sort is necessary.

## Minimal Code Mental Model

```python
small = sort_strategy_summary(row_count=100_000, limit=20, has_ordered_index=False)
large = sort_strategy_summary(row_count=100_000, limit=80_000, has_ordered_index=False)
```

## Function

```python
def full_sort_work_units(row_count: int) -> float:
def top_n_heap_work_units(row_count: int, limit: int) -> float:
def choose_sort_strategy(
    row_count: int,
    limit: int,
    has_ordered_index: bool,
) -> str:
def sort_strategy_summary(
    row_count: int,
    limit: int,
    has_ordered_index: bool,
) -> dict[str, float | str]:
```

## Run tests

```bash
pytest modules/databases/query-plans/top-n-sort-vs-full-sort/python -q
```
