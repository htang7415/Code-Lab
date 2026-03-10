# Agreement Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to distinguish raw agreement from chance-corrected agreement.

## First Principles

- Raw agreement asks how often outcomes match.
- Chance-corrected agreement asks how much of that matching is better than what class frequencies would produce by accident.
- This matters for labeler consistency, judge consistency, and repeated-model evaluation.

## Core Math

- Agreement rate:
  $$
  \mathrm{AgreementRate} = \frac{\max_k c_k}{N}
  $$
- Cohen's kappa:
  $$
  \kappa = \frac{p_o - p_e}{1 - p_e}
  $$

## Minimal Code Mental Model

```python
raw = agreement_rate(outcomes)
kappa = cohen_kappa(confusion_matrix)
```

## Function

```python
def agreement_rate(outcomes: list[str | int]) -> float:
def cohen_kappa(confusion_matrix: list[list[int]]) -> float:
```

## When To Use What

- Use agreement rate when you want the simplest consistency summary.
- Use Cohen's kappa when class imbalance makes raw agreement misleading.
- Use both together when auditing judges, annotators, or model-vs-model consistency.

## Run tests

```bash
pytest modules/ml/evaluation/agreement-metrics/python -q
```
