# Overflow Cutoff Count

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff count measures how many examples reach or exceed a fixed overflow cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowCutoffCount} = \sum_{i=1}^{N} \mathbf{1}[o_i \ge c]
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This is the count version of overflow cutoff rate.
- It reports how many examples cross a hard severity line.
- This module returns an integer count.

## Function

```python
def overflow_cutoff_count(lengths: list[int], max_length: int, cutoff: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-count/python -q
```
