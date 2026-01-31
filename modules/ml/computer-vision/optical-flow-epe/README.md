# Optical Flow (EPE)

> Track: `ml` | Topic: `computer-vision`

## Concept

Endpoint error measures flow prediction error.

## Math

EPE = sqrt((u-u*)^2 + (v-v*)^2)

## Function

```python
def epe(pred: tuple[float, float], target: tuple[float, float]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/optical-flow-epe/python -q
```
