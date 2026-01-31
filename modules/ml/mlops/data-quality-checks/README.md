# Data Quality Checks

> Track: `ml` | Topic: `mlops`

## Concept

Check missing values or out-of-range features.

## Math

missing_rate = missing / N

## Function

```python
def missing_rate(values: list[float | None]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/data-quality-checks/python -q
```
