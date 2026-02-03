# He Initialization

> Track: `ml` | Topic: `deep-learning`

## Concept

He initialization keeps variance stable for ReLU activations. Demo uses deterministic
pseudo-random.

## Math

$$W \sim \mathcal{N}\left(0, \frac{2}{fan_{in}}\right)$$

- $\mathcal{N}$ -- normal (Gaussian) distribution
- $W$ -- weight matrix

## Function

```python
def he_normal(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/he-initialization/python -q
```
