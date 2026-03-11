# Read Replica Routing

> Track: `databases` | Topic: `transactions`

## Concept

Read routing should send traffic to replicas when they are fresh enough, and fall back to the primary when a session needs read-after-write consistency.

## Key Points

- A replica is safe only if it has replayed at least the session's required commit position.
- Sessions that just wrote often need temporary primary reads.
- Once the replica catches up, the same session can route back to the replica.
- Routing decisions should follow replay progress, not a fixed delay guess.

## Minimal Code Mental Model

```python
session = new_session_state()
note_primary_write(session, committed_lsn=10)
target = choose_read_target(session, replica_applied_lsn=8)
release_if_caught_up(session, replica_applied_lsn=10)
```

## Function

```python
def new_session_state() -> dict[str, int]:
def note_primary_write(session_state: dict[str, int], committed_lsn: int) -> None:
def replica_can_serve(
    session_state: dict[str, int],
    replica_applied_lsn: int,
) -> bool:
def choose_read_target(
    session_state: dict[str, int],
    replica_applied_lsn: int,
    prefer_replica: bool = True,
) -> str:
def release_if_caught_up(
    session_state: dict[str, int],
    replica_applied_lsn: int,
) -> None:
```

## Run tests

```bash
pytest modules/databases/transactions/read-replica-routing/python -q
```
