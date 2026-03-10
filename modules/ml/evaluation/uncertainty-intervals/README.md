# Uncertainty Intervals

> Track: `ml` | Topic: `evaluation`

## Concept

Interval estimates quantify uncertainty around a point estimate. The right
interval depends on the statistic: mean estimates often use normal-style
intervals, arbitrary estimators often use bootstrap intervals, and Bernoulli
rates often use Wilson intervals.

## Math

- $\bar{x} \pm z \frac{s}{\sqrt{n}}$
- $[\hat{\theta}_{\alpha/2}, \hat{\theta}_{1-\alpha/2}]$
- $\hat{p}_W = \frac{\hat{p} + z^2/(2n)}{1 + z^2/n}$

- $\bar{x}$ -- sample mean
- $s$ -- sample standard deviation
- $\hat{\theta}_q$ -- bootstrap percentile
- $\hat{p}$ -- observed success rate
- $n$ -- sample or trial count

## Key Points

- Mean confidence intervals are simple but rely on approximate normality.
- Bootstrap percentile intervals are flexible because they work from resampled statistics.
- Wilson intervals are a strong default for binary rates, especially with small samples.

## Function

```python
def mean_confidence_interval(samples: list[float], z: float = 1.96) -> tuple[float, float]:
def bootstrap_percentile_interval(bootstrap_statistics: list[float], alpha: float = 0.05) -> tuple[float, float]:
def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
```

## Pitfalls

- Mean intervals are misleading when the sample is tiny or badly skewed.
- Bootstrap intervals are only as good as the resampling distribution you generated.
- Wilson intervals are for binary proportions, not arbitrary means or losses.

## Run tests

```bash
pytest modules/ml/evaluation/uncertainty-intervals/python -q
```
