# Loss Scaling

> Track: `ml` | Topic: `optimization`

## Concept

Loss scaling multiplies loss to avoid underflow in mixed precision.

## Math
$$g_{\text{scaled}} = s\,g$$

- $g_{\text{scaled}}$ -- scaled gradient
- $g$ -- original gradient
- $s$ -- loss scale factor

## Function

```python
def scale_grad(grad: float, scale: float) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/loss-scaling/python -q
```