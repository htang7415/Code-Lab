# SARSA

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

SARSA uses the next action actually taken for updates.

## Math

Q <- Q + α (r + γ Q' - Q)

## Function

```python
def sarsa_update(q: float, reward: float, next_q: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/sarsa/python -q
```
