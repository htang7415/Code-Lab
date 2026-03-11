# Dedup And Latest Row

> Track: `databases` | Topic: `sql-patterns`

## Concept

The standard way to keep the latest row per key is to rank rows inside each key partition and keep rank 1.

## Key Points

- `ROW_NUMBER()` lets you keep one latest row without losing access to the original columns.
- A tie breaker like `id DESC` matters when timestamps are equal.
- Dedup logic should be explicit, not accidental.
- This pattern shows up in job state, latest feedback, event compaction, and user profile updates.

## Minimal Code Mental Model

```python
conn = create_connection()
create_run_events_table(conn)
record_run_event(conn, "run-1", "queued", "2026-03-10T09:00:00Z")
record_run_event(conn, "run-1", "completed", "2026-03-10T09:05:00Z")
latest = latest_event_per_run(conn)
summary = latest_status_summary(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_run_events_table(conn: sqlite3.Connection) -> None:
def record_run_event(
    conn: sqlite3.Connection,
    run_id: str,
    status: str,
    recorded_at: str,
) -> int:
def latest_event_per_run(conn: sqlite3.Connection) -> list[dict[str, object]]:
def latest_status_summary(conn: sqlite3.Connection) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/dedup-and-latest-row/python -q
```
