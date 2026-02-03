# Step Decay

> Track: `ml` | Topic: `optimization`

## Concept

Step decay drops LR by a factor every k steps.

## Math
$$\eta_t = \eta_0 \gamma^{\lfloor t/s \rfloor}$$

- $\eta_t$ -- learning rate at step $t$
- $\eta_0$ -- initial learning rate
- $\gamma$ -- decay factor
- $t$ -- timestep
- $s$ -- step interval for decay

## Function

```python
def step_decay(lr: float, step: int, gamma: float, t: int) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/lr-step-decay/python -q
```