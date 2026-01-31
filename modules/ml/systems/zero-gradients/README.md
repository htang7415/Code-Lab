# Zeroing Gradients

> Track: `ml` | Topic: `systems`

## Concept

Reset gradients to zero before the next backward pass.

## Math

g = 0

## Function

```python
def zero_grad(grads: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/systems/zero-gradients/python -q
```
