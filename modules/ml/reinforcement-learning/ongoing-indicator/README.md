# Ongoing Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Ongoing indicators convert a boolean done flag into a scalar indicator for a continuing transition.

## Math

$$
o = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $o$ -- ongoing indicator, 1 if the transition continues

## Key Points

- This is a naming alias for nonterminal or continuing indicators.
- It is useful when equations are written around ongoing transitions.
- This module returns `1.0` for ongoing transitions and `0.0` for terminal ones.

## Function

```python
def ongoing_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ongoing-indicator/python -q
```
