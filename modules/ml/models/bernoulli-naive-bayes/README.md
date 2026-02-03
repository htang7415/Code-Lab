# Bernoulli Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Bernoulli NB models binary features per class.

## Math
$$p(x\mid y)=\prod_i p_i^{x_i}(1-p_i)^{1-x_i}$$

- $p_i$ -- i-th probability
- $x_i$ -- i-th input (feature vector or sample)
- $p$ -- probability
- $x$ -- input (feature vector or sample)
- $y$ -- target/label
- $i$ -- index

## Function

```python
def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/bernoulli-naive-bayes/python -q
```