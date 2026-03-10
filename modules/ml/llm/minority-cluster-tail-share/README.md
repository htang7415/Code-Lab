# Minority Cluster Tail Share

> Track: `ml` | Topic: `llm`

## Concept

Minority cluster tail share measures the absolute answer share captured by the strongest cluster inside the residual minority tail.

## Math

After removing the dominant overall normalized answer cluster and the strongest minority
cluster, let the remaining tail sizes be $t_1 \ge \dots \ge t_M$, and let $N$ be total answers:

$$
\mathrm{TailShare} =
\begin{cases}
0 & M = 0 \\
\frac{t_1}{N} & M \ge 1
\end{cases}
$$

## Key Points

- This is an absolute share over all answers, not a share within tail mass.
- Larger values mean one residual tail cluster still has noticeable overall mass.
- This module returns `0.0` when no residual tail exists.

## Function

```python
def minority_cluster_tail_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/minority-cluster-tail-share/python -q
```
