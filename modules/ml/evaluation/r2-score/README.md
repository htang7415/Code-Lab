# R2 Score

> Track: `ml` | Topic: `evaluation`

## Concept

R2 measures explained variance relative to a mean baseline.

## Math
$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$$

- $R^2$ -- coefficient of determination

## Function

```python
def r2_score(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/r2-score/python -q
```