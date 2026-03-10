# Overflow Cutoff Tail Variance

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail variance measures how much severity varies inside the upper tail of cutoff-qualified cases.

## Math

If $x_1, \dots, x_m$ are the tail overflow values:

$$
\mathrm{Var} = \frac{1}{m} \sum_{i=1}^{m} (x_i - \bar{x})^2
$$

## Key Points

- This is a population variance over the tail overflow values.
- Larger values mean upper-tail severity is spread out rather than tightly clustered.
- This module returns `0.0` when the tail has fewer than two cases.

## Function

```python
def overflow_cutoff_tail_variance(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-variance/python -q
```
