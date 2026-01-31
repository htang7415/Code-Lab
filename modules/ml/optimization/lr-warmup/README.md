# Warmup

> Track: `ml` | Topic: `optimization`

## Concept

Warmup linearly ramps LR at the start of training.

## Math

$$\text{lr}_t = \text{lr} \cdot \min\left(1, \frac{t}{T_{\text{warmup}}}\right)$$

## Function

```python
def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-warmup/python -q
```
