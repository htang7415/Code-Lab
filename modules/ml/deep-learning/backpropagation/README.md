# Backpropagation

> Track: `ml` | Topic: `deep-learning`

## Concept

Backprop computes gradients using the chain rule from output to inputs.

## Math
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot x$$

- $w$ -- weight parameter
- $z$ -- pre-activation value
- $x$ -- input (feature vector or sample)

## Function

```python
def linear_backprop(x: float, w: float, grad_out: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/backpropagation/python -q
```