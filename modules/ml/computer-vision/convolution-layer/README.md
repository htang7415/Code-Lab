# Convolution Layer

> Track: `ml` | Topic: `computer-vision`

## Concept

A convolution layer slides a kernel over the input.

## Math
$$(I \ast K)_{i,j} = \sum_{u,v} K_{u,v} I_{i+u, j+v}$$

- $K_u$ -- key matrix or kernel for u
- $I_i$ -- i-th image (pixel grid)
- $I$ -- image (pixel grid)
- $K$ -- key matrix or kernel
- $i$ -- index
- $j$ -- index
- $u$ -- horizontal flow component
- $v$ -- vertical flow component

## Function

```python
def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/convolution-layer/python -q
```