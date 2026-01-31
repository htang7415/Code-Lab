# L1 Regularization

> Track: `ml` | Topic: `deep-learning`

## Concept

L1 adds absolute weight penalty to encourage sparsity.

## Math

L = L0 + λ * Σ|w_i|

## Function

```python
def l1_penalty(weights: list[float], lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/l1-regularization/python -q
```
