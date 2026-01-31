# SGD with Momentum

> Track: `ml` | Topic: `optimization`

## Concept

Momentum accumulates velocity to smooth updates.

## Math

$$
\begin{aligned}
v_t &= \mu v_{t-1} + g_t \\
w_{t+1} &= w_t - \text{lr}\, v_t
\end{aligned}
$$

## Function

```python
def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/sgd-momentum/python -q
```
