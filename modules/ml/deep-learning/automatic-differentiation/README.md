# Automatic Differentiation

> Track: `ml` | Topic: `deep-learning`

## Concept

Autodiff computes derivatives by composing local gradients.

## Math

If $y = x^2$ and $z = y + 3$, then by the chain rule:

$$\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx} = 1 \cdot 2x = 2x$$

- $y$ -- target/label
- $x$ -- input (feature vector or sample)
- $z$ -- pre-activation value

## Function

```python
def forward_grad(x: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/automatic-differentiation/python -q
```
