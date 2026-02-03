# Activation Failure Modes

> Track: `ml` | Topic: `deep-learning`

## Concept

Dead ReLU and saturation reduce gradient flow.

## Math

$$|\sigma'(x)| \approx 0 \quad \text{for large } |x|$$

- $\sigma$ -- activation function
- $x$ -- input (feature vector or sample)

## Function

```python
def dead_relu_fraction(values: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activation-failure-modes/python -q
```
