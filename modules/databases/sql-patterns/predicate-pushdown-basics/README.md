# Predicate Pushdown Basics

> Track: `databases` | Topic: `sql-patterns`

## Concept

Predicate pushdown uses cheap metadata to skip chunks of data that cannot satisfy the filter before reading every row.

## Key Points

- Push filters as close to storage as possible.
- Row-group or file stats can rule out entire chunks without scanning them.
- Pushdown works best when the predicate matches available min/max or partition metadata.
- Without pushdown, the engine reads every chunk and filters later.

## Minimal Code Mental Model

```python
groups = [
    {"id": "g1", "min_score": 0, "max_score": 40, "rows": ["a", "b"]},
    {"id": "g2", "min_score": 50, "max_score": 90, "rows": ["c", "d"]},
]
plan = pushdown_summary(groups, min_score=60)
```

## Function

```python
def group_might_match(group: dict[str, object], min_score: int) -> bool:
def pushed_down_group_ids(
    groups: list[dict[str, object]],
    min_score: int,
) -> list[str]:
def matching_rows(
    groups: list[dict[str, object]],
    min_score: int,
) -> list[str]:
def pushdown_summary(
    groups: list[dict[str, object]],
    min_score: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/predicate-pushdown-basics/python -q
```
