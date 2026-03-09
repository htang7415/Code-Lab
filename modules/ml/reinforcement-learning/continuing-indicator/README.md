# Continuing Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Continuing indicators convert a boolean done flag into a scalar indicator for a nonterminal transition.

## Math

$$
c = 1 - d
$$

- $d$ -- done flag, 1 if the transition ends the episode
- $c$ -- continuing indicator, 1 if the transition continues

## Key Points

- This is the scalar complement of a done indicator.
- It is useful when bootstrap terms should remain active only on nonterminal transitions.
- This module returns `1.0` for ongoing transitions and `0.0` for terminal ones.

## Function

```python
def continuing_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/continuing-indicator/python -q
```
