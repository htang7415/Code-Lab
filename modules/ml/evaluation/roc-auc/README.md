# ROC-AUC

> Track: `ml` | Topic: `evaluation`

## Concept

ROC-AUC measures ranking quality over thresholds.

## Math

$$\mathrm{AUC} = \int_{0}^{1} \mathrm{TPR}(\mathrm{FPR}) \, d(\mathrm{FPR})$$

- $\mathrm{AUC}$ -- area under the ROC curve
- $\mathrm{TPR}$ -- true positive rate
- $\mathrm{FPR}$ -- false positive rate
- $d$ -- dimension

## Function

```python
def auc(fpr: list[float], tpr: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/roc-auc/python -q
```
