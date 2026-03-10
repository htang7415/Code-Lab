# Categorical Encoding Methods

> Track: `ml` | Topic: `data`

## Purpose

Use this module to compare the main ways to turn categories into numeric
features without losing the structure of rare categories or leaking targets.

## First Principles

- Categorical encoding is mostly a trade-off between information, variance, and leakage.
- Frequency encoding is unsupervised and comparatively safe.
- Target-style encodings are strong but dangerous when computed outside the training fold.
- Rare-category grouping often improves every downstream categorical encoding.

## Core Math

- Frequency:
  $$
  \mathrm{freq}(c) = \frac{N_c}{N}
  $$
- Target mean encoding:
  $$
  \mathrm{enc}(c) = \frac{1}{N_c}\sum_{i:x_i=c} y_i
  $$
- Smoothed target mean:
  $$
  \mathrm{smooth}(c) = \frac{\sum_{i:x_i=c} y_i + m\mu}{N_c + m}
  $$

## Minimal Code Mental Model

```python
freq_map = frequency_encoding_map(categories)
target_map = target_encoding_map(categories, targets)
grouped = group_rare_categories(categories, min_count=5)
```

## Function

```python
def frequency_encoding_map(categories: list[str]) -> dict[str, float]:
def target_encoding_map(categories: list[str], targets: list[float]) -> dict[str, float]:
def smoothed_mean_encoding_map(categories: list[str], targets: list[float], smoothing: float) -> dict[str, float]:
def weight_of_evidence(
    positive_count: int,
    negative_count: int,
    total_positive: int,
    total_negative: int,
    smoothing: float = 0.5,
) -> float:
def group_rare_categories(categories: list[str], min_count: int, other_label: str = "__OTHER__") -> list[str]:
```

## When To Use What

- Use frequency encoding when leakage risk is the main concern.
- Use target encoding only with fold-safe computation.
- Use smoothed mean encoding when rare categories would otherwise overfit.
- Use weight of evidence mainly in binary-outcome scorecard-style settings.
- Group rare categories before encoding when the tail is too sparse to learn reliably.

## Run tests

```bash
pytest modules/ml/data/categorical-encoding-methods/python -q
```
