# Data Quality Checks

> Track: `ml` | Topic: `mlops`

## Concept

Check missing values or out-of-range features.

## Math
$$\mathrm{missing\_rate} = \frac{\text{missing}}{N}$$

- $\mathrm{missing\_rate}$ -- fraction of missing values
- $missing$ -- missing values count
- $N$ -- total number of samples

## Function

```python
def missing_rate(values: list[float | None]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/data-quality-checks/python -q
```
