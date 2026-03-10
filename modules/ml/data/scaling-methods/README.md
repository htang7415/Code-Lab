# Scaling Methods

> Track: `ml` | Topic: `data`

## Purpose

Use this module to compare the main numeric preprocessing choices:
- standard scaling
- bounded scaling
- robust scaling
- direct clipping

## First Principles

- Scaling changes numeric geometry before the model sees the feature.
- Distance-based and gradient-based models often depend strongly on feature scale.
- Robust scaling is about using resistant statistics, not just using a different constant.
- Clipping is different from scaling because it changes only the extreme values.

## Core Math

- Z-score scaling:
  $$
  z_i = \frac{x_i - \mu}{\sigma}
  $$
- Min-max scaling:
  $$
  m_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}
  $$
- Robust scaling:
  $$
  r_i = \frac{x_i - \mathrm{median}(x)}{\mathrm{IQR}(x)}
  $$

## Minimal Code Mental Model

```python
scaled = feature_scale(values, method="zscore")
robust = robust_scale(values)
clipped = clip_features(values, min_value, max_value)
```

## Function

```python
def feature_scale(values: list[float], method: str = "zscore") -> list[float]:
def robust_scale(values: list[float]) -> list[float]:
def clip_features(values: list[float], min_value: float, max_value: float) -> list[float]:
```

## When To Use What

- Use z-score scaling as a default for many gradient-based and distance-based models.
- Use min-max scaling when you need an explicit bounded range.
- Use robust scaling when outliers make mean and standard deviation unstable.
- Use clipping when extreme values are the main problem rather than overall scale.

## Run tests

```bash
pytest modules/ml/data/scaling-methods/python -q
```
