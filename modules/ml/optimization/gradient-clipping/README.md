# Gradient Clipping

> Track: `ml` | Topic: `optimization`

## Concept

Clip gradient norm to avoid exploding gradients.

## Math

$$g \leftarrow g \cdot \min\left(1, \frac{\text{clip}}{\lVert g \rVert}\right)$$

- $g$ -- gradient

## Function

```python
def clip_norm(grad: list[float], clip: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/optimization/gradient-clipping/python -q
```
