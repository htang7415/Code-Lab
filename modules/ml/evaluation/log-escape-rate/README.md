# Log Escape Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log escape rate is the logarithm of the proportion of escape cases.

## Math

$$
\log \mathrm{EscapeRate} = \log\left(\frac{e}{n}\right)
$$

- $e$ -- escape-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of an escape rate.
- Larger negative values correspond to rarer escapes.
- This module returns negative infinity when the escape rate is zero.

## Function

```python
def log_escape_rate(escape_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-escape-rate/python -q
```
