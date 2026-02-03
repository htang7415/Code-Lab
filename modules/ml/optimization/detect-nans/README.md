# Detecting NaNs

> Track: `ml` | Topic: `optimization`

## Concept

Check for NaNs to catch divergence early.

## Math
$$x 
e x \iff \mathrm{NaN}$$

- $x$ -- input (feature vector or sample)

## Function

```python
def has_nan(values: list[float]) -> bool:
```

## Run tests

```bash
pytest modules/ml/optimization/detect-nans/python -q
```