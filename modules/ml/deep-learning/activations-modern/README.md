# Modern Activations

> Track: `ml` | Topic: `deep-learning`

## Concept

Modern activations like GeLU, Swish, SwiGLU, and Mish improve expressiveness.

## Math

Swish(x)=x*sigmoid(x), GeLU≈0.5x(1+tanh(sqrt(2/pi)(x+0.0447x^3)))

## Function

```python
def modern_activations(x: float) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-modern/python -q
```
