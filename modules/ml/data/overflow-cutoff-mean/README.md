# Overflow Cutoff Mean

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff mean measures the average overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowCutoffMean} =
\frac{\sum_i o_i \mathbf{1}[o_i \ge c]}{\sum_i \mathbf{1}[o_i \ge c]}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This focuses on the severe-overflow subset only.
- It is useful when teams care about average severity after a hard threshold is crossed.
- This module returns `0.0` when no examples reach the cutoff.

## Function

```python
def overflow_cutoff_mean(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-mean/python -q
```
