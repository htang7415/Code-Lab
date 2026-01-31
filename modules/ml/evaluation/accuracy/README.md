# Accuracy

> Track: `ml` | Topic: `evaluation`

## Concept

Accuracy is the fraction of correct predictions.

## Math

accuracy = correct / N

## Function

```python
def accuracy(y_true: list[int], y_pred: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/accuracy/python -q
```
