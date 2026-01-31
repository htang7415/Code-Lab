# Hinge Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Hinge loss encourages a margin between correct and incorrect classes.

## Math

L = max(0, 1 - y * score)

## Function

```python
def hinge_loss(score: float, label: int) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/hinge-loss/python -q
```
