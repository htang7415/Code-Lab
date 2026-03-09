# TD Error

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Temporal-difference error is the Bellman residual that drives many value-learning updates.

## Math

$$
\delta = r + \gamma V(s') - V(s)
$$

- $r$ -- immediate reward
- $\gamma$ -- discount factor
- $V(s')$ -- next-state value estimate
- $V(s)$ -- current-state value estimate

## Key Points

- TD error is the core signal behind TD learning, SARSA-style updates, and actor-critic advantages.
- Positive TD error means the outcome was better than expected.
- This module isolates the residual itself, not the parameter update.

## Function

```python
def td_error(reward: float, gamma: float, next_value: float, value: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/td-error/python -q
```
