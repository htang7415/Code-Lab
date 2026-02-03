# Nesterov Accelerated Gradient

> Track: `ml` | Topic: `optimization`

## Concept

Nesterov uses a lookahead gradient for faster convergence.

## Math
$$v_t = \mu v_{t-1} + g(w_{t-1} - \eta\mu v_{t-1}),\quad w_{t+1}=w_t-\eta v_t$$

- $\mu$ -- mean
- $\eta$ -- learning rate (step size)
- $v_t$ -- second moment (variance) at step t
- $w_t$ -- weight parameter at step t
- $v$ -- second moment (variance)
- $t$ -- timestep or iteration
- $g$ -- gradient
- $w$ -- weight parameter

## Function

```python
def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/nesterov/python -q
```