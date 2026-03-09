# Overflow Threshold Count

> Track: `ml` | Topic: `data`

## Concept

Overflow threshold count measures how many examples exceed a chosen overflow severity threshold.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowThresholdCount} = \sum_{i=1}^{N} \mathbf{1}[o_i > \tau]
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $\tau$ -- overflow severity threshold

## Key Points

- This is the count version of overflow threshold rate.
- It focuses on materially bad truncation instead of any truncation.
- This module returns an integer count.

## Function

```python
def overflow_threshold_count(lengths: list[int], max_length: int, threshold: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-threshold-count/python -q
```
