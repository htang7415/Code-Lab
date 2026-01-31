# RMSProp

> Track: `ml` | Topic: `optimization`

## Concept

RMSProp scales learning rates by running average of squared gradients.

## Math

v=βv+(1-β)g^2; w-=lr*g/(sqrt(v)+eps)

## Function

```python
def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/rmsprop/python -q
```
