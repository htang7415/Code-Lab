# Markov Chains

> Track: `ml` | Topic: `fundamentals`

## Concept

Markov chains evolve distributions via transition matrices.

## Math

$$p_{t+1} = p_t T$$

- $p_t$ -- probability at step t
- $p$ -- probability
- $t$ -- timestep or iteration

- $T$ -- number of steps

## Function

```python
def next_distribution(p: list[float], t: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/markov-chains/python -q
```
