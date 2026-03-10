# Network Building Blocks

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to learn the smallest useful deep-learning building blocks in
one place: a single neuron and a simple feedforward network.

## First Principles

- A neuron computes an affine score and then applies a nonlinearity.
- A feedforward network is just many such steps stacked layer by layer.
- Depth comes from repeated composition, not from changing the basic rule.

## Core Math

Single neuron:

$$
z = w^\top x + b,\qquad y = \sigma(z)
$$

Feedforward stack:

$$
h_i = \sigma(W_i h_{i-1} + b_i)
$$

## Minimal Code Mental Model

```python
score = neuron(x, w, b)
hidden = feedforward(x, weights, biases)
```

## Functions

```python
def neuron(x: list[float], w: list[float], b: float) -> float:
def feedforward(x: list[float], weights: list[list[list[float]]], biases: list[list[float]]) -> list[float]:
```

## When To Use What

- Use `neuron` when you want the smallest possible nonlinear unit.
- Use `feedforward` when you want the mental model for stacking linear layers and activations.
- Move to `activation-functions` and `normalization-methods` when the question is not structure but training behavior.

## Run tests

```bash
pytest modules/ml/deep-learning/network-building-blocks/python -q
```
