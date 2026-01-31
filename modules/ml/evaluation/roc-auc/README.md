# ROC-AUC

> Track: `ml` | Topic: `evaluation`

## Concept

ROC-AUC measures ranking quality over thresholds.

## Math

AUC = area under TPR vs FPR curve.

## Function

```python
def auc(fpr: list[float], tpr: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/roc-auc/python -q
```
