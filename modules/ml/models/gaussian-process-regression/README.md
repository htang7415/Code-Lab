# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Concept

GPR predicts using a kernel to measure similarity.

## Math

$$k(x,x') = \exp\left(-\frac{\lVert x-x' \rVert^2}{2\ell^2}\right)$$

## Function

```python
def rbf_kernel(x: list[float], y: list[float], length_scale: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-process-regression/python -q
```
