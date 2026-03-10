# Overflow Cutoff Max Gap

> Track: `ml` | Topic: `data`

## Concept

Overflow cutoff max gap measures the gap between the largest and second-largest overflow among examples that reach a fixed cutoff.

## Math

For qualifying overflow amounts $o_{(1)} \ge o_{(2)} \ge \dots$:

$$
\mathrm{OverflowCutoffMaxGap} = o_{(1)} - o_{(2)}
$$

- $o_{(1)}$ -- largest qualifying overflow
- $o_{(2)}$ -- second-largest qualifying overflow

## Key Points

- This focuses on whether one worst-case overflow is isolated from the rest.
- It is useful when teams want a top-tail severity gap.
- This module returns `0.0` when fewer than two cases reach the cutoff.

## Function

```python
def overflow_cutoff_max_gap(lengths: list[int], max_length: int, cutoff: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/overflow-cutoff-max-gap/python -q
```
