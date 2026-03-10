# Log Deferral Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log deferral rate is the logarithm of the proportion of deferred cases.

## Math

$$
\log \mathrm{DeferralRate} = \log\left(\frac{d}{n}\right)
$$

- $d$ -- deferred-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a deferral rate.
- Larger negative values correspond to rarer deferrals.
- This module returns negative infinity when the deferral rate is zero.

## Function

```python
def log_deferral_rate(deferral_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-deferral-rate/python -q
```
