# Overflow Cutoff Median

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff median measures the median overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$ over cases with $o_i \ge c$:

$$
\mathrm{OverflowCutoffMedian} = \mathrm{median}(o_1, \dots, o_M)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This is a robust severity summary for unacceptable overflow cases.
- It complements cutoff mean and cutoff std when outliers are a concern.
- This module returns `0.0` when no example reaches the cutoff.

## Function

```python
def overflow_cutoff_median(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-median/python -q
```
