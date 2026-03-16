# ScaNN Search

> Track: `databases` | Topic: `vector-db`

## Concept

ScaNN narrows the search to a few promising partitions, then reranks that
shortlist with a stronger score. The main tradeoff is how many leaves to search
before the final reorder step.

## Key Points

- ScaNN is a partition-and-reorder ANN strategy.
- Partitioning cuts the number of vectors the exact scorer has to touch.
- `leaves_to_search` controls recall and latency.
- `reorder_k` controls how many shortlisted candidates get the final exact
  ranking.
- ScaNN-style systems are especially common for large inner-product search
  workloads.

## Minimal Code Mental Model

```python
leaves = assign_leaves(documents)
order = leaf_order(query)
hits = scann_candidate_ids(query, documents, leaves_to_search=1, reorder_k=2)
```

## Function

```python
def validate_vector(vector: list[float]) -> None:
def dot_product(left: list[float], right: list[float]) -> float:
def dominant_axis(vector: list[float]) -> int:
def assign_leaves(documents: list[dict[str, object]]) -> dict[int, list[str]]:
def leaf_order(query_vector: list[float]) -> list[int]:
def scann_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    leaves_to_search: int = 1,
    reorder_k: int = 2,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/vector-db/scann-search/python -q
```
