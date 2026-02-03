# Sigmoid/Tanh and Hard Variants

> Track: `ml` | Topic: `deep-learning`

## Concept

Sigmoid and tanh are smooth activations; hard variants approximate them for efficiency.
Dynamic Tanh (DyT) adds learnable scale/bias parameters to tanh.

## Math

- $\sigma(x)=\frac{1}{1+e^{-x}}$
- $\tanh(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$
- $\mathrm{hard\_sigmoid}(x)=\operatorname{clip}(0.2x+0.5, 0, 1)$
- $\mathrm{hardtanh}(x)=\operatorname{clip}(x, -1, 1)$
- $\mathrm{dyt}(x)=\gamma\,\tanh(\alpha x)+\beta$

- $\sigma$ -- sigmoid function
- $\tanh$ -- hyperbolic tangent function
- $\gamma$ -- scale parameter
- $\alpha$ -- slope parameter
- $\beta$ -- bias parameter
- $x$ -- input (feature vector or sample)

## Function

```python
def activations(x: float) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-sigmoid-tanh/python -q
```
