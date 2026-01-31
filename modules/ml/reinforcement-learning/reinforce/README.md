# REINFORCE

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

REINFORCE updates policy parameters with reward-weighted gradients.

## Math

$$\Delta \theta \propto R \cdot \nabla \log \pi(a|s)$$

## Function

```python
def reinforce_update(grad_logp: float, reward: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/reinforce/python -q
```
