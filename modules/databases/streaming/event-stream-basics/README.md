# Event Stream Basics

> Track: `databases` | Topic: `streaming`

## Concept

An event stream is an append-only log where consumers read events in offset order and keep track of how far they have progressed.

## Key Points

- Offsets turn a list of events into a replayable stream.
- Reading from an offset lets a consumer resume after restarts.
- Consumer lag is the gap between the end of the stream and the next event a consumer will read.
- Materialized views are often just deterministic folds over an event log.

## Minimal Code Mental Model

```python
stream = []
append_event(stream, "document.ingested", "doc-1", {"status": "ready"})
append_event(stream, "document.ingested", "doc-1", {"status": "embedded"})
events = read_from_offset(stream, offset=1)
lag = consumer_lag(stream, next_offset=1)
```

## Function

```python
def append_event(
    stream: list[dict[str, object]],
    topic: str,
    key: str,
    payload: dict[str, object],
) -> int:
def read_from_offset(
    stream: list[dict[str, object]],
    offset: int,
    max_events: int | None = None,
) -> list[dict[str, object]]:
def consumer_lag(stream: list[dict[str, object]], next_offset: int) -> int:
def materialize_latest_payload_by_key(
    stream: list[dict[str, object]],
    topic: str,
) -> dict[str, dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/streaming/event-stream-basics/python -q
```
