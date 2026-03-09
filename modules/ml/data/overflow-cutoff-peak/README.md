# Overflow Cutoff Peak

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff peak measures the worst overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowCutoffPeak} = \max_i \left(o_i \mathbf{1}[o_i \ge c]\right)
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This focuses on the most severe overflow among unacceptable cases.
- It complements cutoff count and cutoff mean with a worst-case summary.
- This module returns `0` when no example reaches the cutoff.

## Function

```python
def overflow_cutoff_peak(lengths: list[int], max_length: int, cutoff: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-peak/python -q
```
