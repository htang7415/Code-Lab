# Log Hit Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log hit rate is the logarithm of the proportion of successful hits.

## Math

$$
\log \mathrm{HitRate} = \log\left(\frac{h}{n}\right)
$$

- $h$ -- hit count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a binary success rate.
- Larger negative values correspond to rarer hits.
- This module returns negative infinity when the hit rate is zero.

## Function

```python
def log_hit_rate(hit_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-hit-rate/python -q
```
