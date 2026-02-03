# SARSA

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

SARSA uses the next action actually taken for updates.

## Math
$$Q \leftarrow Q + \eta\left(r + \gamma Q(s',a') - Q(s,a)\right)$$

- $\eta$ -- learning rate (step size)
- $\gamma$ -- discount factor
- $Q$ -- action-value function
- $r$ -- reward
- $s$ -- state
- $a$ -- action

## Function

```python
def sarsa_update(q: float, reward: float, next_q: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/sarsa/python -q
```