# Detecting NaNs

> Track: `ml` | Topic: `optimization`

## Concept

Check for NaNs to catch divergence early.

## Math

$$is_nan(x) = true if x != x$$

## Function

```python
def has_nan(values: list[float]) -> bool:
```

## Run tests

```bash
pytest modules/ml/optimization/detect-nans/python -q
```
