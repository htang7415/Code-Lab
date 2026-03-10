# Log Defect Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Log defect rate is the logarithm of the proportion of defect cases.

## Math

$$
\log \mathrm{DefectRate} = \log\left(\frac{d}{n}\right)
$$

- $d$ -- defect count
- $n$ -- total count

## Key Points

- This is a log-scaled version of a defect rate.
- Larger negative values correspond to rarer defects.
- This module returns negative infinity when the defect rate is zero.

## Function

```python
def log_defect_rate(defect_count: int, total_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-defect-rate/python -q
```
