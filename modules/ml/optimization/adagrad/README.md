# Adagrad

> Track: `ml` | Topic: `optimization`

## Concept

Adagrad accumulates squared gradients for per-parameter learning rates.

## Math

G=G+g^2; w-=lr*g/(sqrt(G)+eps)

## Function

```python
def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/adagrad/python -q
```
