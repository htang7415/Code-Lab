# Dice Score

> Track: `ml` | Topic: `evaluation`

## Concept

Dice score measures overlap, common in segmentation.

## Math
$$\mathrm{Dice} = \frac{2|A \cap B|}{|A| + |B|}$$

- $A$ -- set of predicted positives
- $B$ -- set of ground-truth positives
- $Dice$ -- Dice coefficient

## Function

```python
def dice(a: set[int], b: set[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/dice-score/python -q
```