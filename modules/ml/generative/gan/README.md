# GAN

> Track: `ml` | Topic: `generative`

## Concept

GANs train a generator and discriminator adversarially.

## Math

$$L_D = -\log D(x) - \log\left(1 - D(G(z))\right)$$

## Function

```python
def gan_loss(d_real: float, d_fake: float) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/gan/python -q
```
