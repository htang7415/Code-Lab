# KL Divergence

> Track: `ml` | Topic: `fundamentals`

## Concept

KL divergence measures how one distribution diverges from another.

## Math

KL(p||q) = Σ p log(p/q)

## Function

```python
def kl(p: list[float], q: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/kl-divergence/python -q
```
