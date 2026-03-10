# Log Abandon Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log abandon rate is the logarithm of the proportion of abandoned cases.

## Math

$$
\log \mathrm{AbandonRate} = \log\left(\frac{a}{n}\right)
$$

- $a$ -- abandoned-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of an abandon rate.
- Larger negative values correspond to rarer abandonment.
- This module returns negative infinity when the abandon rate is zero.

## Function

```python
def log_abandon_rate(abandon_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-abandon-rate/python -q
```
