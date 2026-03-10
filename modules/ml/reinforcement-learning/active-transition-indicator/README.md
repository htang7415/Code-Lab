# Active Transition Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Active transition indicators convert a boolean done flag into a scalar indicator for a transition that remains active.

## Math

$$
a = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $a$ -- active transition indicator, 1 if the transition continues

## Key Points

- This is a naming alias for other scalar nonterminal indicators.
- It is useful when code describes transitions as active or inactive.
- This module returns `1.0` for continuing transitions and `0.0` for terminal ones.

## Function

```python
def active_transition_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/active-transition-indicator/python -q
```
