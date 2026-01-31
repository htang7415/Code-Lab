# Prediction Distribution Monitoring

> Track: `ml` | Topic: `mlops`

## Concept

Track shifts in prediction mean or variance over time.

## Math

$$\Delta \mu = \left|\mu_{\text{new}} - \mu_{\text{old}}\right|$$

## Function

```python
def mean_shift(old: list[float], new: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/prediction-monitoring/python -q
```
