# Log Skip Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log skip rate is the logarithm of the proportion of skipped cases.

## Math

$$
\log \mathrm{SkipRate} = \log\left(\frac{s}{n}\right)
$$

- $s$ -- skipped-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a skip rate.
- Larger negative values correspond to rarer skips.
- This module returns negative infinity when the skip rate is zero.

## Function

```python
def log_skip_rate(skip_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-skip-rate/python -q
```
