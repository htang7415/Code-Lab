# Adagrad

> Track: `ml` | Topic: `optimization`

## Concept

Adagrad accumulates squared gradients for per-parameter learning rates.

## Math
$$G_t = G_{t-1} + g_t^2,\quad w_{t+1} = w_t - \eta\frac{g_t}{\sqrt{G_t}+\epsilon}$$

- $\eta$ -- learning rate (step size)
- $\epsilon$ -- small constant for numerical stability
- $g_t$ -- gradient at step t
- $w_t$ -- weight parameter at step t
- $t$ -- timestep or iteration
- $g$ -- gradient
- $w$ -- weight parameter

## Function

```python
def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adagrad/python -q
```