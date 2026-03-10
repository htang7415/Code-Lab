# Minority Cluster Dominance

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster dominance measures the gap between the largest minority cluster share and the next-largest minority cluster share.

## Math

If minority cluster shares are $p_{(1)} \ge p_{(2)} \ge \dots$ after removing the
dominant normalized answer cluster:

$$
\mathrm{DominanceGap} = p_{(1)} - p_{(2)}
$$

## Key Points

- Larger values mean one minority alternative dominates the other minority clusters.
- This ignores the largest overall normalized answer cluster by design.
- This module returns `0.0` when no minority cluster exists.

## Function

```python
def minority_cluster_dominance(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-dominance/python -q
```
