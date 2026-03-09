# Undone Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Undone indicators convert a batch of done flags into numeric indicators for continuing transitions.

## Math

$$
u_k = 1 - d_k
$$

- $d_k$ -- done flag for transition $k$
- $u_k$ -- numeric indicator, `1.0` if the transition continues and `0.0` otherwise

## Key Points

- This is the complement of a done indicator batch.
- It is useful for masking bootstrap terms on ongoing transitions.
- This module returns floats for direct use in tensor-like code.

## Function

```python
def undone_indicator(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/undone-indicator/python -q
```
