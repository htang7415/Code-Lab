# DPO vs PPO

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Compare preference optimization to policy optimization.

## Math

$$\text{DPO uses preference logits; PPO uses clipped policy ratios.}$$

## Function

```python
def compare_methods() -> list[str]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/dpo-vs-ppo/python -q
```
