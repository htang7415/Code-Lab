# Contrastive Loss (InfoNCE)

> Track: `ml` | Topic: `representation`

## Concept

Contrastive learning pulls similar pairs together and pushes negatives apart.
InfoNCE uses a softmax over cosine similarities.

## Math

$$
\mathcal{L} = -\log \frac{\exp(\text{sim}(a,p)/\tau)}{\exp(\text{sim}(a,p)/\tau) + \sum_{n}\exp(\text{sim}(a,n)/\tau)}
$$

## Function

```python
def info_nce_loss(
    anchor: list[float],
    positive: list[float],
    negatives: list[list[float]],
    temperature: float = 0.1,
) -> float:
```

## Run tests

```bash
pytest modules/ml/representation/contrastive-loss/python -q
```
