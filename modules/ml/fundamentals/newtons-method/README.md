# Newton's Method

> Track: `ml` | Topic: `fundamentals`

## Concept

Newton's method uses second derivatives for faster convergence.

## Math

x = x - f'(x)/f''(x)

## Function

```python
def newton_step(x: float, f_prime: float, f_double_prime: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/newtons-method/python -q
```
