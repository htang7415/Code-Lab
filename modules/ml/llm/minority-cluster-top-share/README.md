# Minority Cluster Top Share

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster top share measures the largest vote share among the minority normalized answer clusters.

## Math

If minority cluster sizes are $s_1, \dots, s_M$ after removing the dominant cluster:

$$
\mathrm{TopShare} = \frac{\max_j s_j}{\sum_{j=1}^{M} s_j}
$$

## Key Points

- This identifies whether one minority alternative dominates the rest.
- It ignores the largest overall cluster by design.
- This module returns `0.0` when no minority cluster exists.

## Function

```python
def minority_cluster_top_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-top-share/python -q
```
