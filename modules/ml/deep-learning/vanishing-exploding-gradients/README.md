# Vanishing and Exploding Gradients

> Track: `ml` | Topic: `deep-learning`

## Concept

Repeated multiplication by small or large values shrinks or blows up gradients.

## Math

$$g_L = g_0 * Π w_i$$

## Function

```python
def gradient_chain(weights: list[float], grad: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/vanishing-exploding-gradients/python -q
```
