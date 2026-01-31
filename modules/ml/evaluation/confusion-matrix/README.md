# Confusion Matrix

> Track: `ml` | Topic: `evaluation`

## Concept

Confusion matrix counts TP, FP, FN, TN.

## Math

[[TN, FP],[FN, TP]]

## Function

```python
def confusion_matrix(y_true: list[int], y_pred: list[int]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/evaluation/confusion-matrix/python -q
```
