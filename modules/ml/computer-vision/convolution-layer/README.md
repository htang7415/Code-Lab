# Convolution Layer

> Track: `ml` | Topic: `computer-vision`

## Concept

A convolution layer slides a kernel over the input.

## Math

(I * K)[i,j] = Σ K[u,v] I[i+u, j+v]

## Function

```python
def conv2d(image: list[list[float]], kernel: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/computer-vision/convolution-layer/python -q
```
