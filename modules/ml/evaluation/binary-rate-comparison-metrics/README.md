# Binary Rate Comparison Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to compare how often a binary event happens across groups,
baselines, or time periods.

## First Principles

- Everything in this family starts from one primitive: the positive event rate.
- Gaps and deltas are absolute comparisons.
- Ratios and odds are multiplicative comparisons.
- Log ratios turn multiplicative effects into additive ones.

## Core Math

- Positive rate:
  $$
  \hat{p} = \frac{\text{positive events}}{\text{total events}}
  $$
- Gap:
  $$
  \hat{p}_A - \hat{p}_B
  $$
- Ratio:
  $$
  \frac{\hat{p}_A}{\hat{p}_B}
  $$
- Odds:
  $$
  \frac{\hat{p}}{1-\hat{p}}
  $$

## Minimal Code Mental Model

```python
rate = positive_rate(labels)
gap = base_rate_gap(group_a, group_b)
ratio = prevalence_ratio(group_a, group_b)
```

## Core Functions

```python
def positive_rate(labels: list[int]) -> float:
def base_rate_gap(group_a: list[int], group_b: list[int]) -> float:
def prevalence_delta(baseline_labels: list[int], comparison_labels: list[int]) -> float:
def prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
def prevalence_index(labels: list[int], baseline_rate: float) -> float:
def prevalence_odds(labels: list[int]) -> float:
def log_prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
def log_rate_ratio(event_count: int, total_count: int, baseline_event_count: int, baseline_total_count: int) -> float:
```

## When To Use What

- Use gaps when absolute change matters.
- Use ratios when relative lift matters.
- Use odds mainly when the surrounding model or domain already uses odds framing.
- Use log ratios when you want additive effect interpretation or symmetry around no effect.

## Run tests

```bash
pytest modules/ml/evaluation/binary-rate-comparison-metrics/python -q
```
