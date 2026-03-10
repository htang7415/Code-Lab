# Log Fallback Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log fallback rate is the logarithm of the proportion of fallback cases.

## Math

$$
\log \mathrm{FallbackRate} = \log\left(\frac{f}{n}\right)
$$

- $f$ -- fallback-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a fallback rate.
- Larger negative values correspond to rarer fallbacks.
- This module returns negative infinity when the fallback rate is zero.

## Function

```python
def log_fallback_rate(fallback_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-fallback-rate/python -q
```
