# IVF Search

> Track: `databases` | Topic: `vector-db`

## Concept

IVF uses coarse centroids to partition vectors into inverted lists, then probes
only a few lists at query time instead of scanning the whole collection.

## Key Points

- IVF is a coarse quantization strategy for reducing candidate count.
- Each vector is assigned to its nearest centroid during indexing.
- `nprobe` controls how many centroid lists the query explores.
- Better centroids and a higher `nprobe` usually improve recall.
- Skewed or poorly trained centroids can make candidate lists unbalanced.

## Minimal Code Mental Model

```python
lists = build_inverted_lists(documents, centroids)
probed = probed_centroid_ids(query, centroids, nprobe=2)
candidates = ivf_candidate_ids(query, documents, centroids, nprobe=1)
```

## Function

```python
def validate_vector(vector: list[float]) -> None:
def squared_l2_distance(left: list[float], right: list[float]) -> float:
def nearest_centroid_id(
    vector: list[float],
    centroids: list[dict[str, object]],
) -> str:
def build_inverted_lists(
    documents: list[dict[str, object]],
    centroids: list[dict[str, object]],
) -> dict[str, list[str]]:
def probed_centroid_ids(
    query_vector: list[float],
    centroids: list[dict[str, object]],
    nprobe: int,
) -> list[str]:
def ivf_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    centroids: list[dict[str, object]],
    nprobe: int,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/vector-db/ivf-search/python -q
```
