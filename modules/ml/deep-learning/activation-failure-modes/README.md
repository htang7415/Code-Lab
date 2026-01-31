# Activation Failure Modes

> Track: `ml` | Topic: `deep-learning`

## Concept

Dead ReLU and saturation reduce gradient flow.

## Math

Saturation: |σ'(x)| ≈ 0 for large |x|.

## Function

```python
def dead_relu_fraction(values: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activation-failure-modes/python -q
```
