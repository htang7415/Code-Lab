# Newton's Method

> Track: `ml` | Topic: `fundamentals`

## Concept

Newton's method uses second derivatives for faster convergence.

## Math
$$x_{t+1} = x_t - \frac{f'(x_t)}{f''(x_t)}$$

- $x_t$ -- input (feature vector or sample) at step t
- $x$ -- input (feature vector or sample)
- $t$ -- timestep or iteration

## Function

```python
def newton_step(x: float, f_prime: float, f_double_prime: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/newtons-method/python -q
```