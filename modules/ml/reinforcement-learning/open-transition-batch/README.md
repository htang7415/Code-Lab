# Open Transition Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Open transition batch vectorizes the indicator for transitions that remain open.

## Math

For done flags $d_i \in \{0, 1\}$:

$$
o_i = 1 - d_i
$$

## Key Points

- Each open transition maps to `1.0`.
- Each terminal transition maps to `0.0`.
- This is another batched companion to scalar continuation indicators.

## Function

```python
def open_transition_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/open-transition-batch/python -q
```
