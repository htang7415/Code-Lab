# Jaccard Index

> Track: `ml` | Topic: `evaluation`

## Concept

Jaccard measures overlap between sets.

## Math
$$\mathrm{Jaccard} = \frac{|A \cap B|}{|A \cup B|}$$

- $A$ -- set of predicted positives
- $B$ -- set of ground-truth positives

## Function

```python
def jaccard(a: set[int], b: set[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/jaccard-index/python -q
```