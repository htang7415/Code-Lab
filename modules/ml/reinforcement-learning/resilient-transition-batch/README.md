# Resilient Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Resilient transition batch vectorizes the indicator for transitions that remain resilient after the step.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
r_i = 1 - d_i
$$

## Key Points

- Each resilient transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is another batched continuation indicator.

## Function

```python
def resilient_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/resilient-transition-batch/python -q
```
