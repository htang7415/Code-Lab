# AdaBoost

> Track: `ml` | Topic: `models`

## Concept

AdaBoost reweights samples to focus on errors.

## Math
$$w_i \leftarrow w_i \cdot \exp\left(\alpha\,\mathbb{I}[y_i \ne \hat{y}_i]\right)$$

- $\mathbb{I}$ -- indicator function
- $w_i$ -- weight of sample $i$
- $y_i$ -- true label for sample $i$
- $\hat{y}_i$ -- predicted label for sample $i$
- $\alpha$ -- weak learner weight (boosting coefficient)

## Function

```python
def update_weights(weights: list[float], errors: list[int], alpha: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/adaboost/python -q
```
