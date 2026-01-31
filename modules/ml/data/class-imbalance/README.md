# Handling Class Imbalance

> Track: `ml` | Topic: `data`

## Concept

Compute class weights to rebalance loss contributions.

## Math

$$w_c = N / (K * count_c)$$

## Function

```python
def class_weights(labels: list[int]) -> dict[int, float]:
```

## Run tests

```bash
pytest modules/ml/data/class-imbalance/python -q
```
