# Deadlocks And Lock Ordering

> Track: `databases` | Topic: `transactions`

## Concept

Deadlocks happen when transactions wait on each other in a cycle, and a consistent global lock order is one of the simplest ways to avoid them.

## Key Points

- Exclusive locks on overlapping resources can deadlock if transactions acquire them in different orders.
- The bug is the conflicting order, not just the fact that two transactions overlap.
- A canonical order like sorted resource IDs removes inversion risk.
- Lock ordering is easier to apply than debugging deadlocks in production traces.

## Minimal Code Mental Model

```python
order_a = ["account:1", "account:2"]
order_b = ["account:2", "account:1"]
risk = has_deadlock_risk(order_a, order_b)
safe_orders = apply_canonical_order({"a": order_a, "b": order_b})
```

## Function

```python
def inversion_pairs(order_a: list[str], order_b: list[str]) -> list[tuple[str, str]]:
def has_deadlock_risk(order_a: list[str], order_b: list[str]) -> bool:
def canonical_lock_order(resources: list[str]) -> list[str]:
def apply_canonical_order(
    transaction_requests: dict[str, list[str]],
) -> dict[str, list[str]]:
```

## Run tests

```bash
pytest modules/databases/transactions/deadlocks-and-lock-ordering/python -q
```
