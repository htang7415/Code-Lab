# L1 Regularization

> Track: `ml` | Topic: `deep-learning`

## Concept

L1 adds an absolute weight penalty to encourage sparsity. This is also known as Lasso regularization.

## Math

$$L = L_0 + \lambda \sum_i |w_i|$$

- $\lambda$ -- regularization strength or weighting coefficient
- $L_0$ -- initial loss value
- $w_i$ -- i-th weight parameter
- $L$ -- loss value
- $i$ -- index
- $w$ -- weight parameter

## Function

```python
def l1_penalty(weights: list[float], lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/l1-regularization/python -q
```
