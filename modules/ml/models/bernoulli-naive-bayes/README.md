# Bernoulli Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Bernoulli NB models binary features per class.

## Math

$$p(x|y)=∏ p_i^{x_i} (1-p_i)^{1-x_i}$$

## Function

```python
def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/bernoulli-naive-bayes/python -q
```
