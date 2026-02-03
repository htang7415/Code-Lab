# REINFORCE

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

REINFORCE updates policy parameters with reward-weighted gradients.

## Math
$$
\nabla_\theta J = \mathbb{E}\left[R \nabla_\theta \log \pi_\theta(a \mid s)\right]$$

- $\mathbb{E}$ -- expectation
- $\theta$ -- model parameters
- $\pi$ -- policy
- $J$ -- objective
- $a$ -- action
- $s$ -- state

- $\pi_\theta$ -- policy parameterized by \theta

## Function

```python
def reinforce_update(grad_logp: float, reward: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/reinforce/python -q
```