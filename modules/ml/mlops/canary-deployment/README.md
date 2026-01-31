# Canary Deployment

> Track: `ml` | Topic: `mlops`

## Concept

Canary routes a small fraction of traffic to a new model.

## Math

new_pct = new / total

## Function

```python
def split_traffic(total: int, canary_pct: float) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/mlops/canary-deployment/python -q
```
