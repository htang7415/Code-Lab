# Expected Calibration Error

> Track: `ml` | Topic: `evaluation`

## Concept

Expected calibration error (ECE) measures the gap between predicted confidence and observed accuracy across confidence bins.

## Math

$$\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \right|$$

- $M$ -- number of confidence bins
- $B_m$ -- set of samples in bin $m$
- $n$ -- total number of samples
- $\mathrm{acc}(B_m)$ -- empirical accuracy in bin $m$
- $\mathrm{conf}(B_m)$ -- average confidence in bin $m$

## Key Points

- Calibration is different from accuracy and AUC.
- A model can rank examples well but still be overconfident.
- ECE is a compact summary, not a full calibration picture.

## Function

```python
def expected_calibration_error(
    confidences: list[float],
    predictions: list[int],
    labels: list[int],
    num_bins: int = 10,
) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/expected-calibration-error/python -q
```
