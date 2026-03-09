# Feature Scaling

> Track: `ml` | Topic: `data`

## Concept

Feature scaling rescales numeric inputs so one feature does not dominate another purely because of units or magnitude.
This module covers the two most common baselines: z-score standardization and min-max scaling.

## Math

$$z_i = \frac{x_i - \mu}{\sigma}$$

$$m_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$$

- $x_i$ -- original value
- $\mu$ -- mean of the feature
- $\sigma$ -- standard deviation of the feature
- $x_{\min}$ -- minimum feature value
- $x_{\max}$ -- maximum feature value

## Key Points

- Standardization is common for linear models, SVMs, and neural networks.
- Min-max scaling is useful when a bounded range is desired.
- Tree models often need much less scaling than distance-based or gradient-based models.

## Function

```python
def feature_scale(values: list[float], method: str = "zscore") -> list[float]:
```

## Run tests

```bash
pytest modules/ml/data/feature-scaling/python -q
```
