# Developer Experience As Leverage

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Developer experience matters because slow setup, testing, or deployment feedback multiplies across every engineer and every change.

## Key Points

- Small per-engineer delays become large org-wide waste.
- Setup time, test feedback time, and deploy feedback time are high-signal DX metrics.
- DX work is leverage when it saves repeated minutes across many engineers every week.

## Minimal Code Mental Model

```python
risk = feedback_loop_risk(setup_minutes=20, test_minutes=15, deploy_feedback_minutes=10)
worth_it = dx_investment_worth_it(engineers=10, minutes_saved_per_week=30)
focus = dx_priority(setup_minutes=20, test_minutes=5, deploy_feedback_minutes=8)
```

## Function

```python
def feedback_loop_risk(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
def dx_investment_worth_it(engineers: int, minutes_saved_per_week: int) -> bool:
def dx_priority(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/developer-experience-as-leverage/python -q
```
