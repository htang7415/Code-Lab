# Log Failure Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log failure rate is the logarithm of the proportion of failures or misses.

## Math

$$
\log \mathrm{FailureRate} = \log\left(\frac{f}{n}\right)
$$

- $f$ -- failure count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a miss or failure rate.
- Larger negative values correspond to rarer failures.
- This module returns negative infinity when the failure rate is zero.

## Function

```python
def log_failure_rate(failure_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-failure-rate/python -q
```
