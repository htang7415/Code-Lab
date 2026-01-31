# Nesterov Accelerated Gradient

> Track: `ml` | Topic: `optimization`

## Concept

Nesterov uses a lookahead gradient for faster convergence.

## Math

$$
\begin{aligned}
v_t &= \mu v_{t-1} + g\left(w_{t-1} - \text{lr}\,\mu v_{t-1}\right) \\
w_{t+1} &= w_t - \text{lr}\, v_t
\end{aligned}
$$

## Function

```python
def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/nesterov/python -q
```
