# Retrieval Precision@k

> Track: `ml` | Topic: `llm`

## Concept

Retrieval Precision@k measures what fraction of the top-k retrieved results are relevant.

## Math

$$
\mathrm{Precision@}k = \frac{|\mathrm{TopK} \cap \mathrm{Relevant}|}{k}
$$

- $\mathrm{TopK}$ -- first `k` retrieved documents
- $\mathrm{Relevant}$ -- set of relevant documents

## Key Points

- Precision@k emphasizes purity of the retrieved set.
- This complements Recall@k, which emphasizes coverage of relevant documents.
- The metric is capped by `k` even when there are fewer than `k` retrieved items.

## Function

```python
def retrieval_precision_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/retrieval-precision-at-k/python -q
```
