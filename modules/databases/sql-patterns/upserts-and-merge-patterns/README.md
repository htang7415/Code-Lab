# Upserts And Merge Patterns

> Track: `databases` | Topic: `sql-patterns`

## Concept

Upserts let a write either insert a new row or update the existing row for the same business key.

## Key Points

- Upserts make idempotent writes easier.
- The conflict target should match the real business key.
- Merge logic often needs freshness rules so stale writes do not overwrite newer data.
- Batch merge is usually just repeated upsert against a unique key.

## Minimal Code Mental Model

```python
conn = create_connection()
create_model_scores_table(conn)
upsert_score(conn, "gpt-mini", "helpfulness", 0.81, "2026-03-10T09:00:00Z")
upsert_score(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z")
rows = score_rows(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_model_scores_table(conn: sqlite3.Connection) -> None:
def upsert_score(
    conn: sqlite3.Connection,
    model_name: str,
    dataset_name: str,
    score: float,
    updated_at: str,
) -> None:
def merge_score_batch(
    conn: sqlite3.Connection,
    rows: list[tuple[str, str, float, str]],
) -> None:
def score_rows(conn: sqlite3.Connection) -> list[tuple[str, str, float, str]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/upserts-and-merge-patterns/python -q
```
