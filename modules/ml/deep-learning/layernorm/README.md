# LayerNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

LayerNorm normalizes across features within a single sample.

## Math

$$y = \frac{x - \mu_f}{\sqrt{\sigma_f^2 + \epsilon}}$$

## Function

```python
def layernorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/layernorm/python -q
```
