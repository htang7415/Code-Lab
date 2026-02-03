# Stratified Split

> Track: `ml` | Topic: `data`

## Concept

A stratified split divides a dataset into subsets (e.g., train and test) while preserving the original class proportions in each subset. In a standard random split, rare classes may end up severely under-represented or even entirely absent from one of the partitions, leading to biased training or unreliable evaluation. Stratification guarantees that every class is represented in roughly the same ratio as in the full dataset.

This technique is especially critical for imbalanced datasets where some classes contain only a handful of samples. Without stratification, a small test set might contain zero examples of a minority class, making it impossible to evaluate performance on that class. Scikit-learn's `train_test_split` supports stratification directly through the `stratify` parameter.

## Math
$$\frac{|S_c^{\text{train}}|}{|S_c|} \approx f,\quad \frac{|S_c^{\text{test}}|}{|S_c|} \approx 1-f$$

- $S_c$ -- samples belonging to class c
- $f$ -- train split fraction

## Key Points

- Stratification is most important when classes are rare; with balanced classes, random splitting is often sufficient.
- Each class is split independently, so the overall train fraction is maintained per class, not just globally.
- In scikit-learn, pass `stratify=y` to `train_test_split` to enable stratified splitting.
- For very small classes, even stratification may leave too few samples for reliable evaluation; consider cross-validation in such cases.

## Function

```python
def stratified_split(labels: list[int], train_frac: float) -> tuple[list[int], list[int]]:
```

- `labels` -- list of integer class labels for each sample
- `train_frac` -- fraction of samples to assign to the training set ($f$)

## Run tests

```bash
pytest modules/ml/data/stratified-split/python -q
```