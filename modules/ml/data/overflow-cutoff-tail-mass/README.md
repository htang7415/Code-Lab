# Overflow Cutoff Tail Mass

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail mass measures how much qualifying overflow severity lives in the upper tail.

## Math

For qualifying overflow values $x_1, \dots, x_n$, define the tail threshold $Q(q)$ and compute:

$$
\mathrm{TailMass}(q) = \frac{\sum_{i: x_i \ge Q(q)} x_i}{\sum_{i=1}^{n} x_i}
$$

## Key Points

- This weights the upper tail by overflow severity, not just case count.
- Larger values mean the severe tail carries most of the overflow burden.
- This module returns `0.0` when nothing exceeds the cutoff.

## Function

```python
def overflow_cutoff_tail_mass(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-mass/python -q
```
