# Overflow Cutoff IQR

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff IQR measures the interquartile range of overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$ over cases with $o_i \ge c$:

$$
\mathrm{OverflowCutoffIQR} = Q_{0.75}(o) - Q_{0.25}(o)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This is a robust spread summary for unacceptable overflow cases.
- It complements cutoff median when teams need variability without tail sensitivity.
- This module returns `0.0` when fewer than two cases reach the cutoff.

## Function

```python
def overflow_cutoff_iqr(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-iqr/python -q
```
