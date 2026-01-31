# Huber Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Huber loss is quadratic near zero and linear for large errors.

## Math

L = 0.5 e^2 if |e|<=δ else δ(|e|-0.5δ)

## Function

```python
def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/huber-loss/python -q
```
