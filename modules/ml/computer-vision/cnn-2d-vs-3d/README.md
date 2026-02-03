# 2D vs 3D CNN

> Track: `ml` | Topic: `computer-vision`

## Concept

3D CNNs convolve over time/depth in addition to height/width.

## Math
$$d_{\text{out}} = d_{\text{in}} - k_d + 1$$

- $k_d$ -- index or number of neighbors for d
- $d$ -- dimension
- $k$ -- index or number of neighbors

## Function

```python
def output_depth(input_depth: int, kernel_depth: int) -> int:
```

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-2d-vs-3d/python -q
```