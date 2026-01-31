# Focal Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Focal loss down-weights easy examples for imbalanced classification.

## Math

$$L = -(1-p)^{\gamma} \log(p)$$

## Function

```python
def focal_loss(p: float, gamma: float = 2.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/focal-loss/python -q
```
