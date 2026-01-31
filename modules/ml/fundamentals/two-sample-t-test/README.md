# Two-Sample t-test

> Track: `ml` | Topic: `fundamentals`

## Concept

Two-sample t-test compares means of two groups.

## Math

t = (m1-m2) / sqrt(s1^2/n1 + s2^2/n2)

## Function

```python
def t_stat(x: list[float], y: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/two-sample-t-test/python -q
```
