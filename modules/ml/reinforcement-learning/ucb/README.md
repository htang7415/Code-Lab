# UCB

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Upper Confidence Bound balances mean reward and uncertainty.

## Math
$$\mathrm{UCB}_t = Q_t + c\sqrt{\frac{\ln t}{N_t}}$$

- $Q_t$ -- action-value function at step t
- $t$ -- timestep or iteration
- $Q$ -- action-value function

- $N_t$ -- number of samples at step t
- $N$ -- number of samples

## Function

```python
def ucb_score(q: float, t: int, n: int, c: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ucb/python -q
```