# ELBO

> Track: `ml` | Topic: `fundamentals`

## Concept

ELBO lower-bounds log-likelihood in variational inference.

## Math

ELBO = E_q[log p(x|z)] - KL(q||p)

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/elbo/python -q
```
