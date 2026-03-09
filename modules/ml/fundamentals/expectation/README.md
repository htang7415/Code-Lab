# Expectation

> Track: `ml` | Topic: `fundamentals`

## Concept

Expectation is the probability-weighted average of a random variable. It tells
you the long-run average value you would see if you repeatedly sampled from the
same distribution.

## Math

$$\mathbb{E}[X] = \sum_i x_i p_i$$

- $\mathbb{E}$ -- expectation
- $X$ -- discrete random variable
- $x_i$ -- i-th possible value of the random variable
- $p_i$ -- i-th probability
- $i$ -- index

## Key Points

- Expectation averages values using probabilities, not uniform weights.
- Large values matter only if they also have meaningful probability mass.
- Many ML objectives are expectations over data or noise distributions.

## Function

```python
def expectation(values: list[float], probs: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/expectation/python -q
```
