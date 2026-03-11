# Change Budgets And Blast Radius

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Teams should size rollout plans to the blast radius of the change instead of spending the same deployment budget on every diff.

## Key Points

- Big write-path changes deserve stricter release controls than tiny read-only fixes.
- Blast radius comes from who is affected, how fast the effect propagates, and whether rollback is cheap.
- Change budgets help teams avoid stacking too many risky changes into one window.

## Minimal Code Mental Model

```python
radius = blast_radius(users_affected_percent=40, touches_write_path=True, multi_region=False)
budget = change_budget_available(open_high_risk_changes=1, oncall_load="medium")
rollout = progressive_delivery_required(radius, budget)
```

## Function

```python
def blast_radius(users_affected_percent: int, touches_write_path: bool, multi_region: bool) -> str:
def change_budget_available(open_high_risk_changes: int, oncall_load: str) -> bool:
def progressive_delivery_required(radius: str, budget_available: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/change-budgets-and-blast-radius/python -q
```
