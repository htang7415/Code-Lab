# Categorical Encoding Methods

> Track: `ml` | Topic: `data`

## Concept

Categorical preprocessing usually combines two steps: stabilize long-tail
categories, then choose an encoding that uses either feature frequency or label
statistics. These methods are best learned together because the trade-offs are
mostly about leakage, variance, and model compatibility.

## Math

- $\mathrm{freq}(c) = \frac{N_c}{N}$
- $\mathrm{enc}(c) = \frac{1}{N_c}\sum_{i:x_i=c} y_i$
- $\mathrm{smooth}(c) = \frac{\sum_{i:x_i=c} y_i + m\mu}{N_c + m}$
- $\mathrm{WoE}(c) = \log \frac{(p+s)/(P+2s)}{(n+s)/(N+2s)}$

- $N_c$ -- count of category $c$
- $N$ -- total sample count
- $\mu$ -- global target mean
- $m$ -- smoothing strength
- $p, n$ -- positive and negative counts for the category
- $P, N$ -- total positives and negatives in the dataset

## Key Points

- Frequency encoding is unsupervised and safer when leakage risk is high.
- Target encoding is strong but must be computed fold-safely.
- Smoothing regularizes target encoding for rare categories.
- Weight of evidence is common in scorecards and linear models.
- Rare-category grouping often improves every downstream categorical encoding.

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

## Pitfalls

- Target-based encodings leak badly when computed outside the training fold.
- Rare categories can overfit even when the mean encoding looks numerically reasonable.
- WoE assumes a binary outcome framing and can become unstable without smoothing.

## Run tests

```bash
pytest modules/ml/data/categorical-encoding-methods/python -q
```
