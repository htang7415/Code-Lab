# RMSProp

> Track: `ml` | Topic: `optimization`

## Concept

RMSProp scales learning rates by running average of squared gradients.

## Math
$$v_t = \beta v_{t-1} + (1-\beta) g_t^2,\quad w_{t+1} = w_t - \eta\frac{g_t}{\sqrt{v_t}+\epsilon}$$

- $\beta$ -- momentum/decay coefficient
- $\eta$ -- learning rate (step size)
- $\epsilon$ -- small constant for numerical stability
- $v_t$ -- second moment (variance) at step t
- $g_t$ -- gradient at step t
- $w_t$ -- weight parameter at step t
- $v$ -- second moment (variance)
- $t$ -- timestep or iteration
- $g$ -- gradient
- $w$ -- weight parameter

## Function

```python
def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/rmsprop/python -q
```