# Multi-Tenant Index Design

> Track: `databases` | Topic: `indexing`

## Concept

In a multi-tenant system, the tenant key usually needs to lead the index so the engine can narrow to one tenant before it scans shared data.

## Key Points

- Index column order matters because B-tree lookups use a leading prefix.
- A shared-table multi-tenant system should usually lead hot indexes with `workspace_id` or `tenant_id`.
- Putting tenant second can leave the engine scanning many rows from other tenants first.
- Tenant-leading indexes often pair the tenant key with status, time, or foreign-key columns used on the hot path.

## Minimal Code Mental Model

```python
rows = [
    {"id": "d1", "workspace_id": 7, "status": "open", "created_day": 1},
    {"id": "d2", "workspace_id": 8, "status": "open", "created_day": 1},
]
summary = index_cost_summary(
    rows,
    index_order=("workspace_id", "status", "created_day"),
    filters={"workspace_id": 7, "status": "open"},
)
```

## Function

```python
def prefix_match_columns(
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> tuple[str, ...]:
def candidate_row_ids(
    rows: list[dict[str, object]],
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> list[str]:
def final_row_ids(
    rows: list[dict[str, object]],
    filters: dict[str, object],
) -> list[str]:
def index_cost_summary(
    rows: list[dict[str, object]],
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/indexing/multi-tenant-index-design/python -q
```
