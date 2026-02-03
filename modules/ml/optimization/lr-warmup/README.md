# Warmup

> Track: `ml` | Topic: `optimization`

## Concept

Warmup linearly ramps LR at the start of training.

## Math
$$\eta_t = \eta_0 \min\left(1, \frac{t}{T_{\text{warm}}}\right)$$

- $\eta$ -- learning rate (step size)
- $t$ -- timestep or iteration

- $\eta_t$ -- learning rate (step size) at step t
- $\eta_0$ -- learning rate (step size) for 0
- $T$ -- number of steps

## Function

```python
def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-warmup/python -q
```