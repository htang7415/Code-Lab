# Gradient Clipping

> Track: `ml` | Topic: `optimization`

## Concept

Clip gradient norm to avoid exploding gradients.

## Math

g = g * min(1, clip / ||g||)

## Function

```python
def clip_norm(grad: list[float], clip: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/optimization/gradient-clipping/python -q
```
