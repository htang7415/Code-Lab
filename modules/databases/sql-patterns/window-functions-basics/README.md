# Window Functions Basics

> Track: `databases` | Topic: `sql-patterns`

## Concept

Window functions compute row-level statistics while still keeping one row per record.

## Key Points

- `ROW_NUMBER()` ranks rows inside a partition like `model_name`.
- `LAG()` compares the current row to a previous row without a self-join.
- Window functions are often the cleanest way to get best-run, latest-row, and running-delta queries.
- They do not collapse the result set the way `GROUP BY` does.

## Minimal Code Mental Model

```python
conn = create_connection()
create_eval_results_table(conn)
record_eval_result(conn, "gpt-mini", "helpfulness", 0.81, "2026-03-01T09:00:00Z")
record_eval_result(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-02T09:00:00Z")
ranked = rank_runs_within_model(conn)
best = best_run_per_model(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_eval_results_table(conn: sqlite3.Connection) -> None:
def record_eval_result(
    conn: sqlite3.Connection,
    model_name: str,
    dataset_name: str,
    score: float,
    recorded_at: str,
) -> int:
def rank_runs_within_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
def best_run_per_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
def score_deltas_by_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/window-functions-basics/python -q
```
