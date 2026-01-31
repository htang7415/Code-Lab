# F1 Score

> Track: `ml` | Topic: `evaluation`

## Concept

F1 is the harmonic mean of precision and recall.

## Math

F1 = 2PR/(P+R)

## Function

```python
def f1_score(precision: float, recall: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/f1-score/python -q
```
