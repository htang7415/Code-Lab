# Two-Sample t-test

> Track: `ml` | Topic: `fundamentals`

## Concept

Two-sample t-test compares means of two groups.

## Math

$$t = \frac{m_1 - m_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

## Function

```python
def t_stat(x: list[float], y: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/two-sample-t-test/python -q
```
