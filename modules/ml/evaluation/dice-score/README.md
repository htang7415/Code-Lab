# Dice Score

> Track: `ml` | Topic: `evaluation`

## Concept

Dice score measures overlap, common in segmentation.

## Math

2|A∩B|/(|A|+|B|)

## Function

```python
def dice(a: set[int], b: set[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/dice-score/python -q
```
