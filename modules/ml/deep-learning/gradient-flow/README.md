# Effect on Gradient Flow

> Track: `ml` | Topic: `deep-learning`

## Concept

Initialization affects gradient variance as it propagates through layers.

## Math

$$Var(g_{l}) ≈ Var(g_{l+1}) * Var(W_l)$$

## Function

```python
def propagate_variance(var: float, layer_vars: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-flow/python -q
```
