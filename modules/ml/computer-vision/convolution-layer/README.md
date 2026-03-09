# Convolution Layer

> Track: `ml` | Topic: `computer-vision`

## Concept

A convolution layer slides a small learned kernel across an image or feature map
and computes a weighted sum at each spatial position. The same kernel weights
are reused everywhere, which is why convolutions are translation-aware and
parameter-efficient.

## Math
$$(I \ast K)_{i,j} = \sum_{u,v} K_{u,v} I_{i+u, j+v}$$

- $I$ -- input image or feature map
- $K$ -- convolution kernel
- $(i, j)$ -- output location
- $(u, v)$ -- offsets inside the kernel window
- $(I \ast K)_{i,j}$ -- convolution response at location $(i, j)$

## Key Points

- Each output value depends only on a local receptive field.
- Weight sharing lets one kernel detect the same pattern in many locations.
- Stacking convolution layers increases the effective receptive field.

## Function

```python
def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/convolution-layer/python -q
```
