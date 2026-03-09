# Neuron, Weights, Bias, Activation

> Track: `ml` | Topic: `deep-learning`

## Concept

A neuron first computes an affine score from its inputs, then applies a
non-linearity. This is the smallest building block of a feedforward network.

## Math

$$z = w^\top x + b,\qquad y = \sigma(z)$$

- $\sigma$ -- activation function
- $w$ -- weight vector
- $x$ -- input feature vector
- $b$ -- bias term
- $z$ -- pre-activation score
- $y$ -- activated output

## Key Points

- The weights decide how strongly each input contributes.
- The bias shifts the activation threshold.
- The activation adds non-linearity so stacked neurons can model complex
  functions.

## Function

```python
def neuron(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/neuron-weights-bias-activation/python -q
```
