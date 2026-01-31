# PPO

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

PPO clips policy updates to avoid large deviations.

## Math

$$L = \min\left(r_t A_t, \operatorname{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t\right)$$

## Function

```python
def clip_ratio(ratio: float, eps: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ppo/python -q
```
