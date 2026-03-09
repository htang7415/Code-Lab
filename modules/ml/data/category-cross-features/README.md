# Category Cross Features

> Track: `ml` | Topic: `data`

## Concept

Category cross features combine two categorical fields into a single interaction feature.

## Math

$$
\mathrm{cross}(a, b) = a \oplus b
$$

- $a$ -- category from the first field
- $b$ -- category from the second field
- $\oplus$ -- string or index combination operation

## Key Points

- Cross features let linear models represent simple interactions between categories.
- They are common in recommendation systems and ads pipelines.
- This module returns string crosses directly for clarity.

## Function

```python
def category_cross_features(left: list[str], right: list[str], separator: str = "__X__") -> list[str]:
```

## Run tests

```bash
pytest modules/ml/data/category-cross-features/python -q
```
