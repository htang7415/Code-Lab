# Mean Imputation

> Track: `ml` | Topic: `data`

## Concept

Imputation fills missing values so a model can train on incomplete data.
Mean imputation is simple and common for numeric features, though it can shrink variance and hide missingness patterns.

## Math

$$\hat{x}_j = \frac{1}{N_j} \sum_{i : x_{ij} \neq \varnothing} x_{ij}$$

- $\hat{x}_j$ -- imputed mean for feature column $j$
- $N_j$ -- number of observed entries in column $j$
- $x_{ij}$ -- value for row $i$, column $j$
- $\varnothing$ -- missing value

## Key Points

- Impute using training data statistics, not full-dataset statistics after the split.
- Mean imputation is fast but underestimates uncertainty.
- Entirely missing columns need a fallback rule.

## Function

```python
def mean_impute(table: list[list[float | None]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/data/imputation/python -q
```
