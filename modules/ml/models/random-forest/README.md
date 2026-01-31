# Random Forest (Bagging)

> Track: `ml` | Topic: `models`

## Concept

Random forests train many trees on bootstrap samples.

## Math

Bootstrap sample size = N with replacement.

## Function

```python
def bootstrap_indices(n: int, seed: int = 0) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/random-forest/python -q
```
