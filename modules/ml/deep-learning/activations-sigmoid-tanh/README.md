# Sigmoid/Tanh and Hard Variants

> Track: `ml` | Topic: `deep-learning`

## Concept

Sigmoid and tanh are smooth activations; hard variants approximate them for efficiency.
Dynamic Tanh (DyT) adds learnable scale/bias parameters to tanh.

## Math

- sigmoid(x)=1/(1+e^-x)
- tanh(x)=(e^x-e^-x)/(e^x+e^-x)
- hard_sigmoid(x)=clip(0.2x+0.5, 0, 1)
- hardtanh(x)=clip(x, -1, 1)
- dyt(x)=gamma * tanh(alpha * x) + beta

## Function

```python
def activations(x: float) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-sigmoid-tanh/python -q
```
