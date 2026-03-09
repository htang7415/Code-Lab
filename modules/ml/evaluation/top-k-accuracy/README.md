# Top-k Accuracy

> Track: `ml` | Topic: `evaluation`

## Concept

Top-k accuracy checks whether the true label appears anywhere in the model's first `k` predicted classes.

## Math

$$
\mathrm{Top\text{-}k\ Accuracy} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}[y_i \in \hat{Y}_i^{(k)}]
$$

- $y_i$ -- true label for example $i$
- $\hat{Y}_i^{(k)}$ -- top `k` predicted labels for example $i$
- $n$ -- number of examples

## Key Points

- This is useful when several labels are semantically similar or visually confusable.
- `k = 1` reduces to standard accuracy on ranked predictions.
- The module takes explicit ranked label lists instead of logits.

## Function

```python
def top_k_accuracy(predicted_rankings: list[list[int]], labels: list[int], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/top-k-accuracy/python -q
```
