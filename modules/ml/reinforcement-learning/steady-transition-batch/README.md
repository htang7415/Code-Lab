# Steady Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Steady transition batch vectorizes the indicator for transitions that remain steady after the step.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
s_i = 1 - d_i
$$

## Key Points

- Each steady transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is another batched continuation indicator.

## Function

```python
def steady_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/steady-transition-batch/python -q
```
