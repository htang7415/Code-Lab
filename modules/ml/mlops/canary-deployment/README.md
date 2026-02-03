# Canary Deployment

> Track: `ml` | Topic: `mlops`

## Concept

Canary routes a small fraction of traffic to a new model.

## Math
$$p_{\text{new}} = \frac{n_{\text{new}}}{n_{\text{total}}}$$

- $total$ -- total requests or samples
- $p$ -- probability
- $n$ -- number of samples

## Function

```python
def split_traffic(total: int, canary_pct: float) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/mlops/canary-deployment/python -q
```