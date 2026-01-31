# Train/Validation/Test Split

> Track: `ml` | Topic: `data`

## Concept

Split indices into train, validation, and test partitions.

## Math

$$n_train = floor(N * train_frac), n_val = floor(N * val_frac)$$

## Function

```python
def split_indices(n: int, train_frac: float, val_frac: float) -> tuple[list[int], list[int], list[int]]:
```

## Run tests

```bash
pytest modules/ml/data/train-validation-test-split/python -q
```
