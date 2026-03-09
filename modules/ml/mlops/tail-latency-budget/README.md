# Tail Latency Budget

> Track: `ml` | Topic: `mlops`

## Concept

Tail latency budget measures how much of an allowed high-percentile latency budget has been consumed.

## Math

$$
\mathrm{budget\_usage} = \frac{\mathrm{observed\_tail\_latency}}{\mathrm{latency\_budget}}
$$

$$
\mathrm{remaining\_fraction} = \max(0, 1 - \mathrm{budget\_usage})
$$

- $\mathrm{observed\_tail\_latency}$ -- measured high-percentile latency, such as p95 or p99
- $\mathrm{latency\_budget}$ -- allowed tail-latency target

## Key Points

- Tail latency is often a better operational guardrail than average latency.
- A budget usage above `1.0` means the service has exceeded its target.
- This module exposes both usage and remaining fraction.

## Function

```python
def tail_latency_budget_status(observed_tail_ms: float, budget_ms: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/tail-latency-budget/python -q
```
