# Minority Cluster Mode

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster mode measures the most common cluster size among normalized answer clusters outside the largest one.

## Math

If normalized answer cluster sizes are $s_1 \ge s_2 \ge \dots \ge s_K$:

$$
\mathrm{MinorityClusterMode} = \mathrm{mode}(s_2, \dots, s_K)
$$

## Key Points

- This focuses on the typical size of alternative answer clusters.
- It ignores the single largest cluster by design.
- This module returns `0` when there is no minority cluster.

## Function

```python
def minority_cluster_mode(answers: list[str]) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-mode/python -q
```
