# Bandits

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Bandits estimate action values from rewards.

## Math

Q <- Q + (1/N)(r - Q)

## Function

```python
def update_value(q: float, n: int, reward: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bandits/python -q
```
