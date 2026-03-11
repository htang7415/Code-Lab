# Composite Index Order

> Track: `databases` | Topic: `indexing`

## Concept

Composite indexes only help efficiently when the query starts from the left side of the index column order.

## Key Points

- `(status, workspace_id, created_at)` is not equivalent to `(workspace_id, created_at)`.
- The left-prefix rule is why column order is part of index design, not a detail.
- A poorly ordered composite index can still leave a query doing a full scan and a temp sort.
- `EXPLAIN QUERY PLAN` is the fastest way to catch this mistake.

## Minimal Code Mental Model

```python
conn = create_connection()
create_runs_table(conn)
seed_runs(conn, rows)
add_bad_index_status_workspace_created(conn)
bad_plan = plan_flags(plan_for_workspace_recent_runs(conn, 7))
add_good_index_workspace_created(conn)
good_plan = plan_flags(plan_for_workspace_recent_runs(conn, 7))
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_runs_table(conn: sqlite3.Connection) -> None:
def seed_runs(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str]],
) -> None:
def add_bad_index_status_workspace_created(conn: sqlite3.Connection) -> None:
def add_good_index_workspace_created(conn: sqlite3.Connection) -> None:
def plan_for_workspace_recent_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
def recent_runs_for_workspace(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[tuple[int, str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/composite-index-order/python -q
```
