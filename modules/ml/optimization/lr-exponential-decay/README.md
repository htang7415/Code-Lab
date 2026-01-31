# Exponential Decay

> Track: `ml` | Topic: `optimization`

## Concept

Exponential decay reduces LR continuously.

## Math

lr_t = lr * exp(-k t)

## Function

```python
def exp_decay(lr: float, k: float, t: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-exponential-decay/python -q
```
