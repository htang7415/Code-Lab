# Prediction Distribution Monitoring

> Track: `ml` | Topic: `mlops`

## Concept

Track shifts in prediction mean or variance over time.

## Math
$$\Delta \mu = |\mu_{\text{new}} - \mu_{\text{old}}|$$

- $\Delta \mu$ -- change in mean
- $\mu_{\text{new}}$ -- mean of new predictions
- $\mu_{\text{old}}$ -- mean of reference predictions

## Function

```python
def mean_shift(old: list[float], new: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/prediction-monitoring/python -q
```