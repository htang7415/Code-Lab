# Convex vs Non-Convex

> Track: `ml` | Topic: `fundamentals`

## Concept

Convex functions have a single global minimum.

## Math

$$f(x)=ax^2+bx+c \text{ is convex if } a \ge 0$$

## Function

```python
def is_convex_quadratic(a: float) -> bool:
```

## Run tests

```bash
pytest modules/ml/fundamentals/convex-vs-nonconvex/python -q
```
