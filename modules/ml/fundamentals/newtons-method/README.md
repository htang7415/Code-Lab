# Newton's Method

> Track: `ml` | Topic: `fundamentals`

## Concept

Newton's method updates the current estimate using local slope and curvature.

## Math
$$x_{t+1} = x_t - \frac{f'(x_t)}{f''(x_t)}$$

- $x_t$ -- current iterate at step $t$
- $x_{t+1}$ -- next iterate after the Newton update
- $f'(x_t)$ -- first derivative (local slope) at $x_t$
- $f''(x_t)$ -- second derivative (local curvature) at $x_t$
- $t$ -- timestep or iteration

## Function

```python
def newton_step(x: float, f_prime: float, f_double_prime: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/newtons-method/python -q
```
