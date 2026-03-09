# Log Relative Risk

> Track: `ml` | Topic: `evaluation`

## Concept

Log relative risk is the logarithm of the relative risk between an exposed group and a baseline group.

## Math

$$
\log \mathrm{RR} = \log\left(\frac{p_{\mathrm{exposed}}}{p_{\mathrm{baseline}}}\right)
$$

- $p_{\mathrm{exposed}}$ -- positive rate of the exposed group
- $p_{\mathrm{baseline}}$ -- positive rate of the baseline group

## Key Points

- This is another naming convention for log risk ratio.
- Zero means equal risk across the two groups.
- This module returns infinities when one rate is zero and the other is positive.

## Function

```python
def log_relative_risk(exposed_labels: list[int], baseline_labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-relative-risk/python -q
```
