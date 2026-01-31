# Precision and Recall

> Track: `ml` | Topic: `evaluation`

## Concept

Precision measures correctness of positive predictions; recall measures coverage.

## Math

$$precision=TP/(TP+FP), recall=TP/(TP+FN)$$

## Function

```python
def precision_recall(y_true: list[int], y_pred: list[int]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/precision-recall/python -q
```
