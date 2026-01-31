# R2 Score

> Track: `ml` | Topic: `evaluation`

## Concept

R2 measures explained variance relative to a mean baseline.

## Math

$$R2 = 1 - SS_res/SS_tot$$

## Function

```python
def r2_score(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/r2-score/python -q
```
