# Q-Learning

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Q-learning updates state-action values toward TD targets.

## Math

Q <- Q + α (r + γ max Q' - Q)

## Function

```python
def q_update(q: float, reward: float, next_max: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/q-learning/python -q
```
