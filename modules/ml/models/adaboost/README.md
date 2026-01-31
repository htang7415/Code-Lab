# AdaBoost

> Track: `ml` | Topic: `models`

## Concept

AdaBoost reweights samples to focus on errors.

## Math

$$w_i \leftarrow w_i \cdot \exp\left(\alpha \mathbb{I}[\text{misclassified}]\right)$$

## Function

```python
def update_weights(weights: list[float], errors: list[int], alpha: float) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/adaboost/python -q
```
