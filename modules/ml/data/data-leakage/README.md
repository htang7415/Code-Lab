# Data Leakage

> Track: `ml` | Topic: `data`

## Concept

Data leakage occurs when information from outside the training distribution contaminates the model during training, leading to overly optimistic performance estimates that do not generalize to production. The most common forms are train/test overlap (the same sample appears in both sets), temporal leakage (using future data to predict the past), and preprocessing leakage (fitting a scaler or encoder on the full dataset before splitting).

Leakage is dangerous precisely because it is invisible at training time -- the model appears to perform well on the test set, but fails once deployed on truly unseen data. The fundamental safeguard is to ensure that train and test sets are strictly disjoint and that every preprocessing step is fitted only on the training partition. Feature leakage, where a feature is derived from or strongly correlated with the target, is another subtle variant that can inflate metrics without providing real predictive power.

## Math

$$\text{Train} \cap \text{Test} = \emptyset$$

$$|\text{Train}| + |\text{Test}| \leq N$$

- $\text{Train}$ -- set of sample identifiers used for training
- $\text{Test}$ -- set of sample identifiers reserved for evaluation
- $N$ -- total number of samples in the dataset

## Key Points

- Always split the data before any preprocessing (scaling, encoding, imputation) to avoid information leaking from test into train.
- In time-series problems, use temporal splits rather than random splits to prevent future data from influencing past predictions.
- Feature leakage from target encoding or proxy variables can be as harmful as direct sample overlap.
- A simple overlap check ($|\text{Train} \cap \text{Test}| > 0$) catches the most obvious form of leakage.

## Function

```python
def has_leakage(train_ids: list[int], test_ids: list[int]) -> bool:
```

- `train_ids` -- list of sample identifiers in the training set
- `test_ids` -- list of sample identifiers in the test set

## Run tests

```bash
pytest modules/ml/data/data-leakage/python -q
```
