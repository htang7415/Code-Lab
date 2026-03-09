# SMOTE Interpolation

> Track: `ml` | Topic: `data`

## Concept

SMOTE generates synthetic minority samples by interpolating between a minority example and one of its neighbors.
This module focuses on the interpolation step itself.

## Math

$$x_{\mathrm{new}} = x_i + \lambda (x_j - x_i)$$

- $x_i$ -- base minority example
- $x_j$ -- neighbor minority example
- $\lambda$ -- interpolation gap between 0 and 1
- $x_{\mathrm{new}}$ -- synthetic sample

## Key Points

- SMOTE adds new minority samples rather than only reweighting loss terms.
- The synthetic point stays on the line segment between two minority examples.
- Bad neighbors can create unrealistic samples, so neighbor choice matters.

## Function

```python
def smote_samples(
    minority_points: list[list[float]],
    neighbor_pairs: list[tuple[int, int]],
    gaps: list[float],
) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/data/smote/python -q
```
