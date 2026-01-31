# Gradient Accumulation

> Track: `ml` | Topic: `systems`

## Concept

Accumulate gradients across steps to simulate larger batches.

## Math

$$g_{\text{total}} = \sum_i g_i$$

## Function

```python
def accumulate(grads: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/systems/gradient-accumulation/python -q
```
