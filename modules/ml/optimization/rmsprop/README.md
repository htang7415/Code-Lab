# RMSProp

> Track: `ml` | Topic: `optimization`

## Concept

RMSProp scales learning rates by running average of squared gradients.

## Math

$$
\begin{aligned}
v_t &= \beta v_{t-1} + (1-\beta) g_t^2 \\
w_{t+1} &= w_t - \text{lr} \frac{g_t}{\sqrt{v_t} + \epsilon}
\end{aligned}
$$

## Function

```python
def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/rmsprop/python -q
```
