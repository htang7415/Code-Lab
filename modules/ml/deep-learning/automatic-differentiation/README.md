# Automatic Differentiation

> Track: `ml` | Topic: `deep-learning`

## Concept

Automatic differentiation computes gradients by traversing a computation graph and applying the chain rule.

## Math

For scalar nodes in a graph:

$$\frac{\partial L}{\partial x}=\sum_{\text{paths }x\rightarrow L}\prod \text{local derivatives}$$

- $L$ -- scalar output/loss
- $x$ -- input scalar node
- local derivatives -- per-operation gradients (e.g., add, multiply, ReLU)

This module uses a tiny `Value` scalar wrapper API:
- Python: delegates gradient computation to PyTorch autograd
- Rust: mirrors the same graph idea with explicit reverse traversal

## Function

```python
class Value:
```

## Run tests

```bash
pytest modules/ml/deep-learning/automatic-differentiation/python -q
```
