# Linear Autoencoder

> Track: `ml` | Topic: `representation`

## Concept

An autoencoder compresses inputs into a bottleneck and reconstructs them.
With a linear encoder and decoder, it behaves like a learned projection.

## Math

$$z = W x,\quad \hat{x} = W^T z$$

## Function

```python
def linear_autoencode(x: list[float], W: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/representation/autoencoder/python -q
```
