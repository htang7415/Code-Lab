# First-Visit Monte Carlo Prediction

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

First-visit Monte Carlo prediction estimates state values from complete episodes.
For each state, only the return following its first occurrence in the episode is used.

## Math

$$V(s) \leftarrow G_t \quad \text{for the first } t \text{ such that } S_t = s$$

$$G_t = \sum_{k=0}^{T-t-1} \gamma^k R_{t+k}$$

- $S_t$ -- state at timestep $t$
- $R_t$ -- reward observed at timestep $t$
- $G_t$ -- return from timestep $t$
- $\gamma$ -- discount factor

## Key Points

- Monte Carlo prediction waits until the episode ends before computing returns.
- First-visit and every-visit Monte Carlo differ only in which occurrences are used.
- This module computes single-episode first-visit returns.

## Function

```python
def first_visit_returns(
    states: list[str],
    rewards: list[float],
    gamma: float,
) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/first-visit-monte-carlo-prediction/python -q
```
