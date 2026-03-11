# Anti-Entropy And Repair

> Track: `databases` | Topic: `nosql`

## Concept

Replicas can drift apart after missed writes or partial failures. Anti-entropy compares states in the background and repairs divergent keys until replicas converge again.

## Key Points

- Replication alone does not guarantee every replica stayed in sync forever.
- Anti-entropy is a background consistency process, not the main write path.
- Repair usually copies the newest known version of a divergent key.
- The system should converge after repair even if replicas were temporarily inconsistent.

## Minimal Code Mental Model

```python
left = empty_replica("left")
right = empty_replica("right")
write_value(left, "doc:1", "v2", version=2)
write_value(right, "doc:1", "v1", version=1)
keys = divergent_keys(left, right)
repair_pair(left, right)
```

## Function

```python
def empty_replica(name: str) -> dict[str, object]:
def write_value(
    replica: dict[str, object],
    key: str,
    value: object,
    version: int,
) -> None:
def divergent_keys(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
def repair_pair(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
def visible_values(replica: dict[str, object]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/anti-entropy-and-repair/python -q
```
