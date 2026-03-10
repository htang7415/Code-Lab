# Log Bypass Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log bypass rate is the logarithm of the proportion of bypass cases.

## Math

$$
\log \mathrm{BypassRate} = \log\left(\frac{b}{n}\right)
$$

- $b$ -- bypass-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a bypass rate.
- Larger negative values correspond to rarer bypasses.
- This module returns negative infinity when the bypass rate is zero.

## Function

```python
def log_bypass_rate(bypass_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-bypass-rate/python -q
```
