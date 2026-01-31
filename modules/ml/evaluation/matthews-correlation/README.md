# Matthews Correlation Coefficient

> Track: `ml` | Topic: `evaluation`

## Concept

MCC balances all confusion matrix terms.

## Math

$$\mathrm{MCC} = \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$

## Function

```python
def mcc(tp: int, tn: int, fp: int, fn: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/matthews-correlation/python -q
```
