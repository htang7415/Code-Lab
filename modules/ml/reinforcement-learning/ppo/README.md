# PPO

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

PPO clips policy updates to avoid large deviations.

## Math
$$L^{\text{CLIP}} = \min\left(r_t A_t, \mathrm{clip}(r_t, 1-\epsilon, 1+\epsilon)A_t\right)$$

- $L^{\text{CLIP}}$ -- PPO clipped objective
- $r_t$ -- policy probability ratio at step $t$
- $A_t$ -- advantage estimate at step $t$
- $\epsilon$ -- PPO clip range

- $L$ -- loss value
- $r$ -- reward
- $t$ -- timestep or iteration
- $A$ -- advantage estimate

## Function

```python
def clip_ratio(ratio: float, eps: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ppo/python -q
```
