# Jensen–Shannon Divergence

> Track: `ml` | Topic: `fundamentals`

## Concept

JS divergence symmetrizes KL using the mean distribution.

## Math

JS(p,q) = 0.5 KL(p||m)+0.5 KL(q||m)

## Function

```python
def js(p: list[float], q: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/jensen-shannon-divergence/python -q
```
