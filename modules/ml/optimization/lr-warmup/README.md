# Warmup

> Track: `ml` | Topic: `optimization`

## Concept

Warmup linearly ramps LR at the start of training.

## Math

lr_t = lr * min(1, t / warmup_steps)

## Function

```python
def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-warmup/python -q
```
