# Train/Validation/Test Split

> Track: `ml` | Topic: `data`

## Concept

A three-way split partitions data into training, validation, and test sets, each serving a distinct purpose. The training set is used to fit model parameters, the validation set guides hyperparameter tuning and model selection, and the test set provides a final, unbiased estimate of generalization performance. This separation ensures that decisions made during development do not contaminate the evaluation.

Using the test set for tuning leaks information about the test distribution into the model selection process, producing optimistic performance estimates that fail to generalize. The validation set acts as a proxy for unseen data during development: you train multiple model configurations, evaluate each on the validation set, select the best, and only then report its performance on the held-out test set. The test set should ideally be touched only once.

## Math

$$n_{\text{train}} = \lfloor N \cdot f_{\text{train}} \rfloor$$

$$n_{\text{val}} = \lfloor N \cdot f_{\text{val}} \rfloor$$

$$n_{\text{test}} = N - n_{\text{train}} - n_{\text{val}}$$

- $N$ -- total number of samples
- $f_{\text{train}}$ -- fraction allocated to training (commonly $0.6$ -- $0.8$)
- $f_{\text{val}}$ -- fraction allocated to validation (commonly $0.1$ -- $0.2$)
- $n_{\text{train}}, n_{\text{val}}, n_{\text{test}}$ -- resulting partition sizes

## Key Points

- The validation set guides model selection and hyperparameter tuning without touching the test set.
- The test set should be evaluated only once to provide an unbiased generalization estimate.
- A common ratio is 60/20/20 or 80/10/10 for train/validation/test.
- When data is scarce, $k$-fold cross-validation can replace a fixed validation set to make better use of limited samples.
- All three partitions must be mutually disjoint: $\text{Train} \cap \text{Val} = \text{Val} \cap \text{Test} = \text{Train} \cap \text{Test} = \emptyset$.

## Function

```python
def split_indices(n: int, train_frac: float, val_frac: float) -> tuple[list[int], list[int], list[int]]:
```

- `n` -- total number of samples ($N$)
- `train_frac` -- fraction of samples allocated to the training set ($f_{\text{train}}$)
- `val_frac` -- fraction of samples allocated to the validation set ($f_{\text{val}}$)

## Run tests

```bash
pytest modules/ml/data/train-validation-test-split/python -q
```
