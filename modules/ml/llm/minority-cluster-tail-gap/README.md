# Minority Cluster Tail Gap

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail gap measures the dominance gap between the two strongest clusters in the residual minority tail.

## Math

After removing the dominant overall normalized answer cluster and the strongest minority cluster,
let the remaining tail shares be $p_1 \ge p_2 \ge \dots$:

$$
\mathrm{TailGap} = p_1 - p_2
$$

where $p_2 = 0$ if only one tail cluster remains.

## Key Points

- Larger values mean the residual tail is dominated by one cluster.
- Smaller values mean the residual tail is more evenly split.
- This module returns `0.0` when no residual tail exists.

## Function

```python
def minority_cluster_tail_gap(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-gap/python -q
```
