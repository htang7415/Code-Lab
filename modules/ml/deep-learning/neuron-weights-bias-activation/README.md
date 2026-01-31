# Neuron, Weights, Bias, Activation

> Track: `ml` | Topic: `deep-learning`

## Concept

A neuron computes a weighted sum plus bias, then applies an activation.

## Math

$$y = sigma(w · x + b)$$

## Function

```python
def neuron(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/neuron-weights-bias-activation/python -q
```
