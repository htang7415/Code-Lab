# Expectation

> Track: `ml` | Topic: `fundamentals`

## Concept

Expectation is the average value of a random variable.

## Math

$$\mathbb{E}[X] = \sum_i x_i p_i$$

- $\mathbb{E}$ -- expectation
- $x_i$ -- i-th input (feature vector or sample)
- $p_i$ -- i-th probability
- $X$ -- data matrix
- $i$ -- index
- $x$ -- input (feature vector or sample)
- $p$ -- probability

## Function

```python
def expectation(values: list[float], probs: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/expectation/python -q
```
