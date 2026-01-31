# A/B Testing

> Track: `ml` | Topic: `mlops`

## Concept

A/B testing compares conversion rates between variants.

## Math

$$rate = conversions / trials$$

## Function

```python
def conversion_rate(conversions: int, trials: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/ab-testing/python -q
```
