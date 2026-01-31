# Knowledge Distillation Loss

> Track: `ml` | Topic: `deep-learning`

## Concept

Distillation matches student logits to teacher logits.

## Math

L = KL(softmax(z_s/T) || softmax(z_t/T))

## Function

```python
def distill_loss(student: list[float], teacher: list[float], temp: float = 1.0) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/knowledge-distillation-loss/python -q
```
