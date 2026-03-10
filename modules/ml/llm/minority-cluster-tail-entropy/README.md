# Minority Cluster Tail Entropy

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail entropy measures diversity inside the lower-mass minority answer clusters after removing the strongest minority cluster.

## Math

After removing the dominant overall normalized answer cluster and the strongest remaining
minority cluster, let the tail shares be $p_1, \dots, p_M$:

$$
\mathrm{TailEntropy} = -\sum_{i=1}^{M} p_i \log p_i
$$

## Key Points

- This isolates diversity in the minority tail instead of the strongest alternative cluster.
- Higher values mean the lower-mass minority clusters are more spread out.
- This module returns `0.0` when there is no minority tail.

## Function

```python
def minority_cluster_tail_entropy(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-entropy/python -q
```
