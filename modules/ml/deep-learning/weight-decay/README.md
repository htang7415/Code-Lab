# Weight Decay

> Track: `ml` | Topic: `deep-learning`

## Concept

Weight decay shrinks weights during optimization, decoupled in AdamW.

## Math

$$w \leftarrow w - \text{lr}\left(g + \lambda w\right)$$

## Function

```python
def weight_decay_step(w: float, grad: float, lr: float, lam: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/weight-decay/python -q
```
