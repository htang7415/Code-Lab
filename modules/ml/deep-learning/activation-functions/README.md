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
- SwiGLU gate:
  $$
  \mathrm{SwiGLU}(v, g)=v \cdot \mathrm{SiLU}(g)=v \cdot g \cdot \sigma(g)
  $$

## From Math To Code

- Hidden-layer activations usually map one scalar to another scalar.
- Softmax maps a whole vector of logits to a probability distribution.
- Gated activations such as SwiGLU need both a value path and a gate path, so they should not be faked as a one-input scalar activation.

## Minimal Code Mental Model

```python
hidden = scalar_activations(x)["gelu"]
probs = softmax(logits)
gated = swiglu(value_stream, gate_stream)
```

## Function

```python
def sigmoid(x: float) -> float:
def relu(x: float) -> float:
def leaky_relu(x: float, alpha: float = 0.01) -> float:
def gelu(x: float) -> float:
def swish(x: float) -> float:
def softplus(x: float) -> float:
def softsign(x: float) -> float:
def swiglu(value: float, gate: float) -> float:
def dynamic_tanh(x: float, alpha: float = 1.0, gamma: float = 1.0, beta: float = 0.0) -> float:
def scalar_activations(x: float, alpha: float = 0.01) -> dict[str, float]:
def softmax(row: list[float]) -> list[float]:
```

## When To Use What

- Use ReLU-family activations as the default baseline for many feedforward and CNN-style models.
- Use GeLU or Swish-style activations when you want smoother transformer-style behavior.
- Use sigmoid or tanh mainly for historical intuition, bounded outputs, or gate construction.
- Use softmax only when you need a probability distribution over logits.
- Use SwiGLU-style gating only when the block really has separate value and gate streams.

## Run tests

```bash
pytest modules/ml/deep-learning/activation-functions/python -q
```
