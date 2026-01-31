# Handling Class Imbalance

> Track: `ml` | Topic: `data`

## Concept

Class imbalance occurs when some classes appear far more frequently than others in a dataset. In such settings a model can achieve high overall accuracy by simply predicting the majority class for every input, which makes raw accuracy a misleading metric. The minority class, often the class of greatest interest (e.g., fraud detection, rare disease diagnosis), is effectively ignored by the model.

Reweighting the loss function is one of the most straightforward remedies. By assigning each class a weight inversely proportional to its frequency, the contribution of rare-class samples to the total loss is amplified, encouraging the model to learn meaningful decision boundaries for every class. Alternative strategies include oversampling the minority class, undersampling the majority class, or generating synthetic samples (e.g., SMOTE), each with different trade-offs in variance and computational cost.

## Math

$$w_c = \frac{N}{C \cdot N_c}$$

- $w_c$ -- weight assigned to class $c$
- $N$ -- total number of samples
- $C$ -- total number of classes
- $N_c$ -- number of samples belonging to class $c$

## Key Points

- Accuracy is misleading under class imbalance; prefer metrics like precision, recall, F1, or AUC.
- Reweighting the loss is simple and effective but does not add new information; oversampling can help the model see more minority examples at the cost of potential overfitting.
- Undersampling discards majority-class data, which may hurt performance when the dataset is already small.
- A perfectly balanced dataset yields $w_c = 1$ for every class.

## Function

```python
def class_weights(labels: list[int]) -> dict[int, float]:
```

- `labels` -- list of integer class labels for every sample in the dataset

## Run tests

```bash
pytest modules/ml/data/class-imbalance/python -q
```
