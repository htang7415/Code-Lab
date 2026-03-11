# Incremental Refresh Watermarks

> Track: `databases` | Topic: `sql-patterns`

## Concept

An incremental refresh watermark marks how far a materialized table has safely processed source changes. New refreshes should only consume rows beyond the last watermark.

## Key Points

- A watermark prevents reprocessing the same source rows on every refresh.
- Refresh windows should move forward monotonically.
- The view should match a full rebuild up to the same watermark.
- Late rows below the watermark need a different repair path because normal incremental refresh will skip them.

## Minimal Code Mental Model

```python
state = empty_refresh_state()
rows = [
    source_row(100, 7, 10),
    source_row(105, 7, 20),
    source_row(120, 8, 5),
]
applied = apply_incremental_refresh(state, rows, next_watermark=105)
```

## Function

```python
def source_row(updated_at: int, workspace_id: int, amount: int) -> dict[str, int]:
def empty_refresh_state() -> dict[str, object]:
def rows_in_window(
    rows: list[dict[str, int]],
    last_watermark: int,
    next_watermark: int,
) -> list[dict[str, int]]:
def apply_incremental_refresh(
    state: dict[str, object],
    rows: list[dict[str, int]],
    next_watermark: int,
) -> list[int]:
def current_watermark(state: dict[str, object]) -> int:
def workspace_totals(state: dict[str, object]) -> dict[int, int]:
def full_rebuild(rows: list[dict[str, int]], up_to_watermark: int) -> dict[int, int]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/incremental-refresh-watermarks/python -q
```
