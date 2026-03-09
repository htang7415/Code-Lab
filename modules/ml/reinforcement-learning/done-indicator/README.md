# Done Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Done indicators convert a boolean done flag into a scalar numeric indicator.

## Math

$$
i = d
$$

- $d$ -- done flag, 1 if the transition ends the episode

## Key Points

- This is a scalar helper for code following the `done` naming convention.
- It is numerically the same idea as a terminal indicator.
- This module returns `1.0` for done and `0.0` otherwise.

## Function

```python
def done_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/done-indicator/python -q
```
