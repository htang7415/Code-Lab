# SVM (Pegasos)

> Track: `ml` | Topic: `models`

## Concept

Pegasos is a stochastic subgradient method for SVMs.

## Math

w = (1 - lr*λ)w + lr*y*x if y(w·x) < 1

## Function

```python
def pegasos_step(w: list[float], x: list[float], y: int, lr: float, lam: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/svm-pegasos/python -q
```
