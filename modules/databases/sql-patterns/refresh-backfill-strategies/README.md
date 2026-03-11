# Refresh Backfill Strategies

> Track: `databases` | Topic: `sql-patterns`

## Concept

Incremental refresh moves forward from the watermark. Backfill reprocesses a historical interval when a gap, correction, or new source appears behind that watermark.

## Key Points

- Forward refresh is cheap because it only scans new rows.
- Historical holes require backfill because the watermark has already passed them.
- Choosing the wrong strategy either wastes work or misses data.
- A good pipeline makes the forward path and the historical repair path explicit.

## Minimal Code Mental Model

```python
strategy = choose_strategy(current_watermark=105, request_start=90, request_end=100)
summary = strategy_summary(
    rows,
    current_watermark=105,
    request_start=90,
    request_end=100,
)
```

## Function

```python
def source_row(event_time: int, workspace_id: int, amount: int) -> dict[str, int]:
def incremental_rows(
    rows: list[dict[str, int]],
    current_watermark: int,
    next_watermark: int,
) -> list[int]:
def backfill_rows(
    rows: list[dict[str, int]],
    start_time: int,
    end_time: int,
) -> list[int]:
def choose_strategy(
    current_watermark: int,
    request_start: int,
    request_end: int,
) -> str:
def strategy_summary(
    rows: list[dict[str, int]],
    current_watermark: int,
    request_start: int,
    request_end: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/refresh-backfill-strategies/python -q
```
