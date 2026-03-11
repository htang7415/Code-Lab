# Replay And Backfill Consumers

> Track: `databases` | Topic: `streaming`

## Concept

Durable event logs let consumers rebuild state from the beginning or patch gaps later. Replay reconstructs a full view. Backfill applies a missed offset range into an existing view.

## Key Points

- Offsets are not just progress markers. They make historical reprocessing possible.
- New consumers often start with a replay from offset `0`.
- Existing consumers use backfills when code bugs, outages, or late connectors leave holes.
- Replay and backfill only work cleanly when handlers are deterministic over the same input range.

## Minimal Code Mental Model

```python
stream = []
append_amount_event(stream, "sales", "ws-a", 5)
append_amount_event(stream, "sales", "ws-a", 4)
totals = replay_topic(stream, "sales")
```

## Function

```python
def append_amount_event(
    stream: list[dict[str, object]],
    topic: str,
    key: str,
    amount: int,
) -> int:
def consume_range(
    stream: list[dict[str, object]],
    topic: str,
    start_offset: int,
    end_offset: int | None = None,
) -> tuple[dict[str, int], int]:
def replay_topic(stream: list[dict[str, object]], topic: str) -> dict[str, int]:
def backfill_into_state(
    state: dict[str, int],
    stream: list[dict[str, object]],
    topic: str,
    start_offset: int,
    end_offset: int,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/streaming/replay-and-backfill-consumers/python -q
```
