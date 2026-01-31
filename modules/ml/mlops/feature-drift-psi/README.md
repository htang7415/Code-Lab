# Feature Drift Detection (PSI)

> Track: `ml` | Topic: `mlops`

## Concept

PSI compares expected vs actual distributions.

## Math

$$\mathrm{PSI} = \sum_i (a_i - e_i) \ln\left(\frac{a_i}{e_i}\right)$$

## Function

```python
def psi(expected: list[float], actual: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/feature-drift-psi/python -q
```
