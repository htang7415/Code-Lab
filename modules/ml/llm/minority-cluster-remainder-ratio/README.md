# Minority Cluster Remainder Ratio

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster remainder ratio measures the share of minority mass left after removing the strongest minority cluster.

## Math

After removing the dominant overall normalized answer cluster, let the remaining minority
cluster sizes be $m_1 \ge \dots \ge m_K$:

$$
\mathrm{RemainderRatio} =
\begin{cases}
0 & K = 0 \\
\frac{\sum_{i=2}^{K} m_i}{\sum_{i=1}^{K} m_i} & K \ge 1
\end{cases}
$$

## Key Points

- This is the minority-tail share after removing the strongest alternative cluster.
- Values near `0` mean one minority cluster dominates the disagreement.
- This module returns `0.0` when no minority mass remains.

## Function

```python
def minority_cluster_remainder_ratio(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-remainder-ratio/python -q
```
