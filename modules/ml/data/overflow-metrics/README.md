# Overflow Metrics

> Track: `ml` | Topic: `data`

## Purpose

Use this module to measure how often inputs exceed a hard token or length budget
and how severe the overflow becomes.

## First Principles

- Overflow is a data and systems problem before it is a modeling problem.
- The main questions are frequency, magnitude, and tail severity.
- A simple rate is usually the first useful number.
- Cutoff-aware metrics matter when only large overflow causes real product failure.

## Core Math

- Overflow amount:
  $$
  o_i = \max(0, \ell_i - L)
  $$
- Truncation rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[o_i > 0]
  $$
- Overrun share:
  $$
  \frac{\sum_i o_i}{\sum_i \ell_i}
  $$
- Cutoff rate:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[o_i \ge c]
  $$

## Minimal Code Mental Model

```python
count, rate = truncation_rate(lengths, max_length)
share = budget_overrun_share(lengths, max_length)
```

## Function

```python
def truncation_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
def budget_overrun_share(lengths: list[int], max_length: int) -> float:
def overflow_quantile(lengths: list[int], max_length: int, quantile: float) -> float:
def overflow_cutoff_rate(lengths: list[int], max_length: int, cutoff: int) -> float:
def overflow_cutoff_tail_mass(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
```

## When To Use What

- Use truncation rate for the first dashboard number.
- Use overrun share when comparing datasets or prompts of different total lengths.
- Use overflow quantiles when a few extreme examples drive the problem.
- Use cutoff rate and tail mass when only large overflow counts as failure.

## Run tests

```bash
pytest modules/ml/data/overflow-metrics/python -q
```
