# Done Fraction

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Done fraction measures what share of transitions are marked as terminal.

## Math

$$
\mathrm{DoneFraction} = \frac{\sum_{i=1}^{N} \mathbf{1}[d_i]}{N}
$$

- $d_i$ -- done flag for transition $i$

## Key Points

- This is a descriptive batch summary of terminal transitions.
- It is numerically the same concept as episode-end rate and terminal share.
- This module returns the fraction of `True` done flags.

## Function

```python
def done_fraction(done_flags: list[bool]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/done-fraction/python -q
```
