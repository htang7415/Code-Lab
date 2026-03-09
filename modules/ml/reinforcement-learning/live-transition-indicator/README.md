# Live Transition Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Live transition indicators convert a boolean done flag into a scalar indicator for a transition that continues.

## Math

$$
\ell = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $\ell$ -- live transition indicator, 1 if the transition continues

## Key Points

- This is a naming alias for other nonterminal scalar indicators.
- It is useful when code talks about whether a transition remains live.
- This module returns `1.0` for ongoing transitions and `0.0` for terminal ones.

## Function

```python
def live_transition_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/live-transition-indicator/python -q
```
