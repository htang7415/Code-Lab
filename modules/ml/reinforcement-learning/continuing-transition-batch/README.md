# Continuing Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Continuing transition batch vectorizes the indicator for transitions that do not terminate.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
c_i = 1 - d_i
$$

## Key Points

- Each continuing transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is the batched companion of scalar continuing-transition indicators.

## Function

```python
def continuing_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/continuing-transition-batch/python -q
```
