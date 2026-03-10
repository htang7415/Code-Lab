# Persistent Transition Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Persistent transition indicators convert a boolean done flag into a scalar indicator for a transition that persists.

## Math

$$
p = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $p$ -- persistent transition indicator, 1 if the transition continues

## Key Points

- This is a naming alias for other scalar nonterminal indicators.
- It is useful when code describes a transition as persisting across steps.
- This module returns `1.0` for continuing transitions and `0.0` for terminal ones.

## Function

```python
def persistent_transition_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/persistent-transition-indicator/python -q
```
