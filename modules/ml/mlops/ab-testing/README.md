# A/B Testing

> Track: `ml` | Topic: `mlops`

## Concept

A/B testing compares conversion rates between variants.

## Math
$$\mathrm{rate} = \frac{\text{conversions}}{\text{trials}}$$

- $rate$ -- conversion rate
- $conversions$ -- number of conversions
- $trials$ -- number of trials

## Function

```python
def conversion_rate(conversions: int, trials: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/ab-testing/python -q
```