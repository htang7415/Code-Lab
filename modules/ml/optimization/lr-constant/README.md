# Constant Learning Rate

> Track: `ml` | Topic: `optimization`

## Concept

Constant LR keeps the step size fixed.

## Math
$$\eta_t = \eta_0$$

- $\eta$ -- learning rate (step size)
- $t$ -- timestep or iteration

- $\eta_t$ -- learning rate (step size) at step t
- $\eta_0$ -- learning rate (step size) for 0

## Function

```python
def constant_lr(lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-constant/python -q
```