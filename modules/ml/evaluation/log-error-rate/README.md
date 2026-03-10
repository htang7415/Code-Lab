# Log Error Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log error rate is the logarithm of a generic error rate.

## Math

$$
\log \mathrm{ErrorRate} = \log\left(\frac{e}{n}\right)
$$

- $e$ -- error count
- $n$ -- total count

## Key Points

- This is a generic log-scaled error-rate helper.
- Larger negative values correspond to rarer errors.
- This module returns negative infinity when the error rate is zero.

## Function

```python
def log_error_rate(error_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-error-rate/python -q
```
