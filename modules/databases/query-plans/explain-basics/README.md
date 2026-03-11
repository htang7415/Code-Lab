# Explain Basics

> Track: `databases` | Topic: `query-plans`

## Concept

`EXPLAIN QUERY PLAN` shows whether a query is scanning rows, using an index, or sorting with temporary work.

## Key Points

- A plan is about the work the database expects to do, not just the SQL text you wrote.
- Full scans and temporary sorts are common reasons a query gets slower as data grows.
- A good plan often comes from better indexes or a simpler query shape, not magic hints.
- You should read plans before guessing at performance fixes.

## Minimal Code Mental Model

```python
conn = create_connection()
create_events_table(conn)
seed_events(conn, rows)
before = plan_flags(explain_recent_workspace_events(conn, workspace_id=7))
add_recent_events_index(conn)
after = plan_flags(explain_recent_workspace_events(conn, workspace_id=7))
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_events_table(conn: sqlite3.Connection) -> None:
def seed_events(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str]],
) -> None:
def add_recent_events_index(conn: sqlite3.Connection) -> None:
def explain_recent_workspace_events(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
def plan_flags(plan_details: list[str]) -> dict[str, bool]:
def recent_workspace_events(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[tuple[int, str]]:
```

## Run tests

```bash
pytest modules/databases/query-plans/explain-basics/python -q
```
