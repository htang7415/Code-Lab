# SARSA

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

SARSA uses the next action actually taken for updates.

## Math

$$Q \leftarrow Q + \alpha\left(r + \gamma Q' - Q\right)$$

## Function

```python
def sarsa_update(q: float, reward: float, next_q: float, alpha: float, gamma: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/sarsa/python -q
```
