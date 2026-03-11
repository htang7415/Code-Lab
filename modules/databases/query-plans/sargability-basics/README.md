# Sargability Basics

> Track: `databases` | Topic: `query-plans`

## Concept

A predicate is sargable when the optimizer can turn it into an index search. Wrapping the indexed column in a function often breaks that search shape and forces a scan instead.

## Key Points

- `created_day >= ? AND created_day < ?` is usually index-friendly.
- `substr(created_day, 1, 7) = ?` asks the engine to transform every row first, which often prevents an index search.
- Sargability is about predicate shape, not just whether an index exists.
- Many “slow query” fixes are simple rewrites from function-on-column predicates to equivalent ranges.

## Minimal Code Mental Model

```python
range_plan = sargable_range_plan(conn, "2026-01-01", "2026-02-01")
month_plan = nonsargable_month_plan(conn, "2026-01")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_event_table(conn: sqlite3.Connection) -> None:
def seed_events(conn: sqlite3.Connection, days: list[str]) -> None:
def add_created_day_index(conn: sqlite3.Connection) -> None:
def sargable_range_plan(conn: sqlite3.Connection, start_day: str, end_day: str) -> list[str]:
def nonsargable_month_plan(conn: sqlite3.Connection, month_prefix: str) -> list[str]:
def plan_summary(details: list[str]) -> dict[str, bool]:
```

## Run tests

```bash
pytest modules/databases/query-plans/sargability-basics/python -q
```
