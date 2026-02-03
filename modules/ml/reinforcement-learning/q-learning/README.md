# Q-Learning

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Q-learning updates state-action values toward TD targets.

## Math
$$Q \leftarrow Q + \eta\left(r + \gamma \max_{a'} Q(s',a') - Q(s,a)\right)$$

- $\eta$ -- learning rate (step size)
- $\gamma$ -- discount factor
- $Q$ -- action-value function
- $r$ -- reward
- $a$ -- action
- $s$ -- state

## Function

```python
def q_update(q: float, reward: float, next_max: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/q-learning/python -q
```