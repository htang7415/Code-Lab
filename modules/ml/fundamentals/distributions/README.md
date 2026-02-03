# Distributions

> Track: `ml` | Topic: `fundamentals`

## Concept

A probability distribution assigns probabilities to outcomes.

## Math

$$\sum_i p_i = 1$$

- $p_i$ -- i-th probability
- $i$ -- index
- $p$ -- probability

## Function

```python
def normalize_probs(values: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/distributions/python -q
```
