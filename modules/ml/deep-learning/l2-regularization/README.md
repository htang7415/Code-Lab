# L2 Regularization

> Track: `ml` | Topic: `deep-learning`

## Concept

L2 adds a squared weight penalty to discourage large weights. This is also known as **Ridge** regularization.

## Math

$$L = L_0 + \lambda \sum_i w_i^2$$

## Function

```python
def l2_penalty(weights: list[float], lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/l2-regularization/python -q
```
