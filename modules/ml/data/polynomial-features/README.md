# Polynomial Feature Expansion

> Track: `ml` | Topic: `data`

## Concept

Polynomial features add powers of input to increase model capacity.

## Math

$$phi(x) = [x, x^2, ..., x^d]$$

## Function

```python
def poly_features(x: float, degree: int) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/data/polynomial-features/python -q
```
