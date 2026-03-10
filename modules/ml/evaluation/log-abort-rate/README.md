# Log Abort Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log abort rate is the logarithm of the proportion of aborted cases.

## Math

$$
\log \mathrm{AbortRate} = \log\left(\frac{a}{n}\right)
$$

- $a$ -- abort count
- $n$ -- total count

## Key Points

- This is a log-scaled version of an abort rate.
- Larger negative values correspond to rarer aborts.
- This module returns negative infinity when the abort rate is zero.

## Function

```python
def log_abort_rate(abort_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-abort-rate/python -q
```
