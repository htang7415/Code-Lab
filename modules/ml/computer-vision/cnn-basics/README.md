# CNNs

> Track: `ml` | Topic: `computer-vision`

## Concept

CNNs use learned convolutional filters to detect local patterns such as edges,
corners, and textures. By stacking layers, they build increasingly abstract
features from raw pixels.

## Math
$$\text{feature\_map} = x \ast k$$

- $x$ -- input signal or image
- $k$ -- convolution kernel
- $x \ast k$ -- filtered feature map

## Key Points

- Early kernels usually capture simple local patterns.
- Deeper layers combine local features into larger structures.
- Convolution gives CNNs spatial bias and parameter sharing.

## Function

```python
def conv1d(signal: list[float], kernel: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-basics/python -q
```
