# Label Smoothing

> Track: `ml` | Topic: `deep-learning`

## Concept

Label smoothing replaces a one-hot target with a softened target distribution.
This reduces overconfidence and can improve generalization.

## Math

$$
y'_i =
\begin{cases}
1 - \epsilon & i = y \\
\epsilon / (K - 1) & i \ne y
\end{cases}
$$

- $\epsilon$ -- smoothing factor
- $K$ -- number of classes
- $y$ -- target class index

## Function

```python
def label_smoothed_cross_entropy(probabilities: list[float], target_index: int, smoothing: float) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/label-smoothing/python -q
```
