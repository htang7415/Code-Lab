# Snapshot Vs Current State Tables

> Track: `databases` | Topic: `schema-design`

## Concept

Current-state tables answer “what is true now.” Snapshot tables answer “what was true then.” Good systems often need both because operational reads and historical reads are different jobs.

## Key Points

- Current-state rows are compact and easy to update.
- Snapshot tables preserve time-travel history for audits, analytics, and backtests.
- If you overwrite the only row, historical reconstruction becomes impossible.
- AI systems often need snapshots for prompt configs, eval thresholds, routing policies, and model settings.

## Minimal Code Mental Model

```python
upsert_current_config(conn, "retrieval-answer", "gpt-5-small", "2026-02-01")
capture_prompt_snapshot(conn, "retrieval-answer", "gpt-5-small", "2026-02-01")
model = snapshot_model_as_of(conn, "retrieval-answer", "2026-02-15")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_snapshot_schema(conn: sqlite3.Connection) -> None:
def upsert_current_config(
    conn: sqlite3.Connection,
    prompt_id: str,
    model_name: str,
    updated_at: str,
) -> None:
def capture_prompt_snapshot(
    conn: sqlite3.Connection,
    prompt_id: str,
    model_name: str,
    captured_at: str,
) -> int:
def current_prompt_models(conn: sqlite3.Connection) -> dict[str, str]:
def snapshot_model_as_of(conn: sqlite3.Connection, prompt_id: str, as_of: str) -> str | None:
```

## Run tests

```bash
pytest modules/databases/schema-design/snapshot-vs-current-state-tables/python -q
```
