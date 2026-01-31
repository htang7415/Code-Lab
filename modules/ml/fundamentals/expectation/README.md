# Expectation

> Track: `ml` | Topic: `fundamentals`

## Concept

Expectation is the average value of a random variable.

## Math

$$\mathbb{E}[X] = \sum_i x_i p_i$$

## Function

```python
def expectation(values: list[float], probs: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/expectation/python -q
```
