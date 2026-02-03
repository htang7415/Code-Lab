# Gradient Descent

> Track: `ml` | Topic: `fundamentals`

## Concept

Gradient descent updates parameters along negative gradient.

## Math
$$x_{t+1} = x_t - \eta\,\nabla f(x_t)$$

- $\eta$ -- learning rate (step size)
- $x_t$ -- input (feature vector or sample) at step t
- $x$ -- input (feature vector or sample)
- $t$ -- timestep or iteration

## Function

```python
def gd_step(x: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/gradient-descent/python -q
```