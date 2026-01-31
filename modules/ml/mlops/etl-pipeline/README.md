# ETL Pipeline

> Track: `ml` | Topic: `mlops`

## Concept

ETL extracts raw data, transforms it, and loads it for training or serving.

## Math

$$x' = \frac{x - \mu}{\sigma}$$

## Function

```python
def normalize(values: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/etl-pipeline/python -q
```
