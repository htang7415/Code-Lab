# Overflow Cutoff Tail Skew

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail skew measures asymmetry in the upper tail of cutoff-qualified overflow.

## Math

For tail overflow values $x_1, \dots, x_m$ with mean $\mu$ and standard deviation $\sigma$:

$$
\mathrm{Skew} = \frac{1}{m} \sum_{i=1}^{m} \left(\frac{x_i - \mu}{\sigma}\right)^3
$$

## Key Points

- Positive skew means a long right tail of especially severe overflow cases.
- Values near `0` mean the upper tail is roughly symmetric.
- This module returns `0.0` when the tail is too small or has no variation.

## Function

```python
def overflow_cutoff_tail_skew(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-skew/python -q
```
