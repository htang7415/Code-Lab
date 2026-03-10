# Retrieval Metrics

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to separate retrieval evaluation into coverage, purity,
first-hit quality, and reranking change.

## First Principles

- Retrieval quality is not one number; different products care about different failure modes.
- Recall asks whether relevant items were found.
- Precision asks whether early retrieved items are clean.
- Reciprocal rank asks how early the first useful item appears.
- Reranking metrics ask whether a second-stage model improved order instead of just changing it.

## Core Math

- Recall@k:
  $$
  \frac{|\mathrm{TopK}\cap\mathrm{Relevant}|}{|\mathrm{Relevant}|}
  $$
- Precision@k:
  $$
  \frac{|\mathrm{TopK}\cap\mathrm{Relevant}|}{k}
  $$
- Reciprocal rank:
  $$
  \mathrm{RR}=\frac{1}{r}
  $$
  where $r$ is the first relevant rank.

## Minimal Code Mental Model

```python
recall = retrieval_recall_at_k(retrieved_ids, relevant_ids, k=5)
rr = reciprocal_rank(relevance_labels)
gain = rerank_gain(baseline_labels, reranked_labels)
```

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

## When To Use What

- Use Recall@k when missing relevant documents is the main failure.
- Use Precision@k when early purity matters more than full coverage.
- Use HitRate@k when one successful retrieval is enough.
- Use reciprocal rank or MRR-style metrics when the first useful result dominates user experience.
- Use rerank gain together with disagreement rate when measuring a reranker over a baseline.

## Run tests

```bash
pytest modules/ml/llm/retrieval-metrics/python -q
```
