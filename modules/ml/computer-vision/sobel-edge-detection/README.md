# Sobel Edge Detection

> Track: `ml` | Topic: `computer-vision`

## Concept

Sobel filters estimate image gradients.

## Math
$$G_x = K_x \ast I,\quad G_y = K_y \ast I$$

- $K_x$ -- key matrix or kernel for x
- $K_y$ -- key matrix or kernel for y
- $x$ -- input (feature vector or sample)
- $K$ -- key matrix or kernel
- $I$ -- image (pixel grid)
- $y$ -- target/label

## Function

```python
def sobel_center(patch: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/sobel-edge-detection/python -q
```