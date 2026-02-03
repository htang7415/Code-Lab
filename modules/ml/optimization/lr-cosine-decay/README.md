# Cosine Decay

> Track: `ml` | Topic: `optimization`

## Concept

Cosine decay anneals LR smoothly to zero.

## Math
$$\eta_t = \eta_0 \frac{1}{2}\left(1+\cos\left(\frac{\pi t}{T}\right)\right)$$

- $\eta$ -- learning rate (step size)
- $\pi$ -- circle constant
- $t$ -- timestep or iteration

- $\eta_t$ -- learning rate (step size) at step t
- $\eta_0$ -- learning rate (step size) for 0
- $T$ -- number of steps

## Function

```python
def cosine_decay(lr: float, t: int, t_max: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-cosine-decay/python -q
```
