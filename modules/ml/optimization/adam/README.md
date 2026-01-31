# Adam

> Track: `ml` | Topic: `optimization`

## Concept

Adam combines momentum and adaptive learning rates.

## Math

m=β1 m+(1-β1)g; v=β2 v+(1-β2)g^2; w-=lr*m/(sqrt(v)+eps)

## Function

```python
def adam_step(w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adam/python -q
```
