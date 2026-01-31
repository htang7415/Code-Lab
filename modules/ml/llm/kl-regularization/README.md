# KL Regularization

> Track: `ml` | Topic: `llm`

## Concept

KL regularization keeps a policy close to a reference distribution.

## Math

Penalty: L = β * KL(p || q).

## Function

```python
def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/kl-regularization/python -q
```
