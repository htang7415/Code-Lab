# Reranking Pipelines

> Track: `databases` | Topic: `vector-db`

## Concept

Reranking takes a coarse candidate set from first-stage retrieval and reorders it with a more expensive, more precise scoring function.

## Key Points

- First-stage retrieval is about recall.
- Reranking is about improving the final ordering inside the candidate set.
- A reranker cannot rescue a relevant document that never made it into the candidate pool.
- Hybrid systems often use vector retrieval first, then rerank with lexical or model-based signals.

## Minimal Code Mental Model

```python
top_candidates = initial_retrieve(documents, candidate_k=2)
reranked = rerank_candidates("approval gated actions", top_candidates)
final_ids = pipeline_rank("approval gated actions", documents, candidate_k=2, final_k=2)
```

## Function

```python
def tokenize(text: str) -> list[str]:
def initial_retrieve(
    documents: list[dict[str, object]],
    candidate_k: int,
) -> list[dict[str, object]]:
def rerank_score(query_text: str, document: dict[str, object]) -> float:
def rerank_candidates(
    query_text: str,
    candidates: list[dict[str, object]],
) -> list[tuple[str, float]]:
def pipeline_rank(
    query_text: str,
    documents: list[dict[str, object]],
    candidate_k: int,
    final_k: int,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/vector-db/reranking-pipelines/python -q
```
