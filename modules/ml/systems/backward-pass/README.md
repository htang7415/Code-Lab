# Backward Pass

> Track: `ml` | Topic: `systems`

## Concept

Backward pass computes gradients of loss w.r.t parameters.

## Math

$$dL/dw = dL/dy * x$$

## Function

```python
def backward(dy: float, x: float) -> float:
```

## Run tests

```bash
pytest modules/ml/systems/backward-pass/python -q
```
