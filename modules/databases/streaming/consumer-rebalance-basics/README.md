# Consumer Rebalance Basics

> Track: `databases` | Topic: `streaming`

## Concept

When consumers join or leave a group, partition ownership changes. That rebalance is necessary for availability and load sharing, but it can also pause work and move state around.

## Key Points

- Partitions belong to consumers, not the whole group at once.
- A rebalance redistributes ownership when group membership changes.
- More consumers can reduce per-consumer load, but they may force partition movement and state handoff.
- Operators care about both balance and churn: a perfectly even plan can still be disruptive if too much moves.

## Minimal Code Mental Model

```python
summary = rebalance_summary(
    partitions=[0, 1, 2, 3],
    before_consumers=["a", "b"],
    after_consumers=["a", "b", "c"],
)
```

## Function

```python
def assign_round_robin(partitions: list[int], consumers: list[str]) -> dict[str, list[int]]:
def consumer_load(assignments: dict[str, list[int]]) -> dict[str, int]:
def moved_partitions(
    before: dict[str, list[int]],
    after: dict[str, list[int]],
) -> list[tuple[int, str | None, str | None]]:
def rebalance_summary(
    partitions: list[int],
    before_consumers: list[str],
    after_consumers: list[str],
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/streaming/consumer-rebalance-basics/python -q
```
