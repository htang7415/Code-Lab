# Retrieval Metrics

> Track: `ml` | Topic: `llm`

## Concept

Retrieval evaluation asks two different questions: did the system retrieve any
relevant item early enough, and how much did reranking improve the ordering?
This family groups top-k coverage metrics, first-hit metrics, and reranker
change metrics.

## Math

- $\mathrm{Recall@}k=\frac{|\mathrm{TopK}\cap\mathrm{Relevant}|}{|\mathrm{Relevant}|}$
- $\mathrm{Precision@}k=\frac{|\mathrm{TopK}\cap\mathrm{Relevant}|}{k}$
- $\mathrm{F1@}k=\frac{2PR}{P+R}$
- $\mathrm{HitRate@}k=\frac{1}{Q}\sum_q \mathbf{1}[\mathrm{TopK}_q\cap\mathrm{Relevant}_q\neq\emptyset]$
- $\mathrm{RR}=\frac{1}{r}$ for first relevant rank $r$
- $\mathrm{gain}=\mathrm{RR}_{\mathrm{reranked}}-\mathrm{RR}_{\mathrm{baseline}}$

- $\mathrm{TopK}$ -- retrieved items up to rank $k$
- $\mathrm{Relevant}$ -- relevant item set
- $Q$ -- number of queries
- $P$ -- precision
- $R$ -- recall

## Key Points

- Recall@k measures coverage; Precision@k measures purity.
- F1@k balances the two when you need both.
- HitRate@k only asks whether at least one relevant item appears.
- Reciprocal rank focuses on how early the first relevant result appears.
- Rerank gain and disagreement separate quality improvement from ordering churn.

## Function

```python
def retrieval_recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
def retrieval_precision_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
def retrieval_f1_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
def retrieval_hit_rate_at_k(
    query_retrievals: list[list[str]],
    query_relevants: list[set[str]],
    k: int,
) -> float:
def reciprocal_rank(relevance: list[int]) -> float:
def reranker_metrics(relevance: list[int], k: int) -> tuple[float, float]:
def rerank_gain(baseline_relevance: list[int], reranked_relevance: list[int]) -> float:
def rerank_disagreement_rate(baseline_ids: list[str], reranked_ids: list[str], k: int | None = None) -> float:
```

## Pitfalls

- Precision@k can look low even when the system retrieves all relevant items if the relevant set is small.
- HitRate@k ignores how many relevant documents were retrieved after the first hit.
- Reciprocal rank and rerank gain only see the first relevant item, not the full ranking.
- Disagreement rate alone cannot tell whether the reranker changed the order for better or worse.

## Run tests

```bash
pytest modules/ml/llm/retrieval-metrics/python -q
```
