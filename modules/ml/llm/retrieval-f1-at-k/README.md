# Retrieval F1@k

> Track: `ml` | Topic: `llm`

## Concept

Retrieval F1@k combines precision@k and recall@k into a single balance score.

## Math

$$
\mathrm{F1@}k = \frac{2 \cdot \mathrm{Precision@}k \cdot \mathrm{Recall@}k}{\mathrm{Precision@}k + \mathrm{Recall@}k}
$$

- $\mathrm{Precision@}k$ -- fraction of retrieved top-k items that are relevant
- $\mathrm{Recall@}k$ -- fraction of relevant items covered by top-k retrieval

## Key Points

- This is useful when neither purity nor coverage alone is sufficient.
- It is zero when either precision or recall is zero.
- The module reuses the same top-k set semantics as the existing retrieval metrics.

## Function

```python
def retrieval_f1_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/retrieval-f1-at-k/python -q
```
