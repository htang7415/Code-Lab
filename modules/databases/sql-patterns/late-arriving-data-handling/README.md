# Late-Arriving Data Handling

> Track: `databases` | Topic: `sql-patterns`

## Concept

Late-arriving rows show up after the watermark has already advanced past their event time. A normal incremental refresh will skip them unless the system has a repair path.

## Key Points

- Watermarks are efficient, but they assume rows arrive roughly in order.
- Rows with timestamps below the current watermark are “late” for the normal refresh path.
- Late rows should be recorded and repaired explicitly instead of silently ignored.
- A correct system makes late data visible eventually, even if not in the first incremental pass.

## Minimal Code Mental Model

```python
state = empty_state()
rows = [
    source_row(100, 7, 10),
    source_row(105, 7, 20),
]
apply_incremental_rows(state, rows, next_watermark=105)
apply_incremental_rows(state, [source_row(103, 7, 5), source_row(110, 8, 7)], next_watermark=110)
repair_late_rows(state)
```

## Function

```python
def source_row(event_time: int, workspace_id: int, amount: int) -> dict[str, int]:
def empty_state() -> dict[str, object]:
def apply_incremental_rows(
    state: dict[str, object],
    rows: list[dict[str, int]],
    next_watermark: int,
) -> tuple[list[int], list[int]]:
def late_event_times(state: dict[str, object]) -> list[int]:
def repair_late_rows(state: dict[str, object]) -> list[int]:
def workspace_totals(state: dict[str, object]) -> dict[int, int]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/late-arriving-data-handling/python -q
```
