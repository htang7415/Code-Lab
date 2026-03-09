# Log Odds

> Track: `ml` | Topic: `evaluation`

## Concept

Log odds is the logarithm of the odds of a binary positive rate.

## Math

$$
\log \mathrm{Odds} = \log \left( \frac{p}{1 - p} \right)
$$

- $p$ -- positive rate

## Key Points

- A value of `0` means positive and negative classes are equally likely.
- Positive values indicate more positives than negatives.
- This module returns infinities when the positive rate is exactly `0` or `1`.

## Function

```python
def log_odds(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/log-odds/python -q
```
