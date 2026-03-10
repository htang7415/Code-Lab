# Minority Cluster Balance

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster balance measures how evenly vote mass is distributed across the minority normalized answer clusters.

## Math

If minority cluster shares are $p_{(1)} \ge \dots \ge p_{(M)}$ after removing the
dominant normalized answer cluster:

$$
\mathrm{Balance} =
\begin{cases}
0 & M = 0 \\
1 & M = 1 \\
\frac{p_{(M)}}{p_{(1)}} & M \ge 2
\end{cases}
$$

## Key Points

- Values near `1` mean minority clusters are evenly balanced.
- Values near `0` mean one minority cluster dominates the others.
- This module ignores the largest overall cluster by design.

## Function

```python
def minority_cluster_balance(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-balance/python -q
```
