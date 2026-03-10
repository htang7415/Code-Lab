# Overflow Cutoff Upper Tail

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff upper tail measures a high quantile of overflow severity among the cases that exceed a hard cutoff.

## Math

If $x_1, \dots, x_n$ are the qualifying overflow values, report the quantile:

$$
Q(q) = \mathrm{Quantile}_q(x_1, \dots, x_n)
$$

- $q$ -- upper-tail quantile, typically close to `1`

## Key Points

- This focuses on the severe end of the cutoff-qualified overflow cases.
- Larger values mean the worst qualifying overflow cases are much larger.
- This module returns `0.0` when nothing exceeds the cutoff.

## Function

```python
def overflow_cutoff_upper_tail(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.95,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-upper-tail/python -q
```
