# Cosine Decay

> Track: `ml` | Topic: `optimization`

## Concept

Cosine decay anneals LR smoothly to zero.

## Math

lr_t = lr * 0.5 * (1 + cos(pi t / T))

## Function

```python
def cosine_decay(lr: float, t: int, t_max: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-cosine-decay/python -q
```
