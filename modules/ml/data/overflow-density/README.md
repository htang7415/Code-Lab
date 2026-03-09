# Overflow Density

> Track: `ml` | Topic: `data`

## Concept

Overflow density normalizes total overflow by both batch size and the hard cap.

## Math

$$
\mathrm{OverflowDensity} = \frac{\sum_{i=1}^{N} \max(0, l_i - L)}{N L}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- This metric lets overflow severity be compared across batches with the same cap.
- It complements overflow count and mean overflow.
- This module requires a positive cap because the normalization divides by it.

## Function

```python
def overflow_density(lengths: list[int], max_length: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-density/python -q
```
