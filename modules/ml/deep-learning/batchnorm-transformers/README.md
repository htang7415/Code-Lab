# Why BatchNorm is Bad for Transformers

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm mixes statistics across batch/time, which conflicts with sequence modeling.

## Math

Batch stats depend on other tokens: mean = avg over batch/time.

## Function

```python
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm-transformers/python -q
```
