# Log Detour Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log detour rate is the logarithm of the proportion of detour cases.

## Math

$$
\log \mathrm{DetourRate} = \log\left(\frac{d}{n}\right)
$$

- $d$ -- detour-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a detour rate.
- Larger negative values correspond to rarer detours.
- This module returns negative infinity when the detour rate is zero.

## Function

```python
def log_detour_rate(detour_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-detour-rate/python -q
```
