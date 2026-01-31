# Elastic Net

> Track: `ml` | Topic: `models`

## Concept

Elastic Net combines L1 and L2 penalties.

## Math

L = L0 + λ1||w||1 + λ2||w||2^2

## Function

```python
def elastic_net_penalty(w: list[float], l1: float, l2: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/elastic-net/python -q
```
