# Activation Functions

> Track: `ml` | Topic: `deep-learning`

## Concept

Activation functions shape how a neuron responds to an input. Different
families trade saturation, smoothness, sparsity, and gradient flow.

## Math

- $\sigma(x)=\frac{1}{1+e^{-x}}$
- $\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$
- $\mathrm{ReLU}(x)=\max(0,x)$
- $\mathrm{LeakyReLU}(x)=\max(\alpha x, x)$
- $\mathrm{Swish}(x)=x\,\sigma(x)$
- $\mathrm{GeLU}(x)\approx 0.5x\left(1+\tanh\left(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right)\right)$
- $\mathrm{softplus}(x)=\log(1+e^x)$
- $\mathrm{softsign}(x)=\frac{x}{1+|x|}$

- $\sigma$ -- sigmoid function
- $\alpha$ -- negative slope parameter
- $x$ -- scalar input

## Key Points

- Sigmoid and tanh are smooth but can saturate.
- ReLU-family activations keep sparse positive responses and improve gradient flow.
- Modern activations like Swish and GeLU are smoother and often work well in deep models.
- Softmax is an output normalization, while softplus and softsign are scalar activations.

## Function

```python
def scalar_activations(x: float, alpha: float = 0.01) -> dict[str, float]:

def softmax(row: list[float]) -> list[float]:
```

## Pitfalls

- Sigmoid and tanh can cause small gradients at large magnitudes.
- ReLU can die if activations stay negative.
- Softmax should be used on a vector of logits, not a single scalar.

## Run tests

```bash
pytest modules/ml/deep-learning/activation-functions/python -q
```
