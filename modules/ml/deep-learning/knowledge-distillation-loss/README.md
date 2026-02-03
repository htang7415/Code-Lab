# Knowledge Distillation Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Distillation matches student logits to teacher logits.

## Math

$$L = \mathrm{KL}\left(\mathrm{softmax}\left(\frac{z_s}{T}\right)\,\middle\|\,\mathrm{softmax}\left(\frac{z_t}{T}\right)\right)$$

- $L$ -- distillation loss
- $\mathrm{KL}$ -- Kullback-Leibler divergence
- $z_s$ -- student logits
- $z_t$ -- teacher logits
- $T$ -- temperature

## Function

```python
def distill_loss(student: list[float], teacher: list[float], temp: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/knowledge-distillation-loss/python -q
```
