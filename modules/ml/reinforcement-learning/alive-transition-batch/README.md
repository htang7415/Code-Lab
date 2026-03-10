# Alive Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Alive transition batch vectorizes the indicator for transitions that are still alive.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
a_i = 1 - d_i
$$

## Key Points

- Each alive transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is a batched version of scalar alive or continuing indicators.

## Function

```python
def alive_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/alive-transition-batch/python -q
```
