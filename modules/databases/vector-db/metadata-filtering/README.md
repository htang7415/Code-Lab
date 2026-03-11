# Metadata Filtering

> Track: `databases` | Topic: `vector-db`

## Concept

Vector similarity alone is rarely enough; retrieval usually has to respect metadata filters like workspace, document type, or visibility.

## Key Points

- Metadata filters protect correctness and access control.
- Similarity scoring should run only on candidates that already satisfy the filter.
- A high-similarity vector from the wrong tenant is still the wrong result.
- Filtering usually happens before reranking, not after.

## Minimal Code Mental Model

```python
results = top_k_with_metadata(
    query_vector=[1.0, 0.0],
    documents=documents,
    filters={"workspace_id": 7, "doc_type": "spec"},
    k=2,
)
```

## Function

```python
def cosine_similarity(left: list[float], right: list[float]) -> float:
def matches_filters(document: dict[str, object], filters: dict[str, object]) -> bool:
def top_k_with_metadata(
    query_vector: list[float],
    documents: list[dict[str, object]],
    filters: dict[str, object],
    k: int,
) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/databases/vector-db/metadata-filtering/python -q
```
