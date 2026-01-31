# Backpropagation

> Track: `ml` | Topic: `deep-learning`

## Concept

Backprop computes gradients using the chain rule from output to inputs.

## Math

For z = w x, dL/dw = dL/dz * x.

## Function

```python
def linear_backprop(x: float, w: float, grad_out: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/backpropagation/python -q
```
