# Classification Metrics Core

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to compare the small set of classification metrics that matter
most in practice: rank-aware accuracy, class-balanced summaries, multilabel
error, and probability-aware loss.

## First Principles

- No single classification metric is universally correct.
- Accuracy-style metrics reward correct labels.
- F1-style metrics trade precision against recall.
- Balanced metrics matter when class frequencies are uneven.
- Log loss matters when probability quality matters, not just the top label.

## Core Math

- Top-k accuracy:
  $$
  \frac{1}{n}\sum_i \mathbf{1}[y_i \in \hat{Y}_i^{(k)}]
  $$
- Macro F1:
  $$
  \frac{1}{C}\sum_{c=1}^{C}\mathrm{F1}_c
  $$
- Log loss:
  $$
  -\frac{1}{n}\sum_i \left(y_i\log p_i + (1-y_i)\log(1-p_i)\right)
  $$

## Minimal Code Mental Model

```python
score = macro_f1_score(tp, fp, fn)
loss = log_loss(labels, probabilities)
```

## Function

```python
def top_k_accuracy(predicted_rankings: list[list[int]], labels: list[int], k: int) -> float:
def macro_f1_score(true_positives: list[int], false_positives: list[int], false_negatives: list[int]) -> float:
def micro_f1_score(true_positives: list[int], false_positives: list[int], false_negatives: list[int]) -> float:
def balanced_accuracy(true_positives: list[int], false_negatives: list[int]) -> float:
def hamming_loss(predictions: list[list[int]], labels: list[list[int]]) -> float:
def log_loss(labels: list[int], probabilities: list[float], eps: float = 1.0e-15) -> float:
```

## When To Use What

- Use top-k accuracy when several ranked labels are acceptable.
- Use macro F1 or balanced accuracy when class imbalance is important.
- Use micro F1 when overall count-weighted performance matters most.
- Use Hamming loss for multilabel settings, not ordinary multiclass classification.
- Use log loss when the predicted probabilities themselves drive decisions.

## Run tests

```bash
pytest modules/ml/evaluation/classification-metrics-core/python -q
```
