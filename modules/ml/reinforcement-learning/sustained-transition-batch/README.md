# Sustained Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Sustained transition batch vectorizes the indicator for transitions that remain sustained after the step.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
s_i = 1 - d_i
$$

## Key Points

- Each sustained transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is another batched continuation indicator.

## Function

```python
def sustained_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/sustained-transition-batch/python -q
```
