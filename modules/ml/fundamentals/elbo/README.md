# ELBO

> Track: `ml` | Topic: `fundamentals`

## Concept

ELBO lower-bounds log-likelihood in variational inference.

## Math

$$\mathrm{ELBO} = \mathbb{E}_q[\log p(x|z)] - \mathrm{KL}(q\|p)$$

- $\mathrm{ELBO}$ -- evidence lower bound
- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $\mathbb{E}$ -- expectation
- $q$ -- probability distribution
- $p$ -- probability
- $x$ -- input (feature vector or sample)
- $z$ -- latent or pre-activation value

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/elbo/python -q
```
