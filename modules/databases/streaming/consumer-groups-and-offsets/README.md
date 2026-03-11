# Consumer Groups And Offsets

> Track: `databases` | Topic: `streaming`

## Concept

Consumer groups split partitions across consumers, and committed offsets tell each consumer where to resume after a restart.

## Key Points

- Each partition is usually owned by one consumer at a time within a group.
- Offsets represent position, not the payload itself.
- Committing `last_processed + 1` makes restart behavior explicit.
- Rebalancing changes which consumer owns which partitions, but the committed offsets stay with the group.

## Minimal Code Mental Model

```python
assignments = assign_partitions([0, 1, 2], ["c1", "c2"])
events = poll_group(stream, assignments, committed_offsets, "c1")
commit_offsets(committed_offsets, events)
```

## Function

```python
def assign_partitions(
    partitions: list[int],
    consumers: list[str],
) -> dict[str, list[int]]:
def poll_group(
    stream: dict[int, list[dict[str, object]]],
    assignments: dict[str, list[int]],
    committed_offsets: dict[int, int],
    consumer_id: str,
    max_events: int | None = None,
) -> list[dict[str, object]]:
def commit_offsets(
    committed_offsets: dict[int, int],
    events: list[dict[str, object]],
) -> None:
```

## Run tests

```bash
pytest modules/databases/streaming/consumer-groups-and-offsets/python -q
```
