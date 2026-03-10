# Overflow Cutoff Tail Range

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail range measures the full spread inside the upper tail of cutoff-qualified overflow.

## Math

If $x_1, \dots, x_m$ are the tail overflow values:

$$
\mathrm{TailRange} = \max_i x_i - \min_i x_i
$$

## Key Points

- Larger values mean upper-tail severity spans a wide interval.
- A single-value tail has range `0`.
- This module returns `0.0` when there is no tail.

## Function

```python
def overflow_cutoff_tail_range(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-range/python -q
```
