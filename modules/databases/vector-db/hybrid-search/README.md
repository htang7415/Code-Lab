# Hybrid Search

> Track: `databases` | Topic: `vector-db`

## Concept

Hybrid search combines lexical matching with vector similarity so exact keywords and semantic similarity can both influence ranking.

## Key Points

- Vector similarity helps when wording differs but meaning is close.
- Lexical matching helps when exact tokens like product names, IDs, or policy terms matter.
- A weighted hybrid score is often better than either signal alone.
- Real retrieval systems usually add metadata filters and reranking on top of this base layer.

## Minimal Code Mental Model

```python
docs = [
    {"id": "a", "text": "pgvector permissions filter", "vector": [0.6, 0.8]},
    {"id": "b", "text": "semantic ranking only", "vector": [1.0, 0.0]},
]
ranked = rank_documents("pgvector permissions", [1.0, 0.0], docs, alpha=0.4)
```

## Function

```python
def tokenize(text: str) -> list[str]:
def cosine_similarity(left: list[float], right: list[float]) -> float:
def lexical_overlap_score(query_text: str, doc_text: str) -> float:
def hybrid_score(
    query_text: str,
    query_vector: list[float],
    doc_text: str,
    doc_vector: list[float],
    alpha: float = 0.5,
) -> float:
def rank_documents(
    query_text: str,
    query_vector: list[float],
    documents: list[dict[str, object]],
    alpha: float = 0.5,
) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/databases/vector-db/hybrid-search/python -q
```
