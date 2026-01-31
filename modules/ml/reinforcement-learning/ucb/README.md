# UCB

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Upper Confidence Bound balances mean reward and uncertainty.

## Math

UCB = Q + c * sqrt(ln t / N)

## Function

```python
def ucb_score(q: float, t: int, n: int, c: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/ucb/python -q
```
