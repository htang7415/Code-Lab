# Overflow Cutoff Tail Mean

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail mean measures the average overflow severity inside the upper tail of cutoff-qualified cases.

## Math

If $x_1, \dots, x_m$ are the tail overflow values after applying a cutoff and tail quantile:

$$
\mathrm{TailMean} = \frac{1}{m} \sum_{i=1}^{m} x_i
$$

## Key Points

- This summarizes the typical severity inside the unacceptable tail.
- Larger values mean the upper tail is not just frequent but also severe.
- This module returns `0.0` when no tail exists.

## Function

```python
def overflow_cutoff_tail_mean(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-mean/python -q
```
