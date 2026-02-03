# Softmax, Softplus, Softsign

> Track: `ml` | Topic: `deep-learning`

## Concept

Softmax normalizes logits, softplus smooths ReLU, softsign saturates gently.

## Math
$$\mathrm{softplus}(x)=\log(1+e^x),\quad \mathrm{softsign}(x)=\frac{x}{1+|x|}$$

- $x$ -- input (feature vector or sample)

## Function

```python
def softmax(row: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-softmax-softplus-softsign/python -q
```