# Overflow Cutoff Top Share

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff top share measures how much of the cutoff-qualified overflow mass is contributed by the single largest case.

## Math

If the qualifying overflow values are $x_1, \dots, x_n$:

$$
\mathrm{TopShare} = \frac{\max_i x_i}{\sum_{i=1}^{n} x_i}
$$

## Key Points

- Values near `1` mean one case dominates the unacceptable overflow burden.
- Smaller values mean the burden is spread across many qualifying cases.
- This module returns `0.0` when nothing exceeds the cutoff.

## Function

```python
def overflow_cutoff_top_share(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-top-share/python -q
```
