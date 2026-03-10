# Activation Functions

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to understand what a nonlinearity does to signal flow, gradient
flow, and model expressiveness.

## First Principles

- Without a nonlinearity, stacked linear layers collapse into one linear map.
- The activation decides whether the network saturates, stays sparse, or keeps
  smooth gradients.
- In modern practice, ReLU-family and GeLU-style activations matter most.
- Softmax is different from the others: it is mainly an output normalization,
  not a hidden-layer scalar activation.

## Core Math

- Sigmoid:
  $$
  \sigma(x)=\frac{1}{1+e^{-x}}
  $$
- ReLU:
  $$
  \mathrm{ReLU}(x)=\max(0,x)
  $$
- Leaky ReLU:
  $$
  \mathrm{LeakyReLU}(x)=\max(\alpha x, x)
  $$
- GeLU:
  $$
  \mathrm{GeLU}(x)\approx 0.5x\left(1+\tanh\left(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right)\right)
  $$

## Minimal Code Mental Model

```python
hidden = scalar_activations(x)["relu"]
probs = softmax(logits)
```

## Function

```python
def scalar_activations(x: float, alpha: float = 0.01) -> dict[str, float]:
def softmax(row: list[float]) -> list[float]:
```

## When To Use What

- Use ReLU-family activations as the default baseline for many feedforward and CNN-style models.
- Use GeLU or Swish-style activations when you want smoother transformer-style behavior.
- Use sigmoid or tanh mainly for historical intuition, bounded outputs, or gated mechanisms.
- Use softmax only when you need a probability distribution over logits.

## Run tests

```bash
pytest modules/ml/deep-learning/activation-functions/python -q
```
