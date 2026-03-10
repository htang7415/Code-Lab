# Minority Cluster Tail Entropy Gap

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail entropy gap measures how far the residual tail is from a perfectly uniform tail distribution.

## Math

If the residual tail has $M$ clusters with shares $p_1, \dots, p_M$, define:

$$
\mathrm{EntropyGap} = \log M - \left(-\sum_{i=1}^{M} p_i \log p_i\right)
$$

## Key Points

- An exactly uniform residual tail has entropy gap `0`.
- Larger values mean the residual tail is less uniform.
- This module returns `0.0` when the residual tail has fewer than two clusters.

## Function

```python
def minority_cluster_tail_entropy_gap(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-entropy-gap/python -q
```
