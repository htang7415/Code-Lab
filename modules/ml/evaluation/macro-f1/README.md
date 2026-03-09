# Macro F1

> Track: `ml` | Topic: `evaluation`

## Concept

Macro F1 averages per-class F1 scores so each class contributes equally regardless of frequency.

## Math

$$
\mathrm{MacroF1} = \frac{1}{C} \sum_{c=1}^{C} \mathrm{F1}_c
$$

- $C$ -- number of classes
- $\mathrm{F1}_c$ -- F1 score for class $c$

## Key Points

- Macro F1 is useful when class balance matters.
- Rare classes count as much as common ones.
- This module computes macro F1 from per-class confusion counts.

## Function

```python
def macro_f1_score(
    true_positives: list[int],
    false_positives: list[int],
    false_negatives: list[int],
) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/macro-f1/python -q
```
