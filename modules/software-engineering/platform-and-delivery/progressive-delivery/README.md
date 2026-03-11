# Progressive Delivery

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Progressive delivery reduces blast radius by exposing a change gradually and pausing when health signals degrade.

## Key Points

- Staged exposure is useful when rollback cost and user impact both matter.
- Expansion steps should be explicit instead of improvised mid-rollout.
- A bad rollout should pause before it reaches most users.

## Minimal Code Mental Model

```python
stage = next_rollout_stage(current_percentage=10, healthy=True)
radius = blast_radius(current_percentage=10, total_users=100000)
pause = should_pause_rollout(error_rate_delta=0.02, max_allowed_delta=0.01)
```

## Function

```python
def next_rollout_stage(current_percentage: int, healthy: bool) -> int:
def blast_radius(current_percentage: int, total_users: int) -> int:
def should_pause_rollout(error_rate_delta: float, max_allowed_delta: float) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/progressive-delivery/python -q
```
