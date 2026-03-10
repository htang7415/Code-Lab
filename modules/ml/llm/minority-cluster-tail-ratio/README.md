# Minority Cluster Tail Ratio

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail ratio measures the size of the residual minority tail relative to the strongest minority cluster.

## Math

After removing the dominant overall normalized answer cluster, let the minority cluster sizes be
$m_1 \ge \dots \ge m_K$:

$$
\mathrm{TailRatio} =
\begin{cases}
0 & K \le 1 \\
\frac{\sum_{i=2}^{K} m_i}{m_1} & K \ge 2
\end{cases}
$$

## Key Points

- Values near `0` mean one minority cluster dominates the disagreement.
- Larger values mean the rest of the minority mass rivals the strongest alternative.
- This module returns `0.0` when no residual minority tail exists.

## Function

```python
def minority_cluster_tail_ratio(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-ratio/python -q
```
