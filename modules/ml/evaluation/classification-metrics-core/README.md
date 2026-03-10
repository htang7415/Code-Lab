# Classification Metrics Core

> Track: `ml` | Topic: `evaluation`

## Concept

Core classification metrics should cover ranked-label accuracy, class-balanced
averages, multilabel labelwise error, and probability-aware loss. These are the
metrics most often compared side-by-side when choosing a classifier.

## Math

- $\mathrm{Top\text{-}k\ Accuracy} = \frac{1}{n}\sum_i \mathbf{1}[y_i \in \hat{Y}_i^{(k)}]$
- $\mathrm{MacroF1} = \frac{1}{C}\sum_{c=1}^{C}\mathrm{F1}_c$
- $\mathrm{MicroF1} = \frac{2TP}{2TP + FP + FN}$
- $\mathrm{BalancedAccuracy} = \frac{1}{C}\sum_c \frac{TP_c}{TP_c + FN_c}$
- $\mathrm{HammingLoss} = \frac{1}{nL}\sum_{i=1}^{n}\sum_{j=1}^{L}\mathbf{1}[\hat{y}_{ij}\ne y_{ij}]$
- $\mathrm{LogLoss} = -\frac{1}{n}\sum_i \left(y_i\log p_i + (1-y_i)\log(1-p_i)\right)$

- $C$ -- number of classes
- $TP, FP, FN$ -- true positives, false positives, false negatives
- $L$ -- number of label positions
- $p_i$ -- predicted probability for the positive class

## Key Points

- Top-k accuracy is useful when several labels are plausible and predictions are ranked.
- Macro F1 and balanced accuracy help under class imbalance.
- Micro F1 emphasizes overall count-weighted performance.
- Hamming loss is a multilabel metric, not a standard multiclass score.
- Log loss uses probabilities and penalizes confident mistakes heavily.

## Function

```python
def top_k_accuracy(predicted_rankings: list[list[int]], labels: list[int], k: int) -> float:
def macro_f1_score(true_positives: list[int], false_positives: list[int], false_negatives: list[int]) -> float:
def micro_f1_score(true_positives: list[int], false_positives: list[int], false_negatives: list[int]) -> float:
def balanced_accuracy(true_positives: list[int], false_negatives: list[int]) -> float:
def hamming_loss(predictions: list[list[int]], labels: list[list[int]]) -> float:
def log_loss(labels: list[int], probabilities: list[float], eps: float = 1.0e-15) -> float:
```

## Pitfalls

- Macro and micro F1 answer different questions and should not be swapped casually.
- Top-k accuracy can look high even when the model's top prediction is weak.
- Hamming loss ignores label correlations.
- Log loss is very sensitive to overconfident wrong probabilities.

## Run tests

```bash
pytest modules/ml/evaluation/classification-metrics-core/python -q
```
