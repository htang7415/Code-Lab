# Log Shed Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log shed rate is the logarithm of the proportion of shed cases.

## Math

$$
\log \mathrm{ShedRate} = \log\left(\frac{s}{n}\right)
$$

- $s$ -- shed-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a shed rate.
- Larger negative values correspond to rarer shedding.
- This module returns negative infinity when the shed rate is zero.

## Function

```python
def log_shed_rate(shed_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-shed-rate/python -q
```
