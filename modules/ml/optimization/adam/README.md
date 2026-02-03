# Adam

> Track: `ml` | Topic: `optimization`

## Concept

Adam combines momentum and adaptive learning rates.

## Math
$$m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t,\quad v_t=\beta_2 v_{t-1}+(1-\beta_2)g_t^2$$

$$w_{t+1}=w_t-\eta\frac{m_t}{\sqrt{v_t}+\epsilon}$$

- $\beta$ -- momentum/decay coefficient
- $m_t$ -- first moment (momentum) at step t
- $g_t$ -- gradient at step t
- $v_t$ -- second moment (variance) at step t
- $m$ -- first moment (momentum)
- $t$ -- timestep or iteration
- $g$ -- gradient
- $v$ -- second moment (variance)
- $\eta$ -- learning rate (step size)
- $\epsilon$ -- small constant for numerical stability
- $w_t$ -- weight parameter at step t
- $w$ -- weight parameter

- $\beta_1$ -- momentum/decay coefficient for 1
- $\beta_2$ -- momentum/decay coefficient for 2

## Function

```python
def adam_step(w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adam/python -q
```