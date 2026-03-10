# Agreement Metrics

> Track: `ml` | Topic: `evaluation`

## Concept

Agreement analysis starts with raw matching rate and then asks how much of that
agreement would happen by chance. These metrics are useful for labeler
consistency, repeated-model judgments, and evaluation quality control.

## Math

- $\mathrm{AgreementRate} = \frac{\max_k c_k}{N}$
- $\kappa = \frac{p_o - p_e}{1 - p_e}$

- $c_k$ -- count of outcome $k$
- $N$ -- number of observed outcomes
- $p_o$ -- observed agreement
- $p_e$ -- expected agreement under chance

## Key Points

- Agreement rate is the simplest raw consistency summary.
- Cohen kappa discounts agreement that is expected from class marginals alone.
- Raw agreement can look deceptively strong when one class dominates.

## Function

```python
def agreement_rate(outcomes: list[str | int]) -> float:
def cohen_kappa(confusion_matrix: list[list[int]]) -> float:
```

## Pitfalls

- Agreement rate says nothing about chance agreement.
- Cohen kappa is sensitive to class prevalence and marginal imbalance.
- Kappa requires a valid square confusion matrix, not just a list of labels.

## Run tests

```bash
pytest modules/ml/evaluation/agreement-metrics/python -q
```
