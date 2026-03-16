# HNSW Graph Search

> Track: `databases` | Topic: `vector-db`

## Concept

HNSW searches an approximate nearest-neighbor graph instead of scoring the whole
vector table. It follows graph links greedily and expands a bounded candidate
set to trade recall for latency.

## Key Points

- HNSW is a graph index, not a new distance metric.
- Sparse long-range links help the search jump across the space quickly.
- Dense local links help it refine the answer near the target neighborhood.
- `ef_search` controls how many candidates the query expands before stopping.
- Higher recall usually costs more memory and more graph traversal work.

## Minimal Code Mental Model

```python
entry = greedy_entrypoint(documents)
graph = build_hnsw_layer0(documents, max_neighbors=2)
candidates = hnsw_candidate_ids(query, documents, max_neighbors=2, ef_search=3)
```

## Function

```python
def validate_vector(vector: list[float]) -> None:
def cosine_similarity(left: list[float], right: list[float]) -> float:
def greedy_entrypoint(documents: list[dict[str, object]]) -> str:
def build_hnsw_layer0(
    documents: list[dict[str, object]],
    max_neighbors: int = 2,
) -> dict[str, list[str]]:
def hnsw_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    max_neighbors: int = 2,
    ef_search: int = 4,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/vector-db/hnsw-graph-search/python -q
```
