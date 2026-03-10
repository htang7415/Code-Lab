# Log Timeout Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log timeout rate is the logarithm of the proportion of timeout cases.

## Math

$$
\log \mathrm{TimeoutRate} = \log\left(\frac{t}{n}\right)
$$

- $t$ -- timeout count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a timeout rate.
- Larger negative values correspond to rarer timeouts.
- This module returns negative infinity when the timeout rate is zero.

## Function

```python
def log_timeout_rate(timeout_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-timeout-rate/python -q
```
