# Residual Transition Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Residual transition indicators convert a boolean done flag into a scalar indicator for a transition that remains alive.

## Math

$$
r = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $r$ -- residual transition indicator, 1 if the transition continues

## Key Points

- This is a naming alias for other scalar nonterminal indicators.
- It is useful when code talks about the residual live part of a transition.
- This module returns `1.0` for continuing transitions and `0.0` for terminal ones.

## Function

```python
def residual_transition_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/residual-transition-indicator/python -q
```
