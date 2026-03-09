# Overflow Cutoff Rate

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff rate measures the share of examples whose overflow reaches or exceeds a fixed cutoff.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowCutoffRate} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}[o_i \ge c]
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $c$ -- overflow cutoff

## Key Points

- This measures how often overflow passes a fixed severity line.
- It is the rate version of a cutoff-based count.
- This module returns only the rate, not the count.

## Function

```python
def overflow_cutoff_rate(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-rate/python -q
```
