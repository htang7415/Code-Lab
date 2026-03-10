# Overflow Cutoff Tail Count

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff tail count counts how many cutoff-qualified overflow cases fall in the upper tail.

## Math

If $x_1, \dots, x_n$ are the cutoff-qualified overflow values and $Q(q)$ is the tail threshold:

$$
\mathrm{TailCount}(q) = \sum_{i=1}^{n} \mathbf{1}[x_i \ge Q(q)]
$$

## Key Points

- This is a case count, not a severity-weighted metric.
- Larger values mean many unacceptable cases sit in the upper tail.
- This module returns `0` when nothing exceeds the cutoff.

## Function

```python
def overflow_cutoff_tail_count(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> int:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-tail-count/python -q
```
