# CDC Watermarks And Ordering

> Track: `databases` | Topic: `streaming`

## Concept

CDC consumers often see events arrive out of order. A watermark tracks the highest contiguous sequence that has been safely applied.

## Key Points

- A consumer should not advance its watermark past a gap in the sequence.
- Out-of-order events are usually buffered until the missing earlier event arrives.
- The watermark is the safe replay point for restarts and downstream handoffs.
- Delete events still need ordering; applying them early can corrupt the read model.

## Minimal Code Mental Model

```python
state = empty_consumer_state()
ingest_cdc_event(state, cdc_event(1, "orders", "o1", "upsert", {"status": "placed"}))
ingest_cdc_event(state, cdc_event(3, "orders", "o1", "upsert", {"status": "completed"}))
ingest_cdc_event(state, cdc_event(2, "orders", "o1", "upsert", {"status": "paid"}))
watermark = current_watermark(state)
```

## Function

```python
def cdc_event(
    sequence: int,
    table: str,
    row_id: str,
    op: str,
    after: dict[str, object] | None,
) -> dict[str, object]:
def empty_consumer_state() -> dict[str, object]:
def ingest_cdc_event(
    consumer_state: dict[str, object],
    event: dict[str, object],
) -> list[int]:
def current_watermark(consumer_state: dict[str, object]) -> int:
def latest_row(
    consumer_state: dict[str, object],
    table: str,
    row_id: str,
) -> dict[str, object] | None:
```

## Run tests

```bash
pytest modules/databases/streaming/cdc-watermarks-and-ordering/python -q
```
