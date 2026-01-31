# VAE

> Track: `ml` | Topic: `generative`

## Concept

VAEs maximize ELBO = reconstruction - KL.

## Math

$$\mathrm{ELBO} = \mathbb{E}_q[\log p(x|z)] - \mathrm{KL}(q(z)\|p(z))$$

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/vae/python -q
```
