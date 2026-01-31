# VAE

> Track: `ml` | Topic: `generative`

## Concept

VAEs maximize ELBO = reconstruction - KL.

## Math

ELBO = E_q[log p(x|z)] - KL(q(z)||p(z))

## Function

```python
def elbo(recon: float, kl: float) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/vae/python -q
```
