# Softmax, Softplus, Softsign

> Track: `ml` | Topic: `deep-learning`

## Concept

Softmax normalizes logits, softplus smooths ReLU, softsign saturates gently.

## Math

softplus(x)=log(1+e^x), softsign(x)=x/(1+|x|)

## Function

```python
def softmax(row: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/activations-softmax-softplus-softsign/python -q
```
