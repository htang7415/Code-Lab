# Minority Cluster Tail Top Share

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail top share measures the within-tail share of the strongest residual minority cluster.

## Math

After removing the dominant overall normalized answer cluster and the strongest minority
cluster, let the remaining tail sizes be $t_1 \ge \dots \ge t_M$:

$$
\mathrm{TailTopShare} =
\begin{cases}
0 & M = 0 \\
\frac{t_1}{\sum_{i=1}^{M} t_i} & M \ge 1
\end{cases}
$$

## Key Points

- This is normalized within the residual tail only.
- Values near `1` mean one residual tail cluster dominates the tail mass.
- This module returns `0.0` when no residual tail exists.

## Function

```python
def minority_cluster_tail_top_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-top-share/python -q
```
