# Rare Category Grouping

> Track: `ml` | Topic: `data`

## Concept

Rare category grouping replaces low-frequency categories with a shared fallback token before encoding.

## Math

$$
\mathrm{group}(c) =
\begin{cases}
c & \text{if count}(c) \ge m \\
\text{OTHER} & \text{otherwise}
\end{cases}
$$

- $c$ -- original category
- $m$ -- minimum frequency threshold

## Key Points

- Grouping long-tail categories can stabilize downstream encodings.
- This is a practical preprocessing guardrail before one-hot, target, or frequency encoding.
- The module returns the grouped category list directly.

## Function

```python
def group_rare_categories(categories: list[str], min_count: int, other_label: str = "__OTHER__") -> list[str]:
```

## Run tests

```bash
pytest modules/ml/data/rare-category-grouping/python -q
```
