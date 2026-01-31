# RGB to Grayscale

> Track: `ml` | Topic: `computer-vision`

## Concept

Convert RGB to grayscale using luminance weights.

## Math

Y = 0.299R + 0.587G + 0.114B

## Function

```python
def rgb_to_gray(r: int, g: int, b: int) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/rgb-to-grayscale/python -q
```
