# Vanishing and Exploding Gradients

> Track: `ml` | Topic: `deep-learning`

## Concept

Repeated multiplication by small or large values shrinks or blows up gradients.

## Math
$$g_L = g_0 \prod_i w_i$$

- $g_L$ -- gradient for L
- $g_0$ -- initial gradient
- $w_i$ -- i-th weight parameter
- $g$ -- gradient
- $L$ -- loss value
- $i$ -- index
- $w$ -- weight parameter

## Function

```python
def gradient_chain(weights: list[float], grad: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/vanishing-exploding-gradients/python -q
```