# Replica Failover Routing

> Track: `databases` | Topic: `transactions`

## Concept

Failover routing swaps the write target to a promoted replica when the old primary is unavailable, then keeps reads off unhealthy nodes.

## Key Points

- A failed primary cannot keep serving writes.
- A healthy replica can become the new primary during failover.
- Reads should avoid unhealthy nodes even if they were replicas before.
- The routing layer needs explicit cluster state, not just a hardcoded “primary host”.

## Minimal Code Mental Model

```python
state = cluster_state("db-a", ["db-b", "db-c"])
mark_node_down(state, "db-a")
promote_replica(state, "db-b")
writer = write_target(state)
reader = read_target(state)
```

## Function

```python
def cluster_state(primary: str, replicas: list[str]) -> dict[str, object]:
def mark_node_down(state: dict[str, object], node_id: str) -> None:
def mark_node_up(state: dict[str, object], node_id: str) -> None:
def promote_replica(state: dict[str, object], replica_id: str) -> None:
def write_target(state: dict[str, object]) -> str | None:
def read_target(state: dict[str, object], prefer_replica: bool = True) -> str | None:
```

## Run tests

```bash
pytest modules/databases/transactions/replica-failover-routing/python -q
```
