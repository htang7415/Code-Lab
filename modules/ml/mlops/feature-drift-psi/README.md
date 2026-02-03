# Feature Drift Detection (PSI)

> Track: `ml` | Topic: `mlops`

## Concept

PSI compares expected vs actual distributions.

## Math
$$\mathrm{PSI} = \sum_i (a_i - e_i) \ln\left(\frac{a_i}{e_i}\right)$$

- $\mathrm{PSI}$ -- population stability index
- $a_i$ -- actual proportion in bin $i$
- $e_i$ -- expected proportion in bin $i$

## Function

```python
def psi(expected: list[float], actual: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/feature-drift-psi/python -q
```