# Exponential Decay

> Track: `ml` | Topic: `optimization`

## Concept

Exponential decay reduces LR continuously.

## Math

$$\text{lr}_t = \text{lr} \cdot \exp(-k t)$$

## Function

```python
def exp_decay(lr: float, k: float, t: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-exponential-decay/python -q
```
