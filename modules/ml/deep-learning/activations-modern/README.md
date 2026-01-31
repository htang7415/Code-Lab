# Modern Activations

> Track: `ml` | Topic: `deep-learning`

## Concept

Modern activations like GeLU, Swish, SwiGLU, and Mish improve expressiveness.

## Math

$$
\begin{aligned}
\mathrm{Swish}(x) &= x\,\sigma(x) \\
\mathrm{GeLU}(x) &\approx 0.5x\left(1+\tanh\left(\sqrt{\frac{2}{\pi}}\left(x+0.044715x^3\right)\right)\right)
\end{aligned}
$$

## Function

```python
def modern_activations(x: float) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-modern/python -q
```
