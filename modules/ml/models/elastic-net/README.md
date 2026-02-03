# Elastic Net

> Track: `ml` | Topic: `models`

## Concept

Elastic Net combines L1 (Lasso) and L2 (Ridge) penalties to balance sparsity and stability.

## Math
$$L = L_0 + \lambda_1 \lVert w \rVert_1 + \lambda_2 \lVert w \rVert_2^2$$

- $\lambda$ -- regularization strength or weighting coefficient
- $L_0$ -- initial loss value
- $L$ -- loss value
- $w$ -- weight parameter

- $\lambda_1$ -- regularization strength or weighting coefficient for 1
- $\lambda_2$ -- regularization strength or weighting coefficient for 2

## Function

```python
def elastic_net_penalty(w: list[float], l1: float, l2: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/elastic-net/python -q
```