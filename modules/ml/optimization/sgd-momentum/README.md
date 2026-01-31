# SGD with Momentum

> Track: `ml` | Topic: `optimization`

## Concept

Momentum accumulates velocity to smooth updates.

## Math

v = μv + grad; w = w - lr * v

## Function

```python
def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/sgd-momentum/python -q
```
