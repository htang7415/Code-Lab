# Bayesian Inference (Beta-Binomial)

> Track: `ml` | Topic: `fundamentals`

## Concept

Beta prior and Binomial likelihood yield Beta posterior.

## Math

$$\alpha' = \alpha + \text{successes},\ \beta' = \beta + \text{failures}$$

- $\alpha$ -- prior success pseudo-count (shape)
- $\beta$ -- prior failure pseudo-count (shape)
- $\alpha'$ -- posterior success pseudo-count
- $\beta'$ -- posterior failure pseudo-count
- $\mathrm{successes}$ -- observed successes count
- $\mathrm{failures}$ -- observed failures count

## Function

```python
def beta_posterior(alpha: float, beta: float, successes: int, failures: int) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/beta-binomial/python -q
```
