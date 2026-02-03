# ETL Pipeline

> Track: `ml` | Topic: `mlops`

## Concept

ETL extracts raw data, transforms it, and loads it for training or serving.

## Math
$$x' = \frac{x-\mu}{\sigma}$$

- $\mu$ -- mean
- $\sigma$ -- standard deviation
- $x$ -- input (feature vector or sample)

## Function

```python
def normalize(values: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/etl-pipeline/python -q
```