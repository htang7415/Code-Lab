# Diffusion Models

> Track: `ml` | Topic: `generative`

## Concept

Diffusion adds noise forward and denoises backward.

## Math

x_t = sqrt(alpha) x_{t-1} + sqrt(1-alpha) ε

## Function

```python
def add_noise(x: float, noise: float, alpha: float) -> float:
```

## Run tests

```bash
pytest modules/ml/generative/diffusion-models/python -q
```
