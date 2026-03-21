# Convex vs Non-Convex

> Track: `ml` | Topic: `fundamentals`

## Concept

A convex function bends upward, so any local minimum is also a global minimum.
For a 1D quadratic, convexity is determined entirely by the leading coefficient.

## Math

$$f(x)=ax^2+bx+c \text{ is convex if } a \ge 0$$

- $a$ -- quadratic coefficient
- $b$ -- linear coefficient
- $c$ -- constant term
- $x$ -- input scalar

## Function

```python
def is_convex_quadratic(a: float) -> bool:
```

## Run tests

```bash
pytest modules/ml/fundamentals/convex-vs-nonconvex/python -q
```
