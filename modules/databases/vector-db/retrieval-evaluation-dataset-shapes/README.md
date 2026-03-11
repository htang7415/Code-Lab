# Retrieval Evaluation Dataset Shapes

> Track: `databases` | Topic: `vector-db`

## Concept

Retrieval evaluation quality depends on the dataset shape. A useful dataset has unique query IDs, positive labels, and enough query types to expose different failure modes.

## Key Points

- Each evaluation case should identify a query and at least one relevant result.
- Duplicate query IDs make reports ambiguous.
- Query-type coverage matters because keyword, semantic, and multi-hop queries fail differently.
- Dataset structure problems can invalidate the metrics before ranking quality is even measured.

## Minimal Code Mental Model

```python
cases = [
    evaluation_case("q1", ["a"], "keyword", 7),
    evaluation_case("q2", ["b"], "semantic", 7),
]
summary = dataset_summary(cases)
```

## Function

```python
def evaluation_case(
    query_id: str,
    relevant_ids: list[str],
    query_type: str,
    allowed_workspace_id: int,
) -> dict[str, object]:
def duplicate_query_ids(cases: list[dict[str, object]]) -> list[str]:
def invalid_case_ids(cases: list[dict[str, object]]) -> list[str]:
def query_type_counts(cases: list[dict[str, object]]) -> dict[str, int]:
def dataset_summary(cases: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/vector-db/retrieval-evaluation-dataset-shapes/python -q
```
