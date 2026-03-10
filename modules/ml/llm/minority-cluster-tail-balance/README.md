# Minority Cluster Tail Balance

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail balance measures how evenly mass is distributed across the lower-mass minority clusters after removing the strongest alternative.

## Math

After removing the dominant overall normalized answer cluster and the strongest minority cluster,
let the remaining tail sizes be $t_1 \ge \dots \ge t_M$:

$$
\mathrm{TailBalance} =
\begin{cases}
0 & M = 0 \\
1 & M = 1 \\
\frac{t_M}{t_1} & M \ge 2
\end{cases}
$$

## Key Points

- Values near `1` mean the minority tail is evenly balanced.
- Values near `0` mean one tail cluster dominates the rest.
- This module ignores the dominant overall cluster and the strongest minority cluster by design.

## Function

```python
def minority_cluster_tail_balance(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-balance/python -q
```
