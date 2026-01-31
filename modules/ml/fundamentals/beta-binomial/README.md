# Bayesian Inference (Beta-Binomial)

> Track: `ml` | Topic: `fundamentals`

## Concept

Beta prior and Binomial likelihood yield Beta posterior.

## Math

$$\alpha' = \alpha + \text{successes},\ \beta' = \beta + \text{failures}$$

## Function

```python
def beta_posterior(alpha: float, beta: float, successes: int, failures: int) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/beta-binomial/python -q
```
