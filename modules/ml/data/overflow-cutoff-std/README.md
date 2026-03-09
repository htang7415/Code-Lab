# Overflow Cutoff Std

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff std measures the standard deviation of overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$ over cases with $o_i \ge c$:

$$
\mathrm{OverflowCutoffStd} = \sqrt{\frac{1}{M} \sum_{i=1}^{M} (o_i - \bar{o})^2}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff
- $\bar{o}$ -- mean overflow among the qualifying cases

## Key Points

- This measures variability among unacceptable overflow cases only.
- It complements cutoff mean and cutoff peak with a spread summary.
- This module returns `0.0` when fewer than two cases reach the cutoff.

## Function

```python
def overflow_cutoff_std(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-std/python -q
```
