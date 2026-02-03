# Bandits

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Bandits estimate action values from rewards.

## Math
$$Q_{t+1} = Q_t + \frac{1}{N_t}(r_t - Q_t)$$

- $Q_t$ -- action-value function at step t
- $r_t$ -- reward at step t
- $Q$ -- action-value function
- $t$ -- timestep or iteration
- $r$ -- reward

- $N_t$ -- number of samples at step t
- $N$ -- number of samples

## Function

```python
def update_value(q: float, n: int, reward: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/bandits/python -q
```