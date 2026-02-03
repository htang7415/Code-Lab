# F1 Score

> Track: `ml` | Topic: `evaluation`

## Concept

F1 is the harmonic mean of precision and recall.

## Math
$$\mathrm{F1} = \frac{2\,\mathrm{Precision}\,\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}$$

- $\mathrm{F1}$ -- F1 score
- $Precision$ -- precision
- $Recall$ -- recall

## Function

```python
def f1_score(precision: float, recall: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/f1-score/python -q
```