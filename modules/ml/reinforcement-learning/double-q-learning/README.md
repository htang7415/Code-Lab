# Double Q-Learning Target

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Double Q-learning reduces overestimation by selecting the next action with one value table and evaluating it with another.

## Math

$$
\mathrm{target} = r + \gamma Q_B(s', \arg\max_a Q_A(s', a))
$$

- $r$ -- immediate reward
- $\gamma$ -- discount factor
- $Q_A$ -- action-selection value table
- $Q_B$ -- action-evaluation value table

## Key Points

- Standard Q-learning uses the same estimate for selection and evaluation.
- Double Q-learning decouples those roles to reduce optimistic bias.
- This module computes only the bootstrapped target, not the full table update.

## Function

```python
def double_q_target(reward: float, gamma: float, selector_values: list[float], evaluator_values: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/double-q-learning/python -q
```
