# Logistic Regression

> Track: `ml` | Topic: `models`

## Concept

Logistic regression models class probability with a sigmoid.

## Math
$$p = \sigma(w^\top x + b),\quad \sigma(z)=\frac{1}{1+e^{-z}}$$

- $\sigma$ -- sigmoid function
- $p$ -- probability
- $w$ -- weight parameter
- $x$ -- input (feature vector or sample)
- $b$ -- bias term
- $z$ -- latent or pre-activation value

## Function

```python
def predict_proba(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/logistic-regression/python -q
```