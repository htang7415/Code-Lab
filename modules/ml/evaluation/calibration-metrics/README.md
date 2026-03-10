# Calibration Metrics

> Track: `ml` | Topic: `evaluation`

## Concept

Calibration asks whether predicted probabilities match observed frequencies.
Some tools summarize calibration error, while others actively recalibrate model
scores into better probabilities.

## Math

- $\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n}\left|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)\right|$
- $\mathrm{Brier} = \frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2$
- $\hat{p}_1 \le \hat{p}_2 \le \cdots \le \hat{p}_n$ for isotonic regression

- $B_m$ -- confidence bin $m$
- $\mathrm{acc}(B_m)$ -- empirical accuracy in bin $m$
- $\mathrm{conf}(B_m)$ -- average confidence in bin $m$
- $p_i$ -- predicted probability of the positive class
- $y_i$ -- observed binary label

## Key Points

- ECE is a summary of mismatch between confidence and accuracy.
- Brier score combines calibration and sharpness into one proper scoring rule.
- Isotonic calibration is a post-hoc monotonic mapping, not just a metric.
- A model can have strong ranking metrics and still be poorly calibrated.

## Function

```python
def expected_calibration_error(
    confidences: list[float],
    predictions: list[int],
    labels: list[int],
    num_bins: int = 10,
) -> float:
def brier_score(labels: list[int], probabilities: list[float]) -> float:
def isotonic_calibration(scores: list[float], labels: list[int]) -> list[float]:
```

## Pitfalls

- ECE depends on binning and can hide local calibration failures.
- Brier score mixes calibration and discrimination, so it should not be read as a pure calibration number.
- Isotonic calibration can overfit when calibration data is small.

## Run tests

```bash
pytest modules/ml/evaluation/calibration-metrics/python -q
```
