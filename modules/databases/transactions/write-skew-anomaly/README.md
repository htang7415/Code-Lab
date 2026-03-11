# Write Skew Anomaly

> Track: `databases` | Topic: `transactions`

## Concept

Write skew happens when two transactions read the same valid snapshot, each makes a different update, and the combined result violates a cross-row invariant.

## Key Points

- Each transaction can look locally correct on its own snapshot.
- The broken rule usually lives across multiple rows, not inside one row.
- Snapshot isolation prevents many read-write conflicts but does not automatically protect every multi-row invariant.
- This is why some rules need explicit locking, materialized checks, or serializable isolation.

## Minimal Code Mental Model

```python
summary = simulate_write_skew(
    initial_rows=[clinician("alice", True), clinician("bob", True)],
    minimum_on_call=1,
    first_clinician="alice",
    second_clinician="bob",
)
```

## Function

```python
def clinician(name: str, on_call: bool) -> dict[str, object]:
def on_call_count(rows: list[dict[str, object]]) -> int:
def can_leave_on_call(snapshot_rows: list[dict[str, object]], minimum_on_call: int) -> bool:
def apply_leave_on_call(rows: list[dict[str, object]], clinician_name: str) -> list[dict[str, object]]:
def simulate_write_skew(
    initial_rows: list[dict[str, object]],
    minimum_on_call: int,
    first_clinician: str,
    second_clinician: str,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/transactions/write-skew-anomaly/python -q
```
