# Log Reject Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log reject rate is the logarithm of the proportion of rejected cases.

## Math

$$
\log \mathrm{RejectRate} = \log\left(\frac{r}{n}\right)
$$

- $r$ -- reject count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a reject rate.
- Larger negative values correspond to rarer rejects.
- This module returns negative infinity when the reject rate is zero.

## Function

```python
def log_reject_rate(reject_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-reject-rate/python -q
```
