# Mixed Precision Training

> Track: `ml` | Topic: `systems`

## Concept

Mixed precision scales gradients to avoid underflow.

## Math

g_scaled = g * scale

## Function

```python
def scale_gradients(grads: list[float], scale: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/systems/mixed-precision/python -q
```
