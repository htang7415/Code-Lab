# B-Tree Basics

> Track: `databases` | Topic: `indexing`

## Concept

B-tree indexes speed up equality, range, and ordered lookups when the index columns match the query shape.

## Key Points

- A good index follows the filter and sort pattern of a real query.
- Composite index order matters because the database walks the index from left to right.
- Indexes trade write cost and storage for faster reads.
- `EXPLAIN QUERY PLAN` is a fast way to see whether a query is scanning a table or using an index.

## Minimal Code Mental Model

```python
conn = create_connection()
create_eval_runs_table(conn)
seed_eval_runs(conn, rows)
before = plan_for_recent_completed_runs(conn, workspace_id=7)
add_workspace_status_created_index(conn)
after = plan_for_recent_completed_runs(conn, workspace_id=7)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_eval_runs_table(conn: sqlite3.Connection) -> None:
def seed_eval_runs(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str, int]],
) -> None:
def add_workspace_status_created_index(conn: sqlite3.Connection) -> None:
def plan_for_recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[str]:
def recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[tuple[int, str]]:
```

## Run tests

```bash
pytest modules/databases/indexing/btree-basics/python -q
```
