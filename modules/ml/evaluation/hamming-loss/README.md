# Hamming Loss

> Track: `ml` | Topic: `evaluation`

## Concept

Hamming loss measures the fraction of label positions that are predicted incorrectly.

## Math

$$
\mathrm{Hamming\ Loss} = \frac{1}{nL} \sum_{i=1}^{n} \sum_{j=1}^{L} \mathbf{1}[\hat{y}_{ij} \ne y_{ij}]
$$

- $n$ -- number of examples
- $L$ -- number of label positions per example
- $\hat{y}_{ij}$ -- predicted binary label
- $y_{ij}$ -- true binary label

## Key Points

- This is especially useful for multilabel classification.
- Lower is better.
- It counts every label position equally, unlike exact-set matching.

## Function

```python
def hamming_loss(predictions: list[list[int]], labels: list[list[int]]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/hamming-loss/python -q
```
