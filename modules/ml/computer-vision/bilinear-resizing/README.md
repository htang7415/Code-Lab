# Bilinear Resizing

> Track: `ml` | Topic: `computer-vision`

## Concept

Bilinear interpolation estimates a value inside a grid cell by blending the four
nearest corner values. It applies linear interpolation along one axis, then
along the other.

## Math

$$
f(t_x, t_y) =
(1-t_x)(1-t_y)v_{00}
+ t_x(1-t_y)v_{10}
+ (1-t_x)t_y v_{01}
+ t_x t_y v_{11}
$$

- $v_{00}, v_{10}, v_{01}, v_{11}$ -- values at the four neighboring corners
- $t_x, t_y \in [0, 1]$ -- fractional offsets inside the cell
- $f(t_x, t_y)$ -- interpolated value

## Key Points

- Weights are larger for corners closer to the sample point.
- The four interpolation weights always sum to 1.
- Bilinear resizing is smoother than nearest-neighbor resizing because it
  averages neighboring pixels instead of copying a single one.

## Function

```python
def bilinear_sample(v00: float, v01: float, v10: float, v11: float, tx: float, ty: float) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/bilinear-resizing/python -q
```
