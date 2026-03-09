# Sobel Edge Detection

> Track: `ml` | Topic: `computer-vision`

## Concept

Sobel filters estimate local image gradients by convolving an image patch with
horizontal and vertical edge kernels. Large responses indicate strong intensity
changes, which usually correspond to edges.

## Math

$$G_x = K_x \ast I,\qquad G_y = K_y \ast I,\qquad |G| = \sqrt{G_x^2 + G_y^2}$$

- $I$ -- local image patch
- $K_x$ -- horizontal Sobel kernel
- $K_y$ -- vertical Sobel kernel
- $G_x$ -- horizontal gradient response
- $G_y$ -- vertical gradient response
- $|G|$ -- gradient magnitude

## Function

```python
def sobel_center(patch: list[list[float]]) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/sobel-edge-detection/python -q
```
