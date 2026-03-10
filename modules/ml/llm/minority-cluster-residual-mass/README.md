# Minority Cluster Residual Mass

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster residual mass measures how much overall answer mass remains after removing the strongest minority cluster.

## Math

Let $N$ be the total number of answers. After removing the dominant overall normalized answer
cluster, let the remaining minority cluster sizes be $m_1 \ge \dots \ge m_K$:

$$
\mathrm{ResidualMass} = \frac{\sum_{i=2}^{K} m_i}{N}
$$

## Key Points

- This isolates the minority tail after the strongest alternative cluster is removed.
- Larger values mean disagreement is spread beyond a single alternative answer.
- This module returns `0.0` when there is no residual minority tail.

## Function

```python
def minority_cluster_residual_mass(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-residual-mass/python -q
```
