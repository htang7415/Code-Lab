# Minority Cluster Entropy

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster entropy measures how spread the minority normalized answer mass is across alternative clusters.

## Math

If minority cluster vote shares are $p_1, \dots, p_M$ after removing the largest
normalized answer cluster:

$$
\mathrm{Entropy} = -\sum_{j=1}^{M} p_j \log p_j
$$

- $p_j$ -- vote share of minority cluster $j$ within the minority mass

## Key Points

- This ignores the dominant answer cluster by design.
- Higher entropy means minority mass is spread across many alternatives.
- This module returns `0.0` when no minority cluster exists.

## Function

```python
def minority_cluster_entropy(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-entropy/python -q
```
