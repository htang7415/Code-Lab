# VAE Blurry Samples and Posterior Collapse

> Track: `ml` | Topic: `generative`

## Concept

Posterior collapse happens when KL goes to zero.

## Math

$$KL → 0 indicates z ignored.$$

## Function

```python
def kl_is_low(kl: float, threshold: float = 0.1) -> bool:
```

## Run tests

```bash
pytest modules/ml/generative/vae-posterior-collapse/python -q
```
