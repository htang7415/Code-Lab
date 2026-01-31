# Bilinear Resizing

> Track: `ml` | Topic: `computer-vision`

## Concept

Bilinear interpolation blends four neighbors.

## Math

$$f(x,y) = \sum_{i,j} w_{ij} v_{ij}$$

## Function

```python
def bilinear_sample(v00: float, v01: float, v10: float, v11: float, tx: float, ty: float) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/bilinear-resizing/python -q
```
