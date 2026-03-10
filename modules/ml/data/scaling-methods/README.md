# Scaling Methods

> Track: `ml` | Topic: `data`

## Concept

Numeric preprocessing can either rescale all values, use robust statistics to
reduce outlier sensitivity, or directly cap extreme values. These choices are
closely related and are usually selected together during feature preparation.

## Math

- $z_i = \frac{x_i - \mu}{\sigma}$
- $m_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$
- $r_i = \frac{x_i - \mathrm{median}(x)}{\mathrm{IQR}(x)}$
- $\tilde{x}_i = \min(\max(x_i, L), U)$

- $\mu$ -- mean of the feature
- $\sigma$ -- standard deviation
- $\mathrm{IQR}$ -- interquartile range
- $L, U$ -- clipping bounds

## Key Points

- Z-score scaling is a strong default for gradient-based and distance-based models.
- Min-max scaling is useful when a bounded numeric range is desirable.
- Robust scaling is safer when heavy outliers make mean and standard deviation unstable.
- Clipping is not the same as scaling; it only changes values outside a chosen interval.

## Function

```python
def feature_scale(values: list[float], method: str = "zscore") -> list[float]:
def robust_scale(values: list[float]) -> list[float]:
def clip_features(values: list[float], min_value: float, max_value: float) -> list[float]:
```

## Pitfalls

- Scaling statistics should be fit on training data only.
- Robust scaling still fails when the feature has effectively zero spread.
- Clipping can hide important signal if the bounds are chosen mechanically.

## Run tests

```bash
pytest modules/ml/data/scaling-methods/python -q
```
