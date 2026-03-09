# n-Step TD Target

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

n-step TD prediction mixes a finite run of sampled rewards with a bootstrapped value estimate at the horizon.

## Math

$$G_t^{(n)} = \sum_{k=0}^{n-1} \gamma^k R_{t+k} + \gamma^n V(S_{t+n})$$

- $R_{t+k}$ -- reward observed $k$ steps after timestep $t$
- $V(S_{t+n})$ -- bootstrap value after $n$ steps
- $\gamma$ -- discount factor
- $n$ -- number of sampled reward steps

## Key Points

- n-step TD sits between one-step TD and Monte Carlo returns.
- Larger $n$ uses more actual rewards before bootstrapping.
- This module computes the target value, not the final parameter update.

## Function

```python
def n_step_td_target(
    rewards: list[float],
    bootstrap_value: float,
    gamma: float,
) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/n-step-td-prediction/python -q
```
