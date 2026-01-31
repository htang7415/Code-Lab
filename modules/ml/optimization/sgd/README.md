# SGD

> Track: `ml` | Topic: `optimization`

## Concept

SGD updates parameters by stepping opposite the gradient.

## Math

w = w - lr * grad

## Function

```python
def sgd_step(w: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/sgd/python -q
```
