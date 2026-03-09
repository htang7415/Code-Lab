# Not Done Mask

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Not-done masks convert done flags into numeric indicators that are `1` for continuing transitions and `0` for terminal ones.

## Math

$$
m_i = 1 - d_i
$$

- $d_i$ -- terminal indicator, 1 if the transition ends the episode
- $m_i$ -- not-done mask used in bootstrap equations

## Key Points

- This is an alias for the continuation-side mask concept.
- It is useful when code follows the common `not_done` naming convention.
- This module returns floats for direct multiplication in vectorized code.

## Function

```python
def not_done_mask(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/not-done-mask/python -q
```
