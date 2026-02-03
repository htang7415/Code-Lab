# Confusion Matrix

> Track: `ml` | Topic: `evaluation`

## Concept

Confusion matrix counts TP, FP, FN, TN.

## Math
$$\begin{bmatrix}\mathrm{TN} & \mathrm{FP} \\ \mathrm{FN} & \mathrm{TP}\end{bmatrix}$$

- $\mathrm{TN}$ -- true negatives
- $\mathrm{FP}$ -- false positives
- $\mathrm{FN}$ -- false negatives
- $\mathrm{TP}$ -- true positives

## Function

```python
def confusion_matrix(y_true: list[int], y_pred: list[int]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/evaluation/confusion-matrix/python -q
```