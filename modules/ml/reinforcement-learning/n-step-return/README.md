# n-Step Return

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

n-step return accumulates a finite number of discounted rewards and optionally bootstraps from a value after the last included step.

## Math

$$
G^{(n)} = \sum_{t=0}^{n-1} \gamma^t r_{t+1} + \gamma^n V_{boot}
$$

- $r_{t+1}$ -- reward at step $t+1$
- $\gamma$ -- discount factor
- $V_{boot}$ -- bootstrap value after the final included reward

## Key Points

- This is the building block behind many TD methods.
- Longer returns reduce bootstrap bias but can increase variance.
- The module uses the provided reward list length as `n`.

## Function

```python
def n_step_return(rewards: list[float], gamma: float, bootstrap_value: float = 0.0) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/n-step-return/python -q
```
