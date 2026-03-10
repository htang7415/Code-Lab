# Surviving Transition Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Surviving transition indicators convert a boolean done flag into a scalar indicator for a transition that survives to the next state.

## Math

$$
s = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $s$ -- surviving transition indicator, 1 if the transition continues

## Key Points

- This is a naming alias for other scalar nonterminal indicators.
- It is useful when code describes whether a transition survives.
- This module returns `1.0` for continuing transitions and `0.0` for terminal ones.

## Function

```python
def surviving_transition_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/surviving-transition-indicator/python -q
```
