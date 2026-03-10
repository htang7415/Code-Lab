# Overflow Cutoff Skew

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff skew measures asymmetry in overflow severity among the cases that exceed a hard cutoff.

## Math

For qualifying overflow values $x_1, \dots, x_n$ with mean $\mu$ and standard deviation $\sigma$:

$$
\mathrm{Skew} = \frac{1}{n} \sum_{i=1}^{n} \left(\frac{x_i - \mu}{\sigma}\right)^3
$$

## Key Points

- Positive skew means a long right tail of especially bad overflow cases.
- Values near `0` mean the qualifying overflow distribution is roughly symmetric.
- This module returns `0.0` when there are too few qualifying cases or no variation.

## Function

```python
def overflow_cutoff_skew(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-skew/python -q
```
