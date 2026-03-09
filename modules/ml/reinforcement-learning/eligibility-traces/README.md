# Eligibility Trace Update

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Eligibility traces let recent states or features keep a decaying memory so credit can be spread across several past steps.

## Math

$$e_t = \gamma \lambda e_{t-1} + x_t$$

- $e_t$ -- updated eligibility trace
- $\gamma$ -- discount factor
- $\lambda$ -- trace decay parameter
- $x_t$ -- current feature activation

## Key Points

- Eligibility traces interpolate between one-step TD and longer-horizon credit assignment.
- Larger $\lambda$ keeps memory alive longer.
- This module focuses on the trace update itself, not the full TD($\lambda$) parameter update.

## Function

```python
def eligibility_trace_step(
    previous_trace: float,
    feature_value: float,
    gamma: float,
    lam: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/eligibility-traces/python -q
```
