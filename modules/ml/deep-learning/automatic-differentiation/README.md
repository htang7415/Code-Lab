# Automatic Differentiation

> Track: `ml` | Topic: `deep-learning`

## Concept

Autodiff computes derivatives by composing local gradients.

## Math

If y = x^2 and z = y + 3, then dz/dx = 2x.

## Function

```python
def forward_grad(x: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/automatic-differentiation/python -q
```
