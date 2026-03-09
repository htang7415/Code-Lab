# Log Risk Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Log risk ratio is the logarithm of the multiplicative comparison between exposed and baseline positive rates.

## Math

$$
\log \mathrm{RR} = \log\left(\frac{p_{\mathrm{exposed}}}{p_{\mathrm{baseline}}}\right)
$$

- $p_{\mathrm{exposed}}$ -- positive rate of the exposed group
- $p_{\mathrm{baseline}}$ -- positive rate of the baseline group

## Key Points

- A value of `0` means equal risk across the two groups.
- Positive values indicate higher risk in the exposed group.
- This module returns infinities when one rate is zero and the other is positive.

## Function

```python
def log_risk_ratio(exposed_labels: list[int], baseline_labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-risk-ratio/python -q
```
