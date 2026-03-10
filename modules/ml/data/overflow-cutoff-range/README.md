# Overflow Cutoff Range

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff range measures the max-minus-min overflow among examples that reach a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$ over cases with $o_i \ge c$:

$$
\mathrm{OverflowCutoffRange} = \max_i o_i - \min_i o_i
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This is a simple spread summary for unacceptable overflow cases.
- It complements cutoff median and cutoff IQR with a full min-to-max span.
- This module returns `0.0` when fewer than two cases reach the cutoff.

## Function

```python
def overflow_cutoff_range(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-range/python -q
```
