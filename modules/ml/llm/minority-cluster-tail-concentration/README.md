# Minority Cluster Tail Concentration

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail concentration measures how concentrated the residual minority tail is across its clusters.

## Math

After removing the dominant overall normalized answer cluster and the strongest minority
cluster, let the residual tail shares be $p_1, \dots, p_M$:

$$
\mathrm{Concentration} = \sum_{i=1}^{M} p_i^2
$$

## Key Points

- This is a Herfindahl-style concentration score over the residual tail.
- Values near `1` mean the tail is dominated by a single cluster.
- This module returns `0.0` when no residual tail exists.

## Function

```python
def minority_cluster_tail_concentration(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-concentration/python -q
```
