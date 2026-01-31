# Adam

> Track: `ml` | Topic: `optimization`

## Concept

Adam combines momentum and adaptive learning rates.

## Math

$$
\begin{aligned}
m_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t \\
v_t &= \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \\
w_{t+1} &= w_t - \text{lr} \frac{m_t}{\sqrt{v_t} + \epsilon}
\end{aligned}
$$

## Function

```python
def adam_step(w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adam/python -q
```
