# Optimizer Step

> Track: `ml` | Topic: `systems`

## Concept

Apply gradients to update parameters.

## Math

w = w - lr * g

## Function

```python
def step(w: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/systems/optimizer-step/python -q
```
