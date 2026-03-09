# Retrieval Hit Rate

> Track: `ml` | Topic: `llm`

## Concept

Retrieval hit rate measures the fraction of queries for which at least one relevant item appears in the top-k results.

## Math

$$
\mathrm{HitRate@}k = \frac{1}{Q} \sum_{q=1}^{Q} \mathbf{1}[\mathrm{TopK}_q \cap \mathrm{Relevant}_q \ne \emptyset]
$$

- $Q$ -- number of queries
- $\mathrm{TopK}_q$ -- first `k` retrieved items for query $q$
- $\mathrm{Relevant}_q$ -- relevant items for query $q$

## Key Points

- Hit rate is a simple success-at-k metric.
- It ignores how many relevant items were found beyond the first hit.
- This complements precision, recall, and MRR.

## Function

```python
def retrieval_hit_rate_at_k(
    query_retrievals: list[list[str]],
    query_relevants: list[set[str]],
    k: int,
) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/retrieval-hit-rate/python -q
```
