# BatchNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm normalizes activations across the batch.

## Math

y = (x-mean)/sqrt(var+eps)

## Function

```python
def batchnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm/python -q
```
