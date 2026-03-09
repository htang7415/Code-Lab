# Done Indicator Batch

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Done indicator batches convert a list of done flags into numeric terminal indicators.

## Math

$$
i_k = d_k
$$

- $d_k$ -- done flag for transition $k$
- $i_k$ -- numeric indicator, `1.0` if done and `0.0` otherwise

## Key Points

- This is the vectorized batch version of a scalar done indicator.
- It is useful for vectorized RL pipelines that need numeric done flags.
- This module returns floats for direct use in tensor-like code.

## Function

```python
def done_indicator_batch(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/done-indicator-batch/python -q
```
