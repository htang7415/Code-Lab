# Effect on Gradient Flow

> Track: `ml` | Topic: `deep-learning`

## Concept

Initialization affects gradient variance as it propagates through layers.

## Math
$$\mathrm{Var}(g_l) \approx \mathrm{Var}(g_{l+1}) \cdot \mathrm{Var}(W_l)$$

- $g_l$ -- gradient for l
- $W_l$ -- weight matrix for l
- $g$ -- gradient
- $W$ -- weight matrix

## Function

```python
def propagate_variance(var: float, layer_vars: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-flow/python -q
```