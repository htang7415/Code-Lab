# Jaccard Index

> Track: `ml` | Topic: `evaluation`

## Concept

Jaccard measures overlap between sets.

## Math

$$\text{|A∩B| / |A∪B|}$$

## Function

```python
def jaccard(a: set[int], b: set[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/jaccard-index/python -q
```
