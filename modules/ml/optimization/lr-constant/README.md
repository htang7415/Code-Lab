# Constant Learning Rate

> Track: `ml` | Topic: `optimization`

## Concept

Constant LR keeps the step size fixed.

## Math

$$\text{lr}_t = \text{lr}$$

## Function

```python
def constant_lr(lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-constant/python -q
```
