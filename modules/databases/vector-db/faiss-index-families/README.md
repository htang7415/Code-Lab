# FAISS Index Families

> Track: `databases` | Topic: `vector-db`

## Concept

FAISS is a library of index families, not one single ANN algorithm. In
practice, the first choice is usually which family to start with: exact flat
scan, IVF, HNSW, or compressed variants like IVFPQ.

## Key Points

- `Flat` is the exact baseline and the easiest quality reference.
- `IVF` reduces work by probing only a few coarse partitions.
- `HNSW` uses a graph and is often attractive when incremental updates matter.
- `IVFPQ` trades recall for much lower memory by compressing stored vectors.
- Good FAISS usage starts from corpus size, latency, memory, and update pattern,
  not from memorizing one default index string.

## Minimal Code Mental Model

```python
family = recommend_faiss_index(
    corpus_size=5_000_000,
    target_recall="high",
    memory_tier="medium",
    update_pattern="online",
)
profile = faiss_family_profile(family)
```

## Function

```python
def validate_choice_inputs(
    corpus_size: int,
    target_recall: str,
    memory_tier: str,
    update_pattern: str,
) -> None:
def faiss_family_profile(name: str) -> dict[str, str]:
def recommend_faiss_index(
    corpus_size: int,
    target_recall: str,
    memory_tier: str,
    update_pattern: str,
) -> str:
```

## Run tests

```bash
pytest modules/databases/vector-db/faiss-index-families/python -q
```
