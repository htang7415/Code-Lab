# ELBO

> Track: `ml` | Topic: `fundamentals`

## Concept

ELBO lower-bounds log-likelihood in variational inference.

## Math

$$\mathrm{ELBO} = \mathbb{E}_q[\log p(x|z)] - \mathrm{KL}(q\|p)$$

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/elbo/python -q
```
