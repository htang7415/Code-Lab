# KL Regularization

> Track: `ml` | Topic: `llm`

## Concept

KL regularization keeps a policy close to a reference distribution.

## Math

$$L = \beta\, \mathrm{KL}(p\|q)$$

- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $\beta$ -- KL regularization weight
- $L$ -- loss value
- $p$ -- probability
- $q$ -- probability distribution

## Function

```python
def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/kl-regularization/python -q
```
