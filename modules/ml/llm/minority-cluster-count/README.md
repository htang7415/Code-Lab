# Minority Cluster Count

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster count measures how many normalized answer clusters remain after removing the largest one.

## Math

If there are $K$ unique normalized answer clusters:

$$
\mathrm{MinorityClusterCount} = \max(0, K - 1)
$$

## Key Points

- This counts distinct alternatives, not their vote mass.
- It complements minority-answer-share by focusing on cluster variety.
- This module normalizes answers before counting clusters.

## Function

```python
def minority_cluster_count(answers: list[str]) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-count/python -q
```
