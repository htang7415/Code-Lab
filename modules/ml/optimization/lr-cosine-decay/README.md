# Cosine Decay

> Track: `ml` | Topic: `optimization`

## Concept

Cosine decay anneals LR smoothly to zero.

## Math

$$\text{lr}_t = \text{lr} \cdot \frac{1}{2}\left(1+\cos\left(\frac{\pi t}{T}\right)\right)$$

## Function

```python
def cosine_decay(lr: float, t: int, t_max: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-cosine-decay/python -q
```
