# SGD with Momentum

> Track: `ml` | Topic: `optimization`

## Concept

Momentum accumulates velocity to smooth updates.

## Math
$$v_t = \mu v_{t-1} + g_t,\quad w_{t+1} = w_t - \eta v_t$$

- $\mu$ -- mean
- $\eta$ -- learning rate (step size)
- $v_t$ -- second moment (variance) at step t
- $g_t$ -- gradient at step t
- $w_t$ -- weight parameter at step t
- $v$ -- second moment (variance)
- $t$ -- timestep or iteration
- $g$ -- gradient
- $w$ -- weight parameter

## Function

```python
def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/sgd-momentum/python -q
```