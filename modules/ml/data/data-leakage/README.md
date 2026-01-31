# Data Leakage

> Track: `ml` | Topic: `data`

## Concept

Leakage happens when train and test data overlap or share future info.

## Math

$$Leakage if |train ∩ test| > 0.$$

## Function

```python
def has_leakage(train_ids: list[int], test_ids: list[int]) -> bool:
```

## Run tests

```bash
pytest modules/ml/data/data-leakage/python -q
```
