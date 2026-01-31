# Sobel Edge Detection

> Track: `ml` | Topic: `computer-vision`

## Concept

Sobel filters estimate image gradients.

## Math

Gx = Kx * I, Gy = Ky * I

## Function

```python
def sobel_center(patch: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/sobel-edge-detection/python -q
```
