# Gradient Stability

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to learn why gradients stay usable or collapse as depth grows.

## First Principles

- Gradient magnitude changes as it passes through many layers.
- Repeated multiplication by numbers below one shrinks the signal.
- Repeated multiplication by numbers above one blows it up.
- Initialization and architecture choices mostly exist to keep this propagation stable.

## Core Math

Variance propagation:

$$
\mathrm{Var}(g_l) \approx \mathrm{Var}(g_{l+1}) \cdot \mathrm{Var}(W_l)
$$

Gradient chain:

$$
g_L = g_0 \prod_i w_i
$$

## Minimal Code Mental Model

```python
final_var = propagate_variance(var=1.0, layer_vars=[0.8, 1.1, 0.9])
chained = gradient_chain(weights=[0.5, 0.5], grad=1.0)
```

## Functions

```python
def propagate_variance(var: float, layer_vars: list[float]) -> float:
def gradient_chain(weights: list[float], grad: float = 1.0) -> float:
```

## When To Use What

- Use `propagate_variance` when reasoning about how initialization affects gradient scale layer by layer.
- Use `gradient_chain` when you want the simplest possible picture of vanishing or exploding behavior.
- Move to `initialization-methods` and `normalization-methods` when the question becomes how to fix instability in practice.

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-stability/python -q
```
