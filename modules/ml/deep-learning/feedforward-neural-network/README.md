# Feedforward Neural Network

> Track: `ml` | Topic: `deep-learning`

## Concept

A feedforward network applies a sequence of linear layers and activations.

## Math

For layer i: h_i = sigma(W_i h_{i-1} + b_i).

## Function

```python
def feedforward(x: list[float], weights: list[list[list[float]]], biases: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/feedforward-neural-network/python -q
```
