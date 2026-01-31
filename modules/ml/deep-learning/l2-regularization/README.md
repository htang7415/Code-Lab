# L2 Regularization

> Track: `ml` | Topic: `deep-learning`

## Concept

L2 adds squared weight penalty to discourage large weights.

## Math

L = L0 + λ * Σ w_i^2

## Function

```python
def l2_penalty(weights: list[float], lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/l2-regularization/python -q
```
