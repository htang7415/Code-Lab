# AIC and BIC

> Track: `ml` | Topic: `models`

## Concept

AIC and BIC compare models by trading off data fit against model complexity.
Both start from the log-likelihood and then add a penalty for extra parameters.

## Math

$$\mathrm{AIC} = 2k - 2 \log L$$

$$\mathrm{BIC} = k \log n - 2 \log L$$

- $k$ -- number of free parameters
- $n$ -- number of observed samples
- $\log L$ -- model log-likelihood on the data

## Key Points

- Lower AIC or BIC is better.
- BIC penalizes extra parameters more strongly as sample size grows.
- These criteria compare fitted models on the same dataset.

## Function

```python
def aic_bic(
    log_likelihood: float,
    num_params: int,
    num_samples: int,
) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/models/bic-aic/python -q
```
