# Log Miss Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log miss rate is the logarithm of the proportion of misses.

## Math

$$
\log \mathrm{MissRate} = \log\left(\frac{m}{n}\right)
$$

- $m$ -- miss count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a miss rate.
- Larger negative values correspond to rarer misses.
- This module returns negative infinity when the miss rate is zero.

## Function

```python
def log_miss_rate(miss_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-miss-rate/python -q
```
