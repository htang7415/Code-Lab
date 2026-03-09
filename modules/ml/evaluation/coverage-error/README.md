# Coverage Error

> Track: `ml` | Topic: `evaluation`

## Concept

Coverage error measures how deep into a ranked label list we must go to include all relevant labels.

## Math

$$
\mathrm{coverage}(x) =
\begin{cases}
\max \{ i : rel_i = 1 \} & \text{if any relevant label exists} \\
0 & \text{otherwise}
\end{cases}
$$

- $rel_i$ -- binary relevance at rank $i$

## Key Points

- Lower is better.
- This is useful for multilabel ranking settings.
- The module averages coverage across examples.

## Function

```python
def coverage_error(relevance_rankings: list[list[int]]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/coverage-error/python -q
```
