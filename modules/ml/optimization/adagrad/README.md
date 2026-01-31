# Adagrad

> Track: `ml` | Topic: `optimization`

## Concept

Adagrad accumulates squared gradients for per-parameter learning rates.

## Math

$$
\begin{aligned}
G_t &= G_{t-1} + g_t^2 \\
w_{t+1} &= w_t - \text{lr} \frac{g_t}{\sqrt{G_t} + \epsilon}
\end{aligned}
$$

## Function

```python
def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adagrad/python -q
```
