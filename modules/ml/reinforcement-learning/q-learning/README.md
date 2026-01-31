# Q-Learning

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Q-learning updates state-action values toward TD targets.

## Math

$$Q \leftarrow Q + \alpha\left(r + \gamma \max_{a'} Q' - Q\right)$$

## Function

```python
def q_update(q: float, reward: float, next_max: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/q-learning/python -q
```
