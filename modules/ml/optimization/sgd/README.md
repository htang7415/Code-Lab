# SGD

> Track: `ml` | Topic: `optimization`

## Concept

SGD updates parameters by stepping opposite the gradient.

## Math
$$w_{t+1} = w_t - \eta g_t$$

- $\eta$ -- learning rate (step size)
- $w_t$ -- weight parameter at step t
- $g_t$ -- gradient at step t
- $w$ -- weight parameter
- $t$ -- timestep or iteration
- $g$ -- gradient

## Function

```python
def sgd_step(w: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/sgd/python -q
```