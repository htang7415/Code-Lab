# Replication Lag Mental Model

> Track: `databases` | Topic: `transactions`

## Concept

Primary commits become visible on a replica only after the replica has replayed those log records. Replication lag is the gap between primary progress and replica replay progress.

## Key Points

- A committed write can exist on the primary while still being invisible on a replica.
- Lag is usually tracked by an LSN or sequence position, not just by wall-clock time.
- Read-after-write guarantees fail on a stale replica even when the primary commit succeeded.
- The core mental model is “primary commit first, replica replay later.”

## Minimal Code Mental Model

```python
log = empty_primary_log()
lsn = commit_write(log, "order:o1", {"status": "placed"})
replica = empty_replica_state()
lag = replica_lag(log, replica)
apply_replica_writes(replica, log, up_to_lsn=lsn)
```

## Function

```python
def empty_primary_log() -> list[dict[str, object]]:
def commit_write(
    primary_log: list[dict[str, object]],
    key: str,
    value: object | None,
) -> int:
def empty_replica_state() -> dict[str, object]:
def apply_replica_writes(
    replica_state: dict[str, object],
    primary_log: list[dict[str, object]],
    up_to_lsn: int,
) -> list[int]:
def replica_lag(
    primary_log: list[dict[str, object]],
    replica_state: dict[str, object],
) -> int:
def visible_value_on_primary(
    primary_log: list[dict[str, object]],
    key: str,
) -> object | None:
def visible_value_on_replica(
    replica_state: dict[str, object],
    key: str,
) -> object | None:
```

## Run tests

```bash
pytest modules/databases/transactions/replication-lag-mental-model/python -q
```
