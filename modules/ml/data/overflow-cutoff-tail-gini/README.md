# Overflow Cutoff Tail Gini

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail Gini measures how concentrated severity is inside the upper tail of cutoff-qualified overflow.

## Math

Let $x_1, \dots, x_m$ be the overflow values at or above the cutoff-tail threshold. The Gini coefficient is:

$$
\mathrm{Gini} = \frac{\sum_{i=1}^{m}\sum_{j=1}^{m}|x_i - x_j|}{2m \sum_{i=1}^{m} x_i}
$$

## Key Points

- Values near `0` mean the tail severity is evenly spread.
- Larger values mean a few tail cases dominate the severity burden.
- This module returns `0.0` when there is no qualifying tail.

## Function

```python
def overflow_cutoff_tail_gini(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-gini/python -q
```
