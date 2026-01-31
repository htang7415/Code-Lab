# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Concept

GPR predicts using a kernel to measure similarity.

## Math

k(x,x') = exp(-||x-x'||^2 / (2ℓ^2))

## Function

```python
def rbf_kernel(x: list[float], y: list[float], length_scale: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-process-regression/python -q
```
