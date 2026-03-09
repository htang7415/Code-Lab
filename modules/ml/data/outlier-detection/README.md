# Z-Score Outlier Screening

> Track: `ml` | Topic: `data`

## Concept

Outlier screening is a lightweight preprocessing step for spotting extreme values before fitting a downstream model.
This module uses z-scores as a simple baseline.

## Math

$$z_i = \frac{x_i - \mu}{\sigma}$$

- $x_i$ -- observed value
- $\mu$ -- sample mean
- $\sigma$ -- sample standard deviation
- $z_i$ -- standardized distance from the mean

## Key Points

- Z-score screening is simple but sensitive to the very outliers it tries to detect.
- It works best when the feature is roughly unimodal and not too heavy-tailed.
- Robust alternatives include IQR rules and model-based methods such as Isolation Forest.

## Function

```python
def z_score_outliers(values: list[float], threshold: float = 3.0) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/data/outlier-detection/python -q
```
