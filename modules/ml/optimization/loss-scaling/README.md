# Loss Scaling

> Track: `ml` | Topic: `optimization`

## Concept

Loss scaling multiplies loss to avoid underflow in mixed precision.

## Math

$$scaled_grad = grad * scale$$

## Function

```python
def scale_grad(grad: float, scale: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/loss-scaling/python -q
```
