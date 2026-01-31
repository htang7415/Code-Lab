# Feature Drift Detection (PSI)

> Track: `ml` | Topic: `mlops`

## Concept

PSI compares expected vs actual distributions.

## Math

PSI = Σ (a-e) * ln(a/e)

## Function

```python
def psi(expected: list[float], actual: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/feature-drift-psi/python -q
```
