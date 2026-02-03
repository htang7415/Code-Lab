# Exponential Decay

> Track: `ml` | Topic: `optimization`

## Concept

Exponential decay reduces LR continuously.

## Math
$$\eta_t = \eta_0 \exp(-k t)$$

- $\eta$ -- learning rate (step size)
- $t$ -- timestep or iteration
- $k$ -- index or number of neighbors

- $\eta_t$ -- learning rate (step size) at step t
- $\eta_0$ -- learning rate (step size) for 0

## Function

```python
def exp_decay(lr: float, k: float, t: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-exponential-decay/python -q
```