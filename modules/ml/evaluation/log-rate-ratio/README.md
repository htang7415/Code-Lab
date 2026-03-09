# Log Rate Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Log rate ratio is the logarithm of the ratio between two positive event rates.

## Math

$$
\log \mathrm{RateRatio} = \log\left(\frac{e_1 / n_1}{e_0 / n_0}\right)
$$

- $e_1, n_1$ -- events and total trials for group 1
- $e_0, n_0$ -- events and total trials for the baseline group

## Key Points

- Zero means the two groups have the same event rate.
- Positive values mean the first group has a higher rate.
- This module returns infinities when one positive rate is zero and the other is positive.

## Function

```python
def log_rate_ratio(
    event_count: int,
    total_count: int,
    baseline_event_count: int,
    baseline_total_count: int,
) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-rate-ratio/python -q
```
