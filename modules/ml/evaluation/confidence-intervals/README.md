# Mean Confidence Interval

> Track: `ml` | Topic: `evaluation`

## Concept

A confidence interval summarizes uncertainty around an estimated mean by combining sample variability with sample size.

## Math

$$\bar{x} \pm z \frac{s}{\sqrt{n}}$$

- $\bar{x}$ -- sample mean
- $s$ -- sample standard deviation
- $n$ -- number of samples
- $z$ -- critical value for the desired confidence level

## Key Points

- Intervals shrink as sample size grows.
- Wider intervals indicate either more noise or less data.
- This module uses the common normal-approximation form for the mean.

## Function

```python
def mean_confidence_interval(
    samples: list[float],
    z: float = 1.96,
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/confidence-intervals/python -q
```
