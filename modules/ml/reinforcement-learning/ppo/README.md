# PPO

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

PPO clips policy updates to avoid large deviations.

## Math

L = min(r_t A_t, clip(r_t, 1-ε, 1+ε) A_t)

## Function

```python
def clip_ratio(ratio: float, eps: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ppo/python -q
```
