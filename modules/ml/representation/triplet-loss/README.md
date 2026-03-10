# Triplet Loss

> Track: `ml` | Topic: `representation`

## Concept

Triplet loss trains an anchor to stay closer to a positive example than to a
negative example by at least a chosen margin.

## Math

$$L = \max(0, d(a, p) - d(a, n) + m)$$

- $d(a, p)$ -- distance from anchor to positive
- $d(a, n)$ -- distance from anchor to negative
- $m$ -- margin

## Function

```python
def triplet_loss(anchor_positive_distance: float, anchor_negative_distance: float, margin: float = 0.2) -> float:
```

## Run tests

```bash
pytest modules/ml/representation/triplet-loss/python -q
```
