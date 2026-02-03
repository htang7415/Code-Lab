# Feedforward Neural Network

> Track: `ml` | Topic: `deep-learning`

## Concept

A feedforward network applies a sequence of linear layers and activations.

## Math
$$h_i = \sigma(W_i h_{i-1} + b_i)$$

- $\sigma$ -- activation function
- $h_i$ -- i-th hidden representation
- $W_i$ -- i-th weight matrix
- $b_i$ -- i-th bias term
- $h$ -- hidden representation
- $i$ -- index
- $W$ -- weight matrix
- $b$ -- bias term

## Function

```python
def feedforward(x: list[float], weights: list[list[list[float]]], biases: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/feedforward-neural-network/python -q
```