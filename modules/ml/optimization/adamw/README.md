# AdamW

> Track: `ml` | Topic: `optimization`

## Concept

AdamW decouples weight decay from adaptive updates.

## Math

$$w = w - lr * (m/√v) - lr*wd*w$$

## Function

```python
def adamw_step(w: float, grad: float, m: float, v: float, lr: float, wd: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adamw/python -q
```
