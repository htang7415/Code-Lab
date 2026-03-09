# Minority Cluster Share

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster share measures what fraction of normalized answer clusters lies outside the largest one.

## Math

If there are $K$ unique normalized answer clusters:

$$
\mathrm{MinorityClusterShare} =
\begin{cases}
0 & K = 0 \\
\frac{K - 1}{K} & K > 0
\end{cases}
$$

## Key Points

- This normalizes minority cluster count by the total number of clusters.
- It measures cluster diversity without using vote mass.
- This module normalizes answers before counting clusters.

## Function

```python
def minority_cluster_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-share/python -q
```
