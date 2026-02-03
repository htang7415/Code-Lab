# Bilinear Resizing

> Track: `ml` | Topic: `computer-vision`

## Concept

Bilinear interpolation blends four neighbors.

## Math

$$f(x,y) = \sum_{i,j} w_{ij} v_{ij}$$

- $w_ij$ -- weight parameter for ij
- $v_ij$ -- vertical flow component for ij
- $x$ -- input (feature vector or sample)
- $y$ -- target/label
- $i$ -- index
- $j$ -- index
- $w$ -- weight parameter
- $v$ -- vertical flow component

## Function

```python
def bilinear_sample(v00: float, v01: float, v10: float, v11: float, tx: float, ty: float) -> float:
```

## Run tests

```bash
pytest modules/ml/computer-vision/bilinear-resizing/python -q
```
