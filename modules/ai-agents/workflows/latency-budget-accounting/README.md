# Latency Budget Accounting

> Track: `ai-agents` | Topic: `workflows`

## Concept

Latency budget accounting makes an agent track how much response time is left, how much each remaining step can spend, and when the workflow should stream, fall back, or review instead of pretending it is still realtime.

## Key Points

- Realtime behavior starts with a fixed total budget, not with a vague speed target.
- Reserve response time before planning step budgets.
- Step budgets should be explicit so overruns trigger a controlled route instead of silent drift.

## Core Math

- Remaining latency:
  $$
  \text{total budget} - \text{elapsed} - \text{reserved response}
  $$
- Per-step budget:
  $$
  \frac{\text{remaining latency}}{\text{remaining steps}}
  $$

## Minimal Code Mental Model

```python
remaining = remaining_latency_budget(total_budget_ms=1200, elapsed_ms=350, reserved_response_ms=200)
step_budget = per_step_latency_budget(remaining, remaining_steps=2)
route = latency_budget_route(step_latency_ms=320, step_budget_ms=step_budget, can_stream=True, can_fallback=True)
```

## Function

```python
def remaining_latency_budget(
    total_budget_ms: int,
    elapsed_ms: int,
    reserved_response_ms: int = 0,
) -> int:
def per_step_latency_budget(remaining_budget_ms: int, remaining_steps: int) -> int:
def latency_budget_route(
    step_latency_ms: int,
    step_budget_ms: int,
    can_stream: bool,
    can_fallback: bool,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/latency-budget-accounting/python -q
```
