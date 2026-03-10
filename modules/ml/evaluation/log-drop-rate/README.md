# Log Drop Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log drop rate is the logarithm of the proportion of dropped cases.

## Math

$$
\log \mathrm{DropRate} = \log\left(\frac{d}{n}\right)
$$

- $d$ -- dropped-case count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a drop rate.
- Larger negative values correspond to rarer drops.
- This module returns negative infinity when the drop rate is zero.

## Function

```python
def log_drop_rate(drop_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-drop-rate/python -q
```
