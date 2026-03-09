# Nonterminal Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Nonterminal indicators convert a boolean done flag into a scalar indicator for a continuing transition.

## Math

$$
n = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $n$ -- nonterminal indicator, 1 if the transition continues

## Key Points

- This is numerically the same as a continuing indicator.
- It is useful when RL equations are written in nonterminal-mask form.
- This module returns `1.0` for ongoing transitions and `0.0` for terminal ones.

## Function

```python
def nonterminal_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/nonterminal-indicator/python -q
```
