# Overflow Threshold Rate

> Track: `ml` | Topic: `data`

## Concept

Overflow threshold rate measures how often overflow exceeds a specified severity threshold.

## Math

For overflow amounts $o_i = \max(0, l_i - L)$:

$$
\mathrm{OverflowThresholdRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[o_i > \tau]}{N}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length
- $\tau$ -- overflow severity threshold

## Key Points

- This metric focuses on materially bad truncation rather than any truncation.
- It complements overflow presence rate and overflow peak.
- This module returns both the count above threshold and the rate.

## Function

```python
def overflow_threshold_rate(lengths: list[int], max_length: int, threshold: int) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/data/overflow-threshold-rate/python -q
```
