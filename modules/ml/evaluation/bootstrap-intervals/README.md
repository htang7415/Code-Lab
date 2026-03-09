# Bootstrap Percentile Interval

> Track: `ml` | Topic: `evaluation`

## Concept

Bootstrap intervals estimate uncertainty by resampling a statistic many times and taking percentiles of the resampled values.

## Math

$$[\hat{\theta}_{\alpha/2}, \hat{\theta}_{1-\alpha/2}]$$

- $\hat{\theta}_{q}$ -- empirical bootstrap quantile at percentile $q$
- $\alpha$ -- total tail probability excluded from the interval

## Key Points

- Bootstrap intervals avoid strict normality assumptions.
- The percentile interval is simple and widely used.
- This module assumes the bootstrap statistics are already computed.

## Function

```python
def bootstrap_percentile_interval(
    bootstrap_statistics: list[float],
    alpha: float = 0.05,
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/bootstrap-intervals/python -q
```
