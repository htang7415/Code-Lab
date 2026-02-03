# Softmax Regression

> Track: `ml` | Topic: `models`

## Concept

Softmax regression generalizes logistic regression to multiple classes.

## Math
$$p_i = \frac{\exp(z_i)}{\sum_j \exp(z_j)}$$

- $p_i$ -- i-th probability
- $z_i$ -- i-th latent or pre-activation value
- $z_j$ -- j-th latent or pre-activation value
- $p$ -- probability
- $i$ -- index
- $j$ -- index
- $z$ -- latent or pre-activation value

## Function

```python
def softmax(logits: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/softmax-regression/python -q
```