# Idempotent Consumers

> Track: `databases` | Topic: `streaming`

## Concept

An idempotent consumer can safely see the same event more than once without applying the business effect twice.

## Key Points

- At-least-once delivery means duplicates are normal, not rare.
- The consumer usually needs a processed-event ledger keyed by event ID.
- Business state should only change the first time a given event ID is seen.
- Idempotency is one of the main reasons streaming systems stay correct under retries.

## Minimal Code Mental Model

```python
processed_ids = set()
state = {}
event = {"event_id": "evt-1", "key": "doc-1", "status": "embedded"}
first = process_status_event(event, processed_ids, state)
second = process_status_event(event, processed_ids, state)
```

## Function

```python
def process_status_event(
    event: dict[str, str],
    processed_ids: set[str],
    state: dict[str, str],
) -> bool:
def consume_batch(
    events: list[dict[str, str]],
    processed_ids: set[str],
    state: dict[str, str],
) -> int:
```

## Run tests

```bash
pytest modules/databases/streaming/idempotent-consumers/python -q
```
