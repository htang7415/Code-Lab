# Weight Decay

> Track: `ml` | Topic: `deep-learning`

## Concept

Weight decay shrinks weights during optimization, decoupled in AdamW.

## Math

$$w \leftarrow w - \eta\left(g + \lambda w\right)$$

- $\eta$ -- learning rate (step size)
- $\lambda$ -- regularization strength or weighting coefficient
- $w$ -- weight parameter
- $g$ -- gradient

## Function

```python
def weight_decay_step(w: float, grad: float, lr: float, lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/weight-decay/python -q
```
