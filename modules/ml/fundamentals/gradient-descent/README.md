# Gradient Descent

> Track: `ml` | Topic: `fundamentals`

## Concept

Gradient descent improves a parameter by moving it in the direction that most
rapidly decreases the objective. The gradient points uphill, so subtracting it
moves downhill.

## Math
$$x_{t+1} = x_t - \eta\,\nabla f(x_t)$$

- $\eta$ -- learning rate (step size)
- $x_t$ -- current parameter value at iteration $t$
- $\nabla f(x_t)$ -- gradient of the objective at $x_t$
- $x_{t+1}$ -- updated parameter
- $t$ -- timestep or iteration

## Key Points

- The gradient gives local slope information.
- The learning rate controls how far each step moves.
- If $\eta$ is too small, learning is slow; if too large, updates can overshoot.

## Function

```python
def gd_step(x: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/gradient-descent/python -q
```
