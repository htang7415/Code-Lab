# 2D vs 3D CNN

> Track: `ml` | Topic: `computer-vision`

## Concept

3D CNNs convolve over time/depth in addition to height/width.

## Math

$$output_depth = input_depth - kernel_depth + 1$$

## Function

```python
def output_depth(input_depth: int, kernel_depth: int) -> int:
```

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-2d-vs-3d/python -q
```
